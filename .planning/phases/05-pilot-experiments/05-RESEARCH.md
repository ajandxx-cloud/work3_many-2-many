# Phase 5 Research: Pilot Experiments

## RESEARCH COMPLETE

**Phase:** 05 - Pilot Experiments
**Requirement:** REP-03
**Date:** 2026-06-15

## Research Question

What does Phase 5 need to know to plan a small pilot experiment gate that finds bugs, verifies output durability, and prepares Phase 6 without creating formal manuscript evidence?

## Key Findings

### Runner Surface

`experiments/runner.py` already provides the closest execution surface:

- `run_all_experiments(scales=..., seeds=..., beijing=False, results_dir=...)` writes `synthetic_results.csv`, `beijing_results.csv`, `metrics_table.csv`, and `utility_components.csv`.
- Raw rows already include REP-03-critical durability fields: `status`, `detailed_reason`, `runtime_s`, `error_message`, `config_id`, `seed`, `scenario`, `method_label`, `artifact_dir`, and `git_commit_or_code_hash`.
- Timeout and exception paths persist durable rows through `_make_error_row(...)`, which prevents silent omission of failed runs.
- The runner currently executes every `ALL_VARIANTS` entry, including deterministic and algorithm diagnostics. Phase 5 needs a pilot-specific wrapper or filter so the main behavioral pilot uses exactly the four context-approved methods.

### Behavioral Method Boundary

`experiments/variants.py` exposes concept metadata from Phase 4:

- Main behavioral methods have `evidence_family = "behavioral_main"`.
- The four Phase 5 main methods are `DoorToDoor`, `SingleSidedPickup`, `SingleSidedDropoff`, and `FullModel`, with paper-facing `method_label` values `DoorToDoor_Choice_CommonRouting`, `SingleSidedPickup_Choice_CommonRouting`, `SingleSidedDropoff_Choice_CommonRouting`, and `BidirectionalMP_Choice_RH_ALNS`.
- `DoorToDoorCapped`, `BidirectionalNoChoice`, `GreedyInsertionBaseline`, `AblationNoRollingHorizon`, and `AblationNoChoice` must stay diagnostic or supplementary, not main pilot evidence.

### Metric and Schema Checks

`experiments/metrics.py` supports the range checks needed by Phase 5:

- Ratio fields: `acceptance_rate`, `served_share`, `behavioral_acceptance_rate`, `choice_rejection_rate`, `feasibility_rejection_rate`, `detour_ratio`, and `fairness_index`.
- Non-negative fields: `vehicle_km`, `vkm_per_served_trip`, `vkm_per_original_request`, `avg_wait`, `p95_wait`, `avg_walk`, `avg_ivt`, `cpu_time`, and `runtime_s`.
- `compute_metrics(...)` is status-aware, so choice rejection and feasibility rejection can be audited separately.

The pilot should add a validator that checks the persisted CSV/JSON artifacts, not just in-memory return values. This protects Phase 6 from schema drift.

### Utility Log Joinability

`runner.py` writes `utility_components.csv` with `run_id`, `seed`, `scenario`, `method`, and `request_id`. Phase 5 should verify:

- Every completed main behavioral run has one utility row per original request.
- Utility logs are joinable to raw result rows by `run_id`, `seed`, `scenario`, and method identity.
- Feasibility rows may lack utility components, but non-feasibility offer rows must carry offer and probability fields.

### Matched-Coverage Readiness

`experiments/endogenous_matched_coverage.py` contains the closest existing served-share cap control, but it is hard-coded for `SWEEP_SCALE = 200`, writes to `results/endogenous_matched_coverage.csv`, and warns instead of returning a blocking gate result.

Phase 5 should turn the idea into a pilot-scale diagnostic:

- Use the Phase 5 pilot seeds and a small scale such as `n_requests=20`.
- Record target served share, achieved served share, absolute tolerance gap, and pass/fail state.
- Treat tolerance failure as a Phase 5 blocker, matching D-16.
- Keep output in `results/pilot/phase05/`, not in formal result paths.

### Fixed Accepted-Set Smoke

`experiments/milp_gap.py` demonstrates durable diagnostic rows and the no-Gurobi path. Phase 5 needs a smaller fixed accepted-set smoke:

- Build a common serviceable/accepted request intersection across the main methods for one pilot scenario or the pilot seed set.
- Run at least one routing diagnostic on that fixed set, preferably `GreedyInsertionBaseline` or the existing MILP gap path when available.
- If Gurobi is absent, record `status = "no_gurobi"` and keep the row non-blocking.
- Do not promote fixed-set output to manuscript evidence.

### Testing Patterns

Existing tests already cover many Phase 5 prerequisites:

- `tests/test_runner.py` checks runner CSV columns, utility-component columns, timeout rows, and failed rows.
- `tests/test_variants.py` checks the shared actual-offer choice path, metadata, and behavioral method identity.
- `tests/test_metrics.py` checks range and denominator behavior.

Phase 5 should extend these tests rather than add a separate framework.

## Implementation Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Main pilot accidentally includes diagnostics | Pilot report can mix evidence families | Filter to `evidence_family == "behavioral_main"` and exact method labels |
| Pilot files overwrite formal outputs | Phase 6 evidence chain becomes ambiguous | Write only under `results/pilot/phase05/` |
| Runner success hides missing utility logs | Acceptance behavior cannot be explained | Add persisted joinability checks |
| Matched-coverage warning is ignored | Phase 6 controls remain unready | Convert tolerance failure into a blocking gate |
| Optional Gurobi absence blocks Phase 5 | Pilot becomes environment-dependent | Record `no_gurobi` diagnostic row as non-blocking |
| Pilot plots imply method superiority | Review-facing overclaiming risk | Use diagnostic status/range/missingness plots only |

## Recommended Plan Shape

1. Add a pilot harness and validation module that runs exactly the four behavioral methods on 3 seeds at small scale and validates persisted outputs.
2. Add pilot-scale matched-coverage and fixed accepted-set smoke diagnostics with durable rows.
3. Execute the pilot gate, write `05_PILOT_RESULTS.md`, create diagnostic plots, maintain a bug ledger, and block Phase 6 on unresolved core failures.

## Validation Architecture

Use the existing pytest stack.

- Quick command: `PYTHONPATH=src pytest tests/test_runner.py tests/test_metrics.py tests/test_variants.py -q`
- Phase 5 focused command after implementation: `PYTHONPATH=src pytest tests/test_phase05_pilot.py -q`
- Smoke execution command after implementation: `PYTHONPATH=src python -m experiments.phase05_pilot`

Validation must sample persisted artifacts in `results/pilot/phase05/`:

- `synthetic_results.csv`
- `metrics_table.csv`
- `utility_components.csv`
- `matched_coverage_pilot.csv` or equivalent
- `fixed_accepted_set_smoke.json` or equivalent
- `bug_ledger.csv` or equivalent
- `05_PILOT_RESULTS.md`

## Planning Inputs

Downstream plans must read:

- `.planning/phases/05-pilot-experiments/05-CONTEXT.md`
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_BASELINE_VALIDATION.md`
- `.planning/phases/04-baseline-and-algorithm-implementation-check/04_ALGORITHM_VALIDATION.md`
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_PHASE45_CODE_TASKS.md`
- `experiments/runner.py`
- `experiments/variants.py`
- `experiments/metrics.py`
- `experiments/endogenous_matched_coverage.py`
- `experiments/milp_gap.py`
- `tests/test_runner.py`
- `tests/test_metrics.py`
- `tests/test_variants.py`

