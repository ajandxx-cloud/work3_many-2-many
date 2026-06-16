# Phase 09 Experiment Section Plan

**Artifact:** `09_EXPERIMENT_SECTION_PLAN.md`  
**Purpose:** Restructure the experiment section for a Transportation Research
Part E manuscript by separating design, formal evidence, robustness controls,
equity evidence, algorithm diagnostics, and synthetic case boundaries.

## Current Experiment Section Risks

The current experiment section mixes exploratory manuscript evidence with
diagnostics and implementation checks. It contains legacy six-variant tables,
matched-coverage diagnostics, MILP/ALNS diagnostics, Beijing-inspired synthetic
results, sensitivity analysis, equity analysis, gamma welfare accounting, and
weight sensitivity in one narrative stream. That structure makes it too easy to
read diagnostic or pilot-style values as formal headline evidence.

The revision must address these risks:

- Legacy effect-size values are not final manuscript claims. Final numerical
  results require Phase 6 formal synthetic artifacts and Phase 8 claim-gate
  artifacts before they can appear as values in the revised experiment section.
- Behavioral main evidence must not mix all-accept deterministic rows with
  choice-consistent behavioral rows.
- Vehicle-distance efficiency must be reported with coverage and rejection
  context, not as an isolated distance-per-trip headline.
- Diagnostic rows such as MILP, greedy insertion, no-choice, no-rolling-horizon,
  gamma, and weight sensitivity must not leak into the formal main-evidence
  table.
- Beijing language must remain synthetic unless later case-study evidence
  exists and passes the claim gate.

## Target Experiment Section Architecture

The revised experiment section should use the following order.

| Order | Subsection | Manuscript role |
|---:|---|---|
| 1 | Experimental Design | Define synthetic scenario families, paired seeds, request scales, fleet settings, passenger-response assumptions, and output provenance before any results. |
| 2 | Metrics and Paired Comparison Protocol | Define denominators, row statuses, paired-seed comparisons, confidence intervals, and rejection/coverage context. |
| 3 | Formal Main Evidence | Present only the approved behavioral service-design comparison and paired differences after Phase 6 and Phase 8 artifacts support the claims. |
| 4 | Robustness Controls | Summarize matched-coverage and fixed accepted-set controls as robustness checks, with detailed tables in appendix or supplement. |
| 5 | Equity and Passenger-Type Trade-offs | Report type-level acceptance and burden as a bounded trade-off summary, with distributional detail in appendix or supplement. |
| 6 | Algorithm and Implementation Diagnostics | Report ALNS, greedy, no-rolling-horizon, no-choice, MILP, gamma, and weight-sensitivity material as diagnostics unless Phase 8 promotes a limited summary. |
| 7 | Case-Study or Beijing-Inspired Synthetic Boundary | State whether any case material is synthetic, semi-real, or real-data evidence, and keep current Beijing wording synthetic. |

`Formal Main Evidence` must appear before `Robustness Controls`, because the
reader should first see the predeclared behavioral comparison before seeing
controls. `Algorithm and Implementation Diagnostics` must appear after `Equity
and Passenger-Type Trade-offs`, because solver and implementation diagnostics
explain mechanisms rather than serving as the user-facing behavioral result.

## Evidence-Family Order

The section should move from evidence that supports the core manuscript claim
to evidence that bounds or diagnoses it:

| Evidence family | Main-text placement | Claim strength before Phase 8 |
|---|---|---|
| Experimental design and metrics | Main text, before results | Defines validity conditions only. |
| Formal behavioral main matrix | Main text | Placeholder until Phase 6 results and Phase 8 claim grading are available. |
| Matched-coverage control | Main-text robustness summary plus appendix/supplement detail | Robustness evidence, not replacement for unconstrained behavioral evidence. |
| Fixed accepted-set control | Main-text robustness summary plus appendix/supplement detail | Routing/service-design diagnostic under identical passenger set. |
| Equity and passenger-type evidence | Main-text trade-off summary plus appendix/supplement detail | Trade-off evidence, not universal policy proof. |
| Algorithm diagnostics | Mostly appendix/supplement; brief main-text summary only if needed | Implementation credibility and mechanism evidence. |
| Synthetic case boundary | Main text plus limitations | Scenario-transfer boundary, not real-city validation. |

This ordering keeps final numerical claims blocked until the formal evidence
pipeline is complete. Phase 6 must supply the reproducible experiment artifacts,
and Phase 8 must decide which manuscript claims survive the evidence gate.
