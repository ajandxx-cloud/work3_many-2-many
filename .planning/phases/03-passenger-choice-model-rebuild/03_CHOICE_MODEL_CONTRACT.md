# Phase 03 Choice Model Contract

**Phase:** 03 - Passenger Choice Model Rebuild
**Status:** contract draft for execution
**Purpose:** Define the passenger-response semantics that later code, pilot runs, formal experiments, and manuscript tables must follow.

## Purpose

This contract replaces the current proxy-before-routing MNL filter with a single-offer acceptance model evaluated on an actual feasible offered bundle. It exists to make passenger response credible, reproducible, interpretable, and shared across behavioral service-design comparisons.

Phase 3 is allowed to implement choice logic and utility logging. It does not approve final parameter calibration claims, pilot evidence, formal experiment results, or manuscript conclusions.

## Phase Boundary

In scope:

- Single-offer binary-logit acceptance for one feasible service bundle.
- Unified service attractiveness term through `service_asc`.
- Explicit outside option through `outside_option_constant`.
- Passenger type coefficients and seeded passenger type assignment.
- Durable request statuses and utility-component logging for choice outcomes.

Out of scope:

- Multi-offer choice-set selection.
- Fallback offers after passenger rejection.
- Formal experiments, pilot experiments, ALNS/MILP diagnostic validation, and final claim approval.

## Choice Timing

Passenger choice is evaluated on an actual feasible offered bundle after route feasibility is known. The choice model must not compute acceptance from nearest pickup/dropoff meeting-point proxies before routing.

Required flow:

1. Build or identify a candidate offer for the request.
2. Confirm the offer is operationally feasible and contains concrete pickup/dropoff/schedule/vehicle attributes.
3. Evaluate passenger acceptance on that actual offer.
4. Commit the offer to route state only when accepted.
5. Record a terminal request status and utility log row.

This implements D-01 and closes the known weakness in `_mnl_filter_requests()`.

## Single-Offer Contract

Phase 3 implements a single-offer model only. The implementation may use data structures that can later hold multiple offers, but Phase 3 must present exactly one offer to the passenger.

If the passenger rejects the offer, the terminal status is `choice_rejected`; no fallback offer is attempted in this phase. This implements D-02 and D-03.

If no feasible offer exists, the terminal status is `feasibility_rejected`; detailed reasons should preserve the operational cause. Required reason vocabulary includes at least:

- `no_candidate_mp`
- `no_feasible_route`
- `passenger_declined`

Additional implementation-specific reasons are allowed if they map unambiguously to the Phase 2 status vocabulary. This implements D-04.

## Terminal Status Semantics

Every original request in behavioral runs must map to one durable terminal status:

| Status | Meaning | Utility logging rule |
|---|---|---|
| `served` | Passenger accepted and the request is inserted/completed under the run contract. | Log actual offered utility and realized offer attributes. |
| `choice_rejected` | Passenger rejected the actual feasible offer. | Log actual offered utility, outside utility, probability, and draw. |
| `feasibility_rejected` | No feasible offer exists or no candidate meeting point exists. | Do not fabricate proxy utility; log feasibility reason and missing-offer fields. |
| `failed` | Request or run failed due to implementation/runtime error. | Log error/status fields if available. |
| `timeout` | Request or run exceeded configured runtime limit. | Log timeout/status fields if available. |

These statuses are the bridge to `02_METRICS_DEFINITIONS.md`; aggregate metrics must be derivable from raw request rows.

## Utility Specification

For passenger type `k` evaluating one offered bundle `b`, use:

```text
U_offer =
  service_asc
  + beta_walk_k * total_walk
  + beta_wait_k * wait_time
  + beta_ivt_k * ivt
  + beta_fare_k * fare

U_outside = outside_option_constant

P_accept = exp(U_offer) / (exp(U_offer) + exp(U_outside))
```

Required terms:

- `service_asc`: unified DRT service attractiveness constant in the main model.
- `outside_option_constant`: explicit outside-option utility.
- `total_walk`: pickup walk plus dropoff walk.
- `wait_time`: request arrival or earliest time to scheduled pickup.
- `ivt`: scheduled in-vehicle travel time.
- `fare`: offered fare or zero when fare is not modeled.
- `beta_*`: passenger-type coefficients.

The main model uses one unified `service_asc`. Design-specific ASC values are sensitivity-only, not main-model evidence. Door-to-door behavioral comparisons use the same response model with walk set to zero and service attributes adapted to the actual offered door-to-door bundle. This implements D-05 and D-06 and supports CHO-01 and CHO-02.

## Passenger Type Assignment

Passenger type parameters should use literature-anchored values where defensible and explicitly labeled simulation ranges otherwise. The project must not describe these coefficients as real-data calibration unless later real stated/revealed preference data are introduced.

Passenger type shares are scenario parameters. Assignment must be deterministic at request level:

```text
type = assign_type(base_seed, request_id, type_shares)
```

The same seed/request pair must receive the same passenger type across DoorToDoor, SingleSidedPickup, SingleSidedDropoff, and BidirectionalMeetingPoint comparisons. Service-design labels must not influence type assignment. This implements D-07 and D-08 and supports CHO-03.

## Utility Component Logging

Formal row-level logging must include enough information to explain acceptance outcomes.

Required raw passenger-row fields:

- `run_id`
- `seed`
- `scenario`
- `method`
- `request_id`
- `status`
- `detailed_reason`
- `passenger_type`
- `acceptance_probability`
- `random_draw`

Required utility-component fields:

- all raw row join keys
- `pickup_walk`
- `dropoff_walk`
- `wait_time`
- `ivt`
- `fare`
- `service_design`
- `pickup_mp_id`
- `dropoff_mp_id`
- `vehicle_id`
- `scheduled_pickup`
- `scheduled_dropoff`
- walk utility component
- wait utility component
- IVT utility component
- fare utility component
- `service_asc`
- `outside_option_constant`
- `total_utility`
- `outside_utility`

`choice_rejected` rows record the complete utility of the actual offered bundle. `feasibility_rejected` rows must not fabricate proxy utility; they record the missing-offer cause instead. This implements D-14, D-15, and D-16 and supports CHO-04.

## Two-Layer Output Structure

Use a two-layer output structure:

1. Raw passenger rows keep status, detailed reason, passenger type, and key probability fields.
2. A separate utility-components artifact stores the complete utility breakdown.

The utility-components artifact must be joinable by:

```text
run_id, seed, scenario, method, request_id
```

A recommended output name is `utility_components.csv`, written alongside run outputs in the configured results directory. The exact format may be CSV or JSONL if tests document the schema. This implements D-17.

## Sensitivity Ownership

Phase 3 defines parameter hooks and sensitivity design. Later pilot/formal phases execute sensitivity runs.

Main sensitivity emphasis:

- service ASC
- outside option
- passenger type shares
- walk sensitivity

Supplementary sensitivity:

- wait coefficient
- IVT coefficient
- fare coefficient

Main sensitivity should be low/baseline/high one-at-a-time. Targeted interactions are optional only if Phase 6 runtime permits. This implements D-09 through D-12.

## Downstream Integration

Phase 3 implementation should preserve the Phase 2 evidence-family boundary:

- Behavioral main comparisons use shared passenger-response semantics.
- Deterministic/no-choice diagnostics remain separate.
- DoorToDoor in behavioral evidence must not remain deterministic all-accept.
- Fixed accepted-set and matched-coverage experiments consume the same status and utility fields later.

Phase 4 still owns missing service baseline validation and ALNS/MILP diagnostic scope. Phase 5 owns pilot smoke tests. Phase 6 owns formal paired experiments.

## Requirements Coverage

| Requirement | Coverage |
|---|---|
| CHO-01 | Utility specification includes unified `service_asc`; design-specific ASCs are sensitivity-only. |
| CHO-02 | Utility specification includes explicit `outside_option_constant` and outside utility. |
| CHO-03 | Passenger type coefficients, type shares, and deterministic seeded assignment are defined with source-label discipline. |
| CHO-04 | Utility-component logging explains served and choice-rejected outcomes and avoids proxy utility for feasibility rejections. |

## Decision Trace

- D-01: Choice uses actual feasible offered bundle.
- D-02: Single-offer model only.
- D-03: Refusal is terminal `choice_rejected`.
- D-04: Missing feasible offer is `feasibility_rejected` with detailed reason.
- D-05: Unified service ASC in main model.
- D-06: Explicit outside option constant.
- D-07: Passenger type values are literature-anchored where possible or simulation-range.
- D-08: Type shares are scenario parameters with seeded request-level assignment.
- D-09: One-at-a-time sensitivity by default.
- D-10: Main sensitivity focuses on ASC, outside option, type shares, and walk.
- D-11: Wait, IVT, and fare remain parameter-table and supplementary sensitivity terms.
- D-12: Low/baseline/high main values.
- D-13: Calibration document records values, source tags, and evidence status.
- D-14: Logs include status, reason, type, offer attributes, components, probability, and draw.
- D-15: Offer attributes include walk, wait, IVT, fare, design, MPs, vehicle, and schedule.
- D-16: Choice rejections log actual offered utility; feasibility rejections do not fabricate utility.
- D-17: Raw rows and complete utility components are separate joinable artifacts.

