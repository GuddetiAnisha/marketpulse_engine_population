import numpy as np
import pandas as pd

def triangulate(observations: pd.DataFrame, source_scores: pd.DataFrame) -> pd.DataFrame:
    merged = observations.merge(
        source_scores[["source_id", "quality_score"]],
        on="source_id",
        how="left"
    )
    merged["quality_score"] = merged["quality_score"].fillna(0.1).clip(lower=0.01)

    rows = []
    for market, g in merged.groupby("market"):
        x = g["estimate"].astype(float).to_numpy()
        w = g["quality_score"].astype(float).to_numpy()
        mean = float(np.average(x, weights=w))
        variance = float(np.average((x - mean) ** 2, weights=w)) if len(x) > 1 else 0.0
        sd = variance ** 0.5
        # Transparent heuristic uncertainty: disagreement + 5% baseline.
        margin = 1.96 * (sd / max(len(x) ** 0.5, 1)) + 0.05 * mean
        cv = sd / mean if mean else 0.0
        rows.append({
            "market": market,
            "external_estimate": round(mean),
            "lower_95": max(0, round(mean - margin)),
            "upper_95": round(mean + margin),
            "source_count": len(x),
            "disagreement_cv": round(cv, 3),
        })
    return pd.DataFrame(rows)
