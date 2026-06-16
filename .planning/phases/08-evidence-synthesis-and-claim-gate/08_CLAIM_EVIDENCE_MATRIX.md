# Phase 8 Claim-Evidence Matrix

**Phase:** 08 - Evidence Synthesis and Claim Gate
**Date:** 2026-06-16
**Status:** passed

## Purpose

Map every inventoried claim to evidence, limitations, allowed wording, forbidden
wording, claim grade, and manuscript placement. This is the Phase 8 source of
truth for Phase 9 refresh. It is not final manuscript prose.

## Evidence Package Legend

| package | role | row/status summary |
|---|---|---|
| 06-02 main behavioral matrix | main formal evidence | 320 rows, 320 completed, 0 failed, 20 seeds x 4 scales x 4 methods |
| 06-03 matched coverage | main/control evidence | 320 rows, 305 completed, 15 durable failed FullModel matched rows |
| 06-03 fixed accepted-set | routing diagnostic evidence | 320 rows, 320 completed, 0 failed |
| 06-04 utility sensitivity | robustness diagnostic evidence | 420 rows, 420 completed |
| 06-04 walking-radius / MP-density | robustness diagnostic evidence | 180 rows, 180 completed |
| 06-04 fleet-demand stress | robustness diagnostic evidence | 60 rows, 60 completed |
| 06-04 equity type outcomes | exploratory limited evidence | 180 type-level rows, 12,000 individual burden rows |
| 06-04 algorithm diagnostics | diagnostic evidence | 8 rows/artifacts, 8 completed |
| Phase 7 case boundary | limitation / exploratory evidence | no new experiment; legacy `beijing_results.csv` has 21 illustrative rows only |

## Matrix

### C-FWK-01

| field | value |
|---|---|
| proposed manuscript claim | The study develops and evaluates an integrated choice-aware dynamic service-design simulation framework for many-to-many DRT with bidirectional pickup/dropoff meeting-point sets. |
| claim type | Framework / contribution |
| evidence source | Phase 1 novelty positioning; Phase 2 method taxonomy; Phase 6 method labels and formal packages; Phase 9 placeholders |
| evidence package | Planning + formal experiment implementation surface |
| evidence family | main |
| methods compared | DoorToDoor, SingleSidedPickup, SingleSidedDropoff, BidirectionalMP/FullModel |
| seed / scale / row counts | 20 seeds, 4 scales, 320 main rows; supplementary packages as listed in manifest |
| completed / failed / timeout / blocked | main 320 / 0 / 0 / 0 |
| key metrics | method taxonomy, shared response semantics, paired design, vkm and served-share metrics |
| direction of result | framework is implemented and used to generate formal evidence |
| uncertainty evidence | not applicable as a framework-existence claim |
| paired hypothesis test status | not implemented |
| denominator involved | not denominator-specific |
| coverage-confounding risk | low for framework description; high if paired with superiority language |
| case-study data quality | not case-based |
| equity evidence status | framework includes equity diagnostics, but equity claim remains exploratory |
| limitations | do not call individual components first or deployment-ready |
| claim grade | moderate |
| allowed wording | "integrated choice-aware dynamic service-design simulation framework" |
| forbidden wording | "first bidirectional meeting-point DRT paper"; "deployment-ready framework" |
| recommended manuscript location | Abstract, Introduction, Framework |

### C-NOV-01

| field | value |
|---|---|
| proposed manuscript claim | Prior work covers overlapping meeting-point, pickup/dropoff walking, choice, and rolling-horizon ideas; this paper should claim only a conservative integrated-framework contribution. |
| claim type | Novelty |
| evidence source | `01_NOVELTY_POSITIONING.md`; `CLAIMS_AND_RISKS.md`; current manuscript |
| evidence package | literature and novelty audit |
| evidence family | limitation |
| methods compared | not applicable |
| seed / scale / row counts | not applicable |
| completed / failed / timeout / blocked | not applicable |
| key metrics | citation-by-claim risk status |
| direction of result | broad first/only language is not supported |
| uncertainty evidence | unresolved full-text citation cleanup remains |
| paired hypothesis test status | not applicable |
| denominator involved | none |
| coverage-confounding risk | none |
| case-study data quality | none |
| equity evidence status | none |
| limitations | exact prior-work contrast still needs Phase 9 citation cleanup |
| claim grade | unsupported for broad wording; moderate for conservative integrated-framework wording |
| allowed wording | "partially overlapping prior literatures motivate the integrated evidence-chain study" |
| forbidden wording | "No prior work considers dropoff walking"; "existing work is pickup-only"; "first bidirectional meeting-point DRT paper" |
| recommended manuscript location | Literature positioning; not abstract as first/only |

### C-EFF-01

| field | value |
|---|---|
| proposed manuscript claim | In the 20-seed formal synthetic paired main matrix, BidirectionalMP/FullModel shows lower vehicle-km intensity than DoorToDoor and single-sided choice baselines, conditional on reporting served-share and rejection context. |
| claim type | Main efficiency |
| evidence source | `06_STATISTICAL_SUMMARY.md`; `06_FORMAL_SYNTHETIC_RESULTS.md`; `paired_bootstrap_ci.csv` |
| evidence package | 06-02 main behavioral matrix |
| evidence family | main |
| methods compared | BidirectionalMP_Choice_RH_ALNS vs DoorToDoor_Choice_CommonRouting, SingleSidedPickup, SingleSidedDropoff |
| seed / scale / row counts | 20 seeds, 4 scales, 320 rows, 80 aggregate valid pairs per baseline |
| completed / failed / timeout / blocked | 320 / 0 / 0 / 0 |
| key metrics | total_vehicle_km, vkm_per_served_trip, vkm_per_original_request |
| direction of result | FullModel lower: aggregate vkm/served difference vs DoorToDoor -4.714 with 95% bootstrap CI [-5.244, -4.238]; vkm/original -1.332 CI [-1.480, -1.192] |
| uncertainty evidence | paired bootstrap CIs implemented, 5000 resamples, bootstrap seed 20260616 |
| paired hypothesis test status | not implemented |
| denominator involved | served trips and original requests; both must be named |
| coverage-confounding risk | material unless C-COV-01 is reported alongside the efficiency result |
| case-study data quality | synthetic formal evidence only |
| equity evidence status | separate exploratory package |
| limitations | no real/semi-real data; no p-values; claim is conditional and synthetic |
| claim grade | strong |
| allowed wording | "under the tested formal synthetic paired design, FullModel/BidirectionalMP has lower vehicle-km intensity while serving a smaller share" |
| forbidden wording | "unconditionally superior"; "dominates under all metrics"; "wins on every denominator" |
| recommended manuscript location | Abstract bullet, Formal Main Evidence, Conclusion |

### C-COV-01

| field | value |
|---|---|
| proposed manuscript claim | The main efficiency result must be interpreted with lower served share and rejection/feasibility context. |
| claim type | Coverage / served-share |
| evidence source | `06_STATISTICAL_SUMMARY.md`; `paired_bootstrap_ci.csv` |
| evidence package | 06-02 main behavioral matrix |
| evidence family | main |
| methods compared | FullModel vs DoorToDoor and single-sided choice baselines |
| seed / scale / row counts | 80 aggregate valid pairs per baseline |
| completed / failed / timeout / blocked | 320 / 0 / 0 / 0 |
| key metrics | served_share, behavioral_acceptance_rate, choice_rejection_rate, feasibility_rejection_rate |
| direction of result | FullModel served share is lower: vs DoorToDoor -0.0429, CI [-0.0521, -0.0339] |
| uncertainty evidence | paired bootstrap CI available |
| paired hypothesis test status | not implemented |
| denominator involved | original requests for served share; rejection-rate denominators |
| coverage-confounding risk | central risk; mitigated only by reporting coverage and controls |
| case-study data quality | not case-based |
| equity evidence status | separate exploratory package |
| limitations | cannot isolate efficiency from served-share differences without controls |
| claim grade | strong |
| allowed wording | "efficiency gains are accompanied by lower served share and must be read as a coverage-efficiency trade-off" |
| forbidden wording | "same service level"; "no coverage penalty"; "lower vkm proves pure routing superiority" |
| recommended manuscript location | Abstract bullet, Formal Main Evidence, Conclusion |

### C-ACC-01

| field | value |
|---|---|
| proposed manuscript claim | Passenger response is an explicit part of the evidence chain, but acceptance-rate effects are conditional rather than a strong standalone improvement claim. |
| claim type | Passenger response / acceptance |
| evidence source | `06_STATISTICAL_SUMMARY.md`; Phase 3 choice contract and utility logs |
| evidence package | 06-02 main behavioral matrix |
| evidence family | main |
| methods compared | FullModel vs behavioral choice baselines |
| seed / scale / row counts | 20 seeds, 4 scales, 320 main rows |
| completed / failed / timeout / blocked | 320 / 0 / 0 / 0 |
| key metrics | behavioral_acceptance_rate, choice_rejection_rate, feasibility_rejection_rate |
| direction of result | aggregate acceptance-rate differences are small and not uniformly separated from zero; feasibility rejection is higher for FullModel |
| uncertainty evidence | bootstrap CIs available for aggregate differences |
| paired hypothesis test status | not implemented |
| denominator involved | original requests and behavioral choice opportunities |
| coverage-confounding risk | high if used as a benefit claim |
| case-study data quality | not case-based |
| equity evidence status | exploratory by type |
| limitations | utility parameters are simulation ranges, not empirical calibration |
| claim grade | moderate |
| allowed wording | "passenger response and rejection mechanisms change how efficiency should be interpreted" |
| forbidden wording | "FullModel improves acceptance"; "passengers prefer bidirectional meeting points" |
| recommended manuscript location | Experimental Design, Discussion, Conclusion caveat |

### C-MC-01

| field | value |
|---|---|
| proposed manuscript claim | On completed matched-coverage pairs, FullModel retains lower vehicle-km denominators, but the 15 durable failed FullModel matched rows are a limitation. |
| claim type | Matched-coverage |
| evidence source | `06_STATISTICAL_SUMMARY.md`; `06_FORMAL_RESULT_MANIFEST.md` |
| evidence package | 06-03 matched coverage |
| evidence family | control |
| methods compared | FullModel vs DoorToDoor, SingleSidedPickup, SingleSidedDropoff matched controls |
| seed / scale / row counts | 20 seeds, 4 scales, 320 rows; 65 aggregate valid pairs per baseline |
| completed / failed / timeout / blocked | 305 / 15 / 0 / 0 |
| key metrics | total_vehicle_km, vkm_per_served_trip, vkm_per_original_request, served_share |
| direction of result | completed pairs favor FullModel: vs DoorToDoor vkm/served -4.617 and vkm/original -0.681; full_better_share 0.985 |
| uncertainty evidence | descriptive paired summaries; CI not central in current matched table |
| paired hypothesis test status | not implemented |
| denominator involved | served trips and original requests |
| coverage-confounding risk | reduced but not eliminated because failed matched rows are non-random evidence boundary |
| case-study data quality | not case-based |
| equity evidence status | separate exploratory package |
| limitations | 15 durable failed FullModel matched rows must be reported |
| claim grade | moderate |
| allowed wording | "completed matched-coverage pairs are consistent with a FullModel efficiency advantage, with 15 durable failed matched rows carried as a limitation" |
| forbidden wording | "matched coverage fully proves equal-coverage superiority"; "all matched rows completed" |
| recommended manuscript location | Robustness Controls, Conclusion caveat |

### C-FAS-01

| field | value |
|---|---|
| proposed manuscript claim | Fixed accepted-set diagnostics support lower vkm per served request on the common accepted set, but do not support unconditional vkm/original or behavioral dominance. |
| claim type | Fixed accepted-set routing diagnostic |
| evidence source | `06_STATISTICAL_SUMMARY.md`; `06_EVIDENCE_BOUNDARY.md` |
| evidence package | 06-03 fixed accepted-set |
| evidence family | diagnostic |
| methods compared | FullModel routing/service design vs fixed accepted-set baselines |
| seed / scale / row counts | 20 seeds, 4 scales, 320 rows, 80 aggregate valid pairs |
| completed / failed / timeout / blocked | 320 / 0 / 0 / 0 |
| key metrics | vkm_per_served_request, vkm_per_original_request, deterministic_inserted_share |
| direction of result | vkm/served lower (vs DoorToDoor -5.232), but vkm/original slightly positive vs DoorToDoor (0.052) |
| uncertainty evidence | descriptive paired diagnostic summaries |
| paired hypothesis test status | not implemented |
| denominator involved | served request and original request denominators diverge |
| coverage-confounding risk | diagnostic controls accepted set, but not behavioral acceptance |
| case-study data quality | not case-based |
| equity evidence status | separate exploratory package |
| limitations | cannot support behavioral headline claims |
| claim grade | moderate |
| allowed wording | "fixed accepted-set diagnostics support a routing/service-design efficiency signal on vkm per served request" |
| forbidden wording | "fixed accepted-set proves unconditional vkm/original advantage" |
| recommended manuscript location | Diagnostics or robustness summary |

### C-UTIL-01

| field | value |
|---|---|
| proposed manuscript claim | Utility sensitivity diagnostics show favorable FullModel setting-level mean vkm intensity across tested reduced parameter settings. |
| claim type | Utility sensitivity |
| evidence source | `06_FORMAL_SYNTHETIC_RESULTS.md`; `robustness_setting_summary.csv` |
| evidence package | 06-04 utility sensitivity |
| evidence family | diagnostic |
| methods compared | FullModel vs DoorToDoor |
| seed / scale / row counts | 10 seeds, 3 scales, 420 rows |
| completed / failed / timeout / blocked | 420 / 0 / 0 / 0 |
| key metrics | vkm_per_served_trip, vkm_per_original_request, served_share |
| direction of result | all listed utility settings show negative mean FullModel-minus-DoorToDoor vkm intensity differences |
| uncertainty evidence | setting-level summaries; no full hypothesis-test suite |
| paired hypothesis test status | not implemented |
| denominator involved | served and original request denominators |
| coverage-confounding risk | still present; served share often lower |
| case-study data quality | not case-based |
| equity evidence status | simulation-range passenger types |
| limitations | reduced diagnostic grid; not headline evidence |
| claim grade | exploratory |
| allowed wording | "diagnostic utility-sensitivity screens are consistent with the main efficiency direction" |
| forbidden wording | "robust under all utility parameters"; "calibrated behavioral proof" |
| recommended manuscript location | Discussion or robustness diagnostics |

### C-MP-01

| field | value |
|---|---|
| proposed manuscript claim | Walking-radius and meeting-point-density diagnostics bound sensitivity under tested synthetic settings only. |
| claim type | Walking radius / meeting-point density |
| evidence source | `06_FORMAL_SYNTHETIC_RESULTS.md`; current policy section risk |
| evidence package | 06-04 mp density / walking radius |
| evidence family | diagnostic |
| methods compared | FullModel vs DoorToDoor |
| seed / scale / row counts | 10 seeds, 3 scales, 180 rows |
| completed / failed / timeout / blocked | 180 / 0 / 0 / 0 |
| key metrics | vkm_per_served_trip, vkm_per_original_request, served_share |
| direction of result | tested settings preserve favorable vkm intensity means, with served-share trade-offs |
| uncertainty evidence | setting-level summaries |
| paired hypothesis test status | not implemented |
| denominator involved | served and original request denominators |
| coverage-confounding risk | high if converted to threshold claim |
| case-study data quality | not case-based |
| equity evidence status | tied to simulation-range walk sensitivity |
| limitations | no pedestrian network or calibrated walking tolerance |
| claim grade | exploratory |
| allowed wording | "within the tested synthetic radius/density grid" |
| forbidden wording | "1000 m is a universal deployment threshold" |
| recommended manuscript location | Robustness, managerial boundary, limitations |

### C-FLEET-01

| field | value |
|---|---|
| proposed manuscript claim | Fleet-demand stress diagnostics are consistent with FullModel lower vkm intensity in tested synthetic stress settings, but do not create operator fleet rules. |
| claim type | Fleet-demand stress |
| evidence source | `06_FORMAL_SYNTHETIC_RESULTS.md` |
| evidence package | 06-04 fleet-demand stress |
| evidence family | diagnostic |
| methods compared | FullModel vs DoorToDoor |
| seed / scale / row counts | 10 seeds, 60 rows |
| completed / failed / timeout / blocked | 60 / 0 / 0 / 0 |
| key metrics | vkm_per_served_trip, vkm_per_original_request, served_share |
| direction of result | stress settings show negative mean vkm intensity differences |
| uncertainty evidence | setting-level summaries |
| paired hypothesis test status | not implemented |
| denominator involved | served and original request denominators |
| coverage-confounding risk | high if used as service-quality rule |
| case-study data quality | not case-based |
| equity evidence status | separate exploratory package |
| limitations | synthetic fleet-demand grid only |
| claim grade | exploratory |
| allowed wording | "tested fleet-demand diagnostics are consistent with the main direction" |
| forbidden wording | "operators should adopt a universal fleet ratio" |
| recommended manuscript location | Robustness, managerial boundary |

### C-EQ-01

| field | value |
|---|---|
| proposed manuscript claim | Equity metrics are produced as type-level and individual-burden diagnostics, but equity improvement or demographic equity is not established. |
| claim type | Equity / passenger-type outcome |
| evidence source | `equity_summary.json`; type-level and individual burden CSVs; `06_FORMAL_SYNTHETIC_RESULTS.md` |
| evidence package | 06-04 equity type outcomes |
| evidence family | exploratory |
| methods compared | FullModel vs DoorToDoor by passenger type |
| seed / scale / row counts | 180 type-level rows; 12,000 individual burden rows |
| completed / failed / timeout / blocked | 180 / 0 / 0 / 0 |
| key metrics | served_share, type_level_acceptance_rate, avg_wait, avg_walk, avg_ivt, generalized_cost, walking_burden |
| direction of result | type and burden diagnostics exist; no strong equity-benefit direction is approved |
| uncertainty evidence | exploratory summaries; no empirical type calibration |
| paired hypothesis test status | not implemented |
| denominator involved | type-level request denominators and individual burden distributions |
| coverage-confounding risk | material because served/unserved composition affects type outcomes |
| case-study data quality | not case-based |
| equity evidence status | passenger types are simulation-range constructs |
| limitations | no demographic or empirical calibration |
| claim grade | exploratory |
| allowed wording | "equity diagnostics report modeled type-level and individual burden patterns" |
| forbidden wording | "equity benefits are strongly established"; "regulators should require..." |
| recommended manuscript location | Robustness, discussion, limitations |

### C-ALG-01

| field | value |
|---|---|
| proposed manuscript claim | Algorithm diagnostics support implementation credibility and scope disclosure, but not strong ALNS optimality or deployment readiness. |
| claim type | Algorithm / ALNS reliability |
| evidence source | `06_FORMAL_RESULT_MANIFEST.md`; algorithm diagnostic validation report |
| evidence package | 06-04 algorithm diagnostics |
| evidence family | diagnostic |
| methods compared | rolling horizon implementation, ALNS budget, MILP static-snapshot diagnostics |
| seed / scale / row counts | 8 diagnostic rows/artifacts |
| completed / failed / timeout / blocked | 8 / 0 / 0 / 0 |
| key metrics | validation pass, diagnostic status, budget/snapshot outputs |
| direction of result | diagnostics completed and passed structural validation |
| uncertainty evidence | not inferential |
| paired hypothesis test status | not implemented |
| denominator involved | algorithm diagnostic metrics only |
| coverage-confounding risk | not behavioral evidence |
| case-study data quality | not case-based |
| equity evidence status | separate exploratory package |
| limitations | no broad optimality proof; MILP is scoped diagnostic |
| claim grade | exploratory |
| allowed wording | "algorithm diagnostics document implementation behavior and limited exact/snapshot checks" |
| forbidden wording | "MILP validates ALNS optimality"; "real-time deployment-ready" |
| recommended manuscript location | Framework, diagnostics, supplement |

### C-CASE-01

| field | value |
|---|---|
| proposed manuscript claim | The Beijing-labeled material is a Beijing-inspired synthetic scenario and can only illustrate scenario-transfer boundaries. |
| claim type | Beijing-inspired case-study |
| evidence source | `07_DATA_AUDIT.md`; `07_CASE_STUDY_RESULTS.md`; `07_CASE_CLAIM_BOUNDARY.md` |
| evidence package | Phase 7 bounded case closure |
| evidence family | exploratory / limitation |
| methods compared | legacy 3 seeds x 7 variants only; no new formal case experiment |
| seed / scale / row counts | legacy 21 rows; no Phase 7 formal validation package |
| completed / failed / timeout / blocked | not applicable; no new experiment |
| key metrics | legacy served share and vkm denominators; data-quality attributes |
| direction of result | qualitative pattern resembles Phase 6 but is illustrative only |
| uncertainty evidence | none beyond legacy rows |
| paired hypothesis test status | not implemented |
| denominator involved | legacy vkm denominators only if mentioned |
| coverage-confounding risk | high in legacy rows |
| case-study data quality | synthetic generated OD, grid MPs, simulated times, no real network or calibration |
| equity evidence status | not case-calibrated |
| limitations | no observed OD, road network, meeting points, request times, preferences, or fleet data |
| claim grade | exploratory |
| allowed wording | "Beijing-inspired synthetic scenario" |
| forbidden wording | "real Beijing validation"; "semi-real case"; "direct Beijing policy evidence" |
| recommended manuscript location | Discussion, limitations, appendix/supplement |

### C-POL-01

| field | value |
|---|---|
| proposed manuscript claim | Managerial implications must be conditional simulation-based insights tied to experiment conditions and limitations. |
| claim type | Policy / managerial implication |
| evidence source | current `policy.tex`; `09_TABLE_FIGURE_PLAN.md`; Phase 6/7 boundaries |
| evidence package | Phase 6 diagnostics plus Phase 7 limitation evidence |
| evidence family | exploratory / limitation |
| methods compared | depends on insight; no direct policy experiment |
| seed / scale / row counts | varies by diagnostic package; no observed deployment rows |
| completed / failed / timeout / blocked | no policy deployment validation |
| key metrics | vkm, served share, radius/density, fleet-demand stress, type diagnostics |
| direction of result | conditional insights can be discussed, prescriptions cannot |
| uncertainty evidence | limited to simulation diagnostics |
| paired hypothesis test status | not implemented |
| denominator involved | must name denominator for any metric |
| coverage-confounding risk | high if claims omit served share |
| case-study data quality | synthetic only |
| equity evidence status | exploratory |
| limitations | no citywide policy or deployment validation |
| claim grade | exploratory |
| allowed wording | "the simulation suggests operators may need to monitor..." |
| forbidden wording | "Chinese city operators should deploy..."; "regulators should require..." |
| recommended manuscript location | Managerial Insights and Boundary Conditions, after limitations |

### C-REP-01

| field | value |
|---|---|
| proposed manuscript claim | The Phase 6 formal evidence packages are reproducibly documented with raw/processed outputs, manifests, validators, and durable failure rows. |
| claim type | Reproducibility |
| evidence source | `06_FORMAL_RESULT_MANIFEST.md`; `phase06_result_manifest.json`; `phase06_verification_report.json` |
| evidence package | Phase 6 formal manifest |
| evidence family | main |
| methods compared | all formal Phase 6 packages |
| seed / scale / row counts | packages total 1,928 listed rows/artifacts plus 12,000 individual burden rows |
| completed / failed / timeout / blocked | 1,913 completed rows/artifacts, 15 failed matched rows, 0 timeout, 0 blocked |
| key metrics | validator_passed, schema_drift=false, denominator_validation=passed |
| direction of result | all listed formal package validators passed; no silent missing rows |
| uncertainty evidence | paired bootstrap CIs for main formal evidence |
| paired hypothesis test status | not implemented |
| denominator involved | denominator checks passed |
| coverage-confounding risk | addressed through explicit controls and boundaries, not eliminated |
| case-study data quality | Phase 7 not formal validation |
| equity evidence status | exploratory but files exist |
| limitations | REP-01/REP-02 final package still belongs to Phase 10 |
| claim grade | strong |
| allowed wording | "Phase 6 formal outputs are reproducibly documented and validated" |
| forbidden wording | "complete reproducibility package is final"; "main tables/figures are final manuscript-ready" |
| recommended manuscript location | Experimental Design, reproducibility note, conclusion caveat |

### C-LIM-01

| field | value |
|---|---|
| proposed manuscript claim | Current evidence remains synthetic and requires real or semi-real calibration and validation before deployment or citywide transfer. |
| claim type | Limitation |
| evidence source | `07_DATA_AUDIT.md`; `06_EVIDENCE_BOUNDARY.md`; Phase 3 calibration notes; Phase 9 plans |
| evidence package | Phase 7 data audit and Phase 6 evidence boundary |
| evidence family | limitation |
| methods compared | not applicable |
| seed / scale / row counts | not applicable |
| completed / failed / timeout / blocked | real/semi-real case data absent |
| key metrics | data availability audit fields |
| direction of result | no observed OD, road network, MP candidates, request times, passenger calibration, or fleet data found |
| uncertainty evidence | direct repository/data audit |
| paired hypothesis test status | not applicable |
| denominator involved | none |
| coverage-confounding risk | limitation carried to interpretation |
| case-study data quality | synthetic only |
| equity evidence status | simulation-range only |
| limitations | this is the limitation itself |
| claim grade | strong |
| allowed wording | "real/semi-real calibration and validation remain future work" |
| forbidden wording | "validated in real operations"; "calibrated to Beijing" |
| recommended manuscript location | Abstract boundary, Limitations, Conclusion |

### C-LEG-01

| field | value |
|---|---|
| proposed manuscript claim | Legacy 29.1% and 35.0% effect-size claims cannot be used as final proof of superiority. |
| claim type | Main efficiency legacy overclaim |
| evidence source | `00_MANUSCRIPT_CLAIM_AUDIT.md`; current manuscript |
| evidence package | Phase 0 audit; superseded by Phase 6 |
| evidence family | limitation |
| methods compared | legacy FullModel vs DoorToDoor and DoorToDoorCapped |
| seed / scale / row counts | legacy 3-seed / aggregate rows, not Phase 6 formal package |
| completed / failed / timeout / blocked | not formal evidence |
| key metrics | old vkm/trip, served share |
| direction of result | legacy values are coverage-confounded and provenance-mismatched |
| uncertainty evidence | insufficient |
| paired hypothesis test status | not implemented |
| denominator involved | old `vkm/trip` ambiguous; forbidden for new evidence |
| coverage-confounding risk | central and unresolved for legacy values |
| case-study data quality | not applicable |
| equity evidence status | old exploratory |
| limitations | use Phase 6 values only after Phase 8 gating |
| claim grade | unsupported |
| allowed wording | "legacy values motivated the rebuild but are not final evidence" |
| forbidden wording | "29.1% improvement proves superiority"; "35.0% gain proves matched-coverage superiority" |
| recommended manuscript location | Remove from final abstract/intro/conclusion; mention only as provenance if needed |

### C-GAMMA-01

| field | value |
|---|---|
| proposed manuscript claim | Gamma is post-hoc welfare accounting unless implementation changes; it is not a Pareto frontier. |
| claim type | Utility / welfare diagnostic |
| evidence source | `00_CURRENT_EXPERIMENT_MAP.md`; current experiments; Phase 9 table plan |
| evidence package | legacy diagnostic only |
| evidence family | diagnostic / limitation |
| methods compared | FullModel welfare accounting across gamma values |
| seed / scale / row counts | legacy rows only |
| completed / failed / timeout / blocked | not formal Phase 6 evidence |
| key metrics | served share invariant, vkm/served invariant, welfare changes only |
| direction of result | contradicted as Pareto frontier |
| uncertainty evidence | implementation/provenance audit |
| paired hypothesis test status | not implemented |
| denominator involved | served share and vkm/served are invariant |
| coverage-confounding risk | high if called frontier |
| case-study data quality | not case-based |
| equity evidence status | none |
| limitations | gamma does not enter routing or acceptance decisions |
| claim grade | unsupported |
| allowed wording | "post-hoc welfare sensitivity diagnostic" |
| forbidden wording | "coverage-efficiency Pareto frontier" |
| recommended manuscript location | Appendix/supplement limitation or remove |

### C-DEP-01

| field | value |
|---|---|
| proposed manuscript claim | Deployment readiness and direct citywide policy validation are not supported. |
| claim type | Policy / deployment |
| evidence source | current abstract/policy/conclusion; Phase 7 claim boundary |
| evidence package | Phase 7 limitation evidence |
| evidence family | limitation |
| methods compared | none |
| seed / scale / row counts | no observed deployment data |
| completed / failed / timeout / blocked | real/semi-real validation blocked by missing data |
| key metrics | data availability and calibration status |
| direction of result | unsupported |
| uncertainty evidence | direct data audit |
| paired hypothesis test status | not applicable |
| denominator involved | none |
| coverage-confounding risk | not relevant |
| case-study data quality | synthetic only |
| equity evidence status | exploratory only |
| limitations | no observed operations |
| claim grade | unsupported |
| allowed wording | "future real-world validation is required before deployment guidance" |
| forbidden wording | "deployment-ready"; "validated in Chinese city operations"; "direct citywide policy recommendations" |
| recommended manuscript location | Limitations/future work only |

### C-WEIGHT-01

| field | value |
|---|---|
| proposed manuscript claim | Legacy weight sensitivity cannot prove robust efficiency gains; any retained weight/objective discussion must be diagnostic and provenance-bounded. |
| claim type | Robustness / policy |
| evidence source | `00_CURRENT_EXPERIMENT_MAP.md`; current experiments; Phase 9 table plan |
| evidence package | legacy diagnostic only |
| evidence family | diagnostic / limitation |
| methods compared | legacy FullModel vs DoorToDoor weight configurations |
| seed / scale / row counts | legacy 3-seed setup, not Phase 6 formal package |
| completed / failed / timeout / blocked | not formal evidence |
| key metrics | legacy vkm/trip formula/provenance mismatch |
| direction of result | unsupported as robust claim |
| uncertainty evidence | insufficient and formula mismatch |
| paired hypothesis test status | not implemented |
| denominator involved | old vkm/trip ambiguous |
| coverage-confounding risk | high |
| case-study data quality | not case-based |
| equity evidence status | not empirical |
| limitations | not part of formal Phase 6 package |
| claim grade | unsupported |
| allowed wording | "legacy weight sensitivity is diagnostic provenance only unless rebuilt" |
| forbidden wording | "robust efficiency across objective weights"; "policy-relevant objective weights prove transferability" |
| recommended manuscript location | Remove from main claims; appendix limitation if retained |

## Grade Counts

- Strong claims: 4 (C-EFF-01, C-COV-01, C-REP-01, C-LIM-01)
- Moderate claims: 4 (C-FWK-01, C-ACC-01, C-MC-01, C-FAS-01)
- Exploratory claims: 7 (C-UTIL-01, C-MP-01, C-FLEET-01, C-EQ-01, C-ALG-01, C-CASE-01, C-POL-01)
- Unsupported claims: 5 (C-NOV-01 broad wording, C-LEG-01, C-GAMMA-01, C-DEP-01, C-WEIGHT-01)

## Claim Gate Decision

Phase 8 passes if manuscript refresh uses only the allowed wording in this
matrix or weaker wording, carries every listed limitation, and deletes or
rewrites every unsupported claim.

