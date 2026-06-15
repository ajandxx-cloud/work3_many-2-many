# Phase 02 Coverage-Confounding Plan

**Phase:** 02 - Experimental Contract and Metric Standardization
**Status:** coverage-control contract

## Purpose

This plan defines how later experiments distinguish operating-efficiency gains from lower served share or passenger rejection. It exists because Phase 0 verified that current headline vehicle-km results are coverage-confounded.

## Unconstrained Behavioral Comparison

The unconstrained behavioral comparison is the main service-design experiment family. It compares DoorToDoor, SingleSidedPickup, SingleSidedDropoff, and BidirectionalMeetingPoint under the same passenger-response model and comparable routing setup.

Required outputs:

- `served_share`
- `behavioral_acceptance_rate`
- `choice_rejection_rate`
- `feasibility_rejection_rate`
- `total_vkm`
- `vkm_per_served_trip`
- `vkm_per_original_request`
- passenger burden metrics such as wait, walk, IVT, and detour

Interpretation:

- This family shows the full coverage, acceptance, rejection, and efficiency tradeoff.
- D-16: If BidirectionalMeetingPoint has lower vehicle-km but also lower `served_share`, the result must be framed as a coverage-efficiency tradeoff.
- It cannot support unconditional superiority unless coverage, passenger burden, and efficiency all support the exact claim.

## Matched-Coverage Comparison

Matched coverage is core supplementary evidence, not appendix-only robustness.

Design rule:

- Use a target served_share cap.
- Compare each service design near the same target served share.
- The target and tolerance must be reported before formal runs.
- If a method cannot reach the target or exceeds tolerance, record the failure rather than dropping the row.

Required outputs:

- target `served_share` cap
- achieved `served_share`
- matching/capping mechanism
- number of requests removed, capped, or unserved by design
- all main metric columns from `02_METRICS_DEFINITIONS.md`

Interpretation:

- D-14: Matched coverage is a core supplementary experiment in the main manuscript.
- D-15: The design uses a target served_share cap.
- It can test whether efficiency differences persist near equal coverage.
- It does not replace unconstrained behavioral evidence because passenger response and natural coverage are themselves part of the service-design outcome.

## Fixed Accepted-Set Routing Diagnostic

Fixed accepted-set diagnostics compare routing/service-design efficiency for the same passenger set.

Design rule:

- Construct the intersection of requests commonly serviceable/accepted by all methods.
- Run each routing/service-design method on that common set.
- Report the size and composition of the retained set.
- Preserve the diagnostic label in all tables and captions.

Required outputs:

- fixed accepted-set construction rule
- retained request count and retained share
- method-by-method success/failure rows
- `total_vkm`
- `vkm_per_served_trip`
- route-quality and passenger-burden diagnostics where meaningful

Interpretation:

- D-17: The passenger set must be the intersection of requests commonly serviceable/accepted by all methods, avoiding bias toward BidirectionalMP or DoorToDoor.
- D-18: Fixed accepted-set diagnostics do not replace behavioral main evidence.
- This design answers whether routing efficiency differences persist when the passenger set is held constant.
- It cannot claim passenger acceptance, served share, or market attractiveness.

## Interpretation Matrix

| Design | Can claim | Cannot claim |
|---|---|---|
| Unconstrained Behavioral Comparison | Full service-design tradeoff among coverage, acceptance, rejection, and efficiency | Pure routing efficiency independent of coverage/passenger set |
| Matched-Coverage Comparison | Efficiency comparison near a common served share | Natural coverage or passenger response superiority |
| Fixed Accepted-Set Routing Diagnostic | Routing/service-design distance differences on identical passengers | Behavioral acceptance, coverage, or market attractiveness |

## Phase Ownership

| Work item | Owner phase |
|---|---|
| Define this control contract | Phase 2 |
| Rebuild choice model used by behavioral comparisons | Phase 3 |
| Implement target served-share cap and fixed accepted-set mechanics | Phase 4 |
| Smoke-test controls on pilot seeds | Phase 5 |
| Run formal paired matched-coverage and fixed accepted-set diagnostics | Phase 6 |
| Decide final claim strength | Phase 8 |

## Requirements Coverage

| Requirement | Coverage |
|---|---|
| EXP-04 | Defines unconstrained behavioral, matched-coverage, and fixed accepted-set designs. |

## Decision Trace

- D-14: Matched coverage is core supplementary evidence.
- D-15: Matched coverage uses a target served_share cap.
- D-16: Lower vehicle-km with lower served share is a coverage-efficiency tradeoff.
- D-17: Fixed accepted-set diagnostics use the intersection of requests commonly serviceable/accepted by all methods.
- D-18: Fixed accepted-set diagnostics do not replace behavioral evidence.

