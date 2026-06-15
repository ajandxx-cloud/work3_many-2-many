# Phase 5 Pilot Results

## Purpose

This is a readiness gate report for Phase 5 pilot experiments. It records whether the small synthetic pilot matrix, persisted artifact checks, matched-coverage smoke, and fixed accepted-set smoke are ready for Phase 6 planning.

No formal claims are made from these pilot outputs. They are not manuscript evidence, not paired-seed formal evidence, and not a method-superiority comparison.

## Run Matrix

- Scenario family: synthetic only
- Scale: 20 requests
- Seeds: 42, 43, 44
- Main behavioral methods:
  - DoorToDoor_Choice_CommonRouting
  - SingleSidedPickup_Choice_CommonRouting
  - SingleSidedDropoff_Choice_CommonRouting
  - BidirectionalMP_Choice_RH_ALNS
- Diagnostic methods:
  - DoorToDoor_Capped_MatchedCoverage
  - GreedyInsertionBaseline fixed accepted-set smoke

## Artifact Manifest

| Artifact | Role |
|---|---|
| `results/pilot/phase05/synthetic_results.csv` | Main behavioral pilot raw rows |
| `results/pilot/phase05/metrics_table.csv` | Aggregated pilot metrics |
| `results/pilot/phase05/utility_components.csv` | Utility/component logs |
| `results/pilot/phase05/matched_coverage_pilot.csv` | Matched-coverage readiness diagnostic |
| `results/pilot/phase05/fixed_accepted_set_smoke.json` | Fixed accepted-set smoke diagnostic |
| `results/pilot/phase05/plots/status_counts.png` | Diagnostic status-count plot |
| `results/pilot/phase05/plots/failure_timeout_counts.png` | Diagnostic failure/timeout plot |
| `results/pilot/phase05/plots/matched_coverage_gaps.png` | Diagnostic matched-coverage gap plot |
| `.planning/phases/05-pilot-experiments/05_BUG_LEDGER.csv` | Phase 6 blocker ledger |

## Gate Summary

Status: blocked for Phase 6 readiness.

The main behavioral pilot passed persisted schema, provenance, metric sanity, and utility joinability checks. There are zero failed rows and zero timeout rows in the main behavioral pilot.

Phase 6 is blocked by readiness diagnostics:

- `BUG-05-001`: seed 42 matched-coverage gap exceeds tolerance.
- `BUG-05-002`: seed 44 matched-coverage gap exceeds tolerance.
- `BUG-05-003`: fixed accepted-set common served intersection is empty, so the routing diagnostic did not run on a retained set.

## Schema and Provenance Checks

Command:

```powershell
$env:PYTHONPATH='src'; python -c "from experiments.phase05_pilot import MAIN_BEHAVIORAL_METHOD_LABELS; from experiments.pilot_validation import validate_phase05_outputs; import json; r=validate_phase05_outputs('results/pilot/phase05',[42,43,44],MAIN_BEHAVIORAL_METHOD_LABELS,20); print(json.dumps(r, indent=2))"
```

Result:

- `passed`: true
- `synthetic_results`: 12 rows
- `metrics_table`: 4 rows
- `utility_components`: 240 rows
- `main_behavioral_rows`: 12 rows
- `failed_rows`: 0
- `timeout_rows`: 0
- checked files include the main CSVs plus matched-coverage and fixed-set artifacts.

## Metric Sanity Checks

The validator passed all persisted metric sanity checks for the main behavioral pilot:

- Share/proportion fields are within `[0, 1]`.
- Distance, time, CPU/runtime, and detour fields are non-negative.
- Numeric pilot fields do not contain NaN or infinity.

Observed status counts in `synthetic_results.csv`:

| Status | Rows |
|---|---:|
| completed | 12 |

## Utility Log Joinability

The validator confirmed every completed main behavioral pilot run has joinable utility/component rows by `run_id`, `seed`, `scenario`, and variant identity.

Utility rows: 240.

## Matched-Coverage Smoke

Command:

```powershell
$env:PYTHONPATH='src'; python -m experiments.phase05_coverage_smoke
```

Matched-coverage result:

- target mean served share: 0.1333
- achieved DoorToDoorCapped mean served share: 0.1000
- absolute mean gap: 0.0333
- tolerance: 0.0300
- result: failed, blocks Phase 6

Blocking rows:

| Seed | Method | Gap | Tolerance | Status |
|---:|---|---:|---:|---|
| 42 | DoorToDoor_Capped_MatchedCoverage | 0.0833 | 0.0300 | failed |
| 44 | DoorToDoor_Capped_MatchedCoverage | 0.0333 | 0.0300 | failed |

## Fixed Accepted-Set Smoke

Artifact: `results/pilot/phase05/fixed_accepted_set_smoke.json`

Result:

- status: `empty_intersection`
- retained request count: 0
- retained share: 0.0
- routing diagnostic: `GreedyInsertionBaseline`
- routing status: `skipped_empty_intersection`
- evidence family: `algorithm_diagnostic`

This is a readiness problem because the fixed accepted-set smoke did not produce a retained set for routing diagnostics. It is recorded as `BUG-05-003` and blocks Phase 6 planning until resolved or explicitly redesigned.

## Bugs and Reruns

See `.planning/phases/05-pilot-experiments/05_BUG_LEDGER.csv`.

Current blocker count: 3.

No fixes or reruns have been applied yet.

## Phase 6 Readiness

Phase 6 is not ready to plan.

Required before Phase 6:

- Fix or redesign the matched-coverage cap/target logic so the pilot tolerance gate passes, then rerun `python -m experiments.phase05_coverage_smoke`.
- Resolve the empty fixed accepted-set intersection, either by revising the fixed-set construction or by documenting an approved diagnostic redesign, then rerun the smoke.
- Update `05_BUG_LEDGER.csv` with `fix_status=fixed` or a non-blocking approved disposition and record the rerun result.

## Limitations

- This pilot uses only 3 synthetic seeds at scale 20.
- The plots are diagnostic status/range artifacts only. They do not show or imply method wins or losses.
- The matched-coverage and fixed-set diagnostics are readiness checks, not formal supplementary evidence.
- No pilot result should be cited as proof that one service design is superior.

