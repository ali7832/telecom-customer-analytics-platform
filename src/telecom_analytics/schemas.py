from __future__ import annotations

from pydantic import BaseModel, Field


class CustomerProfile(BaseModel):
    customer_id: str | None = None
    tenure_months: int = Field(..., ge=0)
    monthly_charges: float = Field(..., ge=0)
    data_usage_gb: float = Field(..., ge=0)
    support_tickets: int = Field(..., ge=0)
    month_to_month: int = 1
    churn: int = 0


class CustomerInsight(BaseModel):
    customer_id: str | None
    churn_risk: float
    risk_band: str
    high_risk: bool
    segment: int
    model_version: str
    recommended_action: str


class HealthResponse(BaseModel):
    status: str
    service_name: str
    environment: str
    model_version: str
