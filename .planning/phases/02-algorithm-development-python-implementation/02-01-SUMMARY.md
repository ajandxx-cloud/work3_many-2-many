---
phase: 02-algorithm-development-python-implementation
plan: "01"
subsystem: drt-package
tags: [python, dataclasses, mnl, choice-model, scaffold]
dependency_graph:
  requires: []
  provides: [drt-package, types-api, mnl-choice-api]
  affects: [all subsequent Phase 2 plans]
tech_stack:
  added: [Python 3.10+, setuptools, gurobipy, numpy, pytest]
  patterns: [dataclasses, MNL logit, frozen dataclass for hashable value objects]
key_files:
  created:
    - pyproject.toml
    - src/drt/__init__.py
    - src/drt/types.py
    - src/drt/choice.py
  modified: []
decisions:
  - "MeetingPoint and Bundle use frozen=True so Bundle instances are hashable dict keys in choice_probability return value"
  - "Outside option utility fixed at U_r0=0.0 (normalized baseline) per Phase 1 notation"
  - "Pre-defined PassengerType constants (PRICE_SENSITIVE, TIME_SENSITIVE, WALK_SENSITIVE) added to types.py for convenience"
metrics:
  duration: "~15 min"
  completed: "2026-04-11"
  tasks_completed: 2
  files_created: 4
---

# Phase 2 Plan 01: Project Scaffold, Types, and MNL Choice Model Summary

Installable `src/drt/` Python package with all core dataclasses and the MNL passenger choice model, matching Phase 1 mathematical notation exactly.

## Files Created and Their Exports

### pyproject.toml
Package configuration using setuptools. Dependencies: `gurobipy`, `numpy`. Dev extras: `pytest`, `pytest-benchmark`. Source layout: `src/`.

### src/drt/__init__.py
Re-exports full public API:
```python
from drt import Request, Vehicle, Route, MeetingPoint, Bundle, PassengerType
from drt import mnl_utility, choice_probability
```

### src/drt/types.py
Six dataclasses covering all domain objects:

| Class | Key Fields | Notes |
|---|---|---|
| `Request` | id, origin, destination, earliest, latest, max_ride_time | Plain dataclass |
| `Vehicle` | id, capacity, max_route_duration, current_position, current_time | Plain dataclass |
| `MeetingPoint` | id, coords | `frozen=True` (hashable) |
| `Bundle` | request_id, pickup_mp, dropoff_mp, departure_time, price | `frozen=True` (hashable, used as dict key) |
| `Route` | vehicle_id, stops | Mutable; stops = list of (MeetingPoint, float) |
| `PassengerType` | name, beta_walk, beta_wait, beta_ivt, beta_price | Plain dataclass |

Also exports three pre-defined constants: `PRICE_SENSITIVE`, `TIME_SENSITIVE`, `WALK_SENSITIVE`.

### src/drt/choice.py
Two public functions:

- `euclidean(a, b)` — helper, Euclidean distance between coordinate tuples
- `mnl_utility(bundle, request, ptype, current_time) -> float` — computes U_rb^k
- `choice_probability(bundles, request, ptype, current_time) -> dict` — returns {Bundle: prob, None: outside_prob}, sums to 1.0

## Notation Mapping (Python field → math symbol)

| Python | Math symbol | Description |
|---|---|---|
| `Request.id` | r | request identifier |
| `Request.origin` | o_r | (x, y) trip origin |
| `Request.destination` | d_r | (x, y) trip destination |
| `Request.earliest` | e_r | earliest acceptable pickup time |
| `Request.latest` | l_r | latest acceptable pickup time |
| `Request.max_ride_time` | T_r^ride | max in-vehicle time |
| `Vehicle.capacity` | Q_v | vehicle capacity |
| `Vehicle.max_route_duration` | T_v^max | max route duration |
| `MeetingPoint.coords` | (x_m, y_m) | meeting point location |
| `Bundle.pickup_mp` | m_r^pu | pickup meeting point |
| `Bundle.dropoff_mp` | m_r^do | dropoff meeting point |
| `Bundle.departure_time` | τ_r | scheduled pickup time |
| `Bundle.price` | p_r | fare |
| `PassengerType.beta_walk` | β1^k | walk disutility coefficient |
| `PassengerType.beta_wait` | β2^k | wait disutility coefficient |
| `PassengerType.beta_ivt` | β3^k | in-vehicle time disutility coefficient |
| `PassengerType.beta_price` | β4^k | price disutility coefficient |

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Made MeetingPoint and Bundle frozen for hashability**
- Found during: Task 2 verification
- Issue: `Bundle` used as dict key in `choice_probability` return value, but plain `@dataclass` is not hashable
- Fix: Added `frozen=True` to both `MeetingPoint` (required because it is a field of frozen `Bundle`) and `Bundle`
- Files modified: src/drt/types.py
- Commit: 4e11bce

## Self-Check: PASSED

- [x] pyproject.toml exists with gurobipy and numpy
- [x] src/drt/__init__.py re-exports all public types and choice functions
- [x] src/drt/types.py defines all six dataclasses with correct fields
- [x] src/drt/choice.py implements mnl_utility and choice_probability; probabilities sum to 1.0
- [x] Commit 4e11bce exists
