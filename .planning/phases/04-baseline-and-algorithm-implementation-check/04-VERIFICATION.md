---
status: passed
phase: 04-baseline-and-algorithm-implementation-check
verified: 2026-06-15
requirements: [ALG-01, ALG-02, ALG-03, ALG-04]
---

# Phase 04 Verification: Baseline and Algorithm Implementation Check

## Verdict

Passed. Phase 04 satisfies the roadmap goal: all baselines and algorithms are
implemented consistently enough for Phase 5 pilot runs, with behavioral,
diagnostic, schema, failure-row, ALNS, and MILP boundaries documented and tested.

## Roadmap Success Criteria

| Criterion | Status | Evidence |
|---|---|---|
| All required baselines run on a small scenario. | Passed | `DoorToDoor`, `SingleSidedPickup`, `SingleSidedDropoff`, `FullModel`, and diagnostics run in `tests/test_variants.py`. |
| Behavioral variants use consistent passenger-response assumptions. | Passed | Actual-offer choice tests verify no `_mnl_filter_requests` dependency, request-level type pairing, rejected request exclusion, and walking-side contracts. |
| Deterministic diagnostics are separate. | Passed | `method_metadata`, `VARIANT_MAPPING.md`, and tests separate `behavioral_main`, `deterministic_diagnostic`, and `algorithm_diagnostic` rows. |
| Feasibility, route commitment, ALNS, and MILP diagnostic scope are verified. | Passed | Feasibility/insertion/ALNS/MILP suites pass; `04_ALGORITHM_VALIDATION.md` documents route-stop limits, ALNS traces, and MILP static snapshot scope. |
| Output schema is identical across methods and records failure rows. | Passed | Runner schema tests cover method/provenance/status/count fields, timeout rows, failure rows, utility joins, and explicit vehicle-km denominators. |

## Requirement Trace

| Requirement | Status | Evidence |
|---|---|---|
| ALG-01 | Passed | Feasibility, route commitment, tagged stops, completed IDs, pickup times, and walking-radius tests. |
| ALG-02 | Passed | Behavioral baselines, greedy/no-RH diagnostics, method metadata, and comparable diagnostic schema. |
| ALG-03 | Passed | Optional ALNS trace entries, operator counts, improvement counts, and multi-budget smoke diagnostics. |
| ALG-04 | Passed | Static MILP boundary, pure-Python tiny fixtures, no-Gurobi row, and comparable-gap suppression. |

## Automated Checks

```bash
PYTHONPATH=src pytest tests/test_choice.py tests/test_variants.py tests/test_runner.py tests/test_metrics.py tests/test_feasibility.py tests/test_insertion.py tests/test_alns.py tests/test_milp.py -q
```

Result: 114 passed, 1 skipped.

Additional focused checks executed during plan close-out:

- `PYTHONPATH=src pytest tests/test_variants.py -q`: 21 passed at `04-01`; later expanded suite passed in phase verification.
- `PYTHONPATH=src pytest tests/test_runner.py tests/test_metrics.py -q`: 54 passed.
- `PYTHONPATH=src pytest tests/test_feasibility.py tests/test_insertion.py tests/test_alns.py tests/test_variants.py -q`: 42 passed.
- `PYTHONPATH=src pytest tests/test_milp.py -q`: 7 passed, 1 skipped.
- `PYTHONPATH=src python -m experiments.algorithm_diagnostics`: emitted 5, 20, and 50 budget rows with objective/runtime/operator/accepted/unassigned fields.

## Drift Gates

- Schema drift: passed, `drift_detected=false`.
- Codebase drift: non-blocking warning. The SDK reported pre-existing structural churn outside this phase, primarily `.claude`, old debug scripts, and `paper_work3`. Per gate contract, this does not block Phase 04 verification.

## Human Verification

None required. Phase 04 is code, tests, and documentation validation; no external service or manual UI path is required.

## Gaps

None.

## Residual Caveats

- Gurobi-backed solve coverage remains optional and environment-dependent; pure-Python MILP diagnostics and no-Gurobi rows are covered.
- Legacy diagnostic scripts outside the new runner path still contain `vkm_per_trip` naming. New Phase 04 formal runner outputs use `vkm_per_served_trip` and `vkm_per_original_request`.
- Route stops are still tuple-based; Phase 04 added guard tests, but a future route-stop dataclass would reduce fragility.

