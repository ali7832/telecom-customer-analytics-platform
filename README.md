# Telecom Customer Analytics Platform

Production-ready customer analytics and churn intelligence platform for telecom operators.

## Features

- Synthetic telecom customer dataset generation
- Customer churn prediction pipeline
- Revenue and usage feature engineering
- Customer segmentation
- FastAPI analytics service
- CLI workflows for data generation and demo runs
- Docker and Docker Compose deployment
- GitHub Actions CI
- Pytest suite
- Architecture and deployment documentation

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
curl -X POST http://localhost:8000/churn-risk \
  -H 'Content-Type: application/json' \
  -d @sample_customer.json
```

## Docker

```bash
docker-compose up --build
```

## Docs

- `ARCHITECTURE.md`
- `DEPLOYMENT.md`
- `sample_customer.json`

## Portfolio Highlights

- End-to-end customer intelligence platform
- Churn analytics and segmentation
- Production-oriented API and CLI architecture
- Deployable with Docker and CI
- Telecom-specific business relevance for retention and revenue analytics
