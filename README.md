# API Testing Automation & Performance Benchmarking Framework

Python + PyTest + Requests + Locust + GitHub Actions project.

## Run locally
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env

Start API:
uvicorn demo_api:app --reload --port 8000

Run tests:
pytest -v

HTML report:
pytest -v --html=reports/report.html --self-contained-html

Benchmark:
python benchmark.py

Load test:
locust -f locustfile.py --host http://127.0.0.1:8000

## Interview explanation
I built a Python API automation framework using Requests and PyTest. It has a reusable API client, configuration through environment variables, positive and negative tests, logging, HTML reporting, performance benchmarking with average/P50/P95/P99/throughput, Locust load testing, and GitHub Actions CI.
