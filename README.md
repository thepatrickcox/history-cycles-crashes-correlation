# History, Cycles, and Crashes

A cross-axis historical pattern study of US market cycles, political power, and economic stress — covering 1865–2026, with comparative data for the United Kingdom, Germany, and Japan. Assembled by one researcher from primary sources over roughly a decade (c. 2015–2026), consolidated and validated in 2026.

This repository is the **defensible core** of that work: each finding is stated as a falsifiable historical observation with a pre-committed criterion that would mark it wrong. Speculative and intent-based material is deliberately excluded and kept in a private working archive (see "Scope and what's excluded").

## Why this matters, in plain terms

Markets crash on a rhythm that looks almost regular in hindsight, and a recurring cast of conditions travels with each one: a particular phase of the political cycle, a particular debt trajectory, a particular level of overvaluation at the prior handoff. Those conditions are usually studied in separate silos — financial economics here, political science there, legal history somewhere else. This project's one distinguishing move is to put them in the same table and ask how the columns relate.

What comes out is not a theory of who causes crashes. It is a set of measurable observations about how loaded the structure is before one arrives — the kind of thing that, in the words of the work's own review, is "consistent with peer-reviewed academic findings the author had not encountered." The strongest four findings stand on public record (NBER dates, Federal Reserve data, Congressional Research Service counts) and are presented here in neutral language a skeptical reader can check.

## Plain-English summary

A visual, plain-English tour of this archive — the findings, the discard pile, and the graded forecast record — is maintained at:

**[corkscrewwillowadvisory.com/history-archive]((https://corkscrewwillowadvisory.com/history-archive/))**

This repository remains the source of truth. The site page summarizes it and is updated when the dataset or forecast grades change.

## What is in this archive

| Finding | Claim (neutral) | Status |
| --- | --- | --- |
| **A. Partisan crash asymmetry** | Major US crashes since 1907 fall disproportionately under one party relative to its share of presidential time | Substantial; corroborated by Bartels, Blinder & Watson |
| **B. Assassination–stress clustering** | Of 13 documented attempts since 1865, 10 fell within two years of a major crash (~3.5× the random base rate) | Striking; small sample (n=13) |
| **C. Restriction→adoption arc** | Silver, gold, and crypto each followed a restriction-then-institutional-adoption pattern | Defensible as historical observation; crypto leg in progress |
| **D. Inter-crash interval shortening** | Intervals between crashes have shortened alongside the 1971/1999/2018 deregulation events | Plausible and testable; small post-1970 sample |

Full detail, falsification criteria, and defensible phrasings are in [`FINDINGS.md`](FINDINGS.md). Each is graded against May-2026 actuals in [`validation/2025_forecast_review.md`](validation/2025_forecast_review.md).

## Principal data artifacts

- **`data/Master_History_Workbook.xlsx`** — the consolidated workbook (13 tabs): per-administration spine, crash detail, assassinations, global leaders, asset suppression, forecasts, and findings.
- **`data/history_database_long.csv`** — the same observations in flat, one-row-per-fact form (82 observations) for machine ingestion.
- **`data/sources/`** — individual source tables behind the findings.
- **`data/needs_review/`** — tables holding defensible data alongside an interpretive column ("scapegoat/hero" etc.) that must be pre-registered or stripped before full publication.

## Repository layout

```
README.md                      this file
EXECUTIVE_SUMMARY.md           one-page summary of the findings
FINDINGS.md                    the four strong findings + falsification criteria
READING_LIST.md                adjacent literature, reached independently
analysis/METHODOLOGY.md        approach, retention rules, sample-size argument
research_notes/                exploratory notes (clearly marked not-yet-findings)
validation/
  2025_forecast_review.md      Oct-2025 forecast graded against May-2026 actuals
  forecast_log.md              append-only, falsifiable, scored forecast record
data/
  Master_History_Workbook.xlsx consolidated 13-tab workbook
  history_database_long.csv    flat one-row-per-fact database (82 obs)
  master_database.csv          neutral integrated dataset
  data_dictionary.md           column definitions
  sources/                     individual source tables (current versions)
  needs_review/                held back pending a framing pass
LICENSE.md                     CC BY 4.0 (docs + data)
CITATION.cff                   citation metadata
```

## How to read the findings

Three honesty rules run throughout: **pattern, never intent** (each finding says "X recurs with Y," never "actor Z arranged it"); **small samples stated plainly**; and **counter-examples kept in view** — the 1937 FDR drawdown, 1962 Kennedy slide, 1990 GHW Bush recession, and 2022 Biden bear market are all retained because they complicate the pattern rather than confirm it. The findings are historical observations and falsifiable hypotheses, not claims of statistical significance.

## Scope and what's excluded

This is the public, defensible subset. Deliberately **not** included: orchestration or intent claims, unverified net-worth figures, and the "scapegoat/hero" framing in its un-pre-registered form. Those remain in a private working archive as hypothesis-formation material — preserved, not discarded, and available to be revisited if new evidence arrives. The separation protects the verified work from being dismissed by association with the speculative, and follows the recommendation of the project's own independent review.

## A note on what this is not

This repository is historical research. It is not investment advice, and it describes no positions or holdings. The forecast log records the accuracy of dated calls for transparency, nothing more.
