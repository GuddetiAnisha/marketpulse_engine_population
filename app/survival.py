import numpy as np
import pandas as pd

def survival_curve(initial_population: int, annual_retirement_rate: float, years: int = 20):
    rows = []
    for year in range(years + 1):
        remaining = initial_population * ((1 - annual_retirement_rate) ** year)
        rows.append({"year": year, "estimated_surviving_engines": round(remaining)})
    return pd.DataFrame(rows)
