from __future__ import annotations

import random


def generate_customers(rows: int = 1000) -> list[dict]:
    records: list[dict] = []
    for customer_id in range(1, rows + 1):
        tenure = random.randint(1, 72)
        charges = round(random.uniform(10, 150), 2)
        usage = round(random.uniform(1, 200), 2)
        tickets = random.randint(0, 12)
        month_to_month = random.choice([0, 1])
        label = int(month_to_month == 1 and tickets > 4 and tenure < 18)
        records.append(
            {
                'customer_id': customer_id,
                'tenure_months': tenure,
                'monthly_charges': charges,
                'data_usage_gb': usage,
                'support_tickets': tickets,
                'month_to_month': month_to_month,
                'churn': label,
            }
        )
    return records
