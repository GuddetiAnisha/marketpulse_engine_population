# MarketPulse — Project Description

## Research-style question

How can multiple incomplete and contradictory market data sources be assessed and combined into a transparent population estimate with explicit uncertainty?

## Deliberate changes from the Volvo Penta thesis posting

This portfolio project does not attempt to estimate Volvo Penta's real installed base.

Changes:
- synthetic data instead of Volvo internal data;
- synthetic source categories instead of subscriptions or scraped commercial databases;
- generic industrial-engine population rather than brand-specific installed base;
- reliability-weighted triangulation with transparent heuristic uncertainty;
- interactive scenario analysis for engine survival;
- downloadable analytical report;
- no recommendation to purchase any real commercial dataset.

## Components

1. Source Inventory
2. Source Quality Scoring
3. Market Observation Store
4. Weighted Triangulation
5. Uncertainty and Disagreement Analysis
6. Synthetic Internal Validation
7. Survival/Service-Life Scenario Explorer
8. Streamlit Dashboard
9. Automated Tests

## Technologies

Python, Pandas, NumPy, Plotly, Streamlit, Pytest.

## Accuracy note

The bundled data are synthetic and the uncertainty interval is an educational heuristic. A real thesis should justify the statistical model, characterize source bias and dependence, and validate against authorized internal/external data.
