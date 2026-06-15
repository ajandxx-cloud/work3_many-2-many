---
phase: 05-pilot-experiments
status: passed
verified: 2026-06-15
requirements: [REP-03]
plans_verified: [05-01, 05-02, 05-03, 05-04]
---

# Phase 5 Verification

## Verification Complete

Status: `passed`

Phase 5 achieved its readiness goal: the small synthetic pilot matrix runs cleanly, persisted artifact checks pass, matched-coverage and fixed accepted-set diagnostics have been smoke-tested, and the Phase 5 blocker ledger has no unresolved rows blocking Phase 6 planning.

No formal claims are approved from these pilot outputs. Phase 5 remains a readiness gate only.

## Must-Have Results

| Criterion | Status | Evidence |
|---|---|---|
| Four main behavioral methods run on 3 synthetic pilot seeds at scale 20 | passed | `results/pilot/phase05/synthetic_results.csv` has 12 main behavioral rows |
| Main behavioral pilot has zero failed rows and zero timeout rows | passed | `validate_phase05_outputs(...)` reports `failed_rows: 0`, `timeout_rows: 0` |
| Persisted REP-03 status/provenance fields are present | passed | `validate_phase05_outputs(...)` passed schema/provenance checks; `REP-03` is marked complete |
| Utility/component logs are durable and joinable | passed | `validate_phase05_outputs(...)` reports 240 utility rows and passed joinability |
| Metric sanity checks pass for persisted main pilot rows | passed | Share fields in range; non-negative numeric fields; no NaN/infinity |
| Matched-coverage diagnostic passes tolerance | passed | Capped rows for seeds 42, 43, and 44 all have `abs_gap == 0.0000` with `tolerance == 0.03` |
| Fixed accepted-set smoke produces a retained set and routing diagnostic | passed | `fixed_accepted_set_smoke.json` has `retained_request_count: 16`, `status: passed`, and `routing_status: completed` |
| Gate report avoids formal claims and method-superiority framing | passed | `05_PILOT_RESULTS.md` preserves readiness-only and no-formal-claims language |
| Phase 6 readiness is controlled by bug ledger blockers | passed | `05_BUG_LEDGER.csv` has zero unresolved `blocks_phase6=true` rows |

## Automated Checks

```powershell
$env:PYTHONPATH='src'; pytest tests/test_phase05_pilot.py -q
```

Result: 15 passed.

```powershell
$env:PYTHONPATH='src'; python -m experiments.phase05_coverage_smoke
```

Result: matched coverage passed; fixed accepted-set smoke passed.

```powershell
$env:PYTHONPATH='src'; pytest tests/test_phase05_pilot.py tests/test_runner.py tests/test_metrics.py tests/test_variants.py -q
```

Result: 92 passed.

```powershell
$env:PYTHONPATH='src'; pytest tests -q
```

Result: 166 passed, 1 skipped.

```powershell
gsd-sdk query verify.schema-drift 05
```

Result: no schema drift detected.

## Code Review

`05-REVIEW.md` status: `clean`.

Reviewed files:

- `experiments/phase05_coverage_smoke.py`
- `tests/test_phase05_pilot.py`

Findings: 0 critical, 0 warning, 0 info.

## Codebase Drift Gate

The non-blocking codebase drift gate returned `directive: warn` for pre-existing structural drift under paths such as `.claude`, `paper_work3`, and temporary debug/test files. This warning does not block Phase 5 verification and was not introduced as part of the Phase 5 gap-closure source scope.

## Gap Closure Verification

### BUG-05-001

- Source: `results/pilot/phase05/matched_coverage_pilot.csv`
- Trigger: `scale=20 tolerance=0.03`, seed 42
- Rerun result: `matched_coverage_rerun_passed_seed42_target_count_1_gap_0.0000`
- Blocks Phase 6: no

### BUG-05-002

- Source: `results/pilot/phase05/matched_coverage_pilot.csv`
- Trigger: `scale=20 tolerance=0.03`, seed 44
- Rerun result: `matched_coverage_rerun_passed_seed44_target_count_2_gap_0.0000`
- Blocks Phase 6: no

### BUG-05-003

- Source: `results/pilot/phase05/fixed_accepted_set_smoke.json`
- Trigger: `scale=20 seed=42`
- Rerun result: `fixed_set_rerun_passed_candidate_serviceable_retained_16_routing_completed`
- Blocks Phase 6: no

## Carry-Forward Notes

- The seed 42 fixed-set repair uses `common_candidate_serviceable` because stricter served and actual-offer serviceable intersections are empty in the pilot data.
- This fallback is acceptable as a Phase 5 routing diagnostic repair, but Phase 6 should predeclare whether formal fixed accepted-set diagnostics use this fallback, a different seed/instance policy, or a stricter non-empty construction requirement.
- Pilot outputs must not be cited as formal evidence or method-superiority evidence.

## Gaps

None.

