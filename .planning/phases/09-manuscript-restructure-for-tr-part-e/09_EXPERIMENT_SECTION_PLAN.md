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

## Formal Main Evidence Table Contract

The formal main-evidence table is restricted to the behavioral service-design
comparison. It must include only these paper-facing method labels:

- `DoorToDoor + Choice`
- `SingleSidedPickup + Choice`
- `SingleSidedDropoff + Choice`
- `BidirectionalMP + Choice + RollingHorizon/ALNS`

No deterministic diagnostic, solver diagnostic, no-choice ablation, gamma
sweep, or weight-sensitivity row belongs in this table.

Minimum table columns:

| Column | Purpose |
|---|---|
| `method` | One of the four approved paper-facing methods above. |
| `scale` or scenario key | The predeclared request-scale or scenario pairing key. |
| `n_pairs` | Number of valid paired seed comparisons after failure/timeout accounting. |
| `total_vehicle_km` | Total vehicle distance; maps to the code metric `total_vkm` if that name appears in raw outputs. |
| `vkm_per_served_trip` | Vehicle-km normalized by served requests. |
| `vkm_per_original_request` | Vehicle-km normalized by original demand. |
| `served_share` | Served requests divided by original requests. |
| paired difference | Method difference against the declared reference comparison within the same seed/scenario pair. |
| confidence interval | 95% confidence interval for the paired difference, with method named in table note. |

The table note must state that failed, timeout, or incomplete pairs remain
visible in provenance outputs and cannot be silently dropped.

## Metric Language Rules

- `vkm_per_trip is forbidden` for new formal evidence.
- Use `vkm_per_served_trip` when the denominator is served requests.
- Use `vkm_per_original_request` when the denominator is original requests.
- Every efficiency statement must include coverage and rejection context,
  including `served_share` and the relevant choice/feasibility rejection
  mechanisms.
- Do not report a vehicle-km saving without explaining whether it comes from
  shorter routing, lower served share, passenger rejection, feasibility
  rejection, or some combination of these mechanisms.
- Do not use "acceptance rate" for deterministic insertion diagnostics. Use
  served share, inserted share, or the specific status vocabulary required by
  the experiment family.

## Robustness and Diagnostic Allocation

| Material | Main-text role | Appendix/supplement role |
|---|---|---|
| Matched coverage | Main-text robustness summary that asks whether efficiency patterns persist near a common served-share target. | Full target definition, tolerance, achieved shares, failure rows, and paired metrics. |
| Fixed accepted-set controls | Main-text robustness summary that asks whether routing/service-design distance differences persist on a common passenger set. | Construction rule, retained set size/composition, per-method failures, and full metric rows. |
| Equity and passenger-type evidence | Main-text trade-off summary only. | Type-level acceptance, wait, walk, IVT, generalized-cost distributions, and inequality metrics. |
| ALNS diagnostics | Brief credibility note only if needed. | Runtime, convergence, budget, quality, and sensitivity detail. |
| Greedy diagnostics | Diagnostic comparison only. | Full static or greedy insertion comparison and failure cases. |
| No-rolling-horizon diagnostics | Mechanism summary only if Phase 8 supports it. | Full dynamic/static comparison and waiting-time mechanism evidence. |
| No-choice diagnostics | Mechanism summary only. | Deterministic insertion rows and non-behavioral status interpretation. |
| MILP diagnostics | Scoped exact-comparison caveat only. | Small-instance exact model, assumptions, solve status, no-Gurobi path, and comparable-gap rows. |
| Gamma diagnostic | Welfare-accounting limitation only. | Full gamma sweep, with explicit note that gamma is post-hoc unless it affects decisions. |
| Weight-sensitivity diagnostic | Optional bounded robustness note only if Phase 8 promotes a limited summary. | Complete weight grid, metrics, provenance, and sensitivity limits. |

Matched coverage and fixed accepted-set controls belong in the main text as
robustness summaries because they directly test coverage confounding and
same-passenger routing interpretations. Their detailed designs and full tables
belong in appendix or supplement so the main experiment section remains focused
on the formal behavioral comparison.

ALNS, greedy, no-rolling-horizon, no-choice, MILP, gamma, and
weight-sensitivity material are diagnostics unless Phase 8 explicitly promotes
a limited summary. Even then, the promoted text must remain subordinate to the
formal behavioral evidence and must state its diagnostic scope.

Equity can appear in the main text only as a trade-off summary, not a universal
policy claim. Type-level and distributional details belong in appendix or
supplement unless Phase 8 grades a specific equity statement as supported.

## Synthetic Case Boundary

Any current Beijing wording must use the exact phrase `Beijing-inspired
synthetic scenario`. The phrase signals that the current material is a
structured synthetic stress test, not an observed Beijing case study and not a
real-data validation.

Recommended wording:

> We evaluate a Beijing-inspired synthetic scenario with a denser meeting-point
> grid and peak-period demand pattern to test whether the formal synthetic
> findings remain directionally consistent under a different synthetic spatial
> design.

Do not write:

- "Beijing case study" unless Phase 7 or later supplies real or semi-real
  evidence and Phase 8 approves the claim.
- "Calibrated to Beijing" unless the calibration source, data fields, and
  validation level are documented.
- "Chinese city policy recommendation" unless the statement is bounded as a
  scenario-specific managerial insight.

The synthetic case can support a transfer-boundary discussion. It cannot by
itself support a universal policy claim or a real-world deployment claim.
