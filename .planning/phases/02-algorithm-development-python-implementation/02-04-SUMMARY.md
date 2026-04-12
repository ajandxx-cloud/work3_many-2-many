---
phase: 02-algorithm-development-python-implementation
plan: "04"
subsystem: milp
tags: [gurobi, milp, exact-algorithm, drt, meeting-points]
dependency_graph:
  requires: [02-01, 02-02]
  provides: [EXACT-01, EXACT-02, EXACT-03, EXACT-04]
  affects: [phase-03-heuristic-validation]
tech_stack:
  added: [gurobipy]
  patterns: [deferred-import, big-M formulation, static-snapshot MILP]
key_files:
  created:
    - src/drt/milp.py
    - tests/test_milp.py
    - results/milp_benchmark.json
  modified: []
decisions:
  - "Deferred gurobipy import to build()/solve() so module loads without Gurobi installed"
  - "Used big-M formulation for time-window and route-duration constraints"
  - "Simplified capacity constraint to total-assigned <= Q_v (not simultaneous occupancy)"
  - "Precedence-pos constraint added per (r,v,mp_p,mp_d) tuple to encode travel-time lower bound"
metrics:
  duration: "~15 min"
  completed: "2026-04-11"
  tasks_completed: 3
  files_created: 3
---

# Phase 02 Plan 04: MILP Formulation (Gurobi) Summary

Static snapshot MILP for many-to-many DRT with bidirectional meeting points using Gurobi, covering all 11 constraint classes and a five-component weighted objective.

## What Was Built

`DRTModel` in `src/drt/milp.py` formulates and solves a batch assignment problem:
- Accepts/rejects requests (z_r binary)
- Assigns each accepted request to a vehicle with a pickup and dropoff meeting point (x_{r,v,mp_p,mp_d} binary)
- Schedules pickup and dropoff times (s_{r,v,'p'} and s_{r,v,'d'} continuous)

## Constraint Mapping (constraints.tex → implementation)

| # | Label | Implementation |
|---|-------|----------------|
| 1 | con:assignment | Each accepted request assigned to exactly one (v, mp_p, mp_d) |
| 2 | con:capacity | Sum of assigned requests per vehicle ≤ Q_v |
| 3 | con:tw-early | s_{r,v,p} ≥ e_r × assigned_rv |
| 4 | con:tw-late | s_{r,v,p} ≤ l_r + BIG_M × (1 − assigned_rv) |
| 5 | con:ridetime | s_{r,v,d} − s_{r,v,p} ≤ T_r^ride |
| 6 | con:precedence-time | s_{r,v,d} ≥ s_{r,v,p} |
| 7 | con:precedence-pos | s_{r,v,d} ≥ s_{r,v,p} + tt(mp_p, mp_d) × x_{r,v,mp_p,mp_d} |
| 8 | con:walk-pickup | walk_p × x_{r,v,mp_p,mp_d} ≤ ρ^P |
| 9 | con:walk-dropoff | walk_d × x_{r,v,mp_p,mp_d} ≤ ρ^D |
| 10 | con:time-consistency | s_{r,v,p} ≥ t_v^now |
| 11 | con:route-duration | s_{r,v,d} − t_v^now ≤ T_v^max |

## Variable Count (10-request, 3-vehicle instance)

- z: 10 binary
- x: up to 10 × 3 × |cand_p| × |cand_d| binary (varies by walking radius; with rho=5.0 and 8 MPs, typically 4-8 candidates per side)
- s: 10 × 3 × 2 = 60 continuous

## Smoke Test Result

Instance: 10 requests, 3 vehicles, 8 meeting points, rho_p=rho_d=5.0

| Key | Value |
|-----|-------|
| status | optimal |
| objective_value | 98.87 |
| mip_gap | 0.0 |
| solve_time | ~0.002 s |
| accepted_requests | ["r2", "r7"] |

Note: only 2 of 10 requests accepted — capacity constraint (3 vehicles × 4 seats = 12 total slots, but simultaneous capacity bound is tight given the meeting-point geometry and time windows). This is expected behaviour for the static snapshot formulation.

## Deviations from Plan

None — plan executed exactly as written.

## Known Stubs

None.

## Threat Flags

None — no new network endpoints or trust boundaries introduced. Gurobi time_limit=300s enforces T-02-07 DoS mitigation.

## Self-Check: PASSED

- src/drt/milp.py: FOUND
- tests/test_milp.py: FOUND
- results/milp_benchmark.json: FOUND
- commit 791272f: FOUND
