# Phase 9 TR-E Manuscript Structure Refresh

**Phase:** 09 - Manuscript Restructure for TR Part E
**Refresh date:** 2026-06-16
**Status:** claim-gated refresh complete
**Source of truth:** Phase 8 claim gate

## Refresh Purpose

The earlier Phase 9 manuscript structure was created before the Phase 8
claim-evidence gate existed. It correctly kept final claim language blocked, but
it is now stale. This refresh replaces placeholder-driven planning with a
Phase-8-gated manuscript structure.

This file remains a planning artifact. It does not edit manuscript `.tex` files
and does not enter Phase 10.

## Claim-Gated Storyline

The manuscript should not argue that bidirectional meeting points are always
best. The defensible story is:

The paper develops and evaluates an integrated choice-aware dynamic
service-design simulation framework for many-to-many DRT. The framework jointly
models pickup and dropoff meeting-point design, passenger response, and
rolling-horizon routing. Formal paired synthetic experiments show that the
BidirectionalMP/FullModel design can reduce vehicle-km intensity relative to
door-to-door and single-sided choice baselines under the tested conditions, but
this result must be interpreted together with served share, acceptance/rejection
outcomes, matched-coverage controls, diagnostic boundaries, and synthetic-data
limitations. The Beijing-labeled material is a Beijing-inspired synthetic
scenario, not real Beijing validation.

## Allowed Claim Center

The strongest allowed main claim is the Phase 8 C-EFF-01 plus C-COV-01 pair:

- Under the tested formal synthetic paired design, BidirectionalMP/FullModel
  shows lower vehicle-km intensity than DoorToDoor and single-sided choice
  baselines.
- The same result is accompanied by lower served share, so operating efficiency,
  coverage, acceptance, and rejection must be read jointly.

The manuscript may also use the Phase 8 moderate and exploratory claims only at
their approved strength:

- Integrated framework contribution: moderate, no first/only language.
- Passenger response and rejection mechanisms affect interpretation: moderate.
- Matched-coverage completed pairs remain consistent with the efficiency
  direction, but 15 durable failed FullModel rows limit the claim: moderate.
- Fixed accepted-set supports only a routing/service-design diagnostic on vkm
  per served request: moderate diagnostic.
- Utility, meeting-point density/walking radius, fleet-demand, equity,
  algorithm, Beijing-inspired case, and managerial insights are diagnostic,
  exploratory, or limitation-level.

## Forbidden Manuscript Storylines

Do not organize the paper around any of the following claims:

- FullModel is unconditionally superior.
- Bidirectional meeting points dominate all baselines under all metrics.
- FullModel wins on every denominator.
- Fixed accepted-set proves unconditional vkm/original dominance.
- Equity benefits are strongly established.
- The Beijing case validates real-world Beijing operations.
- The paper provides direct citywide policy recommendations for Beijing.
- The method is deployment-ready.
- This is the first bidirectional meeting-point DRT paper.
- No prior work considers dropoff walking.
- Existing work only assigns pickup-side meeting points.
- Gamma sweep is a Pareto frontier.
- Legacy 29.1% vkm/trip improvement is final superiority evidence.

## Refreshed Manuscript Architecture

### 1. Introduction

Purpose: motivate the fair-evidence problem before presenting the framework.

Required content:

- Problem motivation for meeting-point DRT as a service-design problem.
- Why pickup and dropoff meeting-point design matter for route consolidation
  and passenger burden.
- Why passenger response and service coverage must be modeled together.
- Why fair comparison requires matched evidence, explicit denominators, paired
  seeds, and failure-row accounting.
- Contribution framed as an integrated choice-aware dynamic service-design
  simulation framework.
- No broad first/only or universal-superiority language.

### 2. Literature Review

Purpose: position the contribution against overlapping literatures without
overclaiming novelty.

Required content:

- DRT / DARP with meeting points.
- Pickup and dropoff walking-location literature, including overlapping
  ridepooling and DARPmp work.
- Passenger choice, service acceptance, and outside-option modeling.
- Dynamic routing, rolling-horizon heuristics, and ALNS diagnostics.
- Simulation-based service design and evidence-gated evaluation.

The gap should be framed as an integrated fair-evidence framework, not as a
claim that nobody studied dropoff walking or that existing work is pickup-only.

### 3. Method

Purpose: define the framework and operational mechanisms before results.

Required content:

- Service-design alternatives: DoorToDoor + Choice, SingleSidedPickup + Choice,
  SingleSidedDropoff + Choice, and BidirectionalMP + Choice +
  RollingHorizon/ALNS.
- Actual-offer choice and outside-option passenger response.
- Rejection mechanisms: choice rejection, feasibility rejection, and service
  coverage.
- Rolling-horizon routing and ALNS for the FullModel implementation.
- Baseline taxonomy separating behavioral comparisons from diagnostics.
- Metric and denominator discipline: total vehicle-km, vkm per served trip, vkm
  per original request, served share, acceptance, and rejection.

### 4. Experimental Design

Purpose: define evidence families before reporting results.

Required content:

- Main behavioral formal matrix: 20 seeds x 4 scales x 4 methods, 320 completed
  rows, main evidence.
- Coverage-confounding controls: matched coverage as main/control evidence with
  305 completed rows and 15 durable failed FullModel rows.
- Fixed accepted-set routing diagnostic: 320 completed rows, diagnostic only.
- Robustness diagnostics: utility sensitivity, walking-radius / meeting-point
  density, and fleet-demand stress, reduced diagnostic grids.
- Equity/type-level diagnostics: modeled passenger-type and individual-burden
  outputs, exploratory.
- Beijing-inspired synthetic scenario boundary: illustrative only.
- Reproducibility and failure-row policy: raw/processed outputs, manifests,
  validators, denominator checks, and durable failure rows.

### 5. Results

Purpose: present evidence from strongest to most bounded.

Required content:

- Main behavioral results with served share and rejection context shown next to
  vehicle-km intensity.
- Matched-coverage results with 65 valid aggregate pairs per baseline and 15
  durable failed FullModel rows carried as a limitation.
- Fixed accepted-set diagnostic results, limited to routing/service-design
  interpretation and vkm per served request.
- Robustness diagnostics as consistency screens, not universal parameter rules.
- Equity diagnostics as modeled type-level and individual-burden patterns.
- Bounded Beijing-inspired synthetic discussion as an illustration, not
  validation.

### 6. Discussion

Purpose: interpret what the evidence can and cannot support.

Required content:

- Conditional efficiency advantage under the tested synthetic paired design.
- Role of passenger response in changing coverage, acceptance, and rejection.
- Trade-off between operating efficiency and served share.
- Managerial implications as simulation-based boundary conditions.
- Why real/semi-real validation, empirical passenger calibration, and final
  reproducibility reruns are still needed.

### 7. Conclusion

Purpose: close with claim-gated takeaways only.

Required content:

- Integrated framework contribution without first/only wording.
- Conditional synthetic efficiency finding with coverage caveat.
- Matched-coverage and fixed accepted-set boundaries.
- No universal superiority.
- No real Beijing validation.
- No deployment-ready or citywide policy prescription.
- Limitations and future work focused on real/semi-real OD, road-network,
  meeting-point, request-time, preference, fleet, and reproducibility evidence.

## Old-To-New Section Map

| Current source | Target role after refresh | Required Phase 8 boundary |
|---|---|---|
| `manuscript/main.tex` | Later venue/front-matter and include-order update | No direct edit in this refresh. |
| `manuscript/sections/abstract.tex` | Rebuild from `09_REVISED_ABSTRACT.md` | Use C-FWK-01, C-EFF-01, C-COV-01, C-LIM-01; no legacy numbers. |
| `manuscript/sections/intro.tex` | Evidence-confounding introduction | No first/only, no pickup-only prior-work claim, no unsupported effect size. |
| `manuscript/sections/literature.tex` | Conservative literature positioning | Prior work is overlapping; novelty is integrated evidence-chain framing. |
| `manuscript/sections/model.tex` | Framework and method | Framework description, choice semantics, denominators, baseline taxonomy. |
| `manuscript/sections/algorithm.tex` | Operational mechanism and diagnostics | ALNS/MILP are scoped diagnostics, not optimality or deployment proof. |
| `manuscript/sections/experiments.tex` | Experimental design, main evidence, controls, diagnostics | Separate main, control, diagnostic, exploratory, and illustrative evidence. |
| `manuscript/sections/policy.tex` | Managerial insights and boundary conditions | Simulation-based insights only; limitations before implications. |
| `manuscript/sections/conclusion.tex` | Claim-gated conclusion | No universal superiority, no real-Beijing validation, no deployment claim. |

## Evidence-Family Placement Rules

| Evidence family | Manuscript placement | Allowed role | Forbidden role |
|---|---|---|---|
| 06-02 main behavioral matrix | Main results | Headline synthetic evidence when paired with coverage/rejection context | Universal superiority proof |
| 06-03 matched coverage | Robustness/control results | Completed-pair efficiency consistency with 15 failed-row limitation | Equal-coverage proof with no caveat |
| 06-03 fixed accepted-set | Diagnostic results or appendix | Routing/service-design diagnostic on common accepted set | Behavioral headline or vkm/original dominance proof |
| 06-04 robustness | Robustness diagnostics | Reduced-grid consistency screens | Universal parameter rules |
| 06-04 equity | Discussion/limitations and appendix | Modeled type-level and burden diagnostics | Strong equity or demographic conclusion |
| 06-04 algorithm diagnostics | Method diagnostics or supplement | Implementation behavior and scoped exact/static checks | ALNS optimality or real-time deployment proof |
| Phase 7 Beijing-inspired synthetic | Discussion, limitations, appendix | Illustrative scenario-transfer boundary | Real/semi-real Beijing validation |

## Direct LaTeX Edit Boundary

This refresh does not modify `manuscript/**/*.tex`. Later manuscript edits may
only introduce wording that is explicitly supported by Phase 8 or weaker than
the allowed wording. Any future direct manuscript edit must keep REP-01 and
REP-02 pending until Phase 10 reproducibility rerun passes.
