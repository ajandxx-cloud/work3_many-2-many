---
phase: 04-policy-analysis-sensitivity-analysis
plan: "01"
subsystem: analysis
tags: [sensitivity-analysis, walking-tolerance, fleet-size, policy, csv]
dependency_graph:
  requires: [experiments/config.py, experiments/scenarios.py, experiments/variants.py, experiments/metrics.py]
  provides: [analysis/sensitivity.py, results/sensitivity_walk.csv, results/sensitivity_fleet.csv]
  affects: [04-02-PLAN.md, 04-03-PLAN.md]
tech_stack:
  added: []
  patterns: [constructor-injection for rho parameters, csv.DictWriter for output]
key_files:
  created:
    - analysis/sensitivity.py
    - analysis/test_sensitivity.py
    - results/sensitivity_walk.csv
    - results/sensitivity_fleet.csv
  modified:
    - experiments/variants.py
decisions:
  - "Added rho_p/rho_d constructor params to FullModel and DoorToDoor instead of monkey-patching config (T-04-01 mitigation)"
  - "DoorToDoor uses float('inf') internally so rho params are accepted for API consistency but do not affect routing"
  - "16 rows in walk CSV: 6 rho x 2 variants (standard) + 2 density tier rows (FullModel only at rho=500)"
metrics:
  duration: "~5 minutes"
  completed: "2026-04-12"
  tasks_completed: 2
  files_created: 4
  files_modified: 1
---

# Phase 4 Plan 1: Sensitivity Sweeps for Walking Tolerance and Fleet Size Summary

Implemented two sensitivity sweep functions producing CSV evidence for POLICY-02, POLICY-03, and POLICY-06 policy recommendations: walking tolerance sweep (6 rho values x 2 variants + 2 city-tier rows) and fleet size sweep (6 fleet sizes x 2 variants).

## Artifacts Produced

- `analysis/sensitivity.py` — `sweep_walking_tolerance()` and `sweep_fleet_size()` functions
- `results/sensitivity_walk.csv` — 14 rows: rho, variant, acceptance_rate, vehicle_km, avg_walk, avg_wait, density_tier
- `results/sensitivity_fleet.csv` — 12 rows: n_vehicles, variant, acceptance_rate, vehicle_km, avg_wait
- `analysis/test_sensitivity.py` — 10 TDD tests, all passing

## Decisions Made

1. Constructor injection for rho parameters (not monkey-patching) — satisfies T-04-01 threat mitigation, thread-safe
2. `DoorToDoor` accepts rho params for API consistency but routes to origin/destination with `float('inf')` radius
3. City-tier rows (POLICY-06) use FullModel only at rho=500 (midpoint), appended after main sweep

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing functionality] Added `__init__` to DoorToDoor variant**
- Found during: Task 1
- Issue: Plan specified adding rho_p/rho_d constructor params to FullModel and DoorToDoor; DoorToDoor had no `__init__`
- Fix: Added `__init__(self, rho_p=None, rho_d=None)` to DoorToDoor for API consistency with FullModel
- Files modified: experiments/variants.py
- Commit: c3db5e4

## Known Stubs

None — all CSV values are populated from actual simulation runs with deterministic seed=42.

## Threat Flags

None — no new network endpoints, auth paths, or schema changes introduced.

## Self-Check: PASSED

- analysis/sensitivity.py: FOUND
- analysis/test_sensitivity.py: FOUND
- results/sensitivity_walk.csv: FOUND (14 rows)
- results/sensitivity_fleet.csv: FOUND (12 rows)
- Commit c3db5e4: FOUND
