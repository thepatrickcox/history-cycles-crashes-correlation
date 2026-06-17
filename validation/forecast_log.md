# Forecast Logbook

*A public, append-only record of dated, falsifiable market and macro forecasts — each logged **before** the outcome is known, then scored honestly, including the misses.*

**Started:** 2026-05-30
**Scoring:** Brier-scored where probabilistic; confirmed / partial / missed / premature where directional.

---

## Why this exists

Pattern recognition that produces conviction without pre-registered tests is a known source of large losses. The defense is a log like this one. Each entry is committed before the outcome is known, with a specific observable and a falsification line, so it cannot be re-remembered favorably later.

A forecaster willing to mark his own calls wrong in public earns a kind of standing that correct-sounding calls, remembered after the fact, never can. That is the entire purpose of this file. The misses are not embarrassments to be minimized — they are the most valuable rows in the book, because they are the ones that can't be faked.

**What this is not:** this is a record of *forecasts and their accuracy*. It is not investment advice, not a description of any positions held, and not a recommendation to do anything. It tracks whether a method makes good calls. Nothing more.

---

## How a call is logged (the discipline)

Every entry, before the outcome:

1. **Date of forecast** — when committed (the git commit timestamp is the proof).
2. **Source** — which method produced it.
3. **Horizon** — the window the call covers.
4. **Specific observable** — a number or event someone else can check, not a vibe.
5. **Probability** (if probabilistic) — so it can be Brier-scored.
6. **Falsification criterion** — the outcome that would mark this call WRONG.

After the outcome:

7. **Result** — confirmed / partial / missed / premature.
8. **Brier contribution** (if probabilistic) — (forecast − outcome)², outcome = 1 if it happened, 0 if not.
9. **Lesson** — one line.

**Standing rules:** Log the call before the outcome — a call logged after is a memory, not a forecast. The observable must be checkable by someone else. Misses stay in the book, unsoftened, forever. n < 10 is not a track record; resist drawing conclusions early.

---

## Scored entries

### Entry #1 — 2025 crisis probability (45%) ⚠️ PARTIALLY CONFIRMED

*The founding entry. Logged first because the most honest call in the book is the one where the window and trigger were right but the depth was wrong — and saying so plainly is what makes the rest credible. Graded consistently with the full 2025 forecast review.*

| Field | Value |
|---|---|
| **Date of forecast** | 2025-10 (October 2025 forecast set) |
| **Source** | Historical pattern study → phase / watch-window framework |
| **Horizon** | 2025 (Jan–Oct window), observed through May 2026 |
| **Specific observable** | 45% crisis probability for 2025. Triggers flagged: trade taxes (25%+), debt-limit disputes, Fed-rate uncertainty, geopolitical tension. Historical reference for comparable periods: −30 to −40% decline (a dataset reference point, not a committed point forecast). |
| **Falsification criterion** | No material stress event in the flagged window; or the flagged triggers fail to appear. |
| **Result** | ⚠️ **PARTIALLY CONFIRMED.** Window correct (year-1, Q1–Q2 of a second-term Republican presidency). Trigger correct (tariffs; effective rate ~24%). A real drawdown occurred: S&P −19% (Feb 19 → Apr 8 2025). **Miss on depth** — actual ~−19% vs the −30/−40% historical reference. **Miss on recovery speed** — full-year 2025 finished ~+17%, faster than comparable historical recoveries. Classified as a correction, not a full bear market. |
| **Scoring note** | The framework identified the *when* and the *why* correctly; the historical depth/duration reference did not describe the actual outcome. The honest read: useful for windows and mechanisms, not a depth or duration predictor. Not scored as a clean Brier point because the −30/−40% figure was a reference, not a committed probability on a specific depth. |
| **Lesson** | The structural work locates fragility and timing windows well; it does not size the move. Fragility is a map, not a clock — and not a ruler. |

---

### Entry #2 — Macro suite baseline: patience over prediction ⏳ OPEN

*The corrected method, on trial. Logged so it can be scored later.*

| Field | Value |
|---|---|
| **Date of forecast** | 2026-05-30 |
| **Source** | Systematic macro suite (regime + deploy-gate framework) |
| **Horizon** | Ongoing / re-scored periodically |
| **Specific observable** | Deploy gate CLOSED (few of its categories firing). Regime read: reflation with stagflation risk. Posture: stay patient, do not predict timing, let signal convergence decide. |
| **The call being tested** | NOT "a crash is coming." The call is: *patience beats prediction here; the gate will signal when, and it will not be front-run.* |
| **Falsification criterion** | A major buyable bottom forms and the gate never flags it (false negative), OR the gate opens and the flagged window subsequently fares materially worse than staying patient (false positive). Either marks the method wrong. |
| **Result** | ⏳ OPEN |
| **Lesson (interim)** | This is the deliberate opposite of Entry #1: refuse to call timing; let convergence of independent signals make the decision. |

---

### Entry #3 — Rate-direction miss (logged while unresolved) ⏳ OPEN / leaning ❌

*Logged on the date below, while still open, specifically so it cannot be tidied up after the fact. A live miss recorded in real time is worth more than a correct call remembered later.*

| Field | Value |
|---|---|
| **Date of forecast** | 2026-06-16 |
| **Source** | Rate-direction indicators (separate from the macro-suite posture call) |
| **Horizon** | Resolving through 2026 |
| **Specific observable** | Indicators pointed to interest rates moving **down**. As of the log date, rates have stayed sticky-high rather than falling. |
| **Falsification / resolution** | If rates remain sticky-high or rise through the horizon, the rate-direction call is marked MISSED. A timely move down would resolve it the other way. |
| **Result** | ⏳ OPEN, currently running against the call. Recorded now, before resolution, on purpose. |
| **Lesson (interim)** | Sticky-high rates are themselves the stress-transmission mechanism. Logging the miss while it's live is the point — the value is in not waiting for a face-saving resolution. |

---

## Running scorecard

| # | Date | Source | Call (short) | Result | Brier |
|---|------|--------|--------------|--------|-------|
| 1 | 2025-10 | Historical study | 2025 crisis 45%; window + tariff trigger right, depth wrong | ⚠️ PARTIAL | n/a* |
| 2 | 2026-05-30 | Macro suite | Gate closed; patience over prediction | ⏳ OPEN | — |
| 3 | 2026-06-16 | Rate indicators | Rates move down | ⏳ OPEN (leaning miss) | — |

\* Not Brier-scored: the −30/−40% depth figure was a historical reference point, not a committed probability on a specific depth. Window and trigger graded directionally as partial.

**Calls logged:** 3 · **Scored (directional):** 1 · **Confirmed:** 0 · **Partial:** 1 · **Missed:** 0 · **Open:** 2

> One graded call is not a track record. The number means nothing until n ≥ 10–20. The point of starting now is that in two years this table is the only honest answer to "does any of this actually work?" — more honest than any backtest, because these are real calls in real time with no hindsight.

---

## Scope note

This log records forecasts and their accuracy only. It does not disclose positions, amounts, or holdings, and it contains no claims of orchestration or intent — only observable, falsifiable calls and their honest scoring. Each entry stands or falls on whether the stated observable came to pass.

*Started with one honest miss — which is the right way to start.*
