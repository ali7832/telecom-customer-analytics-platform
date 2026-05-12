# Deployment Guide

## Local Development

```bash
pip install .[dev]
uvicorn telecom_analytics.api:app --reload
```

## CLI Demo

```bash
telecomctl demo --rows 1000
```

## Docker

```bash
docker build -t telecom-customer-analytics .
docker run -p 8000:8000 telecom-customer-analytics
```

## Docker Compose

```bash
docker-compose up --build
```

## Health Check

```bash
curl http://localhost:8000/health
```
