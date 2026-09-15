# MarketPulse — Industrial Engine Population Estimation Lab

A software-only portfolio prototype inspired by the methodological problem described in the Volvo Penta thesis posting, but intentionally changed so it does not reproduce Volvo's internal thesis work.

## Adapted scope

Instead of estimating Volvo Penta's real installed engine population or using proprietary/commercial sources, this project:

- uses synthetic market-level engine observations;
- maintains a configurable source catalogue;
- scores source quality from coverage, granularity, freshness, cost accessibility and reliability;
- combines contradictory sources using reliability-weighted estimation;
- reports uncertainty intervals and disagreement;
- validates external estimates against a synthetic internal benchmark;
- performs simple survival/service-life scenario analysis;
- provides an interactive Streamlit dashboard and downloadable reports.

No Volvo internal data, web scraping, paid commercial datasets, or confidential information is included.

## Software pipeline

Source catalogue → source-quality scoring → market observations → weighted triangulation → uncertainty/disagreement → validation → survival scenarios → dashboard/report.

## Run

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Tests

```bash
pytest -q
```

## Why this is useful

The project demonstrates Python, Pandas, statistical estimation, uncertainty, messy-data reasoning, validation, source assessment, transparent analytics and business-facing visualization.
