# MarketPulse — Industrial Engine Population Estimation Lab

A software-only portfolio prototype for transparent market-population estimation using source-quality scoring, reliability-weighted triangulation, uncertainty analysis, internal validation, survival scenarios, and an interactive Streamlit dashboard.

The project uses synthetic/demo data only. It does not contain proprietary Volvo data, commercial datasets, web scraping, or confidential information.

## Package-structure fix

The original repository placed implementation modules and CSV files at the repository root while the code imported modules such as `app.source_quality` and loaded files from `data/...`. This caused test collection and dashboard startup failures.

The repository has been reorganized into a proper Python package:

```text
marketpulse_engine_population/
├── app/
│   ├── __init__.py
│   ├── source_quality.py
│   ├── triangulation.py
│   ├── validation.py
│   ├── survival.py
│   └── report.py
├── data/
│   ├── source_catalogue.csv
│   ├── market_observations.csv
│   └── internal_benchmark.csv
├── tests/
│   └── test_marketpulse.py
├── dashboard.py
├── requirements.txt
├── README.md
└── PROJECT_DESCRIPTION.md
```

## Features

- configurable source catalogue
- source-quality scoring
- reliability-weighted market triangulation
- uncertainty intervals and disagreement indicators
- validation against a synthetic internal benchmark
- survival / retirement scenario modelling
- Streamlit visualisation
- downloadable Markdown report
- automated Pytest validation

## Software pipeline

```text
Source catalogue
      ↓
Source-quality scoring
      ↓
Market observations
      ↓
Reliability-weighted triangulation
      ↓
Uncertainty / disagreement
      ↓
Internal validation
      ↓
Survival scenarios
      ↓
Dashboard + report
```

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run tests

```powershell
python -m pytest -q
```

Validated after the package fix:

```text
4 passed
```

## Run dashboard

```powershell
python -m streamlit run dashboard.py
```

Streamlit normally opens the application at:

```text
http://localhost:8501
```

## Validation scope

The tests verify source-quality scoring, weighted triangulation, interval-based internal validation, and declining survival estimates. Passing tests confirm the implemented software behavior on the bundled cases; they do not establish real-world market accuracy.

See [RESULTS.md](RESULTS.md) for the validation summary.
