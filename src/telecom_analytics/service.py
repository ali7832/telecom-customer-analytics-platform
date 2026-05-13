from __future__ import annotations

from telecom_analytics.config import settings
from telecom_analytics.generator import generate_customers
from telecom_analytics.model import ChurnModel
from telecom_analytics.schemas import CustomerInsight, CustomerProfile
from telecom_analytics.segmentation import CustomerSegmenter


class CustomerAnalyticsService:
    def __init__(self) -> None:
        training_data = generate_customers(settings.training_rows)
        self.churn_model = ChurnModel()
        self.churn_model.fit(training_data)
        self.segmenter = CustomerSegmenter()
        self.segmenter.fit(training_data)

    def analyze(self, profile: CustomerProfile) -> CustomerInsight:
        payload = profile.model_dump()
        risk = self.churn_model.predict_risk(payload)
        segment = self.segmenter.segment(payload)
        risk_band = self._risk_band(risk)
        return CustomerInsight(
            customer_id=profile.customer_id,
            churn_risk=risk,
            risk_band=risk_band,
            high_risk=risk >= settings.high_risk_threshold,
            segment=segment,
            model_version=settings.model_version,
            recommended_action=self._recommended_action(risk_band, profile.support_tickets),
        )

    @staticmethod
    def _risk_band(risk: float) -> str:
        if risk >= 0.75:
            return 'critical'
        if risk >= 0.50:
            return 'high'
        if risk >= 0.25:
            return 'medium'
        return 'low'

    @staticmethod
    def _recommended_action(risk_band: str, support_tickets: int) -> str:
        if risk_band in {'critical', 'high'} and support_tickets >= 5:
            return 'priority_retention_call_with_support_case_review'
        if risk_band in {'critical', 'high'}:
            return 'retention_offer_and_account_manager_follow_up'
        if risk_band == 'medium':
            return 'monitor_usage_and_send_personalized_bundle'
        return 'standard_engagement'
