# Telecom Customer Analytics Platform

Deployable customer intelligence platform for telecom retention teams. The system combines churn prediction, customer segmentation, risk banding, and recommended retention actions behind a production-style FastAPI service.

## Core Capabilities

- Synthetic telecom customer dataset generation for local demo mode
- Churn prediction pipeline
- Customer segmentation baseline
- Customer insight service with churn risk, segment, risk band, and recommended action
- FastAPI analytics API
- CLI workflows for demo and data generation
- Runtime configuration through environment variables
- Docker and Docker Compose deployment
- GitHub Actions CI
- Pytest coverage
- Operations runbook and architecture decision record

## Quickstart

```bash
pip install .[dev]
telecomctl demo --rows 1000
uvicorn telecom_analytics.api:app --reload
pytest -q
```

## API

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/customers/insights \
  -H 'Content-Type: application/json' \
  -d @sample_customer.json
```

Backward-compatible endpoint:

```bash
curl -X POST http://localhost:8000/churn-risk \
  -H 'Content-Type: application/json' \
  -d @sample_customer.json
```

## Docker

```bash
docker-compose up --build
```

## Runtime Configuration

See `.env.example` for model version, training rows, environment, service name, and high-risk threshold settings.

## Documentation

- `ARCHITECTURE.md`
- `DEPLOYMENT.md`
- `OPERATIONS.md`
- `docs/adr-001-customer-insight-service.md`
- `sample_customer.json`

## Production Roadmap

- Warehouse-backed customer ingestion
- Batch scoring for retention campaigns
- Business dashboard for customer success teams
- Model monitoring and drift tracking
- Campaign outcome tracking
- A/B testing for offers and bundles
