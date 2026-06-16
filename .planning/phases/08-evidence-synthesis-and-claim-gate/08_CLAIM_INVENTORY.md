# Phase 8 Claim Inventory

**Phase:** 08 - Evidence Synthesis and Claim Gate
**Date:** 2026-06-16
**Status:** complete

## Purpose

Inventory manuscript-facing claims before any Phase 9 refresh. This file collects
candidate claims from the current manuscript, Phase 0/1 audits, Phase 6 formal
evidence, Phase 7 case boundary, Phase 9 placeholders, README/docs legacy
language, and known review-note risks. It does not write final manuscript prose.

## Inventory

| claim_id | source artifact | original wording or source signal | claim type | intended manuscript location | preliminary risk | needs evidence | abstract candidate | conclusion candidate | discussion candidate | limitation candidate |
|---|---|---|---|---|---|---|---|---|---|---|
| C-FWK-01 | `manuscript/sections/abstract.tex`; `01_NOVELTY_POSITIONING.md`; `09_REVISED_ABSTRACT.md` | "many-to-many DRT framework with bidirectional meeting point sets ... simulated passenger response ... outside option" | Framework / contribution | Abstract, Introduction, Framework | Moderate: framework wording is safe only if it avoids first/only and does not imply deployment validation | yes | yes | yes | yes | no |
| C-NOV-01 | `manuscript/sections/abstract.tex`; `manuscript/sections/intro.tex`; `01_NOVELTY_POSITIONING.md` | "existing work assigns meeting points only on the pickup side"; "No existing work combines..." | Novelty | Introduction, Literature | High: broad first/only and pickup-only prior-work wording is forbidden by Phase 1 | yes | no | no | yes | no |
| C-EFF-01 | `06_STATISTICAL_SUMMARY.md`; `06_FORMAL_SYNTHETIC_RESULTS.md` | FullModel has lower total vkm, vkm/served, and vkm/original than DoorToDoor and single-sided variants in the formal main matrix | Main efficiency | Abstract, Formal Main Evidence, Conclusion | Medium: defensible only with coverage, rejection, paired design, and CI caveats | yes | yes | yes | yes | no |
| C-COV-01 | `06_STATISTICAL_SUMMARY.md`; `06_EVIDENCE_BOUNDARY.md`; current abstract/experiments | FullModel lower vkm occurs with lower served share and higher feasibility rejection; coverage must be reported with efficiency | Coverage / served-share | Abstract, Formal Main Evidence, Conclusion | High if omitted; low if paired with C-EFF-01 | yes | yes | yes | yes | no |
| C-ACC-01 | `06_STATISTICAL_SUMMARY.md`; Phase 3/6 choice logs | Passenger response changes interpretation; behavioral acceptance differences are conditional and not a standalone superiority result | Passenger response / acceptance | Experimental Design, Main Evidence, Discussion | Medium: acceptance-rate differences are mixed across baselines and CIs are not uniformly separated from zero | yes | maybe | yes | yes | no |
| C-MC-01 | `06_STATISTICAL_SUMMARY.md`; `06_FORMAL_RESULT_MANIFEST.md` | Matched-coverage completed pairs preserve FullModel vkm advantages, with 15 durable failed FullModel matched rows | Matched-coverage | Robustness Controls, Conclusion | Medium: supports completed-pair robustness only; failed rows must be visible | yes | maybe | yes | yes | yes |
| C-FAS-01 | `06_STATISTICAL_SUMMARY.md`; `06_EVIDENCE_BOUNDARY.md` | Fixed accepted-set supports lower vkm/served on the common passenger set but not unconditional vkm/original dominance | Fixed accepted-set routing diagnostic | Robustness/Diagnostics | Medium: diagnostic-only; cannot support behavioral headline claim | yes | no | yes | yes | yes |
| C-UTIL-01 | `06_FORMAL_SYNTHETIC_RESULTS.md`; robustness tables | Utility sensitivity diagnostics show favorable setting-level mean vkm intensity across tested parameter settings | Utility sensitivity | Robustness, Discussion | Medium: reduced diagnostic grid and no paired hypothesis tests | yes | no | maybe | yes | yes |
| C-MP-01 | `06_FORMAL_SYNTHETIC_RESULTS.md`; current policy section | Walking-radius / meeting-point-density diagnostics bound when bidirectional meeting points are viable under tested synthetic settings | Walking radius / meeting-point density | Robustness, Managerial Insights | High if turned into universal threshold | yes | no | maybe | yes | yes |
| C-FLEET-01 | `06_FORMAL_SYNTHETIC_RESULTS.md`; current policy section | Fleet-demand stress diagnostics indicate efficiency patterns under tested fleet-demand settings | Fleet-demand stress | Robustness, Managerial Insights | High if turned into real operator fleet rule | yes | no | maybe | yes | yes |
| C-EQ-01 | `06_FORMAL_SYNTHETIC_RESULTS.md`; `equity_summary.json`; current abstract/policy/conclusion | Equity outputs include type-level and individual burden diagnostics; strong equity benefit is not established | Equity / passenger-type outcome | Robustness, Discussion, Limitations | High: passenger types are simulation-range constructs | yes | no | maybe | yes | yes |
| C-ALG-01 | `06_FORMAL_RESULT_MANIFEST.md`; current algorithm/conclusion | Rolling-horizon/ALNS and MILP diagnostics support implementation credibility but not final algorithm optimality | Algorithm / ALNS reliability | Framework, Diagnostics, Supplement | Medium: diagnostics exist but do not establish algorithm-quality dominance | yes | no | maybe | yes | yes |
| C-CASE-01 | `07_DATA_AUDIT.md`; `07_CASE_CLAIM_BOUNDARY.md`; current experiments | Beijing-inspired material is synthetic illustrative scenario-transfer evidence only | Beijing-inspired case-study | Discussion, Limitations, maybe Appendix | High if described as real or semi-real Beijing validation | yes | no | maybe | yes | yes |
| C-POL-01 | current `policy.tex`; `09_TABLE_FIGURE_PLAN.md`; Phase 7 boundary | Managerial implications must be conditional simulation-based insights, not citywide prescriptions | Policy / managerial implication | Managerial Insights and Boundary Conditions | High: direct Chinese-city policy/deployment wording exceeds evidence | yes | no | maybe | yes | yes |
| C-REP-01 | `06_FORMAL_RESULT_MANIFEST.md`; `phase06_result_manifest.json`; `06-VERIFICATION.md` | Phase 6 formal packages have raw/processed/config/seed/validation artifacts and no hidden missing rows | Reproducibility | Experimental Design, Reproducibility note, Conclusion | Low: artifact evidence is strong for Phase 6 packages; REP-01/02 still Phase 10 | yes | maybe | yes | yes | no |
| C-LIM-01 | `07_DATA_AUDIT.md`; `06_EVIDENCE_BOUNDARY.md`; `03_PARAMETER_CALIBRATION.md`; Phase 9 plans | Real/semi-real calibration and validation remain future work; current evidence is synthetic | Limitation | Abstract boundary, Limitations, Conclusion | Low if stated as limitation; high if hidden | yes | yes | yes | yes | yes |
| C-LEG-01 | current abstract/intro/conclusion; `00_MANUSCRIPT_CLAIM_AUDIT.md` | "29.1% improvement" and "35.0% matched-coverage gain" prove superiority | Main efficiency legacy overclaim | Old abstract, Introduction, Conclusion | High: legacy, coverage-confounded, provenance mismatch | yes | no | no | yes | yes |
| C-GAMMA-01 | current experiments; `00_CURRENT_EXPERIMENT_MAP.md`; Phase 9 table plan | Gamma sweep is a coverage-efficiency Pareto frontier | Utility / welfare / policy diagnostic | Old experiments, figures | High: contradicted by implementation because gamma is post-hoc | yes | no | no | yes | yes |
| C-DEP-01 | current abstract/policy/conclusion; Phase 7 boundary | Method is deployment-ready or directly validates Chinese city operations | Policy / deployment | Old policy, Conclusion | High: no real city validation or observed operations | yes | no | no | yes | yes |
| C-WEIGHT-01 | current experiments; `00_CURRENT_EXPERIMENT_MAP.md`; `09_TABLE_FIGURE_PLAN.md` | Weight sensitivity proves robust efficiency gains across policy-relevant objective weights | Robustness / policy | Old experiments, Appendix/Supplement | High: legacy formula/provenance mismatch and not part of Phase 6 formal evidence | yes | no | no | yes | yes |

## Claim Type Coverage

| Required type | Covered by |
|---|---|
| Framework / contribution claim | C-FWK-01 |
| Novelty claim | C-NOV-01 |
| Main efficiency claim | C-EFF-01, C-LEG-01 |
| Coverage / served-share claim | C-COV-01 |
| Passenger response / acceptance claim | C-ACC-01 |
| Matched-coverage claim | C-MC-01 |
| Fixed accepted-set routing diagnostic claim | C-FAS-01 |
| Utility sensitivity claim | C-UTIL-01 |
| Walking radius / meeting-point density claim | C-MP-01 |
| Fleet-demand stress claim | C-FLEET-01 |
| Equity / passenger-type outcome claim | C-EQ-01 |
| Algorithm / ALNS reliability claim | C-ALG-01 |
| Beijing-inspired case-study claim | C-CASE-01 |
| Policy / managerial implication claim | C-POL-01 |
| Reproducibility claim | C-REP-01 |
| Limitation claim | C-LIM-01 |

## Inventory Counts

- Total claims inventoried: 20
- Claims requiring evidence: 20
- Candidate abstract units: 5
- Candidate conclusion units: 13
- Candidate discussion units: 20
- Candidate limitation units: 14

