def markdown_report(scored, estimates, validation):
    lines = [
        "# MarketPulse Estimation Report",
        "",
        "## Method",
        "External observations are combined using source-quality-weighted averages. "
        "The uncertainty interval includes cross-source disagreement plus a 5% baseline margin. "
        "This is a transparent educational heuristic, not a production statistical model.",
        "",
        "## Source priorities",
    ]
    for _, r in scored.iterrows():
        lines.append(f"- {r['source_name']}: quality score {r['quality_score']:.3f}")
    lines += ["", "## Market estimates"]
    for _, r in estimates.iterrows():
        lines.append(
            f"- {r['market']}: {int(r['external_estimate']):,} "
            f"(interval {int(r['lower_95']):,}–{int(r['upper_95']):,}), "
            f"sources={int(r['source_count'])}, disagreement CV={r['disagreement_cv']:.3f}"
        )
    lines += ["", "## Validation"]
    for _, r in validation.iterrows():
        lines.append(
            f"- {r['market']}: internal={int(r['internal_estimate']):,}, "
            f"difference={int(r['difference']):,}, "
            f"error={r['percentage_error']:.1f}%, "
            f"inside interval={bool(r['inside_interval'])}"
        )
    lines += [
        "",
        "## Limitation",
        "All bundled observations and internal benchmarks are synthetic. "
        "The project demonstrates software and methodology only."
    ]
    return "\n".join(lines)
