from __future__ import annotations

import random


def make_customer(customer_id: int) -> dict:
    tenure = random.randint(1, 72)
    charges = round(random.uniform(10, 150), 2)
    usage = round(random.uniform(1, 200), 2)
    tickets = random.randint(0, 12)
    contract = random.choice(['month_to_month', 'one_year', 'two_year'])
    churn = int(contract == 'month_to_month' and tickets > 4 and tenure < 18)
    return {
        'customer_id': customer_id,
        'tenure_months': tenure,
        'monthly_charges': charges,
        'data_usage_gb': usage,
        'support_tickets': tickets,
        'contract_type': contract,
        'churn': churn,
    }


def generate_customers(rows: int = 1000) -> list[dict]:
    return [make_customer(i) for i in range(1, rows + 1)]
