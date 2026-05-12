from __future__ import annotations

from sklearn.ensemble import RandomForestClassifier

from telecom_analytics.features import labels, to_matrix


class ChurnModel:
    def __init__(self) -> None:
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def fit(self, records: list[dict]) -> None:
        self.model.fit(to_matrix(records), labels(records))

    def predict_probability(self, record: dict) -> float:
        probability = self.model.predict_proba(to_matrix([record]))[0][1]
        return round(float(probability), 4)
