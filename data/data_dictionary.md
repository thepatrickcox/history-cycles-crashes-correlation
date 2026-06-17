# Data Dictionary — master_database.csv

**Dataset:** Historical Pattern Study, Cross-Axis Database  
**Observations:** 87  
**Period:** 1215–2026 (primary focus 1865–2026)  
**Last updated:** May 23, 2026  
**Maintainer:** Patrick Cox

---

## Column Definitions

| Column | Type | Description |
|---|---|---|
| `obs_id` | String | Unique observation identifier. Format: OBS-XXXX. Sequential. |
| `date_or_year` | String | Date or year of the observation. Format varies: full date (YYYY-MM-DD) for political violence events; year only for market events and most other categories. Pre-1865 entries exist for human rights timeline context. |
| `category` | String | Primary category. See Category Values below. |
| `subcategory` | String | Secondary classification within category. |
| `entity` | String | The primary actor, asset, or subject of the observation. For market events: the president. For political violence: the target. For asset suppression: the asset. |
| `party_or_country` | String | Political party (US observations) or country (global observations). |
| `observation_neutral` | String | Factual description of the observation, phrased without intent claims. |
| `numeric_value` | Mixed | Quantitative value associated with the observation where applicable. Units specified in `unit` column. |
| `unit` | String | Unit for numeric_value. See Unit Values below. |
| `confidence` | String | Source confidence level: `high`, `moderate`, or `low`. Reflects sourcing quality, not pattern strength. |
| `status` | String | `active` (in primary dataset), `needs_validation` (forecast observation awaiting outcome data). |
| `source_tab` | String | Original source spreadsheet from the 28-CSV archive. |
| `source_originals` | String | Specific original file(s) from archive that contributed this observation. |
| `notes_working` | String | Working notes, context, counter-example flags, and cross-references. |

---

## Category Values

| Value | Description | Count |
|---|---|---|
| `market_event` | Major US market decline events (>20% from peak) | 15 |
| `political_violence` | Documented assassination attempts on US presidents, candidates, former presidents | 13 |
| `asset_suppression` | Regulatory restriction or confiscation events affecting silver, gold, or cryptocurrency | 13 |
| `human_rights` | Significant human rights inflection points mapped against economic context | 33 |
| `forecast` | Forward-looking probability estimates and watch windows | 8 |
| `indicator` | Leading indicator observations (gold, delinquency) | 5 |

---

## Unit Values

| Value | Description |
|---|---|
| `pct_decline` | Percentage decline from peak (market events) |
| `pct_change` | Percentage price change (asset suppression events) |
| `year` | Year of event (political violence — numeric_value is the year) |
| `z_score` | Standard deviations from mean (human rights timeline) |
| `probability_pct` | Probability estimate as percentage (forecast observations) |

---

## Confidence Levels

| Level | Meaning |
|---|---|
| `high` | Primary sources available. Government data, contemporaneous press, established price records. |
| `moderate` | Secondary sources or reconstructed data. Directionally verified but not primary-source confirmed. |
| `low` | Reconstructed proxies. Pre-index data (FTSE pre-1984, DAX pre-1988) or estimated figures. |

**Important:** Confidence reflects the quality of sourcing for the observation itself. A high-confidence observation that contradicts a pattern is still high-confidence. A low-confidence observation that confirms a pattern is still low-confidence. These levels are independent of pattern direction.

---

## Known Data Quality Issues

**Pre-index global data:** The FTSE 100 began 1984. The DAX began 1988. Global market figures for events before these dates are reconstructed proxies from historical sources. These observations carry `confidence: low` and are flagged in `notes_working`.

**P/E ratio sourcing:** Stock P/E ratios in the dataset are not uniformly sourced across eras. The Shiller CAPE ratio (available from Yale at monthly resolution back to 1871) is the appropriate standard for cross-era comparison. Standardization to Shiller CAPE is a planned revision.

**Forecast observations:** OBS-0075 through OBS-0082 are forecast observations from October 2025. Validation status as of May 2026 is documented in `/validation/2025_forecast_review.md`. These observations carry `status: needs_validation` until fully resolved.

---

## What Is Not In This Dataset

The following categories were investigated and excluded:

- **Hurricane/weather frequency:** Mapped against crash timing. Distribution was even. No pattern. Excluded.
- **Named family wealth figures:** Specific asset-controlled estimates from popular financial commentary. Unverifiable from public accounting. Excluded from primary dataset.
- **Intent and orchestration claims:** Pattern observations are in this dataset. Claims that named actors deliberately arrange the patterns are not. Those hypotheses are maintained in a private speculative archive.

---

## Source Archive

The 38 original CSV files that constitute the source archive for this dataset are preserved in `/data/sources/`. These files represent the raw research accumulated over approximately ten years, predating consolidation. File names reflect original working titles and have been lightly cleaned for readability. Timestamps on these files (October 2025) establish the pre-publication state of the research.

---

*Patrick Cox — June 2026*
