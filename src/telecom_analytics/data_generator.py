from __future__ import annotations

import random


def generate_customer() -> dict:
    tenure_months = random.randint(1, 72)
    support_tickets = random.randint(0, 12)
    contract_type = random.choice(['monthly', 'annual', 'two_year'])
    monthly_charges = round(random.uniform(10, 150), 2)
    data_usage_gb = round(random.uniform(1, 200), 2)
    churn = int(contract_type == 'monthly' and support_tickets >= 5 and tenure_months < 18)
    return {
        'tenure_months': tenure_months,
        'support_tickets': support_tickets,
        'contract_type': contract_type,
        'monthly_charges': monthly_charges,
        'data_usage_gb': data_usage_gb,
        'churn': churn,
    }


def generate_customers(rows: int = 1000) -> list[dict]:
    return [generate_customer() for _ in range(rows)]
