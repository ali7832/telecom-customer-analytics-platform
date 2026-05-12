from telecom_analytics.generator import generate_customers
from telecom_analytics.model import ChurnModel


def test_churn_model_predicts_probability():
    records = generate_customers(50)
    model = ChurnModel()
    model.fit(records)
    risk = model.predict_risk(records[0])
    assert 0.0 <= risk <= 1.0
