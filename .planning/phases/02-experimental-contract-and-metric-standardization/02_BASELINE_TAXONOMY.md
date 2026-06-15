# Phase 02 Baseline Taxonomy

**Phase:** 02 - Experimental Contract and Metric Standardization
**Status:** contract draft for execution

## Purpose

This taxonomy separates conceptual evidence categories from current code variant names. It uses four axes required by D-05: service design, passenger response, routing algorithm, and diagnostic role.

## Four-Axis Taxonomy

| Conceptual method | Service design | Passenger response | Routing algorithm | Diagnostic role | Current code variant | Missing implementation or validation work | Downstream owner phase |
|---|---|---|---|---|---|---|---|
| DoorToDoor + Choice + CommonRouting | Door-to-door, zero walking | Shared behavioral choice model | Same validated routing setup as main comparison | Behavioral baseline | `DoorToDoor` exists, but currently deterministic/no shared choice | Add shared choice wrapper with zero walk and standardized status output | Phase 4 |
| SingleSidedPickup + Choice + CommonRouting | Pickup meeting point only | Shared behavioral choice model | Same validated routing setup as main comparison | Behavioral service-design baseline | `SingleSidedPickup` exists, but currently deterministic/no shared choice | Add shared choice wrapper and output status categories | Phase 4 |
| SingleSidedDropoff + Choice + CommonRouting | Dropoff meeting point only | Shared behavioral choice model | Same validated routing setup as main comparison | Behavioral service-design baseline | Missing | Implement and validate symmetric dropoff-side baseline | Phase 4 |
| BidirectionalMP + Choice + RollingHorizon/ALNS | Pickup and dropoff meeting points | Shared behavioral choice model | Rolling horizon / ALNS | Main proposed service design | `FullModel` | Replace paper-facing `FullModel` label with descriptive method label; align choice model after Phase 3 | Phase 3 / Phase 4 |
| BidirectionalNoRollingHorizon + Choice | Pickup and dropoff meeting points | Shared behavioral choice model | Static or greedy insertion without rolling reoptimization | Rolling-horizon diagnostic | `AblationNoRollingHorizon` | Revalidate after shared choice model is rebuilt | Phase 4 |
| GreedyInsertionBaseline | Depends on service design being tested | Deterministic or shared choice, explicitly labeled | Greedy insertion | Algorithm diagnostic | Greedy insertion is used inside several variants | Expose as named diagnostic baseline under fixed accepted sets | Phase 4 |
| ALNSFullModel | Depends on service design being tested | Deterministic or shared choice, explicitly labeled | ALNS / rolling horizon | Algorithm diagnostic or main method, depending on experiment family | `FullModel`, `AblationNoChoice` | Validate convergence, runtime-quality, and operator contribution | Phase 4 |
| ExactOrMILPDiagnostic | Fixed accepted set / small static instances | None or fixed accepted set | Exact/MILP diagnostic | Exact-scope diagnostic only | `src/drt/milp.py`, `experiments/milp_gap.py` | Define honest exact scope and compare only where model semantics match | Phase 4 |

## Naming Rules

- D-06: Do not use `FullModel` as a paper-facing method label. Use `BidirectionalMP + Choice + RollingHorizon/ALNS`.
- Keep code names in implementation maps and provenance tables only.
- D-07: `SingleSidedPickup` and `SingleSidedDropoff` are both required service-design baselines for the behavioral comparison.
- D-08: `DoorToDoor` belongs in the behavioral comparison only when it uses the same passenger choice model with walk distance set to zero.

## Evidence Role Matrix

| Diagnostic role | Valid evidence question | Invalid use |
|---|---|---|
| Behavioral baseline | Does a service design improve efficiency/coverage tradeoffs under shared passenger response? | Comparing all-accept DoorToDoor against choice-filtered BidirectionalMP. |
| Matched-coverage supplementary control | Does efficiency persist near the same served share? | Replacing unconstrained behavioral results. |
| Fixed accepted-set diagnostic | Does routing/service design reduce distance for the same passenger set? | Claiming passengers prefer the service. |
| Algorithm diagnostic | Is ALNS/rolling horizon credible for the claimed operational setting? | Claiming service-design superiority from solver-only comparisons. |
| Exact/MILP diagnostic | How does a small, scoped exact model compare to heuristics? | Presenting simplified MILP as full online stochastic benchmark. |

## Current Code Variant Mapping

| Code variant | Conceptual mapping | Current concern |
|---|---|---|
| `DoorToDoor` | Door-to-door deterministic routing baseline | Not choice-consistent for behavioral main comparison. |
| `DoorToDoorCapped` | Exploratory matched-coverage diagnostic | Cap semantics need formal target `served_share` contract. |
| `SingleSidedPickup` | Pickup-only service-design baseline | Needs shared choice model and symmetric dropoff counterpart. |
| `BidirectionalNoChoice` | Deterministic bidirectional routing diagnostic | Not behavioral evidence. |
| `FullModel` | `BidirectionalMP + Choice + RollingHorizon/ALNS` | Choice currently uses proxy bundle before routing; gamma is not endogenous. |
| `AblationNoRollingHorizon` | Rolling-horizon diagnostic | Shares current MNL limitations. |
| `AblationNoChoice` | No-choice rolling-horizon diagnostic | Not behavioral evidence. |

## Requirements Coverage

| Requirement | Coverage |
|---|---|
| EXP-01 | The taxonomy separates service design, passenger response, routing algorithm, and diagnostic role. |
| EXP-02 | Behavioral rows require shared passenger-response assumptions across service variants. |
| EXP-03 | Diagnostic rows are explicitly separated from behavioral evidence rows. |

## Decision Trace

- D-05: Four-axis taxonomy is the organizing structure.
- D-06: `FullModel` is replaced by `BidirectionalMP + Choice + RollingHorizon/ALNS` for paper-facing contracts.
- D-07: `SingleSidedPickup` and `SingleSidedDropoff` are both required formal baselines.
- D-08: `DoorToDoor` must use the shared choice model in behavioral experiments.

