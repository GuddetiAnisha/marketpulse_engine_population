import pandas as pd
import plotly.express as px
import streamlit as st

from app.source_quality import score_sources
from app.triangulation import triangulate
from app.validation import validate
from app.survival import survival_curve
from app.report import markdown_report

st.set_page_config(page_title="MarketPulse", layout="wide")
st.title("MarketPulse — Industrial Engine Population Estimation Lab")
st.caption("Software-only prototype using synthetic data and transparent source triangulation.")

catalogue = pd.read_csv("data/source_catalogue.csv")
observations = pd.read_csv("data/market_observations.csv")
internal = pd.read_csv("data/internal_benchmark.csv")

scored = score_sources(catalogue)
estimates = triangulate(observations, scored)
validation = validate(estimates, internal)

tab1, tab2, tab3, tab4 = st.tabs(
    ["Source Inventory", "Triangulation", "Validation", "Survival Scenarios"]
)

with tab1:
    st.subheader("Maintainable source catalogue")
    st.dataframe(scored, use_container_width=True)
    fig = px.bar(scored, x="source_name", y="quality_score", title="Source quality ranking")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Market-level population estimates")
    st.dataframe(estimates, use_container_width=True)
    fig = px.bar(
        estimates,
        x="market",
        y="external_estimate",
        error_y=estimates["upper_95"] - estimates["external_estimate"],
        error_y_minus=estimates["external_estimate"] - estimates["lower_95"],
        title="Triangulated external estimates with uncertainty"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Synthetic internal validation")
    st.dataframe(validation, use_container_width=True)
    fig = px.scatter(
        validation,
        x="internal_estimate",
        y="external_estimate",
        text="market",
        title="External vs internal estimates"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    market = st.selectbox("Market", estimates["market"].tolist())
    pop = int(estimates.loc[estimates["market"] == market, "external_estimate"].iloc[0])
    retirement = st.slider("Assumed annual retirement rate", 0.01, 0.15, 0.05, 0.01)
    curve = survival_curve(pop, retirement)
    st.line_chart(curve.set_index("year"))
    st.caption(
        "This is a scenario model, not an empirically estimated Volvo Penta service-life model."
    )

report = markdown_report(scored, estimates, validation)
st.sidebar.download_button("Download report", report, "marketpulse_report.md")
