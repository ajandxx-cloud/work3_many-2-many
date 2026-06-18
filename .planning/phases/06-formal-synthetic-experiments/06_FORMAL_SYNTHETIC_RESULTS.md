# Phase 6 Formal Synthetic Results

This report synthesizes formal Phase 6 evidence only. Phase 6 produces evidence, does not approve final manuscript claims, and Phase 8 owns final claim grading.

## 1. Phase 6 Purpose

Phase 6 generated a reproducible formal synthetic evidence base for conditional comparisons of bidirectional meeting-point DRT under consistent passenger-response assumptions.

## 2. Formal Experiment Packages Executed

- 06-02 main behavioral matrix.
- 06-03 matched-coverage control and fixed accepted-set routing diagnostic.
- 06-04 robustness diagnostics: utility sensitivity, walking-radius / meeting-point-density, fleet-demand stress, equity type-level outcomes, and algorithm diagnostics.

## 3. Seed Count And Paired-Seed Design

The main behavioral and coverage-control packages use 20 paired seeds across four scales. Robustness diagnostics use a reduced paired diagnostic design over seeds 1-10 and scales 100, 200, and 300.

## 4. Method Taxonomy

- DoorToDoor_Choice_CommonRouting: behavioral door-to-door baseline with common response semantics.
- SingleSidedPickup_Choice_CommonRouting: behavioral pickup-side meeting-point baseline.
- SingleSidedDropoff_Choice_CommonRouting: behavioral dropoff-side meeting-point baseline.
- BidirectionalMP_Choice_RH_ALNS: full bidirectional meeting-point design using rolling-horizon / ALNS implementation.

## 5. Scenario And Scale Description

The formal main matrix covers synthetic scales 100, 200, 300, and 500. Robustness diagnostics use reduced diagnostic grids to screen sensitivity without becoming headline evidence.

## 6. Main Behavioral Matrix Summary

| method | served_share | total_vkm | vkm_served | vkm_original |
| --- | --- | --- | --- | --- |
| FullModel | 0.157529 | 444.491 | 9.95103 | 1.56868 |
| DoorToDoor | 0.2004 | 772.698 | 14.6651 | 2.90023 |
| SingleSidedDropoff | 0.193546 | 710.948 | 13.9071 | 2.66234 |
| SingleSidedPickup | 0.199258 | 715.579 | 13.6828 | 2.74061 |

## 7. Coverage-Confounding Control Summary

Matched coverage has 320 durable rows: 305 completed and 15 durable failed FullModel matched rows. On completed pairs, FullModel-minus-baseline differences are negative for vkm/served and vkm/original. Fixed accepted-set routing has 320 completed diagnostic rows; it supports vkm/served efficiency but not an unconditional vkm/original advantage.

Matched coverage paired summaries:

| baseline | metric | n_valid_pairs | mean_difference | full_better_share |
| --- | --- | --- | --- | --- |
| DoorToDoor | vkm_per_served_trip | 65 | -4.61684 | 0.984615 |
| SingleSidedPickup | vkm_per_served_trip | 65 | -3.99848 | 0.969231 |
| SingleSidedDropoff | vkm_per_served_trip | 65 | -4.10731 | 0.984615 |
| DoorToDoor | vkm_per_original_request | 65 | -0.68084 | 0.984615 |
| SingleSidedPickup | vkm_per_original_request | 65 | -0.580799 | 0.969231 |
| SingleSidedDropoff | vkm_per_original_request | 65 | -0.604853 | 0.984615 |

Fixed accepted-set paired summaries:

| baseline | metric | n_valid_pairs | mean_difference | full_better_share |
| --- | --- | --- | --- | --- |
| DoorToDoor | vkm_per_served_request | 80 | -5.23247 |  |
| SingleSidedPickup | vkm_per_served_request | 80 | -3.79588 |  |
| SingleSidedDropoff | vkm_per_served_request | 80 | -3.83108 |  |
| DoorToDoor | vkm_per_original_request | 80 | 0.0523446 | 0.525 |
| SingleSidedPickup | vkm_per_original_request | 80 | 0.126704 | 0.35 |
| SingleSidedDropoff | vkm_per_original_request | 80 | 0.115084 | 0.35 |

## 8. Utility Sensitivity Summary

| parameter_setting_id | metric | n_valid_pairs | mean_full_minus_door_to_door | full_better_share |
| --- | --- | --- | --- | --- |
| baseline_default | vkm_per_served_trip | 30 | -5.20212 | 1 |
| baseline_default | vkm_per_original_request | 30 | -1.55334 | 0.966667 |
| ivt_disutility_high | vkm_per_served_trip | 30 | -6.01926 | 1 |
| ivt_disutility_high | vkm_per_original_request | 30 | -1.45261 | 0.966667 |
| outside_option_high | vkm_per_served_trip | 30 | -6.24348 | 0.933333 |
| outside_option_high | vkm_per_original_request | 30 | -0.876604 | 0.966667 |
| service_asc_low | vkm_per_served_trip | 30 | -6.24348 | 0.933333 |
| service_asc_low | vkm_per_original_request | 30 | -0.876604 | 0.966667 |
| wait_disutility_high | vkm_per_served_trip | 30 | -5.63086 | 1 |
| wait_disutility_high | vkm_per_original_request | 30 | -1.51188 | 0.966667 |
| walk_disutility_high | vkm_per_served_trip | 30 | -5.19963 | 1 |
| walk_disutility_high | vkm_per_original_request | 30 | -1.55513 | 0.966667 |
| walk_sensitive_majority | vkm_per_served_trip | 30 | -4.62992 | 0.966667 |
| walk_sensitive_majority | vkm_per_original_request | 30 | -1.75906 | 1 |

## 9. Walking Radius / Meeting-Point Density Summary

| parameter_setting_id | metric | n_valid_pairs | mean_full_minus_door_to_door | full_better_share |
| --- | --- | --- | --- | --- |
| default_radius_default_density | vkm_per_served_trip | 30 | -5.20212 | 1 |
| default_radius_default_density | vkm_per_original_request | 30 | -1.55334 | 0.966667 |
| high_radius_dense_density | vkm_per_served_trip | 30 | -5.26691 | 1 |
| high_radius_dense_density | vkm_per_original_request | 30 | -1.14521 | 0.966667 |
| low_radius_sparse_density | vkm_per_served_trip | 30 | -15.7067 | 1 |
| low_radius_sparse_density | vkm_per_original_request | 30 | -3.07504 | 1 |

## 10. Fleet-Demand Stress Summary

| parameter_setting_id | metric | n_valid_pairs | mean_full_minus_door_to_door | full_better_share |
| --- | --- | --- | --- | --- |
| stress_base | vkm_per_served_trip | 10 | -5.14502 | 1 |
| stress_base | vkm_per_original_request | 10 | -1.43642 | 1 |
| stress_high_demand | vkm_per_served_trip | 10 | -3.80571 | 1 |
| stress_high_demand | vkm_per_original_request | 10 | -1.5463 | 1 |
| stress_low_demand | vkm_per_served_trip | 10 | -6.04722 | 1 |
| stress_low_demand | vkm_per_original_request | 10 | -1.84164 | 1 |

## 11. Equity / Type-Level Outcome Summary

Equity outputs include 180 type-level rows and 12,000 individual burden rows. They remain exploratory because passenger types are simulation-range constructs.

| passenger_type | metric | n_valid_pairs | mean_full_minus_door_to_door |
| --- | --- | --- | --- |
| price_sensitive | served_share | 30 | -0.0615788 |
| price_sensitive | type_level_acceptance_rate | 30 | -0.0615788 |
| price_sensitive | avg_wait | 30 | -2852.03 |
| price_sensitive | avg_walk | 30 | 177.115 |
| price_sensitive | avg_ivt | 30 | -4796 |
| time_sensitive | served_share | 30 | -0.0116136 |
| time_sensitive | type_level_acceptance_rate | 30 | -0.0116136 |
| time_sensitive | avg_wait | 30 | -2901.64 |
| time_sensitive | avg_walk | 30 | 131.13 |

## 12. Algorithm Diagnostic Summary

The rolling-horizon label implementation check completed without conflict. ALNS budget and MILP static-snapshot diagnostics are diagnostic-only implementation evidence and do not establish a final algorithm-quality claim.

## 13. Durable Failure Row Summary

The failure ledger records 15 durable rows, all from matched coverage. These rows are not hidden and are carried as explicit evidence-boundary limitations.

## 14. Limitations

- The 20-seed main matrix is formal synthetic evidence, not real city policy evidence.
- Matched coverage has 15 durable FullModel failed rows.
- Fixed accepted-set routing is diagnostic-only and cannot support behavioral claims.
- Robustness diagnostics use reduced grids.
- Equity outcomes are exploratory because passenger types are simulation-range constructs.
- Paired bootstrap confidence intervals are generated; paired hypothesis tests are not implemented in Phase 6.

## 15. Evidence Interpretation Boundaries

FullModel evidence is conditional. Phase 6 supports evidence for Phase 8 grading but does not approve final manuscript claims.

## 16. Phase 8 Handoff Notes

Phase 8 may evaluate main behavioral evidence, matched-coverage evidence with durable failures noted, and diagnostic robustness screens. It must not convert diagnostic or exploratory evidence into headline claims.

## Artifact Manifest

See `06_FORMAL_RESULT_MANIFEST.md` and `results/formal/phase06/phase06_result_manifest.json`.

## Critical Conflicts

No structural validation conflicts remain. The 15 matched-coverage durable failed rows are limitations rather than silent missing rows.

## Phase 8 Handoff

Phase 8 owns final claim grading and must apply the evidence boundaries in `06_EVIDENCE_BOUNDARY.md`.
