# Indicator Spec — Housing Death Cross (recovered from working sheet)

**Definition.** DeathCross = TRUE when the 12-month moving average of the Case-Shiller Home Price Index falls below its 48-month moving average. Composite Buy_Signal = TRUE when, post-death-cross, at least 3 of 4 align: debt-to-income < 90 (indexed), affordability index > 100, months of inventory > 10, sentiment < 50.

**Why it's kept.** It is the housing analog of the equity 200-day trend switch — same philosophy (trend regime, not level), different asset, and the composite gates the signal on fundamentals rather than price alone.

**Critical data note.** The recovered sheet's monthly rows (Oct 2025 – Jul 2026, showing the cross flipping TRUE in early 2026 with prices stepping down ~5 pts/month) are a **modeled scenario, not observed data** — actual 2026 prices sit at record highs (NAR May 2026 median $429,300, +1.3% YoY). The scenario rows are therefore **not ingested** into `data/`. The spec is retained; implementation requires wiring to actual FRED series (CSUSHPINSA, plus DTI/affordability/inventory/sentiment sources) with the computation dated and logged. Until then this is an indicator definition, not a signal.
