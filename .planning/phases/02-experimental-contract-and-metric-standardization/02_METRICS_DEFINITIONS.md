# Phase 02 Metric Definitions

**Phase:** 02 - Experimental Contract and Metric Standardization
**Status:** standalone metric contract

## Purpose

This file defines metric names, formulas, denominators, units, valid ranges, and interpretation rules for later pilot and formal experiments. The goal is to make every table reproducible from row-level status data and to prevent ambiguous denominator language.

## Row-Level Status Vocabulary

Every original request in a formal run must have one durable terminal status:

| Status | Meaning | Counts toward served_requests? | Counts toward rejection? |
|---|---|---:|---:|
| `served` | Request accepted and completed or counted as finally served under the run contract | Yes | No |
| `choice_rejected` | Passenger rejected the offered service bundle under the behavioral choice model | No | Yes, choice |
| `feasibility_rejected` | Passenger would accept or is deterministic candidate, but no feasible insertion/service is available | No | Yes, feasibility |
| `failed` | Run or request failed due to implementation/runtime error | No | No; report separately |
| `timeout` | Run or request exceeded configured runtime limit | No | No; report separately |

Additional implementation-specific statuses may be added later, but they must map unambiguously into served, choice rejected, feasibility rejected, failed, or timeout categories.

## Metric Dictionary

| metric_name | formula | numerator | denominator | unit | valid range | interpretation | required experiment families | forbidden uses |
|---|---|---|---|---|---|---|---|---|
| original_requests | count of all generated requests before response/routing | original request rows | none | requests | integer >= 0 | Experiment demand base | all | Do not use served requests as original requests. |
| served_requests | count(status == `served`) | served rows | none | requests | integer >= 0 | Final served demand | all | Do not mix with accepted-before-routing proxies. |
| served_share | served_requests / original_requests | served_requests | original_requests | share | 0 to 1 | Coverage of original demand; D-10 | behavioral, matched coverage, diagnostics | Do not call this behavioral acceptance rate. |
| behavioral_acceptance_rate | choice_accepted_requests / original_requests | requests not `choice_rejected` under behavioral model | original_requests | share | 0 to 1 | Passenger response before feasibility/routing, where observable | behavioral | Do not compute for deterministic all-feasible diagnostics unless labeled not applicable. |
| choice_rejection_rate | count(status == `choice_rejected`) / original_requests | choice_rejected rows | original_requests | share | 0 to 1 | Share lost to passenger choice | behavioral | Do not include feasibility rejections. |
| feasibility_rejection_rate | count(status == `feasibility_rejected`) / original_requests | feasibility_rejected rows | original_requests | share | 0 to 1 | Share lost to operational infeasibility | all | Do not include choice rejections. |
| deterministic_inserted_share | inserted_requests / original_requests | deterministically inserted rows | original_requests | share | 0 to 1 | Feasibility/routing diagnostic coverage | deterministic diagnostics | Do not compare directly to behavioral acceptance as if mechanisms match. |
| total_vkm | sum vehicle distance driven | vehicle-km traveled | none | km | >= 0 | Operator distance burden | all | Do not interpret without served_share. |
| vkm_per_served_trip | vkm_per_served_trip = total_vkm / served_requests | total_vkm | served_requests | km/served trip | >= 0 when served_requests > 0 | Efficiency conditional on served demand | all | Do not label as `vkm_per_trip`. |
| vkm_per_original_request | vkm_per_original_request = total_vkm / original_requests | total_vkm | original_requests | km/original request | >= 0 | System distance burden per demand unit | all | Do not replace served-share reporting. |
| average_wait_time_min | mean pickup wait among served requests / 60 | wait seconds for served rows | served_requests | minutes | >= 0 | Passenger service quality among served users | behavioral, diagnostics | Do not average rejected requests as zero. |
| p95_wait_time_min | 95th percentile pickup wait among served requests / 60 | wait seconds for served rows | served_requests | minutes | >= 0 | Tail waiting burden | behavioral, diagnostics | Do not compute over rejected requests. |
| average_walk_distance_m | mean pickup_walk + dropoff_walk among served requests | walk distance for served rows | served_requests | meters | >= 0 | Walking burden among served users | behavioral, diagnostics | Do not use for DoorToDoor except zero-walk contract. |
| p95_walk_distance_m | 95th percentile pickup_walk + dropoff_walk among served requests | walk distance for served rows | served_requests | meters | >= 0 | Tail walking burden | behavioral, diagnostics | Do not hide by reporting only averages. |
| average_ivt_min | mean in-vehicle time among served requests / 60 | IVT seconds for served rows | served_requests | minutes | >= 0 | In-vehicle burden among served users | all served-trip outputs | Do not include unserved requests as zero. |
| detour_ratio | mean(ivt / direct_time) among served requests with direct_time > 0 | served-trip detour ratios | served_requests with valid direct_time | ratio | >= 1 under physical route semantics | Relative in-vehicle detour | diagnostics, behavioral | Do not treat values below 1 as meaningful without audit. |
| average_fare | mean fare among served requests | fare paid by served rows | served_requests | currency/request | >= 0 if fare modeled | Passenger monetary burden | behavioral if fare is modeled | Do not report if fare is not modeled. |
| operator_cost | cost function defined in config/contract | operating cost components | run or served denominator explicitly stated | currency or index | contract-specific | Operator cost metric | formal outputs if cost defined | Do not mix with vehicle-km unless formula is explicit. |
| revenue | sum fares or payments | collected fares | run | currency | >= 0 if fare modeled | Operator revenue | fare-modeled experiments | Do not report without fare model. |
| profit | revenue - operator_cost | net operating value | run | currency | any real value | Economic output if both cost/revenue defined | fare/cost experiments | Do not report with undefined cost or fare. |
| social_welfare | defined utility/cost welfare formula | utility and penalty terms | run | utility units | contract-specific | Welfare accounting under explicit assumptions | welfare diagnostics | Do not call gamma sweeps Pareto frontier unless gamma affects decisions. |
| type_level_acceptance_rate | served or accepted count for type / original requests of type | type-specific accepted/served rows | original rows of type | share | 0 to 1 | Heterogeneous passenger response | behavioral, equity | Do not overinterpret until Phase 3 calibration/sensitivity. |
| type_level_wait_time | mean wait among served requests by type | wait for served rows of type | served rows of type | minutes | >= 0 | Type-level waiting burden | equity | Do not average unserved as zero. |
| type_level_walk_distance | mean walk among served requests by type | walk for served rows of type | served rows of type | meters | >= 0 | Type-level walking burden | equity | Do not use artificial type assumptions as real population evidence. |
| equity_gini_acceptance | Gini over individual or group acceptance outcomes | acceptance distribution | individuals or groups as stated | index | 0 to 1 | Inequality in access/acceptance | equity | Do not report without declaring individual vs group basis. |
| equity_gini_generalized_cost | Gini over generalized cost/burden among served or all requests | generalized cost distribution | population basis as stated | index | 0 to 1 when non-negative | Inequality in burden | equity | Do not hide whether rejected requests are included. |

## Main Behavioral Table Minimum Columns

Per D-09 and MET-03, main behavioral tables must report these together:

- `served_share`
- `behavioral_acceptance_rate`
- `choice_rejection_rate`
- `feasibility_rejection_rate`
- `total_vkm`
- `vkm_per_served_trip`
- `vkm_per_original_request`

## Forbidden and High-Risk Metric Language

- D-11: The label `vkm_per_trip` is forbidden for new formal evidence. Use `vkm_per_served_trip` or `vkm_per_original_request`.
- D-13: Do not call a post-hoc `gamma` sweep a Pareto frontier unless `gamma` affects routing, offers, or acceptance.
- Do not mix deterministic inserted share with behavioral acceptance rate.
- Do not report vehicle-km savings without served share and rejection rates.
- Do not average rejected passengers as zero wait/walk/IVT unless the table explicitly defines a population-burden metric.

## Requirements Coverage

| Requirement | Coverage |
|---|---|
| MET-01 | Every listed metric includes formula, denominator, unit, valid range, interpretation, and forbidden uses. |
| MET-02 | Served share, behavioral acceptance rate, choice rejection rate, feasibility rejection rate, and deterministic inserted share are distinct. |
| MET-03 | Main behavioral tables must report total vehicle-km, vehicle-km per served trip, vehicle-km per original request, and served share together. |

## Decision Trace

- D-09: Main tables report coverage and rejection mechanisms together.
- D-10: `served_share` denominator is original requests.
- D-11: `vkm_per_trip` is forbidden.
- D-12: Durable row-level request status is required.
- D-13: High-risk metric language is explicitly forbidden.
- D-21: This file is standalone for direct citation by code and manuscript tables.

