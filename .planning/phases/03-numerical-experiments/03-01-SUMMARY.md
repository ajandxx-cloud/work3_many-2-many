---
phase: 03-numerical-experiments
plan: 01
subsystem: experiment-infrastructure
tags: [scenarios, metrics, config, tdd, python]
dependency_graph:
  requires: [src/drt/types.py]
  provides: [experiments/config.py, experiments/scenarios.py, experiments/metrics.py]
  affects: [experiments/variants.py, experiments/runner.py]
tech_stack:
  added: [numpy (for percentile and Gini)]
  patterns: [TDD (RED-GREEN), dataclass contracts, local PRNG for reproducibility]
key_files:
  created:
    - experiments/__init__.py
    - experiments/config.py
    - experiments/scenarios.py
    - experiments/metrics.py
    - tests/test_scenarios.py
    - tests/test_metrics.py
decisions:
  - "Use random.Random(seed) (local PRNG) instead of global random to ensure reproducibility without side effects"
  - "Gini via sorted-array O(n log n) formula rather than pairwise O(n^2) — equivalent results, better performance at scale 500"
  - "Beijing meeting point spacing follows exact plan formula (15000/8 = 1875m), not literal 500m (which would require 30x30=900 points)"
  - "T-03-03 mitigation: ValueError for n_requests > 1000 in both generators"
metrics:
  duration: "252 seconds (~4 minutes)"
  completed: "2026-04-11"
  tasks_total: 2
  tasks_completed: 2
  tests_added: 64
  tests_passing: 64
  files_created: 6
---

# Phase 3 Plan 01: Experiment Infrastructure Summary

**One-liner:** Shared experiment infrastructure — config constants, synthetic/Beijing scenario generators with OOM guard, and 9-metric computation with Gini fairness index.

## Files Created

| File | Purpose |
|------|---------|
| `experiments/__init__.py` | Package marker |
| `experiments/config.py` | Shared constants: RANDOM_SEED, SCALES, VEHICLE_COUNTS, K_TOP, RHO_P/D, H_WINDOW, DELTA, ALPHA_WEIGHTS |
| `experiments/scenarios.py` | `generate_synthetic` (20km, 100 MPs) and `generate_beijing` (15km, 80 MPs, morning peak) |
| `experiments/metrics.py` | `PassengerRecord`, `SimulationResult`, `MetricsResult`, `compute_metrics` |
| `tests/test_scenarios.py` | 30 tests covering counts, bounds, reproducibility, time windows, cap enforcement |
| `tests/test_metrics.py` | 34 tests covering empty result, Gini cases, p95, detour ratio, acceptance rate |

## Key Design Decisions

### Scenario dataclass contract
`Scenario(requests, vehicles, meeting_points, area_km, name)` is the data contract between generators and variant algorithms. The `area_km` field enables variants to infer coordinate bounds without hard-coding them.

### SimulationResult contract
`SimulationResult(records, total_vehicle_km, cpu_time)` is the output contract from any variant. `PassengerRecord` captures per-passenger outcome including accepted/rejected flag, walking distances, IVT, direct time, and MNL disutility — sufficient to compute all 9 metrics.

### Reproducibility via local PRNG
Both generators use `random.Random(seed)` (not the global `random` module) so that generator calls in different orders don't contaminate each other's sequences. This is essential for multi-run experiments where three seeds [42, 43, 44] are used.

### Gini coefficient implementation
Used sorted-array O(n log n) formula rather than the naive O(n^2) pairwise sum. Both are mathematically equivalent; the sorted formula is significantly faster for n=500 acceptance records.

### Beijing meeting point grid
The plan says "~500m spacing" but specifies a 9×9 grid on 15km. A true 500m spacing would require a 30×30 grid (900 points). The plan's grid formula (`x = i * (15000/8)`) gives 1875m spacing, which is correct for 80 points on a 15km area. Implemented exactly per the formula.

## Deviations from Plan

None — plan executed exactly as written. The "~500m spacing" note in the plan description is inconsistent with the actual formula given; the formula was followed as the authoritative specification.

## Test Results

```
tests/test_scenarios.py  30 passed
tests/test_metrics.py    34 passed
Total: 64 passed in 0.11s
```

All plan verification commands pass:
- `from experiments.config import RANDOM_SEED, SCALES` → `config OK`
- `generate_synthetic(100,10,42)` → `100 requests, 100 meeting points`
- `compute_metrics(SimulationResult([],0.0,0.0)).acceptance_rate` → `0.0`

## Commits

| Hash | Message |
|------|---------|
| fff86d9 | test(03-01): add failing tests for scenario generators |
| cedf2a3 | feat(03-01): implement experiment config and scenario generators |
| 724582a | test(03-01): add failing tests for metrics computation |
| c1a9c0e | feat(03-01): implement metrics computation module (9 metrics + Gini) |

## Self-Check: PASSED

- [x] `experiments/__init__.py` exists
- [x] `experiments/config.py` exists and importable
- [x] `experiments/scenarios.py` exists and importable
- [x] `experiments/metrics.py` exists and importable
- [x] `tests/test_scenarios.py` exists (30 tests)
- [x] `tests/test_metrics.py` exists (34 tests)
- [x] All commits verified in git log
- [x] 64/64 tests pass
