# Requirements: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

**Defined:** 2026-04-11
**Updated:** 2026-04-13 (v5.0 milestone)
**Core Value:** Demonstrate that bidirectional meeting point assignment with passenger choice significantly improves DRT efficiency and equity, with actionable policy implications for TR Part A.

---

## v5.0 Requirements (Active)

### Paper Numeric Fixes

- [ ] **NUM-01**: Fix Gini coefficient inconsistency — change `policy.tex` value from 0.122 to 0.1216 to match `experiments.tex` and `abstract.tex`
- [ ] **NUM-02**: Reconcile cap target — verify actual FullModel mean served share from experiment output, then align code default (`cap_share=0.235`), paper paragraph text, table caption, and post-hoc footnote to the same figure
- [ ] **NUM-03**: Fix weight-sensitivity table — verify denominator used for `tab:weight-sensitivity`; if raw vkm, rename column headers from "vkm/trip" to "vkm"; if intended as vkm/trip, recompute and update numbers

### Response Letter Updates

- [ ] **RESP-01**: Update `response_to_reviewers.tex` FIX-02 section — reflect endogenous result (11.1 vs 17.1 vkm/trip, 35.0%) as primary claim; correct "23.5%" to actual cap target; demote post-hoc 74.3% to footnote reference
- [ ] **RESP-02**: Update `response_to_reviewers.tex` R1 response body — replace "3{,}022\,vkm per unit acceptance rate" and "4{,}268" with "15.1\,vkm/trip" and "21.3\,vkm/trip"

### Code Reproducibility

- [ ] **CODE-01**: Replace `hash(request.id)` with SHA-256 deterministic seed in `experiments/variants.py` — add `_stable_seed(request_id: str) -> int` helper using `hashlib.sha256`; update all call sites

### Code Robustness

- [ ] **ROB-01**: Add stop ordering warning in `_find_stop_info` — warn when `pickup_time >= dropoff_time` for a completed trip instead of silently masking via `max(0.0, ...)`
- [ ] **ROB-02**: Make tolerance failure non-silent in `endogenous_matched_coverage.py` — replace print-only warning with `warnings.warn(..., stacklevel=2)` when DoorToDoorCapped mean served share is outside ±3pp of target
- [ ] **ROB-03**: Add empty seeds guard in `endogenous_matched_coverage_experiment` — raise `ValueError("seeds list must be non-empty")` at function entry to prevent ZeroDivisionError
- [ ] **ROB-04**: Deduplicate `state.unassigned` in `DoorToDoor._solve` and `DoorToDoorCapped._solve` before returning state

### Pre-submission Cleanup

- [ ] **CLEAN-01**: Remove audit comment block from `paper/sections/experiments.tex` lines 1-13 (METRIC AUDIT development notes)
- [ ] **CLEAN-02**: Remove "(provisional --- to be confirmed against Work~1/2 calibration before Phase~3)" annotation from `paper/sections/model.tex` lines 268-269
- [ ] **CLEAN-03**: Fix cross-reference in `paper/sections/model.tex` footnote — replace `Section~\ref{subsec:vot-mapping}` with `Section~\ref{sec:policy}` for robustness against future restructuring

---

## Validated Requirements (v1.0-v4.0)

### v1.0 (Problem Formulation & Algorithm)
- [x] PROB-01..05: Many-to-many DRT problem with bidirectional meeting point sets formally defined
- [x] CHOICE-01..04: MNL utility function, outside option, three passenger types, binary logit acceptance
- [x] EXACT-01..04: MILP formulation with Gurobi, ex-post benchmark role
- [x] HEUR-01..06: Rolling horizon ALNS with 5 operators, <1s per request
- [x] EXP-01..09: Synthetic + semi-realistic experiments, 6 variants, 9 metrics
- [x] POLICY-01..06: Sensitivity sweeps, equity analysis, 5 policy recommendations
- [x] PAPER-01..10: Full paper written in academic English
- [x] FIG-01..06: All 6 publication-quality figures produced

### v2.0 (Reviewer Revision)
- [x] REV-01..04: Binary logit replacing multi-bundle MNL; single-offer mechanism justified
- [x] REV-05..08: Gamma sweep Pareto frontier; MILP labeled as ex-post routing lower bound; VOT mapping

### v3.0 (Codex Review Fixes)
- [x] METRIC-01/02: vkm/trip corrected to vkm/(n x alpha); all tables/abstract/policy updated
- [x] COVER-01/02: Post-hoc matched-coverage experiment (10.9 vs 42.3, 74.3%); Section 5.2 updated
- [x] FORM-01/02: Timing/decision diagram (tab:timing-diagram); ALNS online objective (eq:alns-objective)
- [x] PFRAM-01..03: Generalizability caveats for R1 and R2; reviewer response v3.0 section

### v4.0 (GPT-5 Review Fixes)
- [x] COMP-01..03: DoorToDoorCapped endogenous comparison; Section 5.2 updated with 11.1 vs 17.1 vkm/trip (35.0%)
- [x] BEHAV-01..03: Notation table, worked utility example, commitment assumption paragraph
- [x] TEXT-01..03: Old numbers (2383.85/3662.33/-34.9%) replaced throughout; grep-verified clean
- [x] LIT-01..02: Fielbaum et al. (2021) added to references.bib and cited in Section 2.2
- [x] ROB-01..02: ± std in Table 1; 3-seed justification note with wu2025 citation

---

## Out of Scope

| Feature | Reason |
|---------|--------|
| Pricing as decision variable | Avoid overlap with Work 1/2 |
| Reinforcement learning as main method | Extension discussion only |
| Real GPS/smart card data | Simulation-based standard for DARP |
| TR Part D environmental framing | Wrong journal |
| Multi-bundle MNL with single-offer mechanism | Behaviorally inconsistent (v2.0 decision) |
| Endogenous meeting point placement | Outside scope; future work |

---

## Traceability (v5.0)

| Requirement | Phase | Status |
|-------------|-------|--------|
| NUM-01 | Phase 14 | Pending |
| NUM-02 | Phase 14 | Pending |
| NUM-03 | Phase 14 | Pending |
| RESP-01 | Phase 14 | Pending |
| RESP-02 | Phase 14 | Pending |
| CLEAN-01 | Phase 14 | Pending |
| CLEAN-02 | Phase 14 | Pending |
| CLEAN-03 | Phase 14 | Pending |
| CODE-01 | Phase 15 | Pending |
| ROB-01 | Phase 15 | Pending |
| ROB-02 | Phase 15 | Pending |
| ROB-03 | Phase 15 | Pending |
| ROB-04 | Phase 15 | Pending |

**Coverage:**
- v5.0 requirements: 13 total
- Mapped to phases: 13
- Unmapped: 0 ✓

---
*Requirements defined: 2026-04-11*
*Last updated: 2026-04-13 — v5.0 milestone (code review fixes & submission prep)*
