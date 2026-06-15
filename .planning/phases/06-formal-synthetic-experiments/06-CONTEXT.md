# Phase 6: Formal Synthetic Experiments - Context

**Gathered:** 2026-06-15T23:15:28+08:00
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 6 generates the formal synthetic evidence base for the manuscript. It
must run reproducible paired-seed experiments over the approved behavioral
service-design methods, save raw and processed artifacts, preserve failures and
reruns, and produce paper-ready statistical summaries without converting pilot
or diagnostic evidence into headline claims.

In scope:
- Run the formal synthetic main-evidence matrix over the four core behavioral
  service designs under shared passenger-response semantics.
- Run roadmap-listed supplementary experiment packages as independent evidence
  packages: matched coverage, fixed accepted-set, utility sensitivity,
  meeting-point density, fleet/demand, rolling-horizon, equity, and ALNS/MILP.
- Save configs, seeds, raw rows, processed rows, utility logs, failure/timeout
  rows, rerun ledgers, tables, confidence intervals, plots, and result reports.
- Produce `06_FORMAL_SYNTHETIC_RESULTS.md` as the Phase 6 evidence report.

Out of scope:
- Treating Phase 5 pilot results as formal evidence.
- Replacing paired seeds with unplanned replacement seeds.
- Approving final manuscript claims; Phase 8 owns the claim-evidence gate.
- Running Phase 7 case-study evidence or rewriting manuscript sections.

</domain>

<decisions>
## Implementation Decisions

### Main Evidence Experiment Matrix
- **D-01:** The formal main evidence must use 20 paired synthetic seeds as the
  minimum completion target. Runtime may allow expansion to 30 seeds, but
  Phase 6 success cannot depend on completing 30.
- **D-02:** The main evidence table must include only the four core behavioral
  service-design methods: `DoorToDoor + Choice`,
  `SingleSidedPickup + Choice`, `SingleSidedDropoff + Choice`, and
  `BidirectionalMP + Choice + RollingHorizon/ALNS`.
- **D-03:** Diagnostic methods such as no-rolling-horizon, greedy insertion,
  ALNS budget diagnostics, and MILP/static diagnostics must not appear as main
  evidence methods.
- **D-04:** Formal main-evidence request scales must use the existing main
  scale grid from `experiments/config.py`: `100`, `200`, `300`, and `500`.
  The Phase 5 pilot scale `20` stays readiness-only and must not be mixed into
  formal main evidence.
- **D-05:** If seeds 21-30 are attempted, they upgrade the main evidence to a
  30-seed evidence base only if all extra seeds complete under the same
  predeclared rules. If the extension is incomplete, the main evidence remains
  the complete 20 paired seeds.

### Supplementary Experiment Layering
- **D-06:** Phase 6 uses a "main evidence plus independent supplementary
  packages" structure. The main matrix supports the central efficiency claim;
  each supplementary package has its own design, gate, outputs, and reporting
  position.
- **D-07:** Phase 6 should complete all roadmap-listed supplementary packages:
  matched coverage, fixed accepted-set, utility sensitivity, meeting-point
  density, fleet/demand, rolling-horizon, equity, and ALNS/MILP.
- **D-08:** Supplementary packages are reported as main-text summaries plus
  appendix or supplement detail. The main text should show key robustness
  signals; complete tables, failed/timeout rows, diagnostic plots, and parameter
  details belong in appendix/supplement artifacts.
- **D-09:** A critical supplementary conflict blocks Phase 6 from directly
  advancing to Phase 8. The team must explain the conflict, rerun or correct the
  design where appropriate, or downgrade the core claim before claim gating.
- **D-10:** For planning, treat a supplementary result as critical when it
  directly challenges the main efficiency interpretation. Matched coverage,
  fixed accepted-set, and utility sensitivity should be treated as critical for
  headline behavioral claims unless the planner documents a narrower rationale.

### Failure, Timeout, and Rerun Rules
- **D-11:** For formal main evidence, every failed or timeout run must remain as
  a durable raw row. After the cause is fixed, rerun the same `seed x scale x
  method` cell. Do not silently delete failures and do not substitute
  replacement seeds.
- **D-12:** Any unclosed failed or timeout row in the main matrix blocks main
  evidence passage. The four behavioral methods across `100/200/300/500 x 20`
  paired seeds must close before main evidence can pass.
- **D-13:** Supplementary package failures are handled through independent
  package gates. A failed package cannot support its corresponding robustness
  claim. If the failed package is critical and affects the main claim, it blocks
  Phase 6; otherwise, it is recorded as a limitation and audit item.
- **D-14:** Phase 6 must maintain a run-level and reason-level ledger. At
  minimum, record `run_id`, `config_id`, `seed`, `scale`, `method`, `status`,
  `error`, `reason`, `fix`, and `rerun_result`, and summarize this ledger in
  `06_FORMAL_SYNTHETIC_RESULTS.md`.

### Statistical Reporting and Paper Table Scope
- **D-15:** Main tables should prioritize paired differences. For each scale,
  compare `BidirectionalMP` against each baseline within the same seed and
  report difference means, confidence intervals, direction, and matrix
  completeness.
- **D-16:** The main table must report the efficiency-and-coverage quartet:
  `total_vehicle_km`, `vkm_per_served_trip`, `vkm_per_original_request`, and
  `served_share`. Do not report only a vehicle-km-per-trip metric and do not
  hide coverage differences in the appendix.
- **D-17:** Phase 6 should use paired bootstrap 95% confidence intervals as the
  primary uncertainty summary for paired seed differences. Paired t-tests or
  Wilcoxon diagnostics may be added in appendix material, but p-values must not
  drive the main narrative.
- **D-18:** Results can enter the Phase 8 claim gate only when the main matrix
  is complete, the quartet metrics are present, paired confidence intervals are
  reproducible, and no critical supplementary conflict remains unexplained.

### the agent's Discretion
The planner may choose exact seed IDs, extension-seed IDs, formal output
directory names, helper module names, ledger file format, plot filenames,
bootstrap implementation details, and timeout thresholds, provided those choices
preserve the decisions above and are predeclared before formal runs. Prefer
existing project patterns: experiment orchestration under `experiments/`,
generated formal outputs under a clearly isolated `results/formal/phase06/`
directory or equivalent, and phase reports under
`.planning/phases/06-formal-synthetic-experiments/`.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project and Phase Definition
- `.planning/ROADMAP.md` - Phase 6 goal, EXP-05 requirement, success criteria,
  expected outputs, and later phase boundaries.
- `.planning/REQUIREMENTS.md` - Formal experiment, metrics, choice,
  reproducibility, and claim-gate requirements.
- `.planning/PROJECT.md` - Core value, TR-E rigor, strict phase gates,
  pilot/formal separation, paired-experiment discipline, and synthetic-data
  honesty.
- `.planning/STATE.md` - Current project position after Phase 5 and known
  concerns entering formal experiments.

### Prior Phase Contracts
- `.planning/phases/02-experimental-contract-and-metric-standardization/02-CONTEXT.md` - Experiment-family separation, metric denominator rules, and
  coverage-control handoff.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_EXPERIMENT_CONTRACT.md` - Behavioral evidence versus supplementary
  diagnostic boundaries.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_BASELINE_TAXONOMY.md` - Required service-design baseline taxonomy.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_METRICS_DEFINITIONS.md` - Metric formulas, valid denominators, and forbidden
  ambiguous metric language.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_COVERAGE_CONFOUNDING_PLAN.md` - Matched-coverage and fixed accepted-set
  control semantics.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_STATISTICAL_PLAN.md` - Paired-seed and confidence-interval discipline.
- `.planning/phases/03-passenger-choice-model-rebuild/03-CONTEXT.md` - Actual-offer choice model decisions and utility logging requirements.
- `.planning/phases/03-passenger-choice-model-rebuild/03_CHOICE_MODEL_CONTRACT.md` - Choice timing, status semantics, seeded type assignment, and utility
  component contract.
- `.planning/phases/03-passenger-choice-model-rebuild/03_PARAMETER_CALIBRATION.md` - Main and sensitivity parameter values and source labels.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04-CONTEXT.md` - Behavioral baseline, diagnostic, output schema, and failure-row
  decisions.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_IMPLEMENTATION_AUDIT.md` - Implementation status before pilot/formal runs.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_BASELINE_VALIDATION.md` - Baseline and schema validation evidence.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_ALGORITHM_VALIDATION.md` - ALNS/MILP diagnostic scope and no-Gurobi path.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/VARIANT_MAPPING.md` - Concept labels, legacy labels, evidence families, and
  diagnostic roles.
- `.planning/phases/05-pilot-experiments/05-CONTEXT.md` - Pilot/formal
  separation and Phase 6 readiness scope.
- `.planning/phases/05-pilot-experiments/05_PILOT_RESULTS.md` - Pilot pass
  state, matched-coverage and fixed-set findings, and carry-forward warnings.
- `.planning/phases/05-pilot-experiments/05_BUG_LEDGER.csv` - Closed pilot
  blockers and rerun rationale.

### Codebase Maps
- `.planning/codebase/ARCHITECTURE.md` - Experiment architecture, runner flow,
  variant layer, metrics layer, and output paths.
- `.planning/codebase/TESTING.md` - Active pytest patterns, runner smoke tests,
  and deterministic generated scenario patterns.
- `.planning/codebase/CONCERNS.md` - Known risks affecting formal runs:
  timeout behavior, metric/status gaps, generated artifacts, MILP limits,
  performance bottlenecks, and test collection fragility.

### Source Integration Points
- `experiments/config.py` - Existing `SCALES`, `SEEDS`, `VEHICLE_COUNTS`, and
  choice/rolling-horizon constants that Phase 6 must extend carefully.
- `experiments/runner.py` - Shared runner, row schema, utility log writer,
  timeout/error-row behavior, and result CSV output.
- `experiments/phase05_pilot.py` - Behavioral-main method filtering pattern
  that can be adapted for the Phase 6 main matrix.
- `experiments/pilot_validation.py` - Persisted schema, metric range, status,
  expected-matrix, and utility joinability checks to generalize for formal runs.
- `experiments/variants.py` - Method metadata, evidence-family tags, and
  concept-level behavioral labels.
- `experiments/metrics.py` - Metric calculations and names for the
  efficiency-and-coverage quartet.
- `experiments/phase05_coverage_smoke.py` - Matched-coverage pilot repair
  pattern and target-count semantics.
- `experiments/endogenous_matched_coverage.py` - Served-share cap matched
  coverage implementation starting point.
- `experiments/matched_coverage.py` - Historical post-hoc matched coverage
  implementation to contrast with formal controls.
- `experiments/algorithm_diagnostics.py` - ALNS budget diagnostic helper.
- `experiments/milp_gap.py` - Fixed accepted-set/static MILP diagnostic,
  comparable-gap rules, durable statuses, and no-Gurobi behavior.
- `tests/test_phase05_pilot.py` - Pilot harness and validation test patterns to
  generalize for Phase 6.
- `tests/test_runner.py` - Runner CSV-output smoke patterns.
- `tests/test_variants.py` - Behavioral variant and metadata assertions.
- `tests/test_metrics.py` - Metric range and calculation tests.
- `tests/test_milp.py` - Gurobi-gated MILP smoke pattern.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `experiments/runner.py`: Already writes raw rows, metrics tables, utility
  component logs, schema fields, failure/timeout rows, and provenance fields.
- `experiments/phase05_pilot.py`: Provides a clean pattern for selecting only
  `behavioral_main` variants by concept-level `method_label`.
- `experiments/pilot_validation.py`: Provides reusable checks for required
  fields, expected matrix completeness, failed/timeout rows, numeric ranges, and
  utility-log joinability.
- `experiments/metrics.py`: Provides the metric names that should anchor the
  quartet in formal tables.
- `experiments/endogenous_matched_coverage.py` and
  `experiments/phase05_coverage_smoke.py`: Provide starting points for formal
  matched-coverage controls, but Phase 5's pilot fallback semantics must be
  re-evaluated before formal use.
- `experiments/milp_gap.py` and `experiments/algorithm_diagnostics.py`: Provide
  diagnostic-only exact/heuristic comparison paths.

### Established Patterns
- Core DRT algorithms live under `src/drt/`; experiment orchestration and CSV
  writing live under `experiments/`; generated outputs live under `results/`;
  planning evidence reports live under `.planning/phases/`.
- Evidence family and diagnostic-role metadata must travel with each result row
  so behavioral evidence and diagnostics cannot be mixed accidentally.
- Optional Gurobi behavior should record skip/no-Gurobi statuses or comparable
  diagnostic rows without blocking non-MILP runs.
- Tests prefer deterministic generated scenarios and fixed seeds over mocks.

### Integration Points
- Add a Phase 6 formal runner or wrapper that selects only the four behavioral
  methods for the main matrix and writes to an isolated formal output directory.
- Add a Phase 6 validation/reporting layer that checks matrix closure across
  scales, seeds, methods, statuses, utility logs, and quartet metrics.
- Add independent supplementary-package runners or commands, each with its own
  manifest, gate result, and summary section.
- Add paired-difference and paired-bootstrap summary generation for main tables.
- Add a failure/rerun ledger artifact and link it from
  `06_FORMAL_SYNTHETIC_RESULTS.md`.

</code_context>

<specifics>
## Specific Ideas

- Keep Phase 5 scale `20` out of formal main evidence.
- Prefer `results/formal/phase06/` or an equally explicit formal output root.
- Use the existing scale grid `100/200/300/500` and extend the seed list beyond
  `[42, 43, 44]` through a predeclared formal seed manifest.
- Report supplementary packages in the main text only as robustness summaries;
  keep full diagnostic detail in appendix/supplement outputs.

</specifics>

<deferred>
## Deferred Ideas

None. Discussion stayed within Phase 6 scope.

</deferred>

---

*Phase: 6-Formal Synthetic Experiments*
*Context gathered: 2026-06-15T23:15:28+08:00*
