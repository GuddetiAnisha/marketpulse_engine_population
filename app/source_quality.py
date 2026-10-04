import pandas as pd

WEIGHTS = {
    "coverage": 0.25,
    "granularity": 0.15,
    "freshness": 0.15,
    "accessibility": 0.10,
    "reliability": 0.35,
}

def score_sources(catalogue: pd.DataFrame) -> pd.DataFrame:
    df = catalogue.copy()
    for col in WEIGHTS:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).clip(0, 1)
    df["quality_score"] = sum(df[c] * w for c, w in WEIGHTS.items())
    return df.sort_values("quality_score", ascending=False)
