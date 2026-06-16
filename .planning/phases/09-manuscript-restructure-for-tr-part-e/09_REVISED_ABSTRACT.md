# Phase 9 Revised Abstract Refresh

**Phase:** 09 - Manuscript Restructure for TR Part E
**Refresh date:** 2026-06-16
**Status:** claim-gated abstract plan complete
**Source of truth:** Phase 8 supported and unsupported claims

## Abstract Boundary

The abstract may state the integrated framework contribution and the strongest
Phase 8 main finding only as a conditional synthetic result. It must not state
legacy effect sizes, first/only novelty, real Beijing validation, deployment
readiness, universal superiority, or strong equity benefits.

The abstract must report efficiency together with coverage/acceptance context.
It may mention the matched-coverage control only if the 15 durable failed
FullModel matched rows are not hidden.

## Polished Abstract Draft

Meeting-point demand-responsive transit can reduce operating distance, but its
evaluation is easily confounded by passenger response, served-share differences,
baseline definitions, and metric denominators. This study develops a
choice-aware dynamic service-design simulation framework for many-to-many DRT
that evaluates door-to-door, single-sided, and bidirectional pickup/dropoff
meeting-point designs under shared passenger-response semantics and
rolling-horizon routing. Formal paired synthetic experiments compare the
service designs across common seeds, request scales, vehicle-km denominators,
served-share measures, and rejection outcomes. The bidirectional meeting-point
full model shows lower vehicle-km intensity than the tested door-to-door and
single-sided choice baselines, but this result is accompanied by lower served
share and must be interpreted jointly with acceptance, feasibility rejection,
and coverage-control outcomes. Completed matched-coverage comparisons are
consistent with the same efficiency direction, while durable failed matched
rows limit equal-coverage interpretation. Additional robustness, equity,
algorithm, and Beijing-inspired scenario outputs are treated as diagnostics or
limitations rather than headline validation. The study contributes an
evidence-gated simulation framework and a denominator-disciplined comparison
protocol for meeting-point DRT, while real or semi-real calibration and
validation remain necessary before city-transfer or deployment guidance.

## Required Abstract Components

| Component | Refreshed wording direction | Phase 8 claim IDs |
|---|---|---|
| Research problem | Meeting-point DRT evaluation is confounded by passenger response, coverage, baselines, and denominators. | C-COV-01, C-ACC-01 |
| Framework / method | Integrated choice-aware dynamic service-design simulation framework for many-to-many DRT. | C-FWK-01 |
| Formal paired synthetic design | Common seeds, request scales, method family, denominators, served-share and rejection metrics. | C-EFF-01, C-COV-01, C-REP-01 |
| Main evidence-bounded result | Lower vehicle-km intensity under tested synthetic paired design, not universal superiority. | C-EFF-01 |
| Coverage/acceptance context | Lower served share and rejection context must be stated with efficiency. | C-COV-01, C-ACC-01 |
| Coverage-confounding control | Completed matched-coverage pairs are consistent with the efficiency direction, with 15 failed rows. | C-MC-01 |
| Robustness/equity/case boundary | Robustness, equity, algorithm, and Beijing-inspired outputs are diagnostics or limitations. | C-UTIL-01, C-MP-01, C-FLEET-01, C-EQ-01, C-ALG-01, C-CASE-01 |
| Contribution and limitation | Evidence-gated simulation framework; real/semi-real validation remains future work. | C-FWK-01, C-LIM-01 |

## Numerical Discipline

- The draft intentionally avoids full result magnitudes.
- The seed count may be reported as part of experiment design because Phase 6
  and Phase 8 allow the 20-seed formal synthetic paired design.
- Do not include legacy 29.1% or 35.0% values.
- Do not use `vkm_per_trip`; use vehicle-km intensity, vkm per served trip, or
  vkm per original request with the denominator named.

## Forbidden Abstract Content

| Forbidden content | Replacement |
|---|---|
| FullModel is unconditionally superior | Lower vehicle-km intensity under the tested synthetic paired design, with lower served share. |
| Bidirectional meeting points dominate all metrics | Selected vehicle-km denominators improve while coverage and rejection must be reported. |
| First/only bidirectional meeting-point DRT paper | Integrated choice-aware dynamic service-design simulation framework. |
| Real Beijing validation | Beijing-inspired synthetic scenario or illustrative scenario-transfer boundary. |
| Deployment-ready method | Real/semi-real calibration and validation remain necessary. |
| Strong equity benefit | Equity diagnostics are modeled and exploratory. |
| Gamma Pareto frontier | Post-hoc welfare sensitivity diagnostic, if retained outside the abstract. |

## Title Direction

Recommended title direction:

> Choice-aware dynamic service-design evidence for bidirectional meeting points
> in demand-responsive transit

Title rules:

- Keep the contribution descriptive.
- Avoid first/only wording.
- Avoid effect-size or deployment claims.
- Keep TR-E operational and service-design framing visible.

## Keyword Plan

- demand-responsive transit
- meeting points
- passenger choice
- dynamic service design
- rolling-horizon dispatch
- fair comparison
- simulation evidence
- service equity

## Highlights Plan

Final highlights should be 3 to 5 bullets and should stay under the target
journal's length constraints.

- Choice-aware DRT framework links meeting points, response, and routing.
- Fair comparison reports vehicle-km with coverage and rejection.
- Paired synthetic tests show conditional vehicle-km intensity reductions.
- Matched-coverage and diagnostic tests bound the efficiency interpretation.
- Real/semi-real calibration remains necessary before deployment guidance.

## Finalization Checklist

- Confirm the final abstract stays within the journal word limit.
- Confirm no legacy effect size or unsupported numerical claim is present.
- Confirm served share or rejection context appears next to the efficiency
  result.
- Confirm Beijing-related language is synthetic and illustrative only.
- Confirm REP-01 and REP-02 remain pending until Phase 10 rerun.
