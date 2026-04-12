---
phase: 02-algorithm-development-python-implementation
plan: "05"
subsystem: heuristic-solver
tags: [alns, rolling-horizon, drt, heuristic, python]
dependency_graph:
  requires: [02-03, 02-04]
  provides: [alns-rolling-horizon, alns-operators]
  affects: [src/drt/alns.py, tests/test_alns.py]
tech_stack:
  added: []
  patterns: [ALNS, rolling-horizon, regret-insertion, hill-climbing]
key_files:
  created:
    - src/drt/alns.py
    - tests/test_alns.py
  modified: []
decisions:
  - "Destroy operator selection: uniform random among 3 operators (no adaptive weights — sufficient for correctness)"
  - "Repair operator selection: alternating greedy/regret by iteration parity (deterministic, avoids bias)"
  - "Stop tagging: stops stored as 4-tuples (MeetingPoint, time, request_id, role) to enable O(n) request lookup without a separate index"
  - "Hill-climbing acceptance: accept only improvements (no simulated annealing) — keeps reoptimize() fast"
metrics:
  duration: "< 5 minutes"
  completed: "2026-04-11"
  tasks_completed: 2
  files_created: 2
---

# Phase 02 Plan 05: ALNS Rolling Horizon Summary

ALNS rolling horizon controller with 5 destroy/repair operators; 200-request 15-vehicle benchmark measured 0.0002s avg per request (requirement: < 1.0s).

## What Was Built

`src/drt/alns.py` implements HEUR-04/05/06:

- `ALNSState` dataclass: routes dict + unassigned list + cost float
- 3 destroy operators: `random_removal`, `worst_removal`, `related_removal`
- 2 repair operators: `greedy_insertion` (calls `evaluate_insertion`), `regret_insertion` (regret-2 heuristic)
- `RollingHorizon` class: maintains active request set, triggers ALNS every `delta` minutes over horizon `H`
- `benchmark()` function: generates synthetic 200-request, 15-vehicle instance and measures wall-clock time

`tests/test_alns.py` covers:
- `test_all_operators_run`: 5-request, 2-vehicle instance; all 5 operators run without exception
- `test_reoptimize_returns_keys`: result dict contains `routes`, `unassigned`, `cost`, `time_ms`, `objective`, `n_accepted`
- `test_timing_benchmark`: 200-request benchmark; avg < 1.0s

## Benchmark Result

| Metric | Value |
|--------|-------|
| avg_time_per_request_s | 0.0002 |
| total_time_s | 0.05 |
| n_requests | 200 |
| n_reoptimizations | 10 |
| Requirement | < 1.0s |
| Status | PASSED |

## ALNS Operator Summary

| # | Name | Type | Role |
|---|------|------|------|
| 1 | random_removal | Destroy | Remove k random assigned requests |
| 2 | worst_removal | Destroy | Remove k highest-cost requests (walk+IVT proxy) |
| 3 | related_removal | Destroy | Remove k spatially/temporally similar requests |
| 4 | greedy_insertion | Repair | Reinsert by minimum incremental cost via evaluate_insertion |
| 5 | regret_insertion | Repair | Regret-2: insert highest-regret request first |

## RollingHorizon Parameters (Benchmark)

| Parameter | Value |
|-----------|-------|
| H (horizon) | 60 min |
| delta (reopt interval) | 10 min |
| alns_iterations | 50 |
| destroy_fraction | 0.3 |
| k_top | 5 |
| rho_p = rho_d | 10.0 |
| travel_speed | 1.0 |
| Grid | [0,100]^2 |
| n_meeting_points | 20 (uniform grid) |
| Vehicle capacity | 8 |
| max_route_duration | 300 min |

## Performance Tuning

No tuning was required — the default 50-iteration ALNS with k_top=5 and 20 meeting points runs well under the 1s threshold. The dominant cost is the `evaluate_insertion` enumeration inside repair operators; keeping k_top small (5) and n_meeting_points moderate (20) ensures O(k_top^2 * n_vehicles * n_stops^2) per insertion remains fast.

## Deviations from Plan

**1. [Rule 1 - Bug] Fixed InsertionResult sort in regret_insertion**
- Found during: Task 1 verification
- Issue: `all_costs.sort()` failed because `InsertionResult` dataclass has no `__lt__`
- Fix: Changed to `all_costs.sort(key=lambda x: x[0])` to sort by cost float
- Files modified: src/drt/alns.py
- Commit: 7ec91c4

## Known Stubs

None — all operators produce real output; benchmark wires synthetic data end-to-end.

## Threat Flags

None — no new network endpoints, auth paths, or schema changes introduced.

## Self-Check: PASSED

- src/drt/alns.py: FOUND
- tests/test_alns.py: FOUND
- Commit 7ec91c4: FOUND
- All 3 tests: PASSED
- Full suite (25 passed, 1 skipped): PASSED
