---
phase: 02-algorithm-development-python-implementation
plan: "02"
subsystem: drt-core
tags: [candidate-generation, feasibility-checker, heuristic, pytest]
dependency_graph:
  requires: [02-01]
  provides: [candidate.py, feasibility.py]
  affects: [02-03-insertion, 02-04-milp]
tech_stack:
  added: []
  patterns: [dataclass, pure-functions, euclidean-distance-model]
key_files:
  created:
    - src/drt/candidate.py
    - src/drt/feasibility.py
    - tests/test_candidate.py
    - tests/test_feasibility.py
  modified:
    - pyproject.toml
decisions:
  - "Euclidean distance model for travel time (distance / travel_speed)"
  - "Occupancy labelling for existing stops uses alternating pickup/dropoff heuristic"
  - "Precedence check is first (cheapest) in check_feasibility"
metrics:
  duration: "~20 minutes"
  completed: "2026-04-11"
  tasks_completed: 2
  files_created: 4
  files_modified: 1
---

# Phase 02 Plan 02: Candidate Generation and Feasibility Checker Summary

HEUR-01 candidate generation and HEUR-03 feasibility checker implemented with full pytest coverage (14 tests, all passing).

## Function Signatures

### candidate.py

```python
def generate_candidates(
    request: Request,
    meeting_points: list[MeetingPoint],
    rho: float,       # ρ^P or ρ^D — walking radius
    k_top: int,       # k^top — max candidates to return
    side: str,        # 'pickup' → origin; 'dropoff' → destination
) -> list[MeetingPoint]:
```

### feasibility.py

```python
def check_feasibility(
    route: Route,
    request: Request,
    pickup_mp: MeetingPoint,
    dropoff_mp: MeetingPoint,
    pos_p: int,            # insertion index for pickup
    pos_d: int,            # insertion index for dropoff (must be > pos_p)
    vehicle: Vehicle,
    travel_speed: float = 1.0,
) -> tuple[bool, str]:
```

## Constraint Coverage

| Return reason | Constraint label (constraints.tex) | Check |
|---|---|---|
| `"precedence"` | con:precedence-pos | pos_d <= pos_p |
| `"capacity"` | con:capacity | occupancy > Q_v at any stop |
| `"tw_early"` | con:tw-early | scheduled_pickup < e_r |
| `"tw_late"` | con:tw-late | scheduled_pickup > l_r |
| `"ride_time"` | con:ridetime | dropoff_time - pickup_time > T_r^max |
| `"route_duration"` | con:route-duration | last_stop_time - current_time > T_v^max |
| `(True, "")` | all pass | feasible insertion |

Note: con:time-consistency is enforced implicitly — schedule times are recomputed from scratch using travel_speed, so they are always consistent by construction.

## Test Results

| Suite | Tests | Status |
|---|---|---|
| tests/test_candidate.py | 7 | PASSED |
| tests/test_feasibility.py | 7 | PASSED |
| **Total** | **14** | **PASSED** |

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] Fixed pyproject.toml build backend**
- Found during: Task 1 (test execution)
- Issue: `setuptools.backends.legacy:build` is not available in the installed setuptools version
- Fix: Changed to `setuptools.build_meta` (standard backend)
- Files modified: pyproject.toml
- Commit: 580cd07

**2. [Rule 2 - Missing functionality] Added types.py stub**
- Found during: Task 1 setup
- Issue: types.py did not exist yet (plan 02-01 parallel); imports would fail
- Fix: types.py was already created by plan 02-01 (found on disk); no stub needed
- Note: types.py from 02-01 uses `max_ride_time` field name matching plan spec

## Known Stubs

None. Both modules are fully implemented with real logic.

## Threat Flags

None. No new network endpoints, auth paths, or trust boundary crossings introduced. All code is internal simulation logic.

## Self-Check: PASSED

- src/drt/candidate.py: FOUND
- src/drt/feasibility.py: FOUND
- tests/test_candidate.py: FOUND
- tests/test_feasibility.py: FOUND
- Commit 580cd07: FOUND
