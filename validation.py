import pandas as pd
import numpy as np

def validate(estimates: pd.DataFrame, internal: pd.DataFrame) -> pd.DataFrame:
    df = estimates.merge(internal, on="market", how="left")
    df["difference"] = df["external_estimate"] - df["internal_estimate"]
    df["absolute_error"] = df["difference"].abs()
    df["percentage_error"] = np.where(
        df["internal_estimate"] != 0,
        100 * df["difference"] / df["internal_estimate"],
        np.nan
    )
    df["inside_interval"] = (
        (df["internal_estimate"] >= df["lower_95"]) &
        (df["internal_estimate"] <= df["upper_95"])
    )
    return df
