# Claims and Risks

**Initialized:** 2026-06-15

## Current Risk Register

| Risk | Severity | Source | Mitigation Phase |
|------|----------|--------|------------------|
| Novelty overclaim around bidirectional meeting points | High | Review note, rebuild brief | Phase 1 |
| Baseline comparison mixes passenger-response assumptions | High | Review note, `experiments/variants.py` | Phase 2 / Phase 4 |
| Main efficiency result is coverage-confounded | High | Review note, manuscript abstract/experiments | Phase 2 / Phase 6 |
| Choice parameters are not empirically calibrated | High | Review note, manuscript choice setup | Phase 3 |
| ALNS quality validation is insufficient | High | Review note, MILP gap table | Phase 4 / Phase 6 |
| MILP formulation scope may be incomplete | High | Review note, codebase concerns | Phase 4 |
| Formal seed count is too low | High | Review note, manuscript experiments | Phase 6 |
| Beijing-inspired scenario may be overread as real evidence | Medium | Review note, README/manuscript | Phase 7 / Phase 9 |
| Gamma sweep is post-hoc, not a Pareto frontier | High | Review note, codebase concerns | Phase 2 / Phase 4 |
| Equity conclusions overinterpret artificial type parameters | Medium | Review note | Phase 3 / Phase 8 |

## Claim Status Policy

- **Strong:** supported by formal paired experiments, calibrated or sensitivity-tested assumptions, reproducible artifacts, and claim-specific controls.
- **Moderate:** supported by formal experiments but with clear limitations or narrower scope.
- **Exploratory:** supported only by pilot/diagnostic/current runs or incomplete controls.
- **Unsupported:** no reproducible evidence or evidence is contradicted by implementation.

## Phase 1 Literature and Novelty Audit

**Status:** Complete for planning, with citation-cleanup risks carried forward.

### Novelty claims approved for later manuscript use

| Claim | Status | Conditions |
|---|---|---|
| Integrated choice-aware dynamic service-design simulation framework for many-to-many DRT | Approved as planning language | Must be supported by Phase 2 method taxonomy, Phase 6 formal evidence, and Phase 8 claim gate before final manuscript use. |
| Bidirectional pickup/dropoff meeting-point candidate sets are part of the proposed framework | Approved as framework description | Must not be framed as individually first without exact citation support. |
| Simulated binary-logit acceptance with outside option is part of the framework | Approved as framework description | Phase 3 must rebuild calibration/sensitivity before behavioral claims become strong. |
| Rolling-horizon dispatch is part of the framework | Approved as framework description | Phase 4 must validate ALNS and exact-diagnostic scope. |

### Claims forbidden until new evidence appears

| Claim | Reason | Responsible phase |
|---|---|---|
| Existing work assigns meeting points only on the pickup side | Contradicted or narrowed by Fielbaum et al. (2021) and external metadata for Cortenbach et al. (2024). | Phase 9 may replace with precise citation-backed wording. |
| This is the first bidirectional meeting-point DRT paper | Too broad relative to prior ridepooling and DARPmp literature. | Phase 8 only if a narrower scoped claim is verified. |
| No prior work considers dropoff walking | Contradicted by Fielbaum et al. (2021). | Do not use. |
| Current 29.1% vkm/trip improvement proves superiority | Coverage-confounded and exploratory per Phase 0. | Phase 2 and Phase 6. |
| Beijing-inspired results support real city policy recommendations | Current data are synthetic/illustrative. | Phase 7 and Phase 9. |
| Gamma sweep is a Pareto frontier | Gamma is post-hoc and does not affect routing or acceptance. | Phase 2 / Phase 4 if redesigned. |

### Unresolved literature blockers

| Blocker | Residual risk | Responsible phase |
|---|---|---|
| Cortenbach et al. (2024) full-text mechanism needs final verification. | Exact DARPmp scope cannot be summarized confidently from local manuscript text alone. | Phase 9 |
| Local bibliography metadata for Cortenbach et al. (2024) and Wu et al. (2025) appears incorrect. | Manuscript references may be wrong if copied forward unchanged. | Phase 9 |
| Review-note raw file was not readable under the expected path in this checkout. | Phase 0 extracted risks, but raw provenance remains fragile. | Phase 10 |

### Venue-positioning recommendation

Use TR-E-level rigor as the planning bar. The manuscript should emphasize operational evidence, fair behavioral comparisons, metric denominator discipline, reproducibility, and conditional claims. TR-A-style policy language should remain secondary and simulation-based unless Phase 7 supplies stronger case-study evidence.

## Phase 7 Case-Study Boundary

**Status:** Complete - 2026-06-16

Phase 7 found no real or semi-real case-study data in the current repository.
The available Beijing-labeled material is a Beijing-inspired synthetic scenario:
generated OD, generated regular-grid meeting points, simulated morning-peak
request times, simulation-range passenger preferences, and an experimental fleet
setting.

Allowed claim scope:

- Bounded illustrative scenario.
- Scenario-transfer discussion.
- Limitation-level or exploratory external-validity note for Phase 8.

Forbidden claim scope:

- Real Beijing validation.
- Semi-real Beijing case-study evidence.
- Direct city policy recommendations.
- Deployment readiness or universal superiority claims.

Phase 8 must treat Phase 7 as limitation-level or exploratory evidence only.

### Requirement status and residual risk

| Requirement | Phase 1 status | Residual risk |
|---|---|---|
| POS-01 | Complete for planning | Prior work already narrows pickup/dropoff walking novelty; final manuscript wording needs full-text citation cleanup. |
| POS-02 | Complete for planning | Integrated-framework language is approved, but final strength depends on Phase 8. |
| POS-03 | Complete for planning | TR-E-level planning bar is resolved; final venue choice remains a manuscript strategy decision. |

---
*Last updated: 2026-06-16 after Phase 7 bounded synthetic case closure*
