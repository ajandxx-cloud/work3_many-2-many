# Phase 03 Parameter Calibration and Sensitivity Design

**Phase:** 03 - Passenger Choice Model Rebuild
**Status:** calibration contract for execution
**Purpose:** Define baseline passenger-choice parameters, source labels, and low/baseline/high sensitivity values before pilot or formal experiments.

## Purpose

This document records the parameter values and sensitivity ranges that the Phase 3 implementation should expose. It is a simulation calibration contract, not evidence that the project has estimated a real-world choice model.

The values below are intentionally conservative. Existing coefficients are treated as inherited planning inputs from the current codebase unless a later phase adds full-text support or real stated/revealed preference data.

## Parameter Table

| parameter | symbol or code field | baseline value | low value | high value | units | source tag | evidence status | notes |
|---|---:|---:|---:|---:|---|---|---|---|
| Walk coefficient, price sensitive | `beta_walk_price_sensitive` | -0.005 | -0.0025 | -0.010 | utility per km | current `PRICE_SENSITIVE` coefficient, converted to km basis | inherited | Keep negative. Low/high are half/double magnitude sensitivity values. |
| Wait coefficient, price sensitive | `beta_wait_price_sensitive` | -0.04 | -0.02 | -0.08 | utility per minute | current `PRICE_SENSITIVE` coefficient | inherited | Supplementary sensitivity. |
| IVT coefficient, price sensitive | `beta_ivt_price_sensitive` | -0.02 | -0.01 | -0.04 | utility per minute | current `PRICE_SENSITIVE` coefficient | inherited | Supplementary sensitivity. |
| Fare coefficient, price sensitive | `beta_fare_price_sensitive` | -0.15 | -0.075 | -0.30 | utility per fare unit | current `PRICE_SENSITIVE` coefficient | inherited | Fare is zero in current runs unless fare modeling is enabled. |
| Walk coefficient, time sensitive | `beta_walk_time_sensitive` | -0.005 | -0.0025 | -0.010 | utility per km | current `TIME_SENSITIVE` coefficient | inherited | Type primarily varies wait and IVT sensitivity. |
| Wait coefficient, time sensitive | `beta_wait_time_sensitive` | -0.10 | -0.05 | -0.20 | utility per minute | current `TIME_SENSITIVE` coefficient | inherited | Supplementary sensitivity. |
| IVT coefficient, time sensitive | `beta_ivt_time_sensitive` | -0.08 | -0.04 | -0.16 | utility per minute | current `TIME_SENSITIVE` coefficient | inherited | Supplementary sensitivity. |
| Fare coefficient, time sensitive | `beta_fare_time_sensitive` | -0.03 | -0.015 | -0.06 | utility per fare unit | current `TIME_SENSITIVE` coefficient | inherited | Lower fare sensitivity than price-sensitive type. |
| Walk coefficient, walk sensitive | `beta_walk_walk_sensitive` | -0.020 | -0.010 | -0.040 | utility per km | current `WALK_SENSITIVE` coefficient | inherited | Main-paper sensitivity should emphasize walk. |
| Wait coefficient, walk sensitive | `beta_wait_walk_sensitive` | -0.04 | -0.02 | -0.08 | utility per minute | current `WALK_SENSITIVE` coefficient | inherited | Supplementary sensitivity. |
| IVT coefficient, walk sensitive | `beta_ivt_walk_sensitive` | -0.02 | -0.01 | -0.04 | utility per minute | current `WALK_SENSITIVE` coefficient | inherited | Supplementary sensitivity. |
| Fare coefficient, walk sensitive | `beta_fare_walk_sensitive` | -0.05 | -0.025 | -0.10 | utility per fare unit | current `WALK_SENSITIVE` coefficient | inherited | Keep as simulation parameter unless fare model is formalized. |
| Unified service ASC | `service_asc` | 0.0 | -0.5 | 0.5 | utility | Phase 3 contract | simulation-range | Main model uses one unified DRT ASC. Sensitivity tests weaker/stronger service attractiveness. |
| DoorToDoor ASC sensitivity | `service_asc_by_design.DoorToDoor` | 0.0 | -0.5 | 0.5 | utility | Phase 3 contract | simulation-range | Sensitivity-only; not allowed as main-model evidence. |
| BidirectionalMP ASC sensitivity | `service_asc_by_design.BidirectionalMeetingPoint` | 0.0 | -0.5 | 0.5 | utility | Phase 3 contract | simulation-range | Sensitivity-only; do not tune to make one design win. |
| Outside option constant | `outside_option_constant` | 0.0 | -0.5 | 0.5 | utility | explicit outside-option contract | simulation-range | Higher value makes outside option more attractive and lowers acceptance. |
| Type share, price sensitive | `type_shares.price_sensitive` | 0.34 | 0.20 | 0.50 | share | scenario parameter | simulation-range | Shares must sum to 1.0 after normalization. |
| Type share, time sensitive | `type_shares.time_sensitive` | 0.33 | 0.20 | 0.50 | share | scenario parameter | simulation-range | Use paired seeded assignment across methods. |
| Type share, walk sensitive | `type_shares.walk_sensitive` | 0.33 | 0.20 | 0.50 | share | scenario parameter | simulation-range | Main-paper sensitivity may shift mass toward this type. |
| Choice random seed | `choice_seed` | 42 | fixed alternate seed set | fixed alternate seed set | integer | project reproducibility convention | inherited | Used for deterministic type assignment and Bernoulli draws. Formal experiments use paired seeds later. |

## Sensitivity Grid

The main sensitivity grid is low/baseline/high and one-at-a-time:

| sensitivity dimension | low | baseline | high | evidence role |
|---|---:|---:|---:|---|
| walk coefficients | 0.5x magnitude | 1.0x | 2.0x magnitude | main-paper reviewer-critical sensitivity |
| wait coefficients | 0.5x magnitude | 1.0x | 2.0x magnitude | supplementary sensitivity |
| IVT coefficients | 0.5x magnitude | 1.0x | 2.0x magnitude | supplementary sensitivity |
| fare coefficients | 0.5x magnitude | 1.0x | 2.0x magnitude | supplementary sensitivity if fare is modeled |
| unified ASC | -0.5 | 0.0 | 0.5 | main-paper reviewer-critical sensitivity |
| outside option constant | -0.5 | 0.0 | 0.5 | main-paper reviewer-critical sensitivity |
| type shares | more price/time sensitive | balanced 0.34/0.33/0.33 | more walk sensitive | main-paper reviewer-critical sensitivity |

Main-paper sensitivity should focus on:

- ASC
- outside option
- passenger type shares
- walk sensitivity

Wait, IVT, and fare coefficients should appear in the parameter table and supplementary sensitivity unless later evidence makes them central.

Optional targeted interaction checks are allowed only if Phase 6 runtime permits. Recommended interactions, if affordable:

- high walk sensitivity plus high outside option
- high BidirectionalMP ASC sensitivity plus high walk sensitivity, explicitly labeled sensitivity-only
- walk-sensitive type-share shift plus matched-coverage diagnostic context

No full factorial grid is required by Phase 3.

## Claim Discipline

These values do not constitute real-data calibration. Use the following language discipline:

- Values marked `inherited` are carried forward from current code and must be described as inherited simulation inputs until supported by full-text literature review or new data.
- Values marked `simulation-range` are scenario/sensitivity assumptions.
- Do not write "estimated", "calibrated to Beijing", "revealed preference", or "stated preference" for any value in this table.
- The allowed manuscript framing is "simulated passenger heterogeneity and sensitivity ranges" unless a later phase adds real choice data.
- Design-specific ASC values are sensitivity-only and cannot be used to claim the main service design is intrinsically preferred.

## Implementation Notes

- Code should keep units explicit. Existing code mixes meters/seconds in simulation with km/minute-style coefficients; Phase 3 implementation should centralize conversions.
- Type assignment must use stable request-level seeding so the same request has the same type across service designs in paired comparisons.
- Acceptance draws should be reproducible under the configured seed and request identity.
- Feasibility-rejected rows must not receive proxy utility values from nearest meeting points.

## Requirements Coverage

| Requirement | Coverage |
|---|---|
| CHO-01 | `service_asc` and design-specific ASC sensitivity rows define the attractiveness term. |
| CHO-02 | `outside_option_constant` row and grid define explicit outside-option sensitivity. |
| CHO-03 | Passenger type coefficients and type shares are documented with source tags and evidence status. |

## Decision Trace

- D-05: Main model uses unified service ASC.
- D-06: Outside option constant is explicit.
- D-07: Passenger type parameters are source-labeled and not described as real-data calibration.
- D-08: Passenger type shares are scenario parameters with seeded assignment.
- D-09: Main sensitivity is one-at-a-time.
- D-10: Main sensitivity focuses on ASC, outside option, type shares, and walk.
- D-11: Wait, IVT, and fare are parameter-table and supplementary sensitivity terms.
- D-12: Main values use low/baseline/high.
- D-13: Baseline values, low/high values, source tags, and evidence status are documented.

