# Phase 02 Experiment Contract

**Phase:** 02 - Experimental Contract and Metric Standardization
**Status:** contract draft for execution
**Purpose:** Lock fair-comparison rules before new formal evidence is generated.

## Purpose

This contract defines how later phases compare bidirectional pickup/dropoff meeting-point DRT against door-to-door and single-sided variants. It exists to prevent mixed passenger-response assumptions, mixed metric denominators, and coverage-confounded efficiency claims from becoming final manuscript evidence.

Phase 2 is a planning and documentation phase only. It does not run experiments and does not implement code changes.

## Evidence Families

| Family | Role | Can support main claims? | Notes |
|---|---|---:|---|
| Behavioral Main Comparison | Primary service-design evidence under shared passenger-response assumptions | Yes, after Phase 6 formal paired experiments | Must report coverage, acceptance, rejection, and operating efficiency together. |
| Core Supplementary Controls | Matched-coverage and fixed accepted-set controls | Supports interpretation, not standalone superiority | Used to diagnose whether efficiency persists after controlling coverage/passenger set. |
| Deterministic Diagnostics | All-feasible or no-choice routing/feasibility diagnostics | No | Explains mechanisms and implementation behavior only. |
| Algorithm Diagnostics Routed to Phase 4 | ALNS, greedy, no-reoptimization, exact/MILP scope | No until Phase 4 validates scope | Supports algorithm credibility rather than service-design claims. |

## Behavioral Main Comparison

The behavioral main comparison must use one shared passenger-response model across all service designs:

| Service design | Passenger response | Routing setup | Evidence role |
|---|---|---|---|
| DoorToDoor | Same choice model as meeting-point services; walk distance set to zero | Comparable rolling-horizon/ALNS or validated common routing setup | Behavioral baseline |
| SingleSidedPickup | Same choice model | Same routing setup | Service-design baseline |
| SingleSidedDropoff | Same choice model | Same routing setup | Service-design baseline; currently missing downstream implementation |
| BidirectionalMeetingPoint | Same choice model | Same routing setup | Main proposed service design |

This implements D-01, D-07, and D-08. Door-to-door must not remain deterministic all-accept in the behavioral comparison. If BidirectionalMeetingPoint shows lower vehicle-km with lower served share, the result is a coverage-efficiency tradeoff, not unconditional superiority.

## Core Supplementary Controls

Core supplementary controls are part of the main evidence chain:

1. Matched-coverage comparison: compare service designs near a common target `served_share` cap.
2. Fixed accepted-set routing diagnostic: compare routing efficiency on the intersection of requests commonly serviceable/accepted by all methods.

These controls address D-03 and the coverage-confounding risk carried forward from Phase 0.

## Deterministic Diagnostics

Behavioral choice experiments and deterministic feasibility/routing diagnostics are strictly separate evidence families (D-02).

Deterministic diagnostics may include:

- Bidirectional meeting-point routing without passenger choice.
- Door-to-door deterministic insertion.
- No-choice rolling-horizon diagnostics.
- Feasibility rejection diagnostics.

These outputs can explain mechanisms. They cannot be mixed with behavioral comparisons to claim a service design is better for passengers or operators.

## Algorithm Diagnostics Routed to Phase 4

Phase 2 names the need for algorithm diagnostics but does not define detailed ALNS/MILP exact scope (D-04). Phase 4 must define and validate:

- Greedy insertion baseline.
- Rolling-horizon/no-reoptimization comparison.
- ALNS convergence and operator contribution diagnostics.
- Runtime-quality trade-offs.
- Exact or MILP diagnostic scope and limitations.

## Claim Boundaries

Allowed after later evidence:

- Conditional statements about when bidirectional meeting-point design reduces `vkm_per_served_trip` under shared passenger-response assumptions.
- Tradeoff statements that report coverage, acceptance, rejection, and efficiency together.
- Diagnostic statements about routing efficiency under matched coverage or fixed accepted sets.

Forbidden until Phase 8 claim gate:

- "Bidirectional meeting points are overall superior" without reporting served share and rejection mechanisms.
- Vehicle-km improvement claims based on mixed deterministic/choice response comparisons.
- Pareto-frontier language for post-hoc gamma/welfare sweeps unless gamma becomes endogenous.
- Deterministic diagnostic results presented as behavioral service-design evidence.

## Downstream Phase Ownership

| Item | Owner phase | Reason |
|---|---|---|
| Shared passenger-choice model and calibration | Phase 3 | Choice parameters, outside option, service ASC, and type shares are not Phase 2 work. |
| Missing service variants and output schema | Phase 4 | Code implementation and baseline validation happen after the contract is fixed. |
| Pilot smoke tests | Phase 5 | Confirms standardized outputs before formal evidence. |
| Formal paired experiments | Phase 6 | Produces main synthetic evidence. |
| Claim approval | Phase 8 | Final manuscript claim strength depends on formal outputs. |

## Requirements Coverage

| Requirement | Coverage |
|---|---|
| EXP-01 | Separates service design, passenger response, routing algorithm, and diagnostic role through the evidence-family contract and taxonomy dependency. |
| EXP-02 | Requires shared passenger-response assumptions across behavioral service variants. |
| EXP-03 | Separates deterministic feasibility/routing diagnostics from behavioral comparisons. |

## Decision Trace

- D-01: Tradeoff framing among coverage, acceptance, and efficiency.
- D-02: Strict behavioral/deterministic separation.
- D-03: Fixed accepted-set diagnostics as core supplementary diagnostics.
- D-04: ALNS/MILP detail routed to Phase 4.
- D-19: One main experiment contract.
- D-20: Contract locks design, variants, evidence roles, and claim boundaries.

