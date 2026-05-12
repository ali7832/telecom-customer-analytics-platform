from telecom_analytics.generator import generate_customers


def test_generate_customers():
    records = generate_customers(10)
    assert len(records) == 10
    assert 'tenure_months' in records[0]
    assert 'churn' in records[0]
