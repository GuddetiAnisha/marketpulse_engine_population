import pandas as pd
from app.source_quality import score_sources
from app.triangulation import triangulate
from app.validation import validate
from app.survival import survival_curve

def test_source_scores():
    df = pd.DataFrame([{
        "source_id":"A","source_name":"A","coverage":1,"granularity":1,
        "freshness":1,"accessibility":1,"reliability":1
    }])
    out = score_sources(df)
    assert abs(out.iloc[0]["quality_score"] - 1.0) < 1e-9

def test_triangulation_between_sources():
    scores = pd.DataFrame([
        {"source_id":"A","quality_score":1.0},
        {"source_id":"B","quality_score":1.0},
    ])
    obs = pd.DataFrame([
        {"market":"X","source_id":"A","estimate":100},
        {"market":"X","source_id":"B","estimate":200},
    ])
    out = triangulate(obs, scores)
    assert out.iloc[0]["external_estimate"] == 150

def test_validation():
    estimates = pd.DataFrame([{
        "market":"X","external_estimate":100,"lower_95":90,"upper_95":110,
        "source_count":2,"disagreement_cv":0.1
    }])
    internal = pd.DataFrame([{"market":"X","internal_estimate":105}])
    out = validate(estimates, internal)
    assert bool(out.iloc[0]["inside_interval"])

def test_survival_declines():
    out = survival_curve(1000, 0.05, 10)
    assert out.iloc[-1]["estimated_surviving_engines"] < 1000
