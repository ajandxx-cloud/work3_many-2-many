# Phase 1 Novelty Positioning

**Phase:** 01 - Literature and Novelty Audit
**Plan:** 01-01
**Date:** 2026-06-15
**Status:** complete

## Decision Summary

The manuscript should not claim broad firstness for bidirectional meeting points or state that prior work assigns meeting points only on the pickup side. The defensible position is narrower and stronger: this project can be framed as an integrated choice-aware dynamic service-design simulation framework that studies bidirectional pickup/dropoff meeting-point sets under passenger acceptance, rolling-horizon dispatch, many-to-many DRT, and equity/coverage diagnostics.

## Allowed wording

Allowed wording may be used in Phase 9 if Phase 2, Phase 6, and Phase 8 provide the matching evidence.

| Wording | Basis | Conditions |
|---|---|---|
| "We study an integrated choice-aware dynamic service-design simulation framework for many-to-many DRT with bidirectional pickup and dropoff meeting-point sets." | `01_LITERATURE_AUDIT.md` finds the integrated combination remains the conservative contribution center. | Must not imply that each individual component is new. |
| "The framework combines bidirectional pickup/dropoff meeting-point candidate sets, simulated binary-logit acceptance with an outside option, rolling-horizon dispatch, and equity/coverage diagnostics." | Local model/manuscript code surface supports those components as framework description. | Phase 2 must define fair comparison families; Phase 8 must gate final claims. |
| "Prior work has studied meeting points, pickup/dropoff walking locations, dynamic ridepooling, and rolling-horizon DRT separately or in partially overlapping combinations." | Citation-by-claim matrix. | Must cite the relevant prior work for each component. |
| "Our experiments evaluate when the integrated design improves operating efficiency under consistent passenger-response assumptions." | Rebuild roadmap and requirements. | Only allowed after formal paired experiments. |

No row above approves a "first" or "only" claim.

## Risky wording

Risky wording should be avoided unless later phases add exact citation and evidence support.

| Wording | Risk | Required evidence before use |
|---|---|---|
| "First framework combining bidirectional meeting points, passenger choice, and rolling-horizon DRT." | Could be true only under a narrow scope, but the audit did not verify all adjacent literature. | Phase 8 claim matrix plus Phase 9 full-text citation check. |
| "Existing DARPmp work is single-sided." | External metadata for Cortenbach et al. (2024) suggests alternative pickup or drop-off meeting points, so the current manuscript's statement may be wrong. | Full-text verification of the exact Cortenbach model and experiments. |
| "Passenger heterogeneity is ignored in meeting-point DRT literature." | Some related DRT and mobility-on-demand work includes demand management or user-centric service quality, even if not this exact binary-logit setup. | A broader choice-based DRT review. |
| "TR-E is the target journal." | The repository and older manuscript materials still mention TR-A. | Keep as planning bar unless user/coauthors finalize venue. |

## Forbidden wording

These statements should not appear in final manuscript text unless Phase 8 explicitly overturns this audit with new evidence.

| Forbidden wording | Reason |
|---|---|
| "Existing work assigns meeting points only on the pickup side." | Fielbaum et al. (2021) covers optimized pick-up and drop-off walking locations; Cortenbach et al. (2024) metadata also contradicts a simple pickup-only characterization. |
| "This is the first bidirectional meeting-point DRT paper." | Prior work already covers bidirectional walking-location ideas and DARP meeting points; the safe contribution is the integrated simulation framework. |
| "No prior work considers dropoff walking." | Directly contradicted by Fielbaum et al. (2021). |
| "The current 29.1% improvement proves superiority." | Phase 0 found coverage confounding, aggregation/caption mismatch, and exploratory provenance. |
| "The Beijing-inspired scenario supports real Chinese city policy recommendations." | Current case data are synthetic/illustrative. |
| "Gamma sensitivity is a Pareto frontier." | Phase 0 found gamma is post-hoc welfare accounting and does not affect routing or acceptance. |

## Unresolved blockers

| Blocker | Status | Owner |
|---|---|---|
| Correct Cortenbach et al. (2024) metadata and verify full-text mechanism before final citation wording. | Open but non-blocking for Phase 1. | Phase 9 |
| Correct Wu et al. (2025) bibliography metadata before using it as a specific dynamic DRT comparator. | Open but non-blocking for Phase 1. | Phase 9 |
| Decide final venue: TR-E submission target versus TR-A-style policy framing. | Resolved for planning as TR-E-level rigor, final venue still user/coauthor decision. | Phase 9 |
| Formal evidence for the integrated framework claim. | Not part of Phase 1; requires Phase 2 contract, Phase 6 results, and Phase 8 claim gate. | Phase 2 / Phase 6 / Phase 8 |

## Conservative contribution statement

This paper develops and evaluates an integrated choice-aware dynamic service-design simulation framework for many-to-many demand-responsive transit. The framework combines bidirectional pickup and dropoff meeting-point candidate sets, simulated single-offer binary-logit passenger acceptance with an outside option, online rolling-horizon dispatch, scalable heuristic routing, and equity/coverage diagnostics. Its contribution is not that meeting points, walking locations, passenger choice, or dynamic assignment are individually new; rather, it uses their integration to test conditional operational trade-offs under a reproducible evidence chain.

## TR-E vs TR-A positioning

| Position | Fit | Risk |
|---|---|---|
| TR-E / operations and logistics evidence-chain framing | Best fit for a rebuild centered on service-design taxonomy, fair behavioral comparisons, routing diagnostics, reproducibility, and conditional efficiency claims. | Requires stronger formal experiments, clean metrics, and conservative claims. |
| TR-A / policy-practice framing | Fits the current manuscript's policy language and Chinese-city motivation. | Current evidence is synthetic and coverage-confounded; policy claims would be vulnerable without real or semi-real validation. |

**Recommendation:** Use TR-E-level rigor as the planning bar. Keep policy implications secondary and simulation-based until Phase 7 or later supplies stronger external-validity evidence.

## Requirements Coverage

| Requirement | Status | Evidence |
|---|---|---|
| POS-02 | Complete for planning | Unsupported "first" and "only" claims are forbidden; allowed language centers the integrated choice-aware dynamic service-design framework. |
| POS-03 | Complete for planning | TR-E-level rigor is selected as the planning bar while final venue remains a later manuscript decision. |
