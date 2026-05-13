from telecom_analytics.schemas import CustomerProfile
from telecom_analytics.service import CustomerAnalyticsService


def test_customer_analytics_service_returns_retention_metadata():
    profile = CustomerProfile(
        customer_id='cust_001',
        tenure_months=8,
        monthly_charges=120.5,
        data_usage_gb=150.2,
        support_tickets=6,
        month_to_month=1,
    )

    insight = CustomerAnalyticsService().analyze(profile)

    assert insight.customer_id == 'cust_001'
    assert 0.0 <= insight.churn_risk <= 1.0
    assert insight.risk_band in {'low', 'medium', 'high', 'critical'}
    assert insight.model_version
    assert insight.recommended_action
