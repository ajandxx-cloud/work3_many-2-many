# Phase 04 Variant Mapping

## Purpose

This map separates implementation provenance from paper-facing method labels. Code
class names such as `FullModel` and `AblationNoChoice` are legacy/provenance
labels only; they are not paper-facing main-table labels.

## Concept Mapping

| Code variant | method_label | service_design | choice_model | reoptimization | routing_solver | evidence_family | diagnostic_role | Paper-facing eligibility |
|---|---|---|---|---|---|---|---|---|
| `DoorToDoor` | `DoorToDoor_Choice_CommonRouting` | `door_to_door` | `binary_logit` | `common_sequential_insertion` | `greedy_insertion` | `behavioral_main` | `behavioral_baseline` | Main behavioral baseline |
| `SingleSidedPickup` | `SingleSidedPickup_Choice_CommonRouting` | `single_sided_pickup` | `binary_logit` | `common_sequential_insertion` | `greedy_insertion` | `behavioral_main` | `behavioral_service_design_baseline` | Main behavioral baseline |
| `SingleSidedDropoff` | `SingleSidedDropoff_Choice_CommonRouting` | `single_sided_dropoff` | `binary_logit` | `common_sequential_insertion` | `greedy_insertion` | `behavioral_main` | `behavioral_service_design_baseline` | Main behavioral baseline |
| `FullModel` | `BidirectionalMP_Choice_RH_ALNS` | `bidirectional_mp` | `binary_logit` | `rolling_horizon` | `alns` | `behavioral_main` | `main_service_design` | Main proposed service design |
| `DoorToDoorCapped` | `DoorToDoor_Capped_MatchedCoverage` | `door_to_door` | `deterministic_cap` | `none` | `greedy_insertion` | `supplementary_control` | `matched_coverage_control` | Supplementary control only |
| `BidirectionalNoChoice` | `BidirectionalMP_NoChoice_Greedy` | `bidirectional_mp` | `none` | `none` | `greedy_insertion` | `deterministic_diagnostic` | `no_choice_feasibility_diagnostic` | Diagnostic only |
| `AblationNoRollingHorizon` | `BidirectionalMP_Choice_NoRollingHorizon` | `bidirectional_mp` | `binary_logit` | `none` | `greedy_insertion` | `algorithm_diagnostic` | `no_rolling_horizon_diagnostic` | Algorithm diagnostic only |
| `AblationNoChoice` | `BidirectionalMP_NoChoice_RH_ALNS` | `bidirectional_mp` | `none` | `rolling_horizon` | `alns` | `deterministic_diagnostic` | `no_choice_routing_diagnostic` | Diagnostic only |

## Evidence Family Rules

- `behavioral_main` rows may support later service-design evidence only after
  Phase 5/6 smoke and formal paired experiments.
- `supplementary_control` rows support matched-coverage interpretation, not
  standalone superiority claims.
- `deterministic_diagnostic` and `algorithm_diagnostic` rows explain routing and
  solver behavior. They must not be mixed into behavioral main tables.
- `legacy_class` is provenance only. It may appear in audit or traceability
  outputs, but paper-facing main tables must use `method_label`.

