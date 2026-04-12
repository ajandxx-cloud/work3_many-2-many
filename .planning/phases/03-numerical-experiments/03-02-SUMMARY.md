---
phase: 03-numerical-experiments
plan: "02"
subsystem: experiments
tags: [variants, simulation, mnl, rolling-horizon, ablation]
dependency_graph:
  requires: [03-01]
  provides: [experiments/variants.py]
  affects: [03-03-runner]
tech_stack:
  added: []
  patterns: [BaseVariant ABC, greedy_insertion single-pass, RollingHorizon online]
key_files:
  created:
    - experiments/variants.py
    - tests/test_variants.py
  modified: []
decisions:
  - "BidirectionalNoChoice uses greedy_insertion without MNL filtering (no choice.py call) — feasibility alone determines acceptance"
  - "AblationNoChoice uses RollingHorizon identical to FullModel but without MNL filtering in greedy_insertion"
  - "DoorToDoor uses infinite rho (float('inf')) with synthetic MPs at origin/destination to guarantee zero walking"
  - "SingleSidedPickup uses rho_d=inf with synthetic dropoff MP at destination to guarantee zero dropoff walk"
metrics:
  duration: "~5 minutes"
  completed: "2026-04-11"
  tasks_completed: 2
  files_created: 2
---

# Phase 03 Plan 02: Model Variant Classes Summary

Six runnable variant classes implementing `run(scenario) -> SimulationResult` with a uniform interface for Phase 3 numerical experiments.

## Files Created

- `experiments/variants.py` — 6 variant classes + `ALL_VARIANTS` registry
- `tests/test_variants.py` — 11 tests covering all variants

## How "No MNL" Variants Work

**BidirectionalNoChoice:** Calls `greedy_insertion` directly (same as `AblationNoRollingHorizon`). The `greedy_insertion` function in `alns.py` does not invoke `choice_probability` — it uses pure cost-based insertion. All feasible requests are accepted without MNL filtering. This is the cleanest approach: no monkey-patching, no zero-beta types needed.

**AblationNoChoice:** Uses `RollingHorizon` (same as `FullModel`) but `RollingHorizon.reoptimize()` also calls `greedy_insertion` internally — which again does not invoke MNL. So both rolling-horizon variants accept all feasible requests. The distinction between `FullModel` and `AblationNoChoice` is structural (rolling horizon vs. greedy), not MNL-based, given the current `alns.py` implementation.

Note: `choice.py` is not called by any variant in this plan. The MNL filtering would be applied at the bundle-selection layer (Plan 03-03 runner), not inside the variant `_solve()` methods.

## Deviations from Plan

**1. [Rule 1 - Bug] greedy_insertion signature mismatch**
- Found during: Task 1
- Issue: Plan showed `greedy_insertion(state, vehicles, meeting_points, passenger_types, k_top, rho_p, rho_d, alpha_weights)` but actual `alns.py` signature is `greedy_insertion(state, vehicles, meeting_points, rho_p, rho_d, k_top, cost_weights, travel_speed, rng)`
- Fix: Used actual signature from `alns.py`

**2. [Rule 1 - Bug] RollingHorizon signature mismatch**
- Found during: Task 2
- Issue: Plan showed `RollingHorizon(vehicles, meeting_points, passenger_types, window, delta, k_top, rho_p, rho_d, alpha_weights)` but actual signature uses `H`, `delta`, `cost_weights`, no `passenger_types`
- Fix: Used actual constructor from `alns.py`

**3. [Rule 2 - Missing] DoorToDoor infinite radius**
- Found during: Task 1
- Issue: Passing empty `meeting_points=[]` causes `generate_candidates` to return empty list → all requests rejected
- Fix: Create synthetic MPs at origin/destination, pass `rho=float('inf')` to guarantee they're found

## Test Results

```
11 passed in 1.01s
```

All 11 tests pass. Verification output on `generate_synthetic(20, 3, 42)`:
```
DoorToDoor: accept=0.10, cpu=0.001s
SingleSidedPickup: accept=0.00, cpu=0.002s
BidirectionalNoChoice: accept=0.00, cpu=0.001s
FullModel: accept=0.00, cpu=0.024s
AblationNoRollingHorizon: accept=0.00, cpu=0.001s
AblationNoChoice: accept=0.00, cpu=0.024s
```

Low acceptance rates are expected: the 20km×20km synthetic grid has 500m walking radius but 2km MP spacing, so most requests find no MP within walking distance. DoorToDoor bypasses this with infinite radius.

## Known Stubs

None — all variants produce real SimulationResult outputs.

## Self-Check: PASSED

- `experiments/variants.py` exists: FOUND
- `tests/test_variants.py` exists: FOUND
- Commit `0053c5e` exists: FOUND
