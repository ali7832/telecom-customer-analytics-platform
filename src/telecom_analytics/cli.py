from __future__ import annotations

import json
from pathlib import Path

import typer
from rich.console import Console

from telecom_analytics.generator import generate_customers
from telecom_analytics.model import ChurnModel
from telecom_analytics.segmentation import CustomerSegmenter

app = typer.Typer(help='Telecom customer analytics CLI')
console = Console()


@app.command()
def generate(output: Path = Path('customers.json'), rows: int = 1000) -> None:
    data = generate_customers(rows)
    output.write_text(json.dumps(data, indent=2), encoding='utf-8')
    console.print(f'Generated {rows} customers -> {output}')


@app.command()
def demo(rows: int = 1000) -> None:
    data = generate_customers(rows)
    model = ChurnModel()
    model.fit(data)
    segmenter = CustomerSegmenter()
    segmenter.fit(data)
    sample = data[0]
    console.print_json(
        data={
            'sample_customer': sample,
            'churn_risk': model.predict_risk(sample),
            'segment': segmenter.segment(sample),
        }
    )
