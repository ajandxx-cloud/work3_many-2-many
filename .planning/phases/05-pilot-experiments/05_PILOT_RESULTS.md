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

Status: passed for Phase 6 readiness after gap-closure rerun.

The main behavioral pilot passed persisted schema, provenance, metric sanity, and utility joinability checks. There are zero failed rows and zero timeout rows in the main behavioral pilot.

Original readiness diagnostics found three blockers:

- `BUG-05-001`: seed 42 matched-coverage gap exceeds tolerance.
- `BUG-05-002`: seed 44 matched-coverage gap exceeds tolerance.
- `BUG-05-003`: fixed accepted-set common served intersection is empty, so the routing diagnostic did not run on a retained set.

The gap-closure rerun closed all three blocker IDs. Phase 6 planning may proceed after verification reruns, but this report remains readiness-only and still makes no formal claims.

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

- target mean served share: 0.1000
- achieved DoorToDoorCapped mean served share: 0.1000
- maximum per-seed absolute gap: 0.0000
- tolerance: 0.0300
- result: passed

Rerun capped-control rows:

| Seed | Method | Gap | Tolerance | Status |
|---:|---|---:|---:|---|
| 42 | DoorToDoor_Capped_MatchedCoverage | 0.0000 | 0.0300 | passed |
| 43 | DoorToDoor_Capped_MatchedCoverage | 0.0000 | 0.0300 | passed |
| 44 | DoorToDoor_Capped_MatchedCoverage | 0.0000 | 0.0300 | passed |

Corrected target semantics:

- Targets are computed per seed as integer request counts.
- The original FullModel served count/share is persisted in `original_fullmodel_served_count` and `original_fullmodel_served_share`.
- The adjusted target uses `target_count = min(FullModel served count, uncapped DoorToDoorCapped serviceable count)`.
- Seed 42 adjusts from 3 FullModel served requests to an attainable capped target of 1 request; seeds 43 and 44 keep their FullModel target counts.
- Tolerance remains `0.03`; no threshold was loosened.

## Fixed Accepted-Set Smoke

Artifact: `results/pilot/phase05/fixed_accepted_set_smoke.json`

Result:

- status: `passed`
- construction rule: `common_candidate_serviceable`
- served intersection count: 0
- serviceable intersection count: 0
- candidate-serviceable intersection count: 16
- retained request count: 16
- retained share: 0.8
- routing diagnostic: `GreedyInsertionBaseline`
- routing status: `completed`
- evidence family: `algorithm_diagnostic`

The served and actual-offer serviceable intersections are still empty for seed 42, because `SingleSidedDropoff` produces no served or choice-rejected offers in this small pilot seed. The rerun therefore uses the explicit `common_candidate_serviceable` fallback: requests whose utility rows show candidate service geometry across the four main methods (`detailed_reason != no_candidate_mp`). This is a routing diagnostic fallback only; it must not be interpreted as behavioral acceptance or market evidence.

## Gap Closure Rerun

Commands:

```powershell
$env:PYTHONPATH='src'; pytest tests/test_phase05_pilot.py -q
$env:PYTHONPATH='src'; python -m experiments.phase05_coverage_smoke
```

Artifacts:

- `results/pilot/phase05/matched_coverage_pilot.csv`
- `results/pilot/phase05/fixed_accepted_set_smoke.json`
- `.planning/phases/05-pilot-experiments/05_BUG_LEDGER.csv`

Closed blocker IDs:

- `BUG-05-001`: fixed by per-seed integer target count; seed 42 capped row gap is `0.0000`.
- `BUG-05-002`: fixed by per-seed integer target count; seed 44 capped row gap is `0.0000`.
- `BUG-05-003`: fixed by explicit fixed-set construction fallback; seed 42 retains 16 requests and completes `GreedyInsertionBaseline`.

## Bugs and Reruns

See `.planning/phases/05-pilot-experiments/05_BUG_LEDGER.csv`.

Current blocker count: 0.

All Phase 5 blocker rows have `fix_status=fixed` and `blocks_phase6=false`.

## Phase 6 Readiness

Phase 6 is ready to plan after verification reruns.

Carry forward into Phase 6:

- Treat the seed 42 `common_candidate_serviceable` fallback as a pilot diagnostic repair, not as formal fixed accepted-set evidence.
- Revisit fixed accepted-set construction during formal Phase 6 design if strict served or actual-offer serviceable intersections remain empty.
- Keep matched-coverage targets as predeclared integer counts and report any target adjustment explicitly.

## Limitations

- This pilot uses only 3 synthetic seeds at scale 20.
- The plots are diagnostic status/range artifacts only. They do not show or imply method wins or losses.
- The matched-coverage and fixed-set diagnostics are readiness checks, not formal supplementary evidence.
- No pilot result should be cited as proof that one service design is superior.
