---
phase: 01-problem-formulation-model-structure
plan: 02
subsystem: model
tags: [constraints, milp, drt, meeting-points, latex]
dependency_graph:
  requires: [model/notation.tex]
  provides: [model/constraints.tex]
  affects: [Phase 2 MILP formulation, Phase 2 feasibility checker]
tech_stack:
  added: []
  patterns: [LaTeX equation/align environments, labeled constraints for cross-reference]
key_files:
  created: [model/constraints.tex]
  modified: []
decisions:
  - "Used \\pi_r^P < \\pi_r^D (strict less-than) for positional precedence per plan spec"
  - "Walking radius constraints stated explicitly as MILP inequalities even though candidate sets M_r^P/M_r^D encode the same filter — makes MILP formulation self-contained"
  - "con:precedence-time uses t(m_r^P, m_r^D) as lower bound on in-vehicle segment, not exact ride time — exact ride time is captured by con:ridetime"
metrics:
  duration: ~10 min
  completed: "2026-04-11"
  tasks_completed: 1
  files_created: 1
---

# Phase 1 Plan 02: Operational Constraints Summary

One-liner: Seven labeled constraint classes for many-to-many DRT with bidirectional meeting points, covering capacity, time windows, ride time, walking radius, precedence, route consistency, and route duration, plus domain constraints and a summary table.

## Files Created

- `model/constraints.tex` — LaTeX fragment (no `\documentclass`), 158 lines

## Constraint Label Inventory

All `con:*` labels present in `model/constraints.tex`:

| Label | Constraint Class |
|-------|-----------------|
| `con:capacity` | Vehicle Capacity |
| `con:tw-early` | Time Windows (earliest pickup) |
| `con:tw-late` | Time Windows (latest pickup) |
| `con:ridetime` | In-Vehicle Ride Time |
| `con:walk-pickup` | Walking Radius (pickup) |
| `con:walk-dropoff` | Walking Radius (dropoff) |
| `con:precedence-pos` | Precedence: position ordering |
| `con:precedence-time` | Precedence: time ordering |
| `con:time-consistency` | Route Time Consistency |
| `con:route-duration` | Maximum Route Duration |
| `con:binary-z` | Domain: acceptance binary |
| `con:domain-v` | Domain: vehicle assignment |
| `con:domain-mp` | Domain: pickup meeting point |
| `con:domain-md` | Domain: dropoff meeting point |

Total: 14 labels (requirement was >= 11).

## Notation Additions Beyond notation.tex

None. All symbols used in `constraints.tex` are defined in `model/notation.tex`:
- $q_v(i)$, $Q_v$, $\sigma_v$ — Route and Schedule section
- $s_{v,i}$, $L^{\max}$, $T_v^{\max}$ — Route and Schedule section
- $e_r$, $l_r$, $\rho^P$, $\rho^D$ — Spatial and Temporal section
- $d(i,j)$, $t(i,j)$ — Spatial and Temporal section
- $z_r$, $v_r$, $\pi_r^P$, $\pi_r^D$, $m_r^P$, $m_r^D$ — Decision Variables section
- $M_r^P$, $M_r^D$ — Sets and Indices section

## Linearization Notes for Phase 2 MILP

The following constraints require attention when implementing the MILP in Phase 2:

1. **con:capacity** — $q_v(i)$ is a derived quantity (sum of accepted passengers on board at node $i$). In the MILP, this must be expressed via flow-balance auxiliary variables or cumulative load tracking. Not directly linear as written; standard DARP linearization applies.

2. **con:precedence-pos** — $\pi_r^P < \pi_r^D$ is a positional ordering constraint. In a standard MILP route formulation (arc-based), this is enforced implicitly by the arc flow structure rather than as an explicit integer inequality. Phase 2 should note this.

3. **con:time-consistency** — As written, $\sigma_v(i)$ is a sequence index. In an arc-based MILP, this becomes a set of pairwise time-propagation constraints over arc variables. Standard big-M or time-indexed formulation applies.

All other constraints (con:tw-early, con:tw-late, con:ridetime, con:walk-pickup, con:walk-dropoff, con:precedence-time, con:route-duration, con:binary-z, con:domain-v, con:domain-mp, con:domain-md) are directly expressible as linear inequalities or domain restrictions in the MILP.

## Deviations from Plan

None — plan executed exactly as written.

## Self-Check: PASSED

- `model/constraints.tex` exists: FOUND
- Commit `8b57fcf` exists: FOUND
- Label count >= 11: 14 labels found
- All 11 required labels present: verified
- `T_v^{\max}` present: verified
- `L^{\max}` present: verified
- `\rho^P` present: verified
- `\rho^D` present: verified
- `z_r \in \{0,1\}` present: verified
- `\pi_r^P < \pi_r^D` present: verified
- No `\documentclass` or `\begin{document}`: verified
- Line 1 comment `%% constraints.tex`: verified
- `\begin{tabular}{lll}` present: verified
