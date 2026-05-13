# ADR-001: Customer Insight Service Layer

## Status

Accepted

## Context

Telecom retention workflows need more than a raw churn probability. Business teams need interpretable risk bands, customer segments, and recommended next actions that can be connected to campaigns, account managers, or support follow-up.

## Decision

Create a dedicated `CustomerAnalyticsService` that combines churn prediction, segmentation, risk banding, model version metadata, and retention recommendations behind a single API contract.

## Consequences

Benefits:

- API responses are useful for stakeholders, not just ML engineers.
- Risk bands make dashboards and triage easier.
- Model versioning supports operational accountability.
- Service layer keeps FastAPI routes thin and deployable.

Tradeoffs:

- Local/demo mode still uses synthetic data.
- Production use should connect the service to a customer warehouse and batch scoring workflow.
