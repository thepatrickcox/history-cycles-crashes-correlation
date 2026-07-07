# Methodology

## What This Is

An observational cross-axis pattern study built from primary sources over approximately ten years. The methodology is not academic in the formal sense — there are no pre-registered hypotheses, no institutional review, and no econometric modeling. What it has instead is a consistent approach to evidence that is described honestly here.

---

## The Cross-Axis Approach

The defining methodological feature of this project is integration across dimensions that are typically studied in isolation:

- Market cycles → financial economics literature
- Partisan political dynamics → political science literature  
- Asset regulation history → legal-historical scholarship
- Political violence → criminology and political science
- Human rights inflection points → sociology

These literatures rarely speak to one another. This project consistently asks how events in one column relate to events in another. That orientation is the primary methodological contribution — not any single finding within it.

---

## What Was Kept and Why

A finding was retained in the primary dataset if:

1. The underlying events are verifiable from primary sources (government records, contemporaneous press, established price data)
2. The pattern can be stated as an observation without requiring intent to be true
3. A falsification criterion can be specified — something observable that would substantially weaken the pattern
4. Counter-examples are included, not filtered out

Counter-examples in the dataset include: the 1937 FDR drawdown (Democrat, Recovery Term), the 1962 Kennedy slide (Democrat), the 1990 GHW Bush recession (Republican, Hero classification), and the 2022 Biden bear market (Democrat). These complicate clean narratives. They are in the dataset because excluding inconvenient cases is how pattern recognition becomes confirmation bias.

---

## What Was Tested and Discarded

### Hurricane Frequency
Mapped against crash timing across the full dataset period. Distribution was statistically even — no meaningful clustering relative to market events. Discarded. Not in this repository.

### Named Family Wealth and Influence Figures
Several specific figures circulating in popular financial commentary (asset-controlled estimates for major historical banking dynasties) were investigated. These figures lack public accounting verification and cannot be confirmed or denied from available records. Removed from the primary dataset. The underlying institutional history — which is verifiable — remains in the asset suppression and governance sections.

### Intent and Orchestration Hypotheses
Throughout the research, hypotheses about deliberate coordination of market events by named actors were tracked. The data support pattern observation. They do not support the further inference that named actors arrange patterns intentionally.

The distinction matters: *"X recurs in association with Y"* is an empirically defensible historical observation. *"X recurs because actor Z arranges it"* requires an additional class of evidence — documents, communications, testimony, or coincidence so improbable as to rule out chance — that is not present in price data and policy timelines.

These hypotheses are maintained in a private speculative archive. They are not part of this public repository. They were not discarded — they were correctly classified.

---

## On Sample Size and the Complete-Record Problem

The most common objection to this work is that the samples are too small for structural conclusions — roughly fifteen major US market events over ~115 years, thirteen assassination attempts over 160 years.

This objection misunderstands what the data is. **These are not samples drawn from a larger pool. They are the complete population.**

The United States has existed since 1776 and has had meaningful equity markets only since the late nineteenth century. There are not more US market crashes available to study, because there have not been more. You cannot collect a larger sample of US crashes any more than a geologist can collect more than one Earth or a cosmologist can observe more than one universe. The record is small because the country is young, not because the data was sampled poorly.

This has two consequences:

1. **Statistical-significance language is the wrong frame.** Significance testing asks whether a sample result would generalize to a population. Here the data *is* the population. The honest framing is descriptive: across the complete observable US record, this is what the pattern looks like. That is a weaker claim than statistical proof in some respects and a stronger one in others — there is no sampling error because there is no sampling.

2. **The way to enlarge the evidentiary base is not more US data — it is older non-US data.** If the same structural relationships (crash clustering with political stress, war finance as wealth concentration, restriction-then-adoption in stores of value, cross-market synchronization) appear in European financial history before the US existed, then the patterns are not artifacts of American institutions; they are general features of economies under stress. This is the purpose of the pre-1900 research agenda documented in `research_notes/pre_1900_european_precedents.md`. The 1720 South Sea / Mississippi pair and the global Panic of 1873 are the highest-value tests: multi-country events in eras with entirely different institutions.

The pre-1900 extension is the correct response to the sample-size objection. The complete US record is what it is; the question is whether the same structure appears in the older and larger record of European and pre-modern finance.

---

## On the Regime-Break Risk (AI as the Variable the Dataset Cannot See)

Every finding in this project rests on patterns drawn from 1865–2025. That is the framework's foundation and also its blind spot.

If a genuinely new structural variable enters the system — one with no historical analogue — then every pattern in this dataset could be operating on top of a regime change the data cannot see. The patterns held across 160 years; that is not evidence they will hold across a discontinuity unlike anything in the record.

The candidate for such a discontinuity is artificial intelligence. Howard Marks, in his February 2026 memo *AI Hurtles Ahead*, describes AI changing the world at a speed approaching instantaneous, outpacing most observers' ability to anticipate it — and notes that AI has begun participating in its own development. Whether or not one shares that assessment, the methodological point stands: a variable that alters productivity, labor, capital allocation, and the speed of information itself could break the regularities this project documents.

This is not a reason to abandon the framework. It is a reason to state its boundary honestly:

- The findings describe how markets, power, and stress have interacted across the observable historical record.
- That record may not include a variable now entering the system at a pace and scale without precedent.
- Patterns that held across every prior regime can still fail at a true regime break. The honest researcher names the thing that could make his patterns obsolete rather than waiting for it to do so quietly.

Accordingly, all forward-looking applications of this framework carry an explicit caveat: **the patterns are descriptive of the historical record through 2025; their applicability to a post-2025 environment shaped by a possible AI-driven regime change is an open question, not an assumption.** The forecast logbook (`validation/forecast_logbook/`) is the instrument for detecting such a break in real time — a sustained run of framework misses would itself be evidence that the regime has shifted.

---
The dataset contains fifteen major market events and thirteen documented assassination attempts. As noted above, these are complete records rather than samples, but the small absolute counts still preclude the kind of statistical testing that larger datasets permit. All findings are presented as historical observations and falsifiable hypotheses, not as statistically significant results.

**Ex-post classification.**
Labeling a presidential term as a "Crash Term" or "Recovery Term" after the fact introduces hindsight bias. The workbook includes a pre-registered classification framework intended to address this prospectively. Where classifications are retrospective, that is acknowledged.

**Valuation metric inconsistency.**
P/E ratios in the dataset are not uniformly sourced. Shiller CAPE (publicly available from Yale at monthly resolution back to 1871) is the appropriate standard for cross-era comparison and should replace the current figures in a future revision.

**Reconstructed pre-index data.**
The FTSE 100 began in 1984. The DAX began in 1988. Pre-existence figures for these indices are reconstructed proxies, flagged in the dataset with a data quality column.

---

## On Confidence Levels

Each observation in the master database carries a confidence level: high, moderate, or low. These reflect the quality of the underlying sourcing, not the strength of the pattern the observation supports. A well-sourced observation that complicates a finding still carries high confidence. An observation from reconstructed proxy data carries low confidence regardless of whether it supports or undermines a finding.

---

## What "Pattern-Watching" Means

This framework is explicitly described as pattern-watching, not prediction.

| Prediction | Pattern-Watching |
|---|---|
| Claims: X will happen by Y date | Observes: historically, conditions like these preceded X |
| Requires being right | Requires being honest about observations |
| Commits to specific outcomes | Identifies historical reference points and watches |
| Certainty-seeking | Pattern-recognition with explicit epistemic limits |

The October 2025 forecast documents illustrate this distinction. The -30 to -40% figure cited for 2025 was the historical average decline for comparable periods — a reference point, not a committed prediction. The actual 2025 correction was -19%. The timeframe and trigger were correct; the depth was half the historical average. Both facts are in the validation record.

---

## Suggested Improvements for Anyone Extending This Work

1. **Standardize on Shiller CAPE** for all P/E figures. Data is publicly available from Yale at monthly resolution back to 1871.
2. **Pre-register classification criteria** before the next presidential term ends. Specify in writing, before observing outcomes, what would classify a term as "Crash Term" or "Recovery Term."
3. **Run the Japan natural experiment.** Japan's effective single-party (LDP) dominance from 1955 to 2009 is a built-in control group for the partisan cycle hypothesis. If two-party alternation is causally relevant, Japan should show a different crash-incidence pattern over the same period.
4. **Formal statistical testing.** A binomial test on the partisan crash ratio. A temporal clustering test on the assassination data. Neither requires econometric expertise to run; both would strengthen the findings substantially.

---

*Patrick Cox — June 2026*
