from __future__ import annotations

FEATURES = [
    'tenure_months',
    'monthly_charges',
    'data_usage_gb',
    'support_tickets',
    'month_to_month',
]


def to_matrix(records: list[dict]) -> list[list[float]]:
    return [[float(row[name]) for name in FEATURES] for row in records]


def labels(records: list[dict]) -> list[int]:
    return [int(row['churn']) for row in records]
