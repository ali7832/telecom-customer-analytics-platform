from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class TelecomSettings:
    environment: str = os.getenv('TELECOM_ENV', 'local')
    model_version: str = os.getenv('TELECOM_MODEL_VERSION', 'rf-churn-baseline-v1')
    training_rows: int = int(os.getenv('TELECOM_TRAINING_ROWS', '1000'))
    high_risk_threshold: float = float(os.getenv('TELECOM_HIGH_RISK_THRESHOLD', '0.50'))
    service_name: str = os.getenv('TELECOM_SERVICE_NAME', 'telecom-customer-analytics')


settings = TelecomSettings()
