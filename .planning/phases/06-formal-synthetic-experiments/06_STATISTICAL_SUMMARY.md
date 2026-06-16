# Phase 6 Statistical Summary

## 1. Main Behavioral Mean Metrics By Method

| method | served_share_mean | total_vehicle_km_mean | vkm_per_served_trip_mean | vkm_per_original_request_mean | choice_rejection_rate_mean | feasibility_rejection_rate_mean |
| --- | --- | --- | --- | --- | --- | --- |
| FullModel | 0.157529 | 444.491 | 9.95103 | 1.56868 | 0.539508 | 0.302963 |
| DoorToDoor | 0.2004 | 772.698 | 14.6651 | 2.90023 | 0.563021 | 0.236579 |
| SingleSidedDropoff | 0.193546 | 710.948 | 13.9071 | 2.66234 | 0.548517 | 0.257937 |
| SingleSidedPickup | 0.199258 | 715.579 | 13.6828 | 2.74061 | 0.544288 | 0.256454 |

## 2. Paired Differences Versus DoorToDoor

| metric | n_valid_pairs | mean_difference | full_better_share |
| --- | --- | --- | --- |
| served_share | 80 | -0.0428708 | 0.0875 |
| behavioral_acceptance_rate | 80 | 0.0235125 | 0.575 |
| choice_rejection_rate | 80 | -0.0235125 | 0.575 |
| feasibility_rejection_rate | 80 | 0.0663833 | 0.3 |
| total_vehicle_km | 80 | -328.207 | 0.9625 |
| vkm_per_served_trip | 80 | -4.71407 | 0.9875 |
| vkm_per_original_request | 80 | -1.33155 | 0.9625 |

## 3. Paired Differences Versus SingleSidedPickup

| metric | n_valid_pairs | mean_difference | full_better_share |
| --- | --- | --- | --- |
| served_share | 80 | -0.0417292 | 0.05 |
| behavioral_acceptance_rate | 80 | 0.00477917 | 0.5 |
| choice_rejection_rate | 80 | -0.00477917 | 0.5 |
| feasibility_rejection_rate | 80 | 0.0465083 | 0.3625 |
| total_vehicle_km | 80 | -271.088 | 0.9875 |
| vkm_per_served_trip | 80 | -3.73176 | 0.9875 |
| vkm_per_original_request | 80 | -1.17194 | 0.9875 |

## 4. Paired Differences Versus SingleSidedDropoff

| metric | n_valid_pairs | mean_difference | full_better_share |
| --- | --- | --- | --- |
| served_share | 80 | -0.0360167 | 0.1 |
| behavioral_acceptance_rate | 80 | 0.00900833 | 0.55 |
| choice_rejection_rate | 80 | -0.00900833 | 0.55 |
| feasibility_rejection_rate | 80 | 0.045025 | 0.3125 |
| total_vehicle_km | 80 | -266.456 | 0.975 |
| vkm_per_served_trip | 80 | -3.9561 | 0.9875 |
| vkm_per_original_request | 80 | -1.09366 | 0.975 |

## 5. Confidence Intervals

Paired bootstrap percentile 95 percent confidence intervals are implemented with bootstrap seed 20260616 and 5000 resamples.

| baseline | metric | n_valid_pairs | mean_difference | ci_low | ci_high |
| --- | --- | --- | --- | --- | --- |
| DoorToDoor | served_share | 80 | -0.0428708 | -0.0521051 | -0.033854 |
| SingleSidedPickup | served_share | 80 | -0.0417292 | -0.0505343 | -0.033687 |
| SingleSidedDropoff | served_share | 80 | -0.0360167 | -0.0427673 | -0.0292706 |
| DoorToDoor | total_vehicle_km | 80 | -328.207 | -368.694 | -289.573 |
| SingleSidedPickup | total_vehicle_km | 80 | -271.088 | -297.616 | -244.173 |
| SingleSidedDropoff | total_vehicle_km | 80 | -266.456 | -297.561 | -237.175 |
| DoorToDoor | vkm_per_served_trip | 80 | -4.71407 | -5.24388 | -4.23756 |
| SingleSidedPickup | vkm_per_served_trip | 80 | -3.73176 | -4.13762 | -3.33214 |
| SingleSidedDropoff | vkm_per_served_trip | 80 | -3.9561 | -4.51775 | -3.45069 |
| DoorToDoor | vkm_per_original_request | 80 | -1.33155 | -1.47992 | -1.19189 |
| SingleSidedPickup | vkm_per_original_request | 80 | -1.17194 | -1.32126 | -1.03573 |
| SingleSidedDropoff | vkm_per_original_request | 80 | -1.09366 | -1.22317 | -0.973885 |

## 6. Paired Test Results

Paired hypothesis tests are not implemented in Phase 6. Phase 8 can use paired bootstrap confidence intervals and descriptive formal evidence, but should not cite p-values unless a paired test module is added.

## 7. CI / Test Boundary

Confidence intervals are implemented; paired hypothesis tests are not. Any claim gate should treat this as formal descriptive paired evidence with bootstrap uncertainty, not a full inferential test suite.

## 8. Matched-Coverage Paired Comparison Summary

| baseline | metric | n_valid_pairs | mean_difference | missing_pair_count | full_better_share |
| --- | --- | --- | --- | --- | --- |
| DoorToDoor | total_vehicle_km | 65 | -167.184 | 15 | 0.984615 |
| SingleSidedPickup | total_vehicle_km | 65 | -141.51 | 15 | 0.969231 |
| SingleSidedDropoff | total_vehicle_km | 65 | -141.543 | 15 | 0.984615 |
| DoorToDoor | vkm_per_served_trip | 65 | -4.61684 | 15 | 0.984615 |
| SingleSidedPickup | vkm_per_served_trip | 65 | -3.99848 | 15 | 0.969231 |
| SingleSidedDropoff | vkm_per_served_trip | 65 | -4.10731 | 15 | 0.984615 |
| DoorToDoor | vkm_per_original_request | 65 | -0.68084 | 15 | 0.984615 |
| SingleSidedPickup | vkm_per_original_request | 65 | -0.580799 | 15 | 0.969231 |
| SingleSidedDropoff | vkm_per_original_request | 65 | -0.604853 | 15 | 0.984615 |
| DoorToDoor | served_share | 65 | 0 | 15 | 0 |
| SingleSidedPickup | served_share | 65 | 0 | 15 | 0 |
| SingleSidedDropoff | served_share | 65 | 0 | 15 | 0 |

## 9. Fixed Accepted-Set Comparison Summary

| baseline | metric | n_valid_pairs | mean_difference | missing_pair_count | full_better_share |
| --- | --- | --- | --- | --- | --- |
| DoorToDoor | total_vehicle_km | 80 | 2.71168 | 0 | 0.525 |
| SingleSidedPickup | total_vehicle_km | 80 | 27.1686 | 0 | 0.35 |
| SingleSidedDropoff | total_vehicle_km | 80 | 22.9826 | 0 | 0.35 |
| DoorToDoor | vkm_per_served_request | 80 | -5.23247 | 0 |  |
| SingleSidedPickup | vkm_per_served_request | 80 | -3.79588 | 0 |  |
| SingleSidedDropoff | vkm_per_served_request | 80 | -3.83108 | 0 |  |
| DoorToDoor | vkm_per_original_request | 80 | 0.0523446 | 0 | 0.525 |
| SingleSidedPickup | vkm_per_original_request | 80 | 0.126704 | 0 | 0.35 |
| SingleSidedDropoff | vkm_per_original_request | 80 | 0.115084 | 0 | 0.35 |
| DoorToDoor | deterministic_inserted_share | 80 | 0.317981 | 0 |  |
| SingleSidedPickup | deterministic_inserted_share | 80 | 0.309589 | 0 |  |
| SingleSidedDropoff | deterministic_inserted_share | 80 | 0.301117 | 0 |  |

## 10. Robustness Setting-Level Summary

| package_id | parameter_setting_id | metric | n_valid_pairs | mean_full_minus_door_to_door | full_better_share |
| --- | --- | --- | --- | --- | --- |
| utility_sensitivity | baseline_default | vkm_per_served_trip | 30 | -5.20212 | 1 |
| utility_sensitivity | baseline_default | vkm_per_original_request | 30 | -1.55334 | 0.966667 |
| utility_sensitivity | baseline_default | served_share | 30 | -0.0568333 | 0.1 |
| utility_sensitivity | ivt_disutility_high | vkm_per_served_trip | 30 | -6.01926 | 1 |
| utility_sensitivity | ivt_disutility_high | vkm_per_original_request | 30 | -1.45261 | 0.966667 |
| utility_sensitivity | ivt_disutility_high | served_share | 30 | -0.0508333 | 0.0666667 |
| utility_sensitivity | outside_option_high | vkm_per_served_trip | 30 | -6.24348 | 0.933333 |
| utility_sensitivity | outside_option_high | vkm_per_original_request | 30 | -0.876604 | 0.966667 |
| utility_sensitivity | outside_option_high | served_share | 30 | -0.0250556 | 0.133333 |
| utility_sensitivity | service_asc_low | vkm_per_served_trip | 30 | -6.24348 | 0.933333 |
| utility_sensitivity | service_asc_low | vkm_per_original_request | 30 | -0.876604 | 0.966667 |
| utility_sensitivity | service_asc_low | served_share | 30 | -0.0250556 | 0.133333 |
| utility_sensitivity | wait_disutility_high | vkm_per_served_trip | 30 | -5.63086 | 1 |
| utility_sensitivity | wait_disutility_high | vkm_per_original_request | 30 | -1.51188 | 0.966667 |
| utility_sensitivity | wait_disutility_high | served_share | 30 | -0.0515 | 0.0666667 |
| utility_sensitivity | walk_disutility_high | vkm_per_served_trip | 30 | -5.19963 | 1 |
| utility_sensitivity | walk_disutility_high | vkm_per_original_request | 30 | -1.55513 | 0.966667 |
| utility_sensitivity | walk_disutility_high | served_share | 30 | -0.0570556 | 0.1 |
| utility_sensitivity | walk_sensitive_majority | vkm_per_served_trip | 30 | -4.62992 | 0.966667 |
| utility_sensitivity | walk_sensitive_majority | vkm_per_original_request | 30 | -1.75906 | 1 |
| utility_sensitivity | walk_sensitive_majority | served_share | 30 | -0.0634444 | 0.0666667 |
| mp_density_walking_radius | default_radius_default_density | vkm_per_served_trip | 30 | -5.20212 | 1 |
| mp_density_walking_radius | default_radius_default_density | vkm_per_original_request | 30 | -1.55334 | 0.966667 |
| mp_density_walking_radius | default_radius_default_density | served_share | 30 | -0.0568333 | 0.1 |
| mp_density_walking_radius | high_radius_dense_density | vkm_per_served_trip | 30 | -5.26691 | 1 |
| mp_density_walking_radius | high_radius_dense_density | vkm_per_original_request | 30 | -1.14521 | 0.966667 |
| mp_density_walking_radius | high_radius_dense_density | served_share | 30 | -0.0206667 | 0.3 |
| mp_density_walking_radius | low_radius_sparse_density | vkm_per_served_trip | 30 | -15.7067 | 1 |
| mp_density_walking_radius | low_radius_sparse_density | vkm_per_original_request | 30 | -3.07504 | 1 |
| mp_density_walking_radius | low_radius_sparse_density | served_share | 30 | -0.206111 | 0 |
| fleet_demand_stress | stress_base | vkm_per_served_trip | 10 | -5.14502 | 1 |
| fleet_demand_stress | stress_base | vkm_per_original_request | 10 | -1.43642 | 1 |
| fleet_demand_stress | stress_base | served_share | 10 | -0.0435 | 0.1 |
| fleet_demand_stress | stress_high_demand | vkm_per_served_trip | 10 | -3.80571 | 1 |
| fleet_demand_stress | stress_high_demand | vkm_per_original_request | 10 | -1.5463 | 1 |
| fleet_demand_stress | stress_high_demand | served_share | 10 | -0.0703333 | 0 |
| fleet_demand_stress | stress_low_demand | vkm_per_served_trip | 10 | -6.04722 | 1 |
| fleet_demand_stress | stress_low_demand | vkm_per_original_request | 10 | -1.84164 | 1 |
| fleet_demand_stress | stress_low_demand | served_share | 10 | -0.056 | 0.1 |

## 11. Caution Notes For Incomplete Or Diagnostic-Only Evidence

- Matched coverage has 15 durable failed FullModel rows; completed-pair summaries must state their valid-pair counts.
- Fixed accepted-set routing is diagnostic-only.
- Robustness grids are reduced diagnostics.
- Equity outputs are exploratory because type parameters are simulation ranges.
