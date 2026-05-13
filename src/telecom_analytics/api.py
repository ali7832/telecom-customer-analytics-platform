from __future__ import annotations

from fastapi import FastAPI

from telecom_analytics.config import settings
from telecom_analytics.schemas import CustomerInsight, CustomerProfile, HealthResponse
from telecom_analytics.service import CustomerAnalyticsService

app = FastAPI(
    title='Telecom Customer Analytics API',
    description='Production-style telecom customer intelligence API for churn risk, segmentation, and retention actions.',
    version='0.2.0',
)

_service = CustomerAnalyticsService()


@app.get('/health', response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status='ok',
        service_name=settings.service_name,
        environment=settings.environment,
        model_version=settings.model_version,
    )


@app.post('/customers/insights', response_model=CustomerInsight)
def customer_insights(customer: CustomerProfile) -> CustomerInsight:
    return _service.analyze(customer)


@app.post('/churn-risk', response_model=CustomerInsight)
def churn_risk(customer: CustomerProfile) -> CustomerInsight:
    return _service.analyze(customer)
