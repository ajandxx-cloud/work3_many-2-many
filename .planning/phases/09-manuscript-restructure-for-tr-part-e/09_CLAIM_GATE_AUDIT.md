# Phase 9 Claim-Gate Consistency Audit

**Phase:** 09 - Manuscript Restructure for TR Part E
**Audit date:** 2026-06-16
**Status:** complete
**Gate applied:** Phase 8 evidence synthesis and claim gate

## Audit Purpose

The old Phase 9 artifacts were produced before Phase 8. They were safe as
preliminary planning because they used placeholders, but they are stale after
the claim gate. This audit checks each manuscript-facing language area and
records the required refresh action.

## Area-by-Area Audit

| Area | Location / artifact | Old wording or old intended claim | Conflict with Phase 8 | Required action | Replacement direction |
|---|---|---|---|---|---|
| 1. Abstract language | `09_REVISED_ABSTRACT.md` | `[SUPPORTED_CLAIM_FROM_08]`, `[MAIN_EFFECT_SIZE_IF_SUPPORTED]`, and final evidence placeholders. | Phase 8 now exists; leaving placeholders would fail to consume allowed/forbidden claim boundaries. | revise | Use C-FWK-01 plus C-EFF-01/C-COV-01 conditional wording; mention matched coverage only with failed-row caveat; no legacy numbers. |
| 2. Introduction contribution language | `09_REVISED_INTRODUCTION_PLAN.md` | Contribution order included Phase 8 dependencies and allowed "experimental findings" only as placeholders. | Contributions must now explicitly avoid first/only, unconditional superiority, real-city validation, and direct deployment. | revise | Use six-part contribution list: framework, baseline taxonomy, paired formal evidence, coverage controls, bounded diagnostics, reproducibility-oriented Phase 6 package. |
| 3. Novelty language | `09_REVISED_INTRODUCTION_PLAN.md`; old literature rewrite table | Broad novelty was flagged as risky but not fully tied to Phase 8 unsupported claims. | Phase 8 marks broad C-NOV-01 wording unsupported; Phase 1 forbids first/only and pickup-only claims. | downgrade/delete | Frame novelty as integrated choice-aware dynamic service-design evidence chain; describe prior work as partially overlapping. |
| 4. Method framing | `09_TR_E_MANUSCRIPT_STRUCTURE.md`; `09_EXPERIMENT_SECTION_PLAN.md` | Method labels and evidence families were defined but final role depended on absent Phase 8 files. | Phase 8 supports framework description but forbids deployment-ready or individually first component claims. | keep/revise | Keep the integrated framework framing; explicitly separate behavioral methods from diagnostics. |
| 5. Experiment design framing | `09_EXPERIMENT_SECTION_PLAN.md` | Main, robustness, equity, diagnostics, and synthetic case were separated, but Phase 8 placeholders remained. | Phase 8 now assigns main/control/diagnostic/exploratory/limitation grades with row counts and failure boundaries. | revise | Use seven evidence families and list purpose, methods, row counts, metrics, denominator, interpretation, placement, and abstract support. |
| 6. Result interpretation language | `09_EXPERIMENT_SECTION_PLAN.md`; old table contracts | Final numerical claims blocked until Phase 8; old text did not state the strongest allowed result directly. | Strong result must combine lower vehicle-km intensity with lower served share; fixed accepted-set and robustness cannot headline. | revise/downgrade | Present lower vkm intensity as conditional synthetic evidence; report served share/rejection context; keep fixed accepted-set and robustness diagnostic. |
| 7. Table and figure captions/plans | `09_TABLE_FIGURE_PLAN.md` | Display inventory and caption checklist referenced Phase 8 support status placeholders. | Captions must now map to actual Phase 8 claim IDs and forbid legacy display overclaims. | revise | Plan required tables/figures with source artifact, columns, allowed claim, forbidden overclaim, and main/appendix placement. |
| 8. Managerial insight / policy implication language | `09_TABLE_FIGURE_PLAN.md`; current policy-section rewrite template | R1-R5 were converted to conditional rows but still used Phase 8 support-status placeholders. | Phase 8 allows only simulation-based boundary conditions; no Beijing policy, deployment, equity guarantee, or citywide cost guarantee. | revise/downgrade | Add dedicated managerial/limitation plan with condition-based insights and required limitations. |
| 9. Conclusion language | Old Phase 9 structure and carry-forward notes | Conclusion alignment was deferred until Phase 8. | Phase 8 conclusion bullets now forbid legacy effect sizes, universal dominance, gamma frontier, strong equity, real Beijing validation, and deployment readiness. | revise | Conclusion should summarize integrated framework, conditional synthetic efficiency, coverage trade-off, matched/fixed boundaries, synthetic limitation, and future validation. |
| 10. Limitation language | Old table/figure plan | Limitations were listed but still framed around a pending Phase 8 gate. | Phase 8 makes limitations mandatory: synthetic-only, no real/semi-real validation, simulation-range types, failed matched rows, diagnostic boundaries, no p-values, heuristic ALNS. | revise/move to limitation | Add mandatory limitation list and ensure managerial insights start from those boundaries. |

## Required Forbidden-Language Sweep

| Forbidden or overstrong expression | Present as supported wording in refreshed Phase 9? | Action |
|---|---:|---|
| FullModel is unconditionally superior | No | Forbidden; replaced by conditional lower vehicle-km intensity with lower served share. |
| Bidirectional meeting points dominate all baselines under all metrics | No | Forbidden; served share and rejection context must be shown. |
| FullModel wins on every denominator | No | Forbidden; fixed accepted-set vkm/original does not support this. |
| Fixed accepted-set proves unconditional vkm/original dominance | No | Forbidden; diagnostic supports vkm per served request only. |
| Equity benefits are strongly established | No | Forbidden; equity remains exploratory diagnostics. |
| Beijing case validates real-world Beijing operations | No | Forbidden; use Beijing-inspired synthetic scenario. |
| Direct citywide policy recommendations for Beijing | No | Forbidden; use simulation-based boundary conditions. |
| Deployment-ready claim | No | Forbidden; real/semi-real calibration and validation remain future work. |
| First bidirectional meeting-point DRT paper | No | Forbidden; use integrated framework contribution. |
| No prior work considers dropoff walking | No | Forbidden by Phase 1/8. |
| Existing work only assigns pickup-side meeting points | No | Forbidden or too broad; use overlapping prior-literature wording. |
| Gamma sweep as Pareto frontier | No | Forbidden; post-hoc welfare diagnostic if retained. |
| Legacy 29.1% vkm/trip improvement as final superiority evidence | No | Forbidden; legacy values removed from refreshed planning claims. |

## Audit Decision

Phase 9 refresh is allowed to pass if the refreshed artifacts:

- replace Phase 8 placeholders with supported or weaker claim language;
- keep unsupported claims only as forbidden examples or deletion/rewrite actions;
- report served share and rejection context alongside vehicle-km intensity;
- keep diagnostics, equity, and Beijing-inspired material bounded;
- do not modify manuscript `.tex` files;
- do not enter Phase 10.
