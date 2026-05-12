from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from telecom_analytics.generator import generate_customers
from telecom_analytics.model import ChurnModel

app = FastAPI(title='Telecom Customer Analytics API')

_model = ChurnModel()
_model.fit(generate_customers(800))


class Customer(BaseModel):
    tenure_months: int
    monthly_charges: float
    data_usage_gb: float
    support_tickets: int
    month_to_month: int = 1
    churn: int = 0


@app.get('/health')
def health() -> dict:
    return {'status': 'ok'}


@app.post('/churn-risk')
def churn_risk(customer: Customer) -> dict:
    payload = customer.model_dump()
    risk = _model.predict_risk(payload)
    return {'churn_risk': risk, 'high_risk': risk >= 0.5}
