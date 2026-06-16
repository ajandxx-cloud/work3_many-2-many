# Phase 9 Experiment Section Refresh

**Phase:** 09 - Manuscript Restructure for TR Part E
**Refresh date:** 2026-06-16
**Status:** claim-gated experiment plan complete

## Experiment Section Boundary

The experiment section must separate main behavioral evidence, coverage-control
evidence, diagnostics, exploratory equity outputs, illustrative scenario
material, and reproducibility/failure-row reporting. It must not present all
outputs as equal-strength evidence.

Every efficiency statement must name the denominator and report served share or
rejection context. `vkm_per_trip` is forbidden for refreshed manuscript wording.

## Evidence Families

### 1. Main Behavioral Evidence

| Field | Refresh plan |
|---|---|
| Purpose | Test the main behavioral service-design comparison under shared passenger-response assumptions. |
| Methods | DoorToDoor + Choice, SingleSidedPickup + Choice, SingleSidedDropoff + Choice, BidirectionalMP + Choice + RollingHorizon/ALNS. |
| Seed count / row count | 20 paired seeds x 4 request scales x 4 methods = 320 completed rows, no failed/timeout/blocked rows. |
| Metrics | total vehicle-km, vkm per served trip, vkm per original request, served share, behavioral acceptance, choice rejection, feasibility rejection, paired differences, bootstrap CIs. |
| Denominator | Served-trip and original-request vehicle-km denominators must both be shown; served share uses original requests; rejection rates use their defined request/opportunity denominators. |
| Allowed interpretation | Under the tested formal synthetic paired design, BidirectionalMP/FullModel shows lower vehicle-km intensity than door-to-door and single-sided choice baselines. |
| Forbidden interpretation | FullModel is unconditionally superior; bidirectional meeting points dominate all baselines under all metrics; lower vkm proves pure routing superiority. |
| Manuscript placement | Main results section after experiment design and metric protocol. |
| Supports abstract claim? | Yes, only when paired with coverage/acceptance/rejection context. |

### 2. Coverage-Control Evidence

| Field | Refresh plan |
|---|---|
| Purpose | Bound coverage confounding by comparing completed pairs near matched served-share targets. |
| Methods | 06-03 matched-coverage controls comparing FullModel with DoorToDoor, SingleSidedPickup, and SingleSidedDropoff controls. |
| Seed count / row count | 320 durable rows: 305 completed and 15 durable failed FullModel matched rows; 65 aggregate valid pairs per baseline in summaries. |
| Metrics | total vehicle-km, vkm per served trip, vkm per original request, served share, valid-pair count, missing/failed-pair count, full-better share. |
| Denominator | Served and original-request denominators; matched served-share target must be documented. |
| Allowed interpretation | Completed matched-coverage pairs remain consistent with the FullModel efficiency direction. |
| Forbidden interpretation | Matched coverage fully proves equal-coverage superiority or resolves coverage confounding without limitation. |
| Manuscript placement | Robustness/control subsection in main text with full details in appendix/supplement. |
| Supports abstract claim? | Optional, only if the abstract also states the 15 durable failed rows or avoids mentioning matched coverage. |

### 3. Fixed Accepted-Set Routing Diagnostic

| Field | Refresh plan |
|---|---|
| Purpose | Diagnose routing/service-design distance on a common accepted passenger set. |
| Methods | 06-03 fixed accepted-set diagnostic. |
| Seed count / row count | 20 paired seeds x 4 scales x method comparisons = 320 completed rows, no failed rows. |
| Metrics | vkm per served request, vkm per original request, deterministic inserted share, total vehicle-km. |
| Denominator | Served-request denominator for the supported diagnostic; original-request denominator must be shown because it does not support unconditional dominance. |
| Allowed interpretation | Supports a routing/service-design efficiency signal on vkm per served request. |
| Forbidden interpretation | Proves behavioral superiority or unconditional vkm/original advantage. |
| Manuscript placement | Diagnostic subsection or appendix, after main behavioral and matched-coverage evidence. |
| Supports abstract claim? | No. It can support a conclusion caveat or diagnostic note only. |

### 4. Robustness Diagnostics

| Field | Refresh plan |
|---|---|
| Purpose | Screen whether the main vehicle-km direction is consistent across reduced synthetic diagnostic grids. |
| Methods | 06-04 utility sensitivity, walking-radius / meeting-point-density, and fleet-demand stress packages. |
| Seed count / row count | Utility sensitivity: 420 completed rows; walking-radius / MP-density: 180 completed rows; fleet-demand stress: 60 completed rows. |
| Metrics | vkm per served trip, vkm per original request, served share, setting ID, valid-pair count, full-better share. |
| Denominator | Served and original-request denominators must both be named; served share must accompany efficiency. |
| Allowed interpretation | Diagnostics are consistent with the main direction within tested synthetic settings. |
| Forbidden interpretation | Robust under all parameters; universal walking-radius threshold; universal fleet-ratio rule. |
| Manuscript placement | Robustness diagnostics subsection, likely compact main-text summary plus appendix tables. |
| Supports abstract claim? | No headline abstract claim. At most, the abstract may say robustness outputs are bounded diagnostics. |

### 5. Equity / Type-Level Diagnostics

| Field | Refresh plan |
|---|---|
| Purpose | Report modeled passenger-type outcomes and individual-burden distributions without converting them into empirical equity claims. |
| Methods | 06-04 equity type-level outcomes and individual burden distribution. |
| Seed count / row count | 180 type-level rows and 12,000 individual burden rows. |
| Metrics | type-level served share, type-level acceptance, wait, walk, IVT, generalized cost, walking burden, individual burden distributions. |
| Denominator | Type-level request denominators and individual-level distributions; composition effects must be acknowledged. |
| Allowed interpretation | Equity metrics are produced and bounded; modeled type-level and individual-burden patterns can be reported diagnostically. |
| Forbidden interpretation | Strong equity benefits, demographic equity conclusions, or regulator prescriptions. |
| Manuscript placement | Robustness/equity diagnostics plus limitations; detailed burden distributions in appendix/supplement. |
| Supports abstract claim? | No, except as a boundary sentence that equity outputs are diagnostic. |

### 6. Beijing-Inspired Synthetic Illustration

| Field | Refresh plan |
|---|---|
| Purpose | Provide an illustrative scenario-transfer boundary, not external validation. |
| Methods | Phase 7 data audit and legacy `results/beijing_results.csv`; no new Phase 7 experiment. |
| Seed count / row count | Legacy 21 rows, 3 seeds x 7 legacy variants; no Phase 7 formal validation package. |
| Metrics | Legacy served share and vehicle-km denominators if mentioned, plus data-quality attributes. |
| Denominator | Legacy denominators only; do not mix with Phase 6 formal evidence. |
| Allowed interpretation | Beijing-labeled material is a Beijing-inspired synthetic scenario and illustrative transfer check. |
| Forbidden interpretation | Real Beijing case, semi-real validation, direct Beijing policy evidence, deployment readiness. |
| Manuscript placement | Discussion, limitations, appendix/supplement; not headline results. |
| Supports abstract claim? | No strong abstract claim. If mentioned, only as "Beijing-inspired synthetic scenario; real-city validation remains future work." |

### 7. Reproducibility and Failure-Row Reporting

| Field | Refresh plan |
|---|---|
| Purpose | Show that formal Phase 6 evidence packages have durable provenance while preserving Phase 10 final rerun as pending. |
| Methods | Phase 6 raw/processed outputs, manifests, seed/config manifests, validators, denominator checks, failure ledger. |
| Seed count / row count | Phase 6 manifest lists 1,928 rows/artifacts plus 12,000 individual burden rows; 15 durable failed matched rows. |
| Metrics | validator status, schema_drift=false, denominator_validation=passed, completion/failure/timeout/blocked counts. |
| Denominator | Denominator checks must be reported for metric tables; failure-row denominators must not be silently dropped. |
| Allowed interpretation | Phase 6 formal outputs are documented and validated for claim-gate use. |
| Forbidden interpretation | Final reproducibility package is complete; all final manuscript tables and figures can already be regenerated. |
| Manuscript placement | Experimental design/reproducibility note and limitations. |
| Supports abstract claim? | Optional methodological claim only; REP-01 and REP-02 remain Phase 10 pending. |

## Required Section Order

1. Experimental design and service-design variants.
2. Metrics, denominators, paired comparisons, uncertainty, and status rows.
3. Formal main behavioral evidence.
4. Coverage-control evidence.
5. Fixed accepted-set diagnostic.
6. Robustness diagnostics.
7. Equity/type-level diagnostics.
8. Beijing-inspired synthetic illustration.
9. Reproducibility and failure-row reporting.

## Special Required Notes

- 06-02 main behavioral matrix is the primary evidence family.
- 06-03 matched coverage is main/control evidence, but the 15 durable failed
  FullModel rows must be a limitation.
- 06-03 fixed accepted-set is a routing diagnostic and cannot support the
  behavioral headline.
- 06-04 robustness is diagnostic.
- 06-04 equity is exploratory.
- Phase 7 Beijing-inspired synthetic material is illustrative only.

## Metric Language Rules

- Use `total_vehicle_km`, `vkm_per_served_trip`, and
  `vkm_per_original_request`.
- Do not use `vkm_per_trip`.
- Do not report vehicle-km without served share and rejection context.
- Do not collapse choice rejection and feasibility rejection into a generic
  "non-served" bucket when interpreting passenger response.
- Do not mix behavioral, deterministic, diagnostic, and legacy rows in a single
  headline result table.
