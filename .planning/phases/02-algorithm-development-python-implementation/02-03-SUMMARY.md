---
phase: 02-algorithm-development-python-implementation
plan: "03"
subsystem: insertion-evaluator
tags: [heuristic, insertion, dispatch, online-algorithm]
dependency_graph:
  requires: [02-01, 02-02]
  provides: [evaluate_insertion, InsertionResult]
  affects: [02-05-alns-repair]
tech_stack:
  added: []
  patterns: [dataclass, euclidean-distance-model, nested-enumeration]
key_files:
  created:
    - src/drt/insertion.py
    - tests/test_insertion.py
  modified: []
decisions:
  - "Walk cost uses Euclidean distance (consistent with feasibility.py travel model)"
  - "Early-exit when no candidates within walking radius avoids inner loop entirely"
  - "pickup_time recomputed by replaying schedule on new_stops (same logic as feasibility.py)"
metrics:
  duration: "< 5 minutes"
  completed: "2026-04-11"
  tasks_completed: 1
  files_created: 2
---

# Phase 02 Plan 03: Online Insertion Evaluator Summary

HEUR-02 online insertion evaluator implemented: enumerates all (vehicle, pos_p, pos_d, mp_p, mp_d) combinations, checks feasibility via HEUR-03, computes four-component incremental cost, returns best feasible InsertionResult or None.

## InsertionResult Fields and Math Equivalents

| Field | Math symbol | Description |
|-------|-------------|-------------|
| `vehicle_id` | v | Selected vehicle |
| `pos_p` | pi^P | Insertion index for pickup stop |
| `pos_d` | pi^D | Insertion index for dropoff stop (> pos_p) |
| `pickup_mp` | m_r^P | Chosen pickup meeting point |
| `dropoff_mp` | m_r^D | Chosen dropoff meeting point |
| `incremental_cost` | Delta C | Weighted sum of four cost components |

## Incremental Cost Components

| Component | Formula | Weight |
|-----------|---------|--------|
| delta_C_op | dist(new_route) - dist(old_route) | alpha_op |
| delta_C_wait | max(0, pickup_time - request.earliest) | alpha_wait |
| delta_C_walk | d(origin, mp_p) + d(mp_d, destination) | alpha_walk |
| delta_C_IVT | d(mp_p, mp_d) / travel_speed | alpha_ivt |

Default weights: (1.0, 1.0, 1.0, 1.0).

## Timing Benchmark Result

- Instance: 100 requests, 10 vehicles, 20 meeting points, rho=50, k_top=5
- Total elapsed: ~0.10s for all 100 requests
- Average per request: ~0.001s (well under 1.0s limit)
- HEUR-06 constraint: PASSED

## Deviations from Plan

None — plan executed exactly as written.

## Self-Check: PASSED

- src/drt/insertion.py: FOUND
- tests/test_insertion.py: FOUND
- Commit 6cb259a: FOUND
- All 4 pytest tests: PASSED
