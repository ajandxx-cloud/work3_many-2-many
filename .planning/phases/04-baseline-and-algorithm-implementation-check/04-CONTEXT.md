# Phase 4: Baseline and Algorithm Implementation Check - Context

**Gathered:** 2026-06-15T17:22:40+08:00
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 4 ensures that behavioral baselines, deterministic diagnostics, routing
algorithms, MILP diagnostics, output schemas, and failure handling are
implemented consistently before pilot runs. This phase validates small
scenarios and algorithm smoke diagnostics. It does not run pilot experiments,
formal paired experiments, large-scale runtime-quality experiments, or approve
manuscript claims.

In scope:
- Run and validate all required behavioral service-design baselines on small
  scenarios under shared passenger-response semantics.
- Validate that behavioral choice uses actual feasible offers and does not use
  the legacy proxy-before-routing MNL filter.
- Validate greedy, no-rolling-horizon, ALNS convergence/operator diagnostics,
  and small runtime-quality diagnostics.
- Define and verify the limited MILP/exact diagnostic scope honestly.
- Standardize result rows, method labels, provenance fields, failure rows, and
  formal metric names.
- Produce implementation and validation documents required by the roadmap.

Out of scope:
- Pilot experiment execution; Phase 5 owns pilot smoke runs.
- Formal paired-seed evidence; Phase 6 owns final synthetic experiments.
- Large-scale runtime-quality benchmarking.
- Full route-sequencing exact MILP unless a later phase explicitly scopes it.
- Final claim approval or manuscript rewrite.

</domain>

<decisions>
## Implementation Decisions

### Baseline Family and Method Labeling
- **D-01:** Phase 4 must run all four behavioral baselines:
  `DoorToDoor + Choice`, `SingleSidedPickup + Choice`,
  `SingleSidedDropoff + Choice`, and `BidirectionalMP + Choice`.
- **D-02:** `SingleSidedDropoff` must be implemented as the symmetric
  counterpart to `SingleSidedPickup`, changing the meeting-point side from
  pickup to dropoff while preserving the shared comparison harness.
- **D-03:** Do not rush code class renames. Keep legacy class names where that
  reduces implementation risk, but result outputs must use concept labels.
  Paper-facing tables must not expose historical labels such as `FullModel` or
  `AblationNoChoice`.
- **D-04:** Required method-decomposition fields include `method_label`,
  `service_design`, `choice_model`, `reoptimization`, `routing_solver`, and
  optional `legacy_class`. The `legacy_class` field is for traceability only
  and must not enter paper-facing main tables.
- **D-05:** Create `VARIANT_MAPPING.md` to map historical code names to concept
  labels and explain which labels are behavioral evidence versus diagnostics.
- **D-06:** Behavioral runs and deterministic diagnostics may share a runner,
  but every row must include `evidence_family` and `diagnostic_role` fields so
  evidence families cannot be mixed accidentally.

### Shared Choice Integration Validation
- **D-07:** Phase 4 must prove that the legacy `_mnl_filter_requests` path is
  not used by behavioral main variants. Tests should monkeypatch or otherwise
  assert that behavioral variants do not call the old proxy-before-routing
  filter.
- **D-08:** Every behavioral baseline must have integration-level validation
  showing that a feasible offer is built, choice is evaluated on that actual
  offer, accepted requests are inserted, and rejected requests are not inserted.
- **D-09:** `DoorToDoor` uses the same choice model as meeting-point services,
  with `pickup_walk=0` and `dropoff_walk=0`. Wait time, IVT, schedule, and
  other utility fields must come from the actual door-to-door offer.
- **D-10:** Phase 4 must verify that the same `seed + request_id` gives the
  same passenger type across all four service designs.
- **D-11:** Acceptance draws must use reproducible, cross-method paired random
  streams and must not depend on RNG consumption order.

### ALNS, Greedy, and No-Rolling-Horizon Diagnostics
- **D-12:** Expose a named `GreedyInsertionBaseline` diagnostic that can run on
  a fixed accepted set or small scenario and writes the same schema as ALNS
  diagnostics.
- **D-13:** No-rolling-horizon must be a rolling-horizon diagnostic using the
  same service design and choice semantics while disabling reoptimization. Its
  role is to isolate the contribution of rolling-horizon behavior.
- **D-14:** ALNS diagnostics must record per-reoptimization objective/iteration
  traces, best objective, runtime, accepted counts, and unassigned counts.
- **D-15:** ALNS diagnostics must record at least destroy/repair operator
  selection counts plus improvement or accepted-improvement counts.
- **D-16:** Phase 4 should run a small-scenario multi-budget diagnostic, such as
  5/20/50 iterations or comparable time budgets, and record quality and
  runtime. This is algorithm smoke/diagnostic evidence only, not a formal
  large-scale runtime-quality experiment.

### MILP and Exact Diagnostic Boundary
- **D-17:** Use MILP only as a small static snapshot diagnostic, validating
  heuristic behavior or gaps on small instances or fixed accepted sets. Do not
  present it as a full exact online DRT benchmark.
- **D-18:** Phase 4 must include hand-verified tiny instances. If local Gurobi
  is unavailable, MILP solve tests may skip, but pure Python fixture checks for
  feasibility/objective expectations must still run so Phase 4 is not blocked
  by solver licensing.
- **D-19:** Report MILP-vs-ALNS gaps only where semantics match, such as fixed
  accepted-set or static small instances. Explicitly state objective units and
  suppress or mark incomparable cases.
- **D-20:** MILP-dependent tests may skip when Gurobi or a license is
  unavailable, but Phase 4 must preserve a pure-Python fixture or documented
  no-Gurobi diagnostic path.
- **D-21:** Do not require a full route-sequencing exact model in Phase 4.
  Document the simplified MILP scope honestly and fix only obvious bugs or
  schema/output issues discovered during validation.

### Unified Outputs and Failure Rows
- **D-22:** Every result row must include `run_id`, `config_id`, `seed`,
  `scenario`, `method_label`, `service_design`, `choice_model`,
  `reoptimization`, `routing_solver`, `evidence_family`, `diagnostic_role`,
  `status`, `detailed_reason`, `runtime_s`, and `error_message`.
- **D-23:** Phase 4 should also include `result_schema_version`,
  `timestamp_utc`, `artifact_dir`, `git_commit_or_code_hash`, `n_requests`,
  `n_offered`, and `n_served` for Phase 5/6 traceability.
- **D-24:** Failed, timeout, and infeasible outcomes must be durable rows, never
  silent omissions. Aggregate tables must either expose failure status or
  document exclusion rules.
- **D-25:** Fixing the current runner timeout bug is mandatory in Phase 4. The
  existing `ThreadPoolExecutor` timeout path waits for the worker to finish;
  Phase 4 must make timeout truly bounded or replace it with a process-based or
  cancellable path.
- **D-26:** New formal outputs must not use `vkm_per_trip` as an official
  field. Use `vkm_per_served_trip` and `vkm_per_original_request`.
- **D-27:** Phase 4 outputs must include `04_IMPLEMENTATION_AUDIT.md`,
  `04_BASELINE_VALIDATION.md`, `04_ALGORITHM_VALIDATION.md`, and
  `VARIANT_MAPPING.md`.

### the agent's Discretion
The planner may choose exact helper names, test file names, fixture layouts,
and diagnostic artifact filenames as long as the implementation preserves the
decisions above, stays within the Phase 4 boundary, and follows existing
`src/drt/`, `experiments/`, and `tests/` patterns.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project and Phase Definition
- `.planning/ROADMAP.md` - Phase 4 goal, requirements, success criteria, and
  expected outputs.
- `.planning/REQUIREMENTS.md` - ALG-01 through ALG-04 plus output,
  reproducibility, and formal experiment constraints that Phase 4 supports.
- `.planning/PROJECT.md` - Core value, TR-E rigor, strict phase gates,
  paired experiment constraints, and synthetic-data honesty.
- `.planning/STATE.md` - Current project status and blockers entering Phase 4.

### Prior Phase Contracts
- `.planning/phases/02-experimental-contract-and-metric-standardization/02-CONTEXT.md` - Shared-response requirement, status vocabulary, metric
  denominator contract, and coverage-control handoff.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_EXPERIMENT_CONTRACT.md` - Behavioral, supplementary, deterministic, and
  algorithm diagnostic evidence-family boundaries.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_BASELINE_TAXONOMY.md` - Four-axis taxonomy and required service-design
  baselines.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_PHASE45_CODE_TASKS.md` - Concrete downstream implementation and validation
  tasks for Phase 4/5.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_METRICS_DEFINITIONS.md` - Metric formulas, denominator rules, and forbidden
  metric language.
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_COVERAGE_CONFOUNDING_PLAN.md` - Matched-coverage and fixed accepted-set
  context that Phase 4 diagnostics must support.
- `.planning/phases/03-passenger-choice-model-rebuild/03-CONTEXT.md` - Phase 3
  choice decisions and Phase 4 handoff.
- `.planning/phases/03-passenger-choice-model-rebuild/03_CHOICE_MODEL_CONTRACT.md` - Actual-offer choice timing, status semantics, utility logging,
  and seeded type assignment contract.
- `.planning/phases/03-passenger-choice-model-rebuild/03_PARAMETER_CALIBRATION.md` - Choice parameter names, sensitivity scope, and source-label
  discipline.

### Codebase Maps
- `.planning/codebase/ARCHITECTURE.md` - Existing layered architecture,
  variant layer, metrics layer, runner flow, ALNS/MILP locations, and output
  flow.
- `.planning/codebase/TESTING.md` - Active pytest patterns and test locations.
- `.planning/codebase/CONCERNS.md` - Known issues affecting Phase 4: mixed
  import roots, route-stop fragility, runner timeout bug, MILP simplification,
  gamma semantics, and metric/test gaps.

### Source Integration Points
- `experiments/variants.py` - Current behavioral and diagnostic variants,
  legacy `_mnl_filter_requests`, variant registry, and record construction.
- `experiments/runner.py` - Result row construction, CSV writing, timeout
  handling, utility component output, and aggregate metric table writing.
- `experiments/metrics.py` - `PassengerRecord`, `SimulationResult`,
  `MetricsResult`, status-derived metrics, and formal metric names.
- `experiments/endogenous_matched_coverage.py` - Existing served-share cap
  diagnostic semantics that later pilots will smoke-test.
- `experiments/milp_gap.py` - Current MILP/ALNS gap diagnostic and limitations.
- `src/drt/choice.py` - Single-offer choice evaluation and
  feasibility-rejected evaluation helpers.
- `src/drt/types.py` - Shared dataclasses and utility log record structures.
- `src/drt/alns.py` - ALNS state, rolling-horizon controller, destroy/repair
  operators, and reoptimization loop.
- `src/drt/insertion.py` - Greedy feasible insertion evaluator used by
  baseline and repair paths.
- `src/drt/feasibility.py` - Feasibility checks and reason codes.
- `src/drt/milp.py` - Simplified static MILP diagnostic model and solver
  result schema.
- `tests/test_choice.py` - Existing choice helper and utility logging tests.
- `tests/test_variants.py` - Existing variant-level behavioral tests.
- `tests/test_runner.py` - Existing runner output and utility CSV tests.
- `tests/test_alns.py` - Existing ALNS operator and rolling-horizon tests.
- `tests/test_milp.py` - Existing Gurobi-gated MILP smoke tests.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `experiments/variants.py`: Existing `DoorToDoor`, `SingleSidedPickup`,
  `FullModel`, `AblationNoRollingHorizon`, and `AblationNoChoice` provide the
  starting point for concept-labeled behavioral and diagnostic methods.
- `src/drt/choice.py`: Existing choice evaluation and feasibility-rejected
  helper functions should anchor actual-offer choice validation and utility
  logging.
- `experiments/metrics.py`: Existing status-derived metrics already include
  `served_share`, `behavioral_acceptance_rate`, `choice_rejection_rate`, and
  `feasibility_rejection_rate`; Phase 4 should align names and outputs with
  Phase 2.
- `src/drt/alns.py`: Existing rolling-horizon and ALNS loops provide insertion
  points for convergence traces, operator statistics, and small multi-budget
  diagnostics.
- `src/drt/milp.py`: Existing `DRTModel` can remain a limited static snapshot
  diagnostic if its scope is documented and tests avoid license-dependent
  gating.

### Established Patterns
- Core algorithm code lives under `src/drt/`; experiment composition and CSV
  output live under `experiments/`; pytest tests live under `tests/`.
- New comparison behavior should be composed through `BaseVariant` subclasses
  and the variant registry rather than through root-script special cases.
- Optional Gurobi behavior should use skip/diagnostic paths and must not block
  non-MILP validation.
- Result artifacts are file-based CSV/JSON outputs under configurable result
  directories.

### Integration Points
- Add or validate `SingleSidedDropoff` near existing service-design variants.
- Add concept-label mapping and output fields in the variant/runner boundary,
  not by renaming stable classes first.
- Add tests that behavioral variants do not call `_mnl_filter_requests`.
- Add deterministic request-level random streams for passenger type and
  acceptance draw pairing.
- Add ALNS diagnostic artifact generation around `RollingHorizon.reoptimize()`
  or the relevant ALNS iteration loop.
- Fix timeout behavior in `experiments/runner.py` before Phase 5 pilot runs.

</code_context>

<specifics>
## Specific Ideas

- Use `method_label = BidirectionalMP_Choice_RH_ALNS` for the main concept
  label while retaining `legacy_class = FullModel` only for provenance.
- Include structured method fields such as `service_design = bidirectional_mp`,
  `choice_model = binary_logit`, `reoptimization = rolling_horizon`, and
  `routing_solver = alns`.
- Make `VARIANT_MAPPING.md` the bridge between historical code names and
  paper-safe conceptual labels.
- Treat the Phase 4 runtime-quality diagnostic as a small algorithm health
  check, not as formal runtime evidence.

</specifics>

<deferred>
## Deferred Ideas

None. Discussion stayed within Phase 4 scope.

</deferred>

---

*Phase: 4-Baseline and Algorithm Implementation Check*
*Context gathered: 2026-06-15T17:22:40+08:00*
