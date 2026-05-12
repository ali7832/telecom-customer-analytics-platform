from pydantic import BaseModel


class CustomerProfile(BaseModel):
    tenure_months: int
    monthly_charges: float
    data_usage_gb: float
    support_tickets: int
    month_to_month: int
    churn: int = 0


class CustomerInsight(BaseModel):
    churn_risk: float
    segment: int
    recommended_action: str
