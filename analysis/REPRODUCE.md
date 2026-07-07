# Reproduce Every Number

1. **Findings 1–2 and the seasonality candidate:** `python3 analysis/statistical_tests.py` — standard library only, fixed seed, runs in seconds. Inputs are printed with the results; compare them line-by-line against `data/Master_History_Workbook.xlsx` (Crashes Detail, Assassinations tabs).
2. **Finding 1 count by hand:** open Crashes Detail; count party column; the attribution rule (majority of the decline period) is in `analysis/METHODOLOGY.md`.
3. **Finding 2 count by hand:** open Assassinations; each row already carries `years_from_nearest_crash`.
4. **Findings 3–5:** every dated claim carries a citation in `FINDINGS.md`; the underlying tables are in `data/sources/`.
5. **Forecast grades:** `validation/forecast_log.md` is append-only; each entry names its observable and its outcome.

If any number in FINDINGS.md cannot be reproduced this way, open an issue — that is a bug in the archive, and finding it is a contribution.
