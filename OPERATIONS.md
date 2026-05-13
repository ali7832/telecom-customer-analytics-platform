# Operations Runbook

## Purpose

This service provides customer intelligence for telecom retention teams. It estimates churn risk, assigns a behavioral segment, and returns a recommended retention action.

## Runtime Configuration

Configuration is controlled through `.env.example`:

- `TELECOM_ENV`: deployment environment.
- `TELECOM_MODEL_VERSION`: model identifier returned in every insight response.
- `TELECOM_TRAINING_ROWS`: synthetic training size for local/demo startup.
- `TELECOM_HIGH_RISK_THRESHOLD`: risk score threshold for high-risk customers.
- `TELECOM_SERVICE_NAME`: service identifier exposed by health checks.

## API Flow

1. A customer profile is submitted to `/customers/insights`.
2. The service computes churn risk.
3. A segment is assigned.
4. Risk band and recommended retention action are returned.
5. Stakeholders can route high-risk accounts to retention campaigns or account managers.

## Risk Bands

- `low`: routine engagement
- `medium`: monitor usage and send personalized bundle
- `high`: retention offer and account manager follow-up
- `critical`: priority retention call with support case review

## Production Roadmap

- Replace synthetic data with warehouse ingestion.
- Add batch scoring jobs for campaign lists.
- Add dashboard for retention teams.
- Add model monitoring and drift tracking.
- Add customer-level audit history and experiment tracking.
