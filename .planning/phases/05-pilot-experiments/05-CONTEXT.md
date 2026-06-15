# Phase 5: Pilot Experiments - Context

**Gathered:** 2026-06-15T21:20:04+08:00
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 5 runs small pilot experiments to detect bugs, validate output schemas,
sanity-check metric ranges, exercise coverage-control logic, and confirm that
the Phase 6 formal experiment design is ready to plan. Pilot outputs are a
readiness gate only. They must not be used as manuscript evidence, formal
paired-seed evidence, or method-superiority claims.

In scope:
- Run a small synthetic pilot matrix over the four core behavioral service
  designs using shared passenger-response semantics.
- Verify that result rows, provenance fields, utility/component logs, metric
  ranges, failure rows, and diagnostic artifacts are complete and joinable.
- Run a complete small-sample matched-coverage diagnostic as Phase 6 readiness
  evidence.
- Run a minimal fixed accepted-set intersection smoke with at least one routing
  diagnostic.
- Record bugs, fixes, reruns, and blocking status before Phase 6 planning.

Out of scope:
- Beijing-inspired or case-study smoke runs.
- Formal paired-seed synthetic evidence.
- Paper-facing conclusions, comparative claims, or method-win plots.
- Broad ALNS/MILP benchmarking or solver-dependent gates.
- Manuscript claim approval.

</domain>

<decisions>
## Implementation Decisions

### Pilot Run Matrix
- **D-01:** The main Phase 5 pilot matrix must use small synthetic scenarios
  only. Do not include Beijing-inspired smoke runs in Phase 5.
- **D-02:** The pilot matrix must use 3 seeds. This is the roadmap minimum and
  keeps Phase 5 as a readiness gate rather than a quasi-formal experiment.
- **D-03:** The main pilot matrix must include exactly the four core behavioral
  service-design methods:
  `DoorToDoor + Choice`, `SingleSidedPickup + Choice`,
  `SingleSidedDropoff + Choice`, and
  `BidirectionalMP + Choice + RollingHorizon/ALNS`.
- **D-04:** Diagnostic methods such as greedy, no-rolling-horizon, ALNS budget
  smoke, and MILP gap checks must stay separate from the main behavioral pilot
  evidence family.
- **D-05:** The pilot matrix should use one small scale, aligned with existing
  runner smoke practice such as `n_requests=20`. The purpose is fast coverage
  of schema, status, metric, and stability issues.

### Pass/Fail Gates
- **D-06:** The main behavioral pilot matrix must have zero `failed` rows and
  zero `timeout` rows. Any core behavioral method/seed failure blocks Phase 5
  until fixed and rerun.
- **D-07:** Metric sanity checks must enforce strict basic ranges: ratio metrics
  in `[0, 1]`; `vehicle_km`, `vkm_per_served_trip`,
  `vkm_per_original_request`, wait, walk, and IVT values non-negative; and no
  NaN or infinity values.
- **D-08:** Abnormal served-share or acceptance patterns should be recorded as
  investigation items, not automatic Phase 5 failures, unless they accompany
  schema, status, metric-range, crash, or timeout problems.
- **D-09:** Missing joinable utility/component logs or required provenance
  fields is a hard Phase 5 failure for the main behavioral pilot.
- **D-10:** Required provenance includes at least `run_id`, `config_id`, `seed`,
  `scenario`, `method_label`, method-decomposition fields, `status`,
  `runtime_s`, `artifact_dir`, and `git_commit_or_code_hash`.

### Pilot Artifacts
- **D-11:** `05_PILOT_RESULTS.md` must be a gate report, not a small results
  paper. It should record the run matrix, pass/fail state, sanity checks, bugs,
  fixes, and rerun records without method-superiority conclusions.
- **D-12:** Pilot CSV/JSON outputs must be isolated under an explicit pilot
  directory such as `results/pilot/phase05/`. They must not be mixed with
  formal result files.
- **D-13:** Pilot plots should be diagnostic only, such as status distribution,
  metric range checks, failure/timeout counts, or missing-field checks. Do not
  generate paper-style win/loss comparison plots.
- **D-14:** Phase 5 must maintain a structured bug ledger. Each issue should
  record `bug_id`, triggering configuration, affected method/seed, symptom,
  fix status, rerun result, and whether it blocks Phase 6.

### Coverage-Control and Diagnostic Smoke
- **D-15:** Matched-coverage should run as a complete small-sample diagnostic
  in Phase 5, using the pilot scale/seeds where feasible. Its role is Phase 6
  readiness only, not manuscript evidence or method-superiority evidence.
- **D-16:** Matched-coverage served-share matching tolerance failure is a
  Phase 5 blocker. If the matched-coverage diagnostic exceeds its tolerance,
  fix the cap/target logic or explicitly adjust the Phase 6 design before
  proceeding.
- **D-17:** Fixed accepted-set validation should be a minimal intersection
  smoke. Build the common accepted/serviceable request intersection and run at
  least one fixed-set routing diagnostic, without broad small-sample
  comparison.
- **D-18:** ALNS/MILP gap diagnostics are optional and non-blocking in Phase 5.
  If Gurobi is available, a small instance may run; if not, record a complete
  `no_gurobi` status row. Solver unavailability must not block Phase 5.

### the agent's Discretion
The planner may choose the exact seed IDs, exact small scale value, exact pilot
directory/file names, diagnostic plot filenames, bug-ledger file format, and
matched-coverage tolerance value, provided the choices preserve the decisions
above and remain consistent with Phase 2/4 contracts. Prefer existing local
patterns such as the first three configured seeds, a `n_requests=20` smoke
scale, and file-based CSV/JSON/Markdown artifacts under `results/pilot/phase05/`
plus `.planning/phases/05-pilot-experiments/`.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project and Phase Definition
- `.planning/ROADMAP.md` - Phase 5 goal, REP-03 requirement, success criteria,
  and expected outputs.
- `.planning/REQUIREMENTS.md` - REP-03 durable failure-row requirement plus
  experiment, metrics, choice, and formal-evidence constraints carried into
  pilot readiness.
- `.planning/PROJECT.md` - Core value, TR-E rigor, strict phase gates,
  pilot/formal separation, paired-experiment discipline, and synthetic-data
  honesty.
- `.planning/STATE.md` - Current project state entering Phase 5.

### Prior Phase Contracts
- `.planning/phases/02-experimental-contract-and-metric-standardization/02-CONTEXT.md` - Experiment-family separation, metric denominator contract,
  coverage-control handoff, and Phase 5 role.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_EXPERIMENT_CONTRACT.md` - Behavioral evidence versus supplementary
  diagnostic boundaries and formal experiment design constraints.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_BASELINE_TAXONOMY.md` - Four-axis method taxonomy and required
  service-design baselines.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_METRICS_DEFINITIONS.md` - Metric formulas, denominator rules, valid ranges,
  and forbidden ambiguous metric language.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_COVERAGE_CONFOUNDING_PLAN.md` - Matched-coverage and fixed accepted-set
  control semantics.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_STATISTICAL_PLAN.md` - Paired-seed and confidence-interval discipline for
  later Phase 6 formal evidence.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_PHASE45_CODE_TASKS.md` - Phase 4/5 schema, runner, output, and validation
  handoff tasks.
- `.planning/phases/03-passenger-choice-model-rebuild/03-CONTEXT.md` - Shared
  actual-offer choice decisions and utility logging requirements.
- `.planning/phases/03-passenger-choice-model-rebuild/03_CHOICE_MODEL_CONTRACT.md` - Actual-offer choice timing, status semantics, utility components,
  and seeded passenger-type assignment contract.
- `.planning/phases/03-passenger-choice-model-rebuild/03_PARAMETER_CALIBRATION.md` - Choice parameter, sensitivity, and source-label discipline that
  pilot must not overclaim.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04-CONTEXT.md` - Behavioral baseline, diagnostic, output schema, failure-row, and
  timeout decisions feeding Phase 5.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_IMPLEMENTATION_AUDIT.md` - Implementation status entering pilot.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_BASELINE_VALIDATION.md` - Baseline and schema validation evidence before pilot.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_ALGORITHM_VALIDATION.md` - ALNS/MILP diagnostic scope and no-Gurobi path before
  pilot.
- `.planning/phases/04-baseline-and-algorithm-implementation-check/VARIANT_MAPPING.md` - Concept labels, legacy labels, evidence families, and
  diagnostic roles.

### Codebase Maps
- `.planning/codebase/ARCHITECTURE.md` - Runner flow, variant layer, metrics
  layer, analysis/persistence paths, and experiment architecture.
- `.planning/codebase/TESTING.md` - Pytest patterns, runner smoke tests, and
  deterministic generated scenario patterns.
- `.planning/codebase/CONCERNS.md` - Known risks affecting pilot: import roots,
  generated artifacts, timeout behavior, metric/status gaps, MILP limits, and
  long test/runtime constraints.

### Source Integration Points
- `experiments/runner.py` - Pilot matrix execution, result CSV writing, utility
  component logs, schema fields, timeout/failure rows, and output directories.
- `experiments/variants.py` - Four core behavioral methods, method metadata,
  evidence-family tags, diagnostic variants, and choice integration.
- `experiments/metrics.py` - Status-derived metric calculations and formal
  metric names.
- `experiments/endogenous_matched_coverage.py` - Current served-share cap
  matched-coverage implementation to pilot-test or replace.
- `experiments/matched_coverage.py` - Historical post-hoc matched-coverage
  implementation; useful as a contrast but not the preferred formal control.
- `experiments/algorithm_diagnostics.py` - Small ALNS budget diagnostic helper.
- `experiments/milp_gap.py` - Fixed accepted-set/static MILP diagnostic,
  comparable-gap rules, durable statuses, and no-Gurobi behavior.
- `tests/test_runner.py` - Existing runner smoke and CSV-output test patterns.
- `tests/test_variants.py` - Behavioral variant and method metadata tests.
- `tests/test_metrics.py` - Metric range/status behavior tests.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `experiments/runner.py`: `run_all_experiments(scales=..., seeds=...,
  beijing=False, results_dir=...)` can drive the small synthetic pilot and
  already writes raw result, metrics table, and utility component CSV outputs.
- `experiments/variants.py`: The Phase 4 variant surface exposes concept-level
  behavioral labels and diagnostic metadata needed to filter the four main
  behavioral methods from diagnostics.
- `experiments/metrics.py`: The metric layer already computes
  `served_share`, `behavioral_acceptance_rate`, `choice_rejection_rate`,
  `feasibility_rejection_rate`, `vkm_per_served_trip`, and
  `vkm_per_original_request`.
- `experiments/endogenous_matched_coverage.py`: Provides the closest existing
  served-share cap diagnostic semantics and should be the starting point for
  matched-coverage pilot readiness.
- `experiments/algorithm_diagnostics.py`: Provides a tiny ALNS budget smoke
  helper that can remain diagnostic-only.
- `experiments/milp_gap.py`: Provides fixed accepted-set/static diagnostic
  behavior and documented no-Gurobi rows.

### Established Patterns
- Core algorithms remain under `src/drt/`; experiment orchestration and output
  writing belong under `experiments/`; generated pilot files should go under
  `results/pilot/phase05/`; planning gate reports belong under
  `.planning/phases/05-pilot-experiments/`.
- Test patterns prefer deterministic generated scenarios and fixed seeds over
  mocks.
- Optional Gurobi behavior should skip or record `no_gurobi` without blocking
  non-MILP validation.
- Result rows should keep evidence-family and diagnostic-role fields so
  behavioral evidence and diagnostics cannot be mixed accidentally.

### Integration Points
- Add or reuse a pilot-specific runner wrapper that selects only the four core
  behavioral methods and writes into the isolated pilot output directory.
- Add validation checks for row status, metric ranges, required provenance
  fields, and joinability of utility/component logs.
- Add or refine matched-coverage pilot logic so cap/target tolerance is checked
  and blocking when exceeded.
- Add fixed accepted-set intersection construction and at least one small
  routing diagnostic path.
- Add `05_PILOT_RESULTS.md`, pilot diagnostic plots, and a structured bug
  ledger after runs complete.

</code_context>

<specifics>
## Specific Ideas

- Use a single small synthetic scale, preferably aligned with the existing
  runner smoke scale such as `n_requests=20`.
- Use 3 seeds, preferably the first three configured project seeds unless the
  planner has a strong reproducibility reason to choose another fixed set.
- Keep all pilot outputs visibly separate from formal outputs, for example
  under `results/pilot/phase05/`.
- Treat matched-coverage as the strongest Phase 6 readiness check in Phase 5:
  it should run as a complete small-sample diagnostic, but any interpretation
  remains gate-oriented rather than claim-oriented.

</specifics>

<deferred>
## Deferred Ideas

None. Discussion stayed within Phase 5 scope.

</deferred>

---

*Phase: 5-Pilot Experiments*
*Context gathered: 2026-06-15T21:20:04+08:00*
