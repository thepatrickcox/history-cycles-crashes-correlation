# Statistical Tests — Verified Edition (July 2026)

Inputs transcribed directly from `data/Master_History_Workbook.xlsx`. Reproduce with `python3 analysis/statistical_tests.py` (stdlib only, fixed seed, ~seconds). Method: exact binomial tails and Monte Carlo permutation — the correct tools for a complete historical record, since they test *arrangement*, not sampling. No result here licenses prediction; these numbers describe 1865–2026 and stop there.

## Finding 1 — Partisan crash asymmetry
Null: each crash lands under a party with probability equal to its share of presidential time (R = 59/119 years = 0.496). Attribution rule, pre-committed: the president in office for the majority of the decline period (settles C-1980 → R, C-2000 → R under one rule).

- **Baseline: 12 of 15 under R, one-sided p = 0.016.** Sensitivities: C-1980 counted D → 0.056; excluded → 0.027.
- **Lag attribution kills it:** charged to the party 1–2 years earlier, k falls to 8–9, p = 0.29–0.49. The pattern exists under contemporaneous attribution only — a structural fact, stated openly (cf. Blinder & Watson's treatment of the same problem).
- **Severity (candidate 1b):** the workbook's own `term_market_role` classes 9 of 15 as full Crash Terms — **all nine Republican, p = 0.0018** — while the 6 Mid-Term Drawdowns are mixed. Gate: the Crash/Mid-Term criteria must be written and re-derived blind to party (current assignments contain judgment: 1987 at −22% is CrashTerm, 2022 at −25% is MidTerm) before this is claimed.
- Multiple-comparisons: the baseline does not survive Bonferroni at any plausible K; its grade legitimately rests on external replication (Bartels; Blinder & Watson). The severity result, if it survives blind reclassification, does survive moderate K.

## Finding 2 — Assassination-attempt clustering
The previously documented "10 of 13 within 2 years, ~22% base rate, 3.5×" **did not reproduce** from the workbook's own tables and is **retired**. Verified, window shown as the researcher choice it is:

| Window (around crash periods, start→trough) | Coverage of 1865–2024 | In-window | One-sided p |
|---|---|---|---|
| ±1 year | 33.8% | 8 of 13 | **0.037** |
| ±2 years | 46.2% | 8 of 13 | 0.204 |

The same 8 attempts hit under both windows — the hits sit *close* to crash periods; the misses sit far away. Out-of-window: 1865, 1881, 1901, 1912, 1950 — four of five predate the crash table's 1907 start, so they sit in calendar where no crash *could* be near them. **Gate:** extend the crash table to the 19th-century panics (1869, 1873, 1884, 1893, 1896, 1901) blind to attempt dates, using NBER cycle dates; pre-commit one window; then publish whatever the number is. Stated as fact meanwhile: all 7 attempts since 1963 fall in-window; the two same-episode pairs (Ford 1975, Trump 2024) must always be reported raw and merged.

## Candidate — crash start-month seasonality (new, July 2026)
Start months from the workbook: October = 4, January = 4 (8 of 15 in two months). Honest post-hoc denominators: P(some month ≥ 4) = 0.35 — nothing; P(some two months jointly ≥ 8) = 0.062 — weakly suggestive at best. Start-month depends on dating convention (peak vs panic month). Status: candidate, leaning discard; logged in `research_notes/candidate_observations.md`.

## Small, complete datasets — the standing frame
These 15 crashes and 13 attempts are the entire population, not a sample. Permutation tests are the correct instrument for exactly that case. What no test can do: manufacture resolution 13 points don't contain, or extend any pattern to the *next* instance — continuation is a historical judgment outside statistics. The archive's framing (historical observations, falsifiable hypotheses, no predictions) remains the outer frame.

## K (multiple comparisons)
Source-sheet inventory: 38 sheets. K estimation task open in METHODOLOGY; until estimated, single-test p-values here should be read as descriptive, not confirmatory.
