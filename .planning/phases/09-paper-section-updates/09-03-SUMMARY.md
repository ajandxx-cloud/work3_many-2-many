---
phase: 09-paper-section-updates
plan: "03"
subsystem: experiments
tags: [weight-sensitivity, REV-12, table, experiments]
dependency_graph:
  requires: []
  provides: [tab:weight-sensitivity, subsec:weight-sensitivity, results/weight_sensitivity.json]
  affects: [paper/sections/experiments.tex]
tech_stack:
  added: []
  patterns: [variant instantiation with cost_weights, vkm-per-trip normalization]
key_files:
  created:
    - experiments/weight_sensitivity.py
    - results/weight_sensitivity.json
  modified:
    - experiments/variants.py
    - paper/sections/experiments.tex
decisions:
  - "Added optional cost_weights param to FullModel and DoorToDoor constructors (non-invasive; defaults to existing _COST_WEIGHTS)"
  - "Script instantiates variant classes directly rather than using runner.run_all_experiments (no run_variant helper existed)"
  - "vkm_per_trip = vehicle_km / acceptance_rate; guarded against zero denominator (T-09-07)"
metrics:
  duration: ~8min
  completed: 2026-04-12
  tasks_completed: 2
  files_changed: 4
---

# Phase 09 Plan 03: Weight Sensitivity Analysis Summary

Weight sensitivity experiment for REV-12: FullModel reduces vkm/trip by 30-31% vs DoorToDoor under all three objective weight configurations (efficiency-focused, equity-focused, balanced), confirming the efficiency claim is robust to alpha weight choice.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing critical functionality] Added cost_weights parameter to FullModel and DoorToDoor**
- **Found during:** Task 1 — runner.py has no `run_variant()` helper; variants use module-level `_COST_WEIGHTS` hardcoded at import time
- **Fix:** Added optional `cost_weights: tuple | None = None` to both constructors; defaults to `_COST_WEIGHTS` so existing behavior is unchanged
- **Files modified:** `experiments/variants.py`
- **Commit:** d1d612a

**2. [Rule 2 - Missing critical functionality] Script uses direct variant instantiation instead of runner API**
- **Found during:** Task 1 — `run_variant` function referenced in plan does not exist in runner.py
- **Fix:** `weight_sensitivity.py` instantiates `FullModel(cost_weights=alpha)` and `DoorToDoor(cost_weights=alpha)` directly, calls `.run(scenario)` and `compute_metrics()` — same pattern used internally by runner
- **Files modified:** `experiments/weight_sensitivity.py`

## Results Summary

| Config | FM vkm/trip | DD vkm/trip | Reduction |
|--------|-------------|-------------|-----------|
| Efficiency-focused (IVT=2.0) | 2155 ± 378 | 3107 ± 128 | 30.8% |
| Equity-focused (wait=walk=2.0) | 2135 ± 524 | 3093 ± 170 | 31.4% |
| Balanced (baseline) | 2121 ± 425 | 3040 ± 151 | 30.5% |

FullModel beats DoorToDoor in all 9 individual runs (3 configs × 3 seeds).

## Self-Check: PASSED

- `experiments/weight_sensitivity.py` exists and imports cleanly
- `results/weight_sensitivity.json` exists with 9 rows
- `paper/sections/experiments.tex` contains `\label{tab:weight-sensitivity}` at line 331
- `paper/sections/experiments.tex` contains `\label{subsec:weight-sensitivity}` at line 311
- Commits d1d612a and 4fad649 present in git log
