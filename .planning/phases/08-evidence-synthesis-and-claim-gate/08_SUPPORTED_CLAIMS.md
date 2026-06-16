# Phase 8 Supported Claims

**Phase:** 08 - Evidence Synthesis and Claim Gate
**Date:** 2026-06-16
**Status:** complete

## Purpose

List only claims that may be used in the Phase 9 manuscript refresh. The wording
below is allowed claim-unit language, not complete manuscript prose. Stronger
language must not be introduced unless a later claim gate reopens the evidence.

## Strong Claims

| claim_id | final allowed wording | evidence source | evidence grade | allowed manuscript location | required caveat | forbidden stronger wording |
|---|---|---|---|---|---|---|
| C-EFF-01 | Under the tested formal synthetic paired design, the BidirectionalMP/FullModel design shows lower vehicle-km intensity than DoorToDoor and single-sided choice baselines. | 06-02 main behavioral matrix; `06_STATISTICAL_SUMMARY.md`; `paired_bootstrap_ci.csv` | strong | Abstract bullet, Formal Main Evidence, Conclusion | Must report served share, rejection context, denominators, synthetic setting, and no paired p-values. | "unconditionally superior"; "dominates all metrics"; "deployment-ready efficiency proof" |
| C-COV-01 | The lower vehicle-km intensity is accompanied by a lower served share, so efficiency and coverage/acceptance must be interpreted together. | 06-02 main behavioral matrix; bootstrap CI table | strong | Abstract bullet, Formal Main Evidence, Conclusion | Must state FullModel served share is lower than DoorToDoor in the main matrix. | "same-service-level advantage"; "no coverage penalty"; "pure routing superiority" |
| C-REP-01 | The Phase 6 formal synthetic evidence packages are reproducibly documented with raw/processed outputs, manifests, validators, denominator checks, and durable failure rows. | `06_FORMAL_RESULT_MANIFEST.md`; `phase06_result_manifest.json`; `phase06_verification_report.json` | strong | Experimental Design, reproducibility note, Conclusion | REP-01 and REP-02 remain Phase 10 tasks for final manuscript package regeneration. | "final reproducibility package is complete"; "all final figures/tables are regenerated" |
| C-LIM-01 | Current evidence is synthetic and requires real or semi-real calibration and validation before real-city transfer or deployment guidance. | `07_DATA_AUDIT.md`; `06_EVIDENCE_BOUNDARY.md`; Phase 3 calibration boundary | strong limitation | Abstract boundary, Limitations, Conclusion | Must state current Beijing-labeled case material is synthetic. | "validated in real Beijing"; "calibrated to observed Beijing OD/network/preferences" |

## Moderate Claims

| claim_id | final allowed wording | evidence source | evidence grade | allowed manuscript location | required caveat | forbidden stronger wording |
|---|---|---|---|---|---|---|
| C-FWK-01 | The paper develops and evaluates an integrated choice-aware dynamic service-design simulation framework for many-to-many DRT with bidirectional pickup/dropoff meeting-point sets. | Phase 1 positioning; Phase 2 contracts; Phase 6 method taxonomy | moderate | Abstract, Introduction, Framework | Must avoid first/only and deployment language. | "first bidirectional meeting-point DRT paper"; "individually novel components" |
| C-ACC-01 | Passenger response and rejection mechanisms are explicit in the evidence chain and affect interpretation of efficiency and served-share outcomes. | 06-02 main behavioral matrix; Phase 3 choice model artifacts | moderate | Experimental Design, Discussion, Conclusion caveat | Do not claim that FullModel improves acceptance; acceptance effects are conditional. | "passengers prefer FullModel"; "acceptance improvement is established" |
| C-MC-01 | In completed matched-coverage pairs, FullModel retains lower vehicle-km denominators, but 15 durable failed FullModel matched rows must be reported as a limitation. | 06-03 matched coverage; `06_STATISTICAL_SUMMARY.md`; manifest | moderate | Robustness Controls, Conclusion caveat | Must include 65 valid aggregate pairs and 15 missing/failed pairs. | "equal-coverage superiority fully proven"; "all matched rows completed" |
| C-FAS-01 | Fixed accepted-set diagnostics support a routing/service-design efficiency signal on vkm per served request, but not unconditional vkm/original dominance. | 06-03 fixed accepted-set diagnostics | moderate diagnostic | Robustness/Diagnostics | Diagnostic-only; cannot support behavioral headline claim. | "fixed accepted-set proves unconditional vkm/original advantage" |

## Exploratory Claims

| claim_id | final allowed wording | evidence source | evidence grade | allowed manuscript location | required caveat | forbidden stronger wording |
|---|---|---|---|---|---|---|
| C-UTIL-01 | Reduced utility-sensitivity diagnostics are consistent with the main vkm-intensity direction across the tested parameter settings. | 06-04 utility sensitivity | exploratory | Robustness, Discussion | Reduced diagnostic grid; no empirical calibration or p-values. | "robust under all utility parameters" |
| C-MP-01 | Walking-radius and meeting-point-density diagnostics bound sensitivity within the tested synthetic grid only. | 06-04 mp-density/walking-radius package | exploratory | Robustness, Managerial boundary | No universal walking-radius threshold; no pedestrian network calibration. | "1000 m is a universal threshold" |
| C-FLEET-01 | Fleet-demand stress diagnostics are consistent with the main direction within the tested synthetic settings. | 06-04 fleet-demand stress | exploratory | Robustness, Managerial boundary | No operator fleet-ratio rule. | "operators should use a fixed fleet ratio" |
| C-EQ-01 | Equity outputs may be reported as modeled type-level and individual-burden diagnostics. | 06-04 equity type outcomes; `equity_summary.json` | exploratory | Robustness, Discussion, Limitations | Passenger types are simulation-range constructs; MET-04 is metrics produced and bounded. | "equity benefits are strongly established" |
| C-ALG-01 | Algorithm diagnostics document implementation behavior and scoped exact/static checks. | 06-04 algorithm diagnostics | exploratory diagnostic | Framework, Diagnostics, Supplement | They support credibility and scope disclosure only. | "MILP validates ALNS optimality"; "deployment-ready real-time solver" |
| C-CASE-01 | The Beijing-labeled material may be described only as a Beijing-inspired synthetic scenario or illustrative transfer check. | Phase 7 data audit and claim boundary | exploratory / limitation | Discussion, Limitations, Appendix | No new Phase 7 formal experiment was run; legacy rows are illustrative only. | "real Beijing case"; "semi-real validation" |
| C-POL-01 | Managerial insights may be framed as conditional simulation-based boundary conditions. | Phase 6 diagnostics; Phase 7 boundary; Phase 9 table/figure plan | exploratory / limitation | Managerial Insights after limitations | Must begin with experiment condition and avoid prescription. | "Chinese city operators should deploy"; "regulators should require" |

## Limitation Claims

| claim_id | final allowed wording | evidence source | evidence grade | allowed manuscript location | required caveat | forbidden stronger wording |
|---|---|---|---|---|---|---|
| C-MC-01 | Matched coverage has 15 durable failed FullModel rows, which limits the strength of equal-coverage interpretation. | 06-03 matched coverage | moderate limitation | Robustness, Limitations | Do not hide failed rows. | "matched coverage fully resolves coverage confounding" |
| C-EQ-01 | Equity evidence is bounded to simulation-range passenger types and cannot support demographic equity conclusions. | 06-04 equity outputs | exploratory limitation | Limitations, Discussion | Type-level and individual burden metrics exist, but empirical calibration does not. | "strong equity improvement" |
| C-CASE-01 | The case evidence is synthetic and cannot validate real Beijing operations. | Phase 7 artifacts | exploratory limitation | Limitations | Use exact phrase "Beijing-inspired synthetic scenario". | "real Beijing validation" |
| C-LIM-01 | Real/semi-real OD, road-network, meeting-point, request-time, passenger-preference, and fleet validation remain future work. | Phase 7 data audit | strong limitation | Abstract boundary, Limitations, Conclusion | This limitation must carry into Phase 9 and Phase 10. | "calibrated real-world case" |

## Strongest Allowed Main Claim

The strongest allowed main claim is C-EFF-01 plus C-COV-01 together:
FullModel/BidirectionalMP shows lower vehicle-km intensity in formal synthetic
paired experiments, while serving a smaller share; the efficiency result must
therefore be presented as a coverage-aware conditional result.

