# Requirements: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

**Defined:** 2026-04-11
**Updated:** 2026-04-27 (v6.0 milestone)
**Core Value:** Demonstrate that bidirectional meeting point assignment with passenger choice significantly improves DRT efficiency and equity, with actionable policy implications for TR Part A.

---

## v6.0 Requirements (Active)

### CRITICAL 1: Choice Model Unification

- [ ] **C1-01**: Remove `mu_0=5.0` worked example from model.tex, recalculate acceptance probability with `U_0=0` (matching code `choice.py` line 97)
- [ ] **C1-02**: Delete `beta_price=-0.012`, `beta_time=-0.008`, `beta_walk=-0.015` from experiments.tex (these values do not exist in code); replace with cross-reference to the 12 type-specific beta values in model.tex Eqs. 31-33
- [ ] **C1-03**: Replace "Multinomial Logit (MNL)" with "binary logit" (or "binary logit, special case of MNL") in abstract.tex, intro.tex, model.tex — wherever the single-offer acceptance mechanism is described
- [ ] **C1-04**: Unify outside option: keep `U_0=0` throughout paper (already correct in model.tex Eq. 22 and code); remove all references to "outside option penalty" and `mu_0`

### CRITICAL 2: Objective Function Reconciliation

- [ ] **C2-01**: Remove `C_rej` term with `Gamma` from Section 3 system objective (model.tex Eq. 5); note that Gamma is used only in post-hoc social welfare metric (Section 7.6)
- [ ] **C2-02**: Rewrite ALNS online objective description in algorithm.tex — replace `E[Delta C] = P_accept(b*) * routing_cost` with accurate description of the pre-filter-then-route mechanism (MNL Bernoulli sampling before routing, deterministic cost minimization over accepted set)
- [ ] **C2-03**: Update ALNS design rationale in algorithm.tex — explain that pre-filtering decouples stochastic acceptance from deterministic routing, avoiding the perverse incentive where low P_accept artificially reduces expected routing cost
- [ ] **C2-04**: Fix ALNS iteration count in algorithm.tex: change "100 iterations" to the actual benchmark default of 50

### CRITICAL 3: MILP Benchmark Restatement

- [ ] **C3-01**: Rewrite MILP section in algorithm.tex — rename from "Exact Algorithm: MILP" to "Ex-Post Routing Diagnostic: MILP"; clarify that it solves only the routing subproblem given a fixed accepted set, not the full joint optimization
- [ ] **C3-02**: Replace "exact benchmark" / "provably optimal solutions" with "ex-post routing diagnostic" / "optimal routing for the given accepted set" in algorithm.tex, abstract.tex, intro.tex, conclusion.tex
- [ ] **C3-03**: Remove "small optimality gap" claim in algorithm.tex; honestly characterize gaps of 169.6% (n=20) and 98.8% (n=30) as reflecting the difficulty of online insertion with fixed meeting points
- [ ] **C3-04**: Update Table 7 caption in experiments.tex from "MILP vs. ALNS optimality gap" to "MILP ex-post routing diagnostic"

### CRITICAL 4: Numerical Consistency

- [ ] **C4-01**: Unify acceptance rate baseline across all tables — every table must include a footnote explicitly stating the experimental configuration (scale, seeds, scenario type, gamma value where applicable)
- [ ] **C4-02**: Update all hardcoded numerical values in all 6 tables from regenerated experiment CSVs after Phase 19 rerun
- [ ] **C4-03**: Fix detour ratio: remove the physically impossible 0.76 value for AblationNoChoice; ensure all detour ratios are >= 1.0 after metrics.py fix
- [ ] **C4-04**: Remove or correctly reframe the "74.3% conservative lower bound" (it is larger than the 35.0% primary result, so cannot be a conservative lower bound)
- [ ] **C4-05**: Update all numerical claims in abstract.tex, conclusion.tex, policy.tex to match the regenerated table values

### MAJOR 1: Policy Claim Repairs

- [ ] **M1-01**: Scope "1000m walking threshold" as scenario-specific — dependent on MP spacing, beta parameters, and U_0=0 normalization; move generalizability caveats BEFORE the policy recommendation in policy.tex
- [ ] **M1-02**: Fix "15 vehicles per 100 daily requests" to "15 vehicles per 100 peak-hour requests" in policy.tex, abstract.tex, conclusion.tex (experiment used 200 peak-hour requests over 4-hour horizon)
- [ ] **M1-03**: Add fleet ratio caveats — bind the ratio to time window, demand intensity, vehicle capacity, and service area

### MAJOR 2: Beijing Scenario Results

- [ ] **M2-01**: Add "Beijing Semi-Realistic Scenario Results" subsection to experiments.tex with a complete metrics table (acceptance, vkm/trip, wait, walk, IVT, detour, equity, CPU for all 6 variants)
- [ ] **M2-02**: Reference the Beijing table in abstract and conclusion alongside synthetic results
- [ ] **M2-03**: Either strengthen "calibrated to Chinese suburban conditions" claims with Beijing evidence, or weaken them if Beijing results don't support them

### MAJOR 3: Literature Positioning

- [ ] **M3-01**: Add Fielbaum et al. (2021) to literature positioning table (Tab:literature-gap) — already cited in text but missing from comparison table
- [ ] **M3-02**: Add Alonso-Mora et al. (2017) to literature positioning table as row
- [ ] **M3-03**: Scope all "first formulation" claims to the specific combination: "first to jointly address bidirectional meeting points, binary logit passenger choice with heterogeneous types, and rolling horizon re-optimization for many-to-many DRT"

### MAJOR 4: Notation and Units

- [ ] **M4-01**: Add "Units and Implementation Parameters" table to appendix — unify seconds/minutes/meters/CNY for all symbols
- [ ] **M4-02**: Fix ρ vs ρ^P/ρ^D notation — add both to notation table, note that `ρ = ρ^P = ρ^D` in experiments
- [ ] **M4-03**: Fix Gamma description in notation table: "Rejection penalty in ALNS objective" → "Rejection penalty in social welfare metric (post-hoc only)"
- [ ] **M4-04**: Resolve time unit confusion — model uses minutes for utility, code uses seconds internally, Table 6 reports seconds; add conversion notes where needed

### MINOR: Writing and Formatting

- [ ] **MINOR-01**: Unify to American English spelling throughout all sections (Neighborhood, optimization, modeled, behavior, utilizes)
- [ ] **MINOR-02**: Add missing references to references.bib if not present (McFadden 1974, Train 2009, Santi et al. 2014, Simonetto et al. 2019, Vansteenwegen et al. 2022, Quadrifoglio et al. 2008) and cite them where appropriate
- [ ] **MINOR-03**: Add missing ± std values to tables that claim "mean ± std" in caption but don't report std
- [ ] **MINOR-04**: Fix LaTeX overfull hbox and float-too-large warnings; verify PDF layout

### Code Changes

- [ ] **CODE-01**: Change `alns_iterations` from 5 → 50 in FullModel and AblationNoChoice variants (variants.py)
- [ ] **CODE-02**: Add `max(1.0, ...)` guard on detour ratio computation in metrics.py
- [ ] **CODE-03**: Document unit scaling logic in variants.py `_scale_ptype` and pre-filtering mechanism in `FullModel._solve`
- [ ] **CODE-04**: Rerun all experiments (synthetic + Beijing + MILP gap + Pareto + weight sensitivity + matched coverage + endogenous matched coverage)
- [ ] **CODE-05**: Regenerate data-dependent figures (fig04 baseline comparison, fig05 sensitivity, fig07 Pareto)
- [ ] **CODE-06**: Update response_to_reviewers.tex with point-by-point Round 1 responses

---

## v5.0 Requirements (Validated)

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

## Traceability (v6.0)

| Requirement | Phase | Status |
|-------------|-------|--------|
| C1-01..04 | Phase 16 | Pending |
| C2-01..04 | Phase 17 | Pending |
| C3-01..04 | Phase 21 | Pending |
| C4-01..05 | Phase 20 | Pending |
| M1-01..03 | Phase 22 | Pending |
| M2-01..03 | Phase 22 | Pending |
| M3-01..03 | Phase 23 | Pending |
| M4-01..04 | Phase 23 | Pending |
| MINOR-01..04 | Phase 23 | Pending |
| CODE-01..03 | Phase 18 | Pending |
| CODE-04..05 | Phase 19 | Pending |
| CODE-06 | Phase 24 | Pending |

**Coverage:**
- v6.0 requirements: 33 total
- Mapped to phases: 33
- Unmapped: 0

---
*Requirements defined: 2026-04-11*
*Last updated: 2026-04-27 — v6.0 milestone (Round 1 review revision, 4 CRITICAL + 4 MAJOR)*
