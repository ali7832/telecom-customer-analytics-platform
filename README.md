# Telecom Customer Analytics Platform

Deployable customer intelligence platform for telecom retention teams. The system combines churn prediction, customer segmentation, risk banding, and recommended retention actions behind a production-style FastAPI service and a premium React command center.

## Product Demo Video


https://github.com/user-attachments/assets/006988a4-3ce5-49ba-9006-5aeae4750812


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
- Multi-page React/Vite customer intelligence frontend

## Quickstart

```bash
pip install .[dev]
telecomctl demo --rows 1000
uvicorn telecom_analytics.api:app --reload
pytest -q
```

## Frontend Command Center

The `frontend/` directory contains a premium interactive SaaS UI called TelcoPulse AI.

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

Frontend pages:

- Overview: executive KPIs, churn trend, segment mix
- Churn Lab: interactive customer risk simulator
- Segments: customer segment explorer and priority customers
- Campaigns: retention campaign studio and lift forecast
- Revenue Risk: regional ARPU and churn exposure monitoring
- Operations: model operations, SLA view, and workflow checklist

The UI attempts to call `/customers/insights` and gracefully falls back to demo intelligence when the backend is offline.

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
