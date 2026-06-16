---
phase: 06-formal-synthetic-experiments
plan: 06-02
subsystem: experiments
tags: [phase06, formal, main-behavioral, exp-05]
requires:
  - phase: 06-formal-synthetic-experiments
    plan: 06-01
    provides: formal harness, manifests, validators, label implementation gate
provides:
  - 20-seed paired formal main behavioral matrix
  - validated raw, processed, utility, manifest, and validation artifacts
  - denominator, schema, utility linkage, and label implementation checks
affects: [phase06-formal-experiments, exp-05, phase08-claim-gate, phase10-final-verification]
tech-stack:
  added: []
  patterns: [formal paired matrix execution, artifact aliasing, denominator validation]
key-files:
  created:
    - results/formal/phase06/main_behavioral/raw_results.csv
    - results/formal/phase06/main_behavioral/processed_results.csv
    - results/formal/phase06/main_behavioral/utility_logs.csv
    - results/formal/phase06/main_behavioral/config_manifest.json
    - results/formal/phase06/main_behavioral/seed_manifest.json
    - results/formal/phase06/main_behavioral/run_manifest.json
    - results/formal/phase06/main_behavioral/validation_report.json
    - .planning/phases/06-formal-synthetic-experiments/06-02-SUMMARY.md
  modified:
    - experiments/phase06_formal.py
    - experiments/formal_validation.py
    - experiments/runner.py
    - tests/test_phase06_formal.py
    - .planning/STATE.md
key-decisions:
  - "Formal 06-02 evidence uses exactly required seeds 1-20; optional seeds 21-30 were not attempted or included."
  - "The user-facing artifact contract is written under results/formal/phase06/main_behavioral while legacy harness filenames remain as compatibility aliases."
  - "inserted_share is not reported as a behavioral-main metric; deterministic inserted share remains a separate diagnostic metric and is not mixed with served_share or behavioral acceptance."
requirements-completed: []
duration: 44 min
completed: 2026-06-16
status: passed
---

# Phase 06 Plan 02: Main Behavioral Formal Matrix Summary

## Execution Command

```powershell
$env:PYTHONPATH='src'; python -m experiments.phase06_formal --family main --scales 100 200 300 500 --seeds 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 --results-dir results/formal/phase06/main_behavioral
$env:PYTHONPATH='src'; python -m experiments.phase06_formal --validate --results-dir results/formal/phase06/main_behavioral
```

Preflight smoke was run and validated separately in `results/formal/phase06/smoke`; smoke artifacts are not counted as formal evidence.

## Run Identity

- Git commit before run: `d7798a1`
- Started: `2026-06-16T06:18:38.380037+00:00`
- Finished and validated: `2026-06-16T07:02:40.851369+00:00`
- Output directory: `results/formal/phase06/main_behavioral`
- Required row count: `20 seeds x 4 scales x 4 methods = 320`
- Actual raw row count: `320`
- Passed: `true`
- Blockers: none

## Matrix Definition

- Seed list: `1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20`
- Scale list: `100, 200, 300, 500`
- Method list:
  - `DoorToDoor_Choice_CommonRouting`
  - `SingleSidedPickup_Choice_CommonRouting`
  - `SingleSidedDropoff_Choice_CommonRouting`
  - `BidirectionalMP_Choice_RH_ALNS`

Optional seeds `21-30` were not attempted in this plan closeout and are not included in the main evidence base.

## Completeness Checks

| Check | Result |
|---|---:|
| Expected rows | 320 |
| Actual rows | 320 |
| Completed rows | 320 |
| Failed rows | 0 |
| Timeout rows | 0 |
| Infeasible/blocking rows | 0 |
| Missing seed x scale x method cells | 0 |
| Extra cells | 0 |
| Utility rows | 88,000 |
| Unlinked completed runs in utility logs | 0 |
| Schema drift | false |
| Validator passed | true |

## Per-Method Rows

| Method | Rows |
|---|---:|
| `BidirectionalMP_Choice_RH_ALNS` | 80 |
| `DoorToDoor_Choice_CommonRouting` | 80 |
| `SingleSidedDropoff_Choice_CommonRouting` | 80 |
| `SingleSidedPickup_Choice_CommonRouting` | 80 |

## Per-Scale Rows

| Scale | Rows |
|---:|---:|
| 100 | 80 |
| 200 | 80 |
| 300 | 80 |
| 500 | 80 |

## Main Metrics Summary

Means across the 80 paired cells for each method:

| Method | total_vehicle_km | vehicle_km_per_served_trip | vehicle_km_per_original_request | served_share | behavioral_acceptance_rate | feasibility_rejection_rate | choice_rejection_rate | runtime_s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `BidirectionalMP_Choice_RH_ALNS` | 444.491 | 9.951 | 1.569 | 0.158 | 0.460 | 0.303 | 0.540 | 14.498 |
| `DoorToDoor_Choice_CommonRouting` | 772.698 | 14.665 | 2.900 | 0.200 | 0.437 | 0.237 | 0.563 | 3.634 |
| `SingleSidedDropoff_Choice_CommonRouting` | 710.948 | 13.907 | 2.662 | 0.194 | 0.451 | 0.258 | 0.549 | 6.199 |
| `SingleSidedPickup_Choice_CommonRouting` | 715.579 | 13.683 | 2.741 | 0.199 | 0.456 | 0.256 | 0.544 | 6.551 |

`total_vehicle_km` is stored as an explicit alias of the legacy `vehicle_km` column for the formal raw results. `inserted_share` is not used for this behavioral-main matrix because Phase 2 separates deterministic inserted-share diagnostics from behavioral served-share and passenger-response metrics.

## Paired Difference Summary

Values are FullModel minus comparator across the same `seed x scale` pairs (`n=80` each).

| Comparator | Metric | Mean diff | Median diff | Min diff | Max diff |
|---|---|---:|---:|---:|---:|
| DoorToDoor | total_vehicle_km | -328.207 | -301.877 | -903.302 | 2.664 |
| DoorToDoor | vehicle_km_per_served_trip | -4.714 | -4.467 | -16.823 | 0.000 |
| DoorToDoor | vehicle_km_per_original_request | -1.332 | -1.299 | -3.020 | 0.027 |
| DoorToDoor | served_share | -0.043 | -0.040 | -0.150 | 0.070 |
| DoorToDoor | behavioral_acceptance_rate | 0.024 | 0.040 | -0.213 | 0.307 |
| SingleSidedDropoff | total_vehicle_km | -266.456 | -241.437 | -608.144 | 2.615 |
| SingleSidedDropoff | vehicle_km_per_served_trip | -3.956 | -3.555 | -16.873 | 0.000 |
| SingleSidedDropoff | vehicle_km_per_original_request | -1.094 | -0.964 | -3.017 | 0.026 |
| SingleSidedDropoff | served_share | -0.036 | -0.034 | -0.120 | 0.040 |
| SingleSidedDropoff | behavioral_acceptance_rate | 0.009 | 0.010 | -0.180 | 0.180 |
| SingleSidedPickup | total_vehicle_km | -271.088 | -270.999 | -549.846 | 0.000 |
| SingleSidedPickup | vehicle_km_per_served_trip | -3.732 | -3.761 | -9.208 | 0.000 |
| SingleSidedPickup | vehicle_km_per_original_request | -1.172 | -0.957 | -2.983 | 0.000 |
| SingleSidedPickup | served_share | -0.042 | -0.036 | -0.170 | 0.037 |
| SingleSidedPickup | behavioral_acceptance_rate | 0.005 | 0.005 | -0.187 | 0.210 |

This summary is descriptive only. It does not write final manuscript claims.

## Validator Result

`results/formal/phase06/main_behavioral/validation_report.json` reports:

- `passed: true`
- `schema_drift: false`
- `failed_rows: 0`
- `timeout_rows: 0`
- `main_behavioral_rows: 320`
- `utility_components: 88000`
- Label implementation gate: passed for `BidirectionalMP_Choice_RH_ALNS`
- Denominator checks: passed for `served_share`, `vehicle_km_per_served_trip`, `vehicle_km_per_original_request`, `behavioral_acceptance_rate`, rejection partition, and `total_vehicle_km` alias

## Artifacts

- `results/formal/phase06/main_behavioral/raw_results.csv`
- `results/formal/phase06/main_behavioral/processed_results.csv`
- `results/formal/phase06/main_behavioral/utility_logs.csv`
- `results/formal/phase06/main_behavioral/config_manifest.json`
- `results/formal/phase06/main_behavioral/seed_manifest.json`
- `results/formal/phase06/main_behavioral/run_manifest.json`
- `results/formal/phase06/main_behavioral/validation_report.json`
- Compatibility aliases retained: `synthetic_results.csv`, `metrics_table.csv`, `utility_components.csv`, `formal_config_manifest.json`, `formal_seed_manifest.json`, `formal_run_manifest.json`, `main_matrix_validation.json`

## Tests

```powershell
$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py -q
# 12 passed

$env:PYTHONPATH='src'; pytest tests/test_phase06_formal.py tests/test_runner.py tests/test_metrics.py tests/test_variants.py -q
# 89 passed
```

## Outcome

Plan 06-02 passed. Phase 6 may proceed to Plan 06-03 next. Do not treat this as permission to enter Phase 7, Phase 8, or Phase 10, and do not use this summary to write final manuscript claims without the later Phase 6 report and Phase 8 claim gate.
