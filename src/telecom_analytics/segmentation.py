from __future__ import annotations

from sklearn.cluster import KMeans

from telecom_analytics.features import to_matrix


class CustomerSegmenter:
    def __init__(self, clusters: int = 3) -> None:
        self.model = KMeans(n_clusters=clusters, random_state=42, n_init='auto')

    def fit(self, records: list[dict]) -> None:
        self.model.fit(to_matrix(records))

    def segment(self, record: dict) -> int:
        return int(self.model.predict(to_matrix([record]))[0])
