# Phase 9 Table and Figure Plan Refresh

**Phase:** 09 - Manuscript Restructure for TR Part E
**Refresh date:** 2026-06-16
**Status:** claim-gated table/figure plan complete

## Display Boundary

Tables and figures must make evidence roles visible. No display may show
vehicle-km intensity alone without served share and acceptance/rejection
context. Diagnostics must not be titled, ordered, colored, or captioned as
headline superiority evidence.

## Required Main and Supplement Displays

### 1. Table: Method Taxonomy and Evidence Role

| Field | Plan |
|---|---|
| Purpose | Separate behavioral service designs from diagnostics and legacy material. |
| Source artifact | Phase 2 taxonomy; Phase 6 method taxonomy; Phase 8 C-FWK-01. |
| Required columns | Paper-facing method label, code label, service design, passenger response, routing/diagnostic role, evidence family, claim grade. |
| Allowed claim | The study evaluates an integrated choice-aware dynamic service-design framework. |
| Forbidden overclaim | First bidirectional meeting-point DRT paper; individually novel components. |
| Placement | Main text, Method or Experimental Design. |

### 2. Table: Metric Definitions and Denominators

| Field | Plan |
|---|---|
| Purpose | Prevent denominator mixing and ambiguous vkm/trip wording. |
| Source artifact | Phase 2 metric definitions; Phase 6 statistical summary; Phase 8 C-COV-01. |
| Required columns | Metric, formula, numerator, denominator, unit, valid range, evidence family, interpretation warning. |
| Allowed claim | Vehicle-km, served share, acceptance, and rejection are denominator-disciplined. |
| Forbidden overclaim | Efficiency displayed without coverage or rejection context. |
| Placement | Main text, before results. |

### 3. Table: Main Behavioral Results With Served Share and Rejection Rates

| Field | Plan |
|---|---|
| Purpose | Present the primary formal synthetic behavioral evidence. |
| Source artifact | 06-02 main behavioral matrix; `06_STATISTICAL_SUMMARY.md`; bootstrap CI outputs; Phase 8 C-EFF-01/C-COV-01. |
| Required columns | Method, scale or aggregate key, n pairs, total vehicle-km, vkm per served trip, vkm per original request, served share, behavioral acceptance, choice rejection, feasibility rejection, paired difference, 95% bootstrap CI. |
| Allowed claim | BidirectionalMP/FullModel shows lower vehicle-km intensity under tested synthetic paired conditions, with lower served share. |
| Forbidden overclaim | Dominates all metrics; same-service-level superiority; pure routing superiority. |
| Placement | Main text, Formal Main Evidence. |

### 4. Table: Matched-Coverage Comparison

| Field | Plan |
|---|---|
| Purpose | Bound coverage confounding on completed matched pairs. |
| Source artifact | 06-03 matched coverage; manifest; Phase 8 C-MC-01. |
| Required columns | Baseline, target served count/share, valid pairs, durable failed rows, missing pairs, total vehicle-km, vkm per served trip, vkm per original request, served share difference, full-better share. |
| Allowed claim | Completed matched-coverage pairs are consistent with the FullModel efficiency direction. |
| Forbidden overclaim | Matched coverage fully proves equal-coverage superiority; all matched rows completed. |
| Placement | Main-text robustness summary; full detail appendix/supplement. |

### 5. Table: Fixed Accepted-Set Routing Diagnostic

| Field | Plan |
|---|---|
| Purpose | Show common accepted-set routing/service-design diagnostic results. |
| Source artifact | 06-03 fixed accepted-set; Phase 8 C-FAS-01. |
| Required columns | Baseline, n valid pairs, common accepted-set definition, vkm per served request, vkm per original request, deterministic inserted share, total vehicle-km, diagnostic status. |
| Allowed claim | Supports a routing/service-design efficiency signal on vkm per served request. |
| Forbidden overclaim | Unconditional vkm/original dominance; behavioral headline claim. |
| Placement | Diagnostic subsection or appendix/supplement. |

### 6. Table/Figure: Robustness Sensitivity Summary

| Field | Plan |
|---|---|
| Purpose | Summarize utility, walking-radius / MP-density, and fleet-demand diagnostic consistency. |
| Source artifact | 06-04 robustness packages; Phase 8 C-UTIL-01, C-MP-01, C-FLEET-01. |
| Required columns | Package, setting ID, seeds/scales, n valid pairs, vkm per served trip difference, vkm per original request difference, served share difference, diagnostic limitation. |
| Allowed claim | Reduced robustness diagnostics are consistent with the main direction within tested synthetic settings. |
| Forbidden overclaim | Robust under all parameters; universal radius threshold; universal fleet-ratio rule. |
| Placement | Compact main text summary plus appendix/supplement detail. |

### 7. Table/Figure: Equity/Type-Level Outcomes and Burden Distribution

| Field | Plan |
|---|---|
| Purpose | Report modeled type-level and individual burden diagnostics. |
| Source artifact | 06-04 equity outputs; `08_EQUITY_GATE.md`; Phase 8 C-EQ-01. |
| Required columns | Passenger type, request count or denominator, served share, acceptance, wait, walk, IVT, generalized cost, burden distribution metric, exploratory-status note. |
| Allowed claim | Equity diagnostics report modeled type-level and individual burden patterns. |
| Forbidden overclaim | Strong equity benefit; empirical demographic equity; regulatory prescription. |
| Placement | Main text bounded summary; distribution detail appendix/supplement. |

### 8. Table: Claim-Evidence Matrix Summary

| Field | Plan |
|---|---|
| Purpose | Make claim grades transparent for the manuscript reader or supplement. |
| Source artifact | `08_CLAIM_EVIDENCE_MATRIX.md`; `08_SUPPORTED_CLAIMS.md`; `08_UNSUPPORTED_OR_EXPLORATORY_CLAIMS.md`. |
| Required columns | Claim ID, claim unit, evidence family, source artifact, grade, allowed manuscript location, required caveat, forbidden wording. |
| Allowed claim | Manuscript claims are evidence-gated. |
| Forbidden overclaim | Unsupported claims smuggled into supported wording. |
| Placement | Appendix/supplement or concise main reproducibility/evidence note. |

### 9. Figure: Experiment Evidence Pipeline

| Field | Plan |
|---|---|
| Purpose | Show the flow from service-design variants to evidence families and claim gate. |
| Source artifact | Phase 6 manifest; Phase 8 matrix; this Phase 9 refresh. |
| Required columns/elements | Variants, main behavioral matrix, coverage controls, fixed accepted-set diagnostic, robustness diagnostics, equity diagnostics, Beijing-inspired illustration, claim gate, manuscript placement. |
| Allowed claim | Evidence families have different claim strengths. |
| Forbidden overclaim | Diagnostics visually promoted to headline validation. |
| Placement | Main text, Experimental Design. |

### 10. Figure: Service-Design Framework Diagram

| Field | Plan |
|---|---|
| Purpose | Explain the framework: request generation, candidate meeting points, actual-offer choice, passenger response, rolling-horizon routing, and metric logging. |
| Source artifact | Phase 2 contracts; Phase 3 choice model; Phase 4/6 implementation artifacts. |
| Required columns/elements | Passenger request, pickup/dropoff MP candidates, offer construction, utility/outside option, accepted/rejected request, RH/ALNS dispatch, route output, denominator logging. |
| Allowed claim | The framework integrates service design, passenger response, and routing. |
| Forbidden overclaim | Framework is deployment-ready or first/only. |
| Placement | Main text, Method. |

## Additional Appendix/Supplement Displays

| Display family | Source | Required boundary |
|---|---|---|
| Full matched-coverage detail | 06-03 matched coverage | Include 15 durable failed rows and target construction. |
| Full fixed accepted-set detail | 06-03 fixed accepted-set | Diagnostic only; show vkm/original non-dominance. |
| Algorithm diagnostics | 06-04 algorithm diagnostics | Scope disclosure, no ALNS optimality claim. |
| Beijing-inspired synthetic table | Phase 7 artifacts; legacy rows | Illustrative only, not real/semi-real case evidence. |
| Gamma sensitivity | Legacy diagnostic provenance | Post-hoc welfare accounting, not Pareto frontier. |
| Weight sensitivity | Legacy diagnostic provenance | Remove from main claims unless rebuilt. |
| VOT / calibration mapping | Phase 3 and old policy material | Parameter interpretation and calibration limitation only. |

## Display Rules

- Do not show vkm per served trip alone without served share.
- Do not show efficiency without acceptance/rejection.
- Do not label diagnostic tables as headline superiority evidence.
- Do not use Beijing-inspired synthetic rows as real case validation.
- Do not use `vkm_per_trip`.
- Every caption must state evidence family and denominator.
- Every caption implying a finding must map to a Phase 8 claim ID or be weaker
  than the approved wording.

## Caption Templates

Main behavioral caption template:

> Formal paired synthetic behavioral comparison. Vehicle-km denominators are
> reported with served share and rejection outcomes; lower vehicle-km intensity
> should be interpreted as a coverage-aware conditional result.

Matched-coverage caption template:

> Matched-coverage control on completed pairs. The table reports valid-pair
> counts and durable failed FullModel rows; results bound, but do not eliminate,
> coverage-confounding concerns.

Fixed accepted-set caption template:

> Fixed accepted-set routing diagnostic. Results describe a common-passenger-set
> routing/service-design signal and do not support behavioral headline claims.

Beijing-inspired caption template:

> Beijing-inspired synthetic scenario. The display is illustrative and is not
> evidence from real or semi-real Beijing operations.
