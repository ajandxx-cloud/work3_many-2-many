# Phase 9 Revised Introduction and Literature Positioning Refresh

**Phase:** 09 - Manuscript Restructure for TR Part E
**Refresh date:** 2026-06-16
**Status:** claim-gated introduction plan complete

## Introduction Boundary

The introduction must be built around the fair-evidence problem, not a broad
superiority or firstness claim. It may preview the strongest Phase 8 result only
as a conditional synthetic finding: lower vehicle-km intensity under the tested
paired design, accompanied by lower served share and rejection/coverage context.

## Required Introduction Flow

### 1. Opening Motivation

Open with the operational challenge. Meeting-point DRT can reduce vehicle
detours by allowing passengers to walk to pickup and from dropoff points, but
that flexibility changes passenger burden, acceptance, served share, and
route-feasibility outcomes. The evaluation problem is therefore not only
routing, but evidence-consistent service design.

### 2. Research Gap

Frame the gap as an integrated evidence-chain gap. Prior work covers overlapping
ideas in DRT, DARP with meeting points, ridepooling, passenger choice, walking
access/egress, and rolling-horizon dispatch. The gap is not that no one has
considered dropoff walking or meeting points beyond pickup. The gap is that
pickup/dropoff meeting-point design, passenger response, dynamic dispatch, and
denominator-disciplined evidence are rarely evaluated together under a
claim-gated comparison protocol.

### 3. Why Fair Comparison Is Difficult

Explain that distance savings can be inflated or misread when methods serve
different passenger sets, use inconsistent response assumptions, mix behavioral
and deterministic rows, or report vehicle-km without clear denominators.
Comparisons must therefore state method family, seed pairing, served share,
acceptance/rejection, failure rows, and uncertainty evidence.

### 4. Why Passenger Response Matters

Passenger response determines whether the service actually captures demand
under walking, waiting, fare, in-vehicle travel, and outside-option trade-offs.
The introduction may state that passenger response and rejection mechanisms
affect the interpretation of efficiency and served-share outcomes. It must not
claim that passengers prefer the FullModel or that acceptance improves
unconditionally.

### 5. Why Coverage-Confounding Matters

The introduction must state that lower vehicle-km intensity can occur together
with lower served share. The main evidence is therefore a coverage-efficiency
trade-off rather than pure routing superiority. Matched-coverage controls and
fixed accepted-set diagnostics are needed to bound this confounding, but they
do not replace the behavioral main comparison.

### 6. Contribution List

Use this Phase-8-supported contribution order:

1. A choice-aware dynamic service-design simulation framework for many-to-many
   DRT with pickup and dropoff meeting-point design, passenger response, and
   rolling-horizon routing.
2. A consistent passenger-response baseline taxonomy separating behavioral
   service-design comparisons from deterministic and algorithm diagnostics.
3. Paired formal synthetic evidence with explicit vehicle-km denominators,
   served share, acceptance/rejection outcomes, bootstrap uncertainty, and
   durable failure-row accounting.
4. Coverage-confounding controls, including matched-coverage completed pairs
   and fixed accepted-set routing diagnostics, with their limitations stated.
5. Robustness, equity, algorithm, and Beijing-inspired scenario diagnostics
   reported with bounded claim strength.
6. A reproducibility-oriented evidence package for Phase 6 outputs, while final
   table/figure regeneration remains a Phase 10 task.

Contribution wording must avoid:

- first/only claims;
- unconditional superiority;
- real-city validation;
- direct policy deployment;
- final reproducibility-package completion.

### 7. Research Questions

Recommended research questions:

1. Under shared passenger-response assumptions and paired synthetic conditions,
   how does bidirectional pickup/dropoff meeting-point design affect vehicle-km
   intensity relative to door-to-door and single-sided designs?
2. How do served share, behavioral acceptance, choice rejection, and feasibility
   rejection change the interpretation of vehicle-km efficiency?
3. What coverage controls, diagnostics, equity patterns, and scenario
   boundaries are needed before converting simulation evidence into managerial
   insight?

Algorithm diagnostics should not be a standalone research question. They support
implementation credibility and diagnostic scope disclosure.

### 8. Paper Organization

Close the introduction with the refreshed manuscript order:

- Literature Review;
- Method;
- Experimental Design;
- Results;
- Discussion;
- Managerial Insights and Limitations;
- Conclusion.

The organization paragraph should state that formal main evidence is presented
before diagnostics and that limitations bound managerial interpretation.

## Literature Positioning Rules

| Risk | Required replacement |
|---|---|
| "This is the first bidirectional meeting-point DRT paper" | "The paper evaluates an integrated choice-aware dynamic service-design simulation framework." |
| "No prior work considers dropoff walking" | "Prior work covers partially overlapping walking-location and meeting-point designs." |
| "Existing work only assigns pickup-side meeting points" | "Existing literatures motivate the need for an integrated pickup/dropoff evidence-chain comparison." |
| "Algorithm novelty proves the contribution" | "Rolling-horizon ALNS is an operational mechanism and diagnostic support, not the headline claim." |
| "Beijing case validates real operations" | "Beijing-inspired synthetic scenario is illustrative and externally limited." |

## Result Preview Rules

The introduction may preview only this result direction:

Formal paired synthetic experiments show lower vehicle-km intensity for the
BidirectionalMP/FullModel design under the tested conditions, but the result
must be read with lower served share and rejection/coverage outcomes.

Do not preview:

- exact legacy percentage gains;
- universal dominance;
- same-service-level superiority;
- equity improvement;
- real-city validation;
- deployment readiness.

## Manuscript Rewrite Notes

- Put limitations before policy or managerial guidance.
- Cite Phase 8 claim IDs internally during drafting so every contribution and
  result preview maps to the claim gate.
- Keep Cortenbach/Fielbaum/Wu-related novelty language conservative until final
  citation cleanup is complete.
