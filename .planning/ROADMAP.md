# ROADMAP: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

**Project:** Many-to-Many DRT with Bidirectional Meeting Point Assignment and Passenger Choice
**Target:** Transportation Research Part A: Policy and Practice
**Granularity:** Standard (6 phases)
**Coverage:** 47/47 v1 requirements mapped; 73/73 total (v1–v5.0); 33/33 v6.0 requirements mapped (v6.0)

---

## Phases

- [x] **Phase 1: Problem Formulation & Model Structure** - Define the many-to-many DRT problem, notation, constraints, and three-layer coupled model with MNL passenger choice
- [x] **Phase 2: Algorithm Development & Python Implementation** - Build exact MILP benchmark and large-scale rolling horizon + ALNS heuristic; implement and validate in Python
- [x] **Phase 3: Numerical Experiments** - Run synthetic and semi-realistic Chinese city experiments; compare all baselines and ablations; collect performance metrics (completed 2026-04-12)
- [x] **Phase 4: Policy Analysis & Sensitivity Analysis** - Conduct sensitivity sweeps and equity analysis; derive actionable policy recommendations for TR Part A
 (completed 2026-04-12)
- [x] **Phase 5: Paper Writing** - Write all paper sections (abstract through conclusion) in submission-ready form (completed 2026-04-12)
- [x] **Phase 6: Academic Figures & Visualization** - Produce all publication-quality figures (system diagrams, flowcharts, result charts, policy maps)
 (completed 2026-04-12)

---

## Phase Details

### Phase 1: Problem Formulation & Model Structure
**Goal**: The mathematical foundation of the paper is complete — problem is precisely defined, notation is fixed, all constraints are specified, and the three-layer coupled model with MNL passenger choice is fully formalized on paper
**Depends on**: Nothing (first phase)
**Requirements**: PROB-01, PROB-02, PROB-03, PROB-04, PROB-05, CHOICE-01, CHOICE-02, CHOICE-03, CHOICE-04
**Success Criteria** (what must be TRUE):
  1. The many-to-many DRT problem with bidirectional meeting point sets (M_r^P, M_r^D) is formally defined with all notation consistent and unambiguous
  2. The service offer bundle b = (m_r^P, m_r^D, τ_r, p_r) and online decision vector are written out with full mathematical precision
  3. All constraints (capacity, time windows, ride time, walking radius, precedence) are enumerated and each has a corresponding mathematical expression
  4. The MNL utility function with outside option and at least 2-3 passenger types is fully specified with parameter definitions
  5. The three-layer coupled model (service generation → passenger response → dynamic dispatch) is documented in a self-contained model writeup that can be handed directly to the algorithm phase
**Plans:** 4 plans

Plans:
- [x] 01-01-PLAN.md — Notation table (notation.tex) and problem definition (problem-definition.tex): network, M_r^P/M_r^D sets, service offer bundle, objective, decision vector
- [x] 01-02-PLAN.md — Constraints formalization (constraints.tex): capacity, time windows, ride time, walking radius, precedence, route consistency
- [x] 01-03-PLAN.md — MNL passenger choice model (choice-model.tex): utility function, outside option, three passenger types with β profiles, choice probability
- [x] 01-04-PLAN.md — Three-layer model assembly (three-layer.tex + model.tex): integrate all fragments into compilable self-contained model document

### Phase 2: Algorithm Development & Python Implementation
**Goal**: Both the exact MILP benchmark and the large-scale rolling horizon + ALNS heuristic are implemented in Python, tested on small instances, and the heuristic meets the response-time requirement
**Depends on**: Phase 1
**Requirements**: EXACT-01, EXACT-02, EXACT-03, EXACT-04, HEUR-01, HEUR-02, HEUR-03, HEUR-04, HEUR-05, HEUR-06
**Success Criteria** (what must be TRUE):
  1. The MILP formulation solves instances of up to 30-50 passengers and 5-8 vehicles using Gurobi/CPLEX and reports optimality gap and solve time
  2. The candidate generation module produces top-k pickup and dropoff candidates filtered by walking radius for any given request
  3. The online insertion evaluator correctly checks feasibility and computes incremental cost for all (m^P, m^D, vehicle, position) combinations
  4. The rolling horizon ALNS loop runs with configurable window H and time step Δ, and all five destroy/repair operators execute without error
  5. Average decision time per request is below 1 second on large-scale instances (100+ requests, 10+ vehicles) in a timed benchmark run
**Plans:** 5 plans

Plans:
- [x] 02-01-PLAN.md — Project scaffold + data types (pyproject.toml, types.py, choice.py)
- [x] 02-02-PLAN.md — Candidate generation + feasibility checker (candidate.py, feasibility.py)
- [x] 02-03-PLAN.md — Online insertion evaluator (insertion.py)
- [x] 02-04-PLAN.md — MILP formulation with Gurobi (milp.py)
- [x] 02-05-PLAN.md — ALNS rolling horizon (alns.py)

### Phase 3: Numerical Experiments
**Goal**: All experiment results are produced — synthetic and semi-realistic scenarios are run, all four model variants and two ablations are compared, and the full performance metric table is populated
**Depends on**: Phase 2
**Requirements**: EXP-01, EXP-02, EXP-03, EXP-04, EXP-05, EXP-06, EXP-07, EXP-08, EXP-09
**Success Criteria** (what must be TRUE):
  1. Synthetic experiments run across the full range (100-500 requests, 10-30 vehicles) and produce reproducible results with a fixed random seed
  2. The semi-realistic Chinese city scenario (suburban/low-density district) is configured and produces results comparable in scale to the synthetic case
  3. All four model variants (door-to-door, single-sided, bidirectional no-choice, full model) and both ablations (no rolling horizon, no passenger choice) produce complete metric tables
  4. All nine performance metrics (acceptance rate, vehicle-km, waiting time avg/95th, walking distance, IVT, detour ratio, fairness index, CPU time) are computed and recorded for every variant
  5. The full model shows measurable improvement over all baselines on at least acceptance rate and vehicle-km, confirming the core thesis
**Plans:** 3/3 plans complete

Plans:
- [x] 03-01-PLAN.md — Experiment infrastructure: config constants, synthetic + Beijing scenario generators, 9-metric computation module
- [x] 03-02-PLAN.md — Model variants: 6 runnable classes (DoorToDoor, SingleSidedPickup, BidirectionalNoChoice, FullModel, AblationNoRollingHorizon, AblationNoChoice)
- [x] 03-03-PLAN.md — Run experiments and collect results: runner.py orchestration, synthetic_results.csv, beijing_results.csv, metrics_table.csv

### Phase 4: Policy Analysis & Sensitivity Analysis
**Goal**: The TR Part A policy contribution is complete — sensitivity sweeps across demand density, walking tolerance, and fleet size are done, equity analysis across passenger types is documented, and concrete policy recommendations for Chinese city DRT deployment are written
**Depends on**: Phase 3
**Requirements**: POLICY-01, POLICY-02, POLICY-03, POLICY-04, POLICY-05, POLICY-06
**Success Criteria** (what must be TRUE):
  1. Sensitivity analysis across demand density levels shows a clear relationship between density and the benefit of bidirectional meeting point assignment
  2. Sensitivity analysis across walking tolerance thresholds shows how system performance degrades or improves as tolerance changes
  3. Fleet size sensitivity analysis produces a service quality vs. fleet size tradeoff curve
  4. Equity analysis compares service quality distribution across at least two passenger types (price-sensitive vs. time-sensitive) and identifies any systematic disadvantage
  5. At least three concrete, actionable policy recommendations for Chinese city DRT operators are written in plain language, covering when and where to deploy bidirectional DRT
**Plans:** 3/3 plans complete

Plans:
- [x] 04-01-PLAN.md — Walking tolerance sweep (ρ ∈ [200,1000]m) + fleet size sweep + city tier comparison
- [x] 04-02-PLAN.md — Equity analysis: per-type acceptance rates, Gini coefficient
- [x] 04-03-PLAN.md — Policy recommendations document (5 structured recommendations)

### Phase 5: Paper Writing
**Goal**: A complete, submission-ready draft of the full paper exists -- all sections from abstract to conclusion are written in academic English at TR Part A standard, with references formatted
**Depends on**: Phase 1, Phase 2, Phase 3, Phase 4
**Requirements**: PAPER-01, PAPER-02, PAPER-03, PAPER-04, PAPER-05, PAPER-06, PAPER-07, PAPER-08, PAPER-09, PAPER-10
**Success Criteria** (what must be TRUE):
  1. Abstract is written within 250 words and covers motivation, method, key results, and policy implication
  2. Introduction clearly states the research gap and lists 3-4 specific contributions that differentiate Work 3 from Work 1/2 and from Cortenbach et al. (2024)
  3. Model and algorithm sections are self-contained and match the Phase 1 formulation and Phase 2 implementation exactly (no notation drift)
  4. Experiments and policy sections present results in narrative form with all tables and figure placeholders in place
  5. Reference list contains 50-80 citations formatted consistently, covering DARP/DRT, meeting points, passenger choice, and dynamic scheduling literature
**Plans:** 5 plans

Plans:
- [x] 05-01-PLAN.md -- Front matter: abstract.tex + intro.tex (PAPER-01, PAPER-02)
- [x] 05-02-PLAN.md -- Literature review: literature.tex (PAPER-03)
- [x] 05-03-PLAN.md -- Model + algorithm: model.tex + algorithm.tex (PAPER-04, PAPER-05, PAPER-06)
- [x] 05-04-PLAN.md -- Experiments + policy: experiments.tex + policy.tex (PAPER-07, PAPER-08)
- [x] 05-05-PLAN.md -- Back matter + assembly: conclusion.tex + references.bib + main.tex (PAPER-09, PAPER-10)

### Phase 6: Academic Figures & Visualization
**Goal**: All six publication-quality figures are produced in Python/matplotlib at journal resolution, match the paper narrative, and are export-ready for TR Part A submission
**Depends on**: Phase 3, Phase 4, Phase 5
**Requirements**: FIG-01, FIG-02, FIG-03, FIG-04, FIG-05, FIG-06
**Success Criteria** (what must be TRUE):
  1. System overview diagram clearly shows the many-to-many DRT structure with bidirectional meeting points, vehicle routes, and passenger walking legs
  2. Three-layer model architecture diagram matches the Phase 1 model structure and is readable at single-column journal width
  3. Algorithm flowchart covers the full online insertion + rolling horizon + ALNS loop with decision branches labeled
  4. Experiment result charts (bar/line) show all baseline comparisons with error bars or confidence intervals where applicable
  5. Sensitivity heatmaps and policy benefit map are generated at 300 dpi and saved as PDF/EPS for journal submission
**Plans:** 3/3 plans complete

Plans:
- [x] 06-01-PLAN.md -- Conceptual diagrams (Wave 1): FIG-01 system overview, FIG-02 three-layer architecture, FIG-03 algorithm flowchart
- [x] 06-02-PLAN.md -- Data-driven charts (Wave 1): FIG-04 baseline comparison bar charts, FIG-05 sensitivity line plots
- [x] 06-03-PLAN.md -- Policy map + LaTeX integration (Wave 2): FIG-06 policy deployment map, replace all 6 figure placeholders in paper sections

### Phase 8: Pareto Experiment & New Metrics (Reviewer Revision)
**Goal**: The paper presents a coverage--efficiency Pareto frontier that directly addresses the reviewer concern that efficiency gains are partly driven by endogenous coverage reduction
**Depends on**: Phase 3, Phase 6 (uses FullModel infrastructure and figure style)
**Requirements**: REV-05, REV-06, REV-07, REV-08
**Success Criteria** (what must be TRUE):
  1. Gamma sweep [0, 5, 10, 20, 50, 100] runs FullModel at scale=200 with 3 seeds and produces pareto_gamma_sweep.csv
  2. Social welfare W = sum_r[z_r*U_rb* - (1-z_r)*Gamma] is computed for each run and reported in the CSV
  3. fig07_pareto.pdf and fig07_pareto.png are produced at 300 dpi showing the Pareto frontier with one labeled point per Gamma value
  4. experiments.tex Section 5.1 defines W, Section 5.2 addresses the endogeneity concern, and Section 5.5 presents the frontier with Table 2 and fig07
**Plans:** 2/2 plans complete

Plans:
- [x] 08-01-PLAN.md -- Gamma sweep experiment: extend metrics.py + variants.py, write pareto_sweep.py runner, write fig07_pareto.py figure script, execute sweep and generate outputs
- [x] 08-02-PLAN.md -- experiments.tex update: add W definition to Section 5.1, reframe Section 5.2 efficiency discussion, add Section 5.5 with Table 2 and fig07 reference

---

## v3.0 -- Codex Review Fixes (Complete)

### v3.0 Phases

- [x] **Phase 10: Metric Audit & Coverage Comparison** - Recompute vkm/trip with correct denominator throughout all paper artifacts; add matched-coverage experiment and update efficiency narrative
- [x] **Phase 11: Formalization & Policy Reframing** - Add timing/decision diagram and ALNS objective statement; soften policy thresholds to scenario-specific findings; update reviewer response document

---

## v4.0 -- GPT-5 Review Fixes

### v4.0 Phases

- [x] **Phase 12: Endogenous Matched-Coverage Experiment** - Implement DoorToDoorCapped variant with acceptance cap + re-routing; run experiment at matched served share; update Section 5.2 with endogenous comparison as primary claim (completed 2026-04-13)
- [x] **Phase 13: Paper Fixes & Literature Update** - Fix old numbers in intro/conclusion; add behavioral consistency materials (units table, worked example, commitment assumption); add Fielbaum et al. (2021) to literature; add confidence intervals to Table 1 (completed 2026-04-13)

### Phase Details (v3.0 -- Complete)

### Phase 10: Metric Audit & Coverage Comparison (Complete)
**Goal**: Every efficiency number in the paper uses a consistent, dimensionally correct vkm/trip denominator, and the primary efficiency claim is supported by a matched-coverage comparison that controls for served share
**Requirements**: METRIC-01, METRIC-02, COVER-01, COVER-02
**Plans**: 2/2 complete

### Phase 11: Formalization & Policy Reframing (Complete)
**Goal**: The coupled decision problem is formally stated with a timing diagram and ALNS objective, and all policy thresholds are reframed as scenario-specific managerial insights rather than general prescriptions
**Requirements**: FORM-01, FORM-02, PFRAM-01, PFRAM-02, PFRAM-03
**Plans**: 2/2 complete

---

### Phase Details (v4.0)

### Phase 12: Endogenous Matched-Coverage Experiment
**Goal**: The primary efficiency claim is supported by an endogenous matched-coverage comparison -- DoorToDoor re-routed with an acceptance cap so served share matches FullModel at ~23.5%, giving a fair vehicle-routing comparison at equal coverage
**Depends on**: Phase 10-11 (uses existing experiment infrastructure)
**Requirements**: COMP-01, COMP-02, COMP-03
**Success Criteria** (what must be TRUE):
  1. DoorToDoorCapped variant is implemented: DoorToDoor ALNS with a served-share cap; once cap is reached, all subsequent requests are rejected without route insertion
  2. Experiment runs for seeds 42/43/44 at n=200, 15 vehicles and produces CSV with served_share, vkm, vkm/trip for DoorToDoorCapped
  3. Mean served_share of DoorToDoorCapped is within +/-3pp of FullModel mean served_share (~23.5%)
  4. Section 5.2 is updated to present the endogenous result as the primary claim; post-hoc 74.3% is retained as a supplementary lower-bound footnote
**Plans**: 2 plans

Plans:
- [x] 12-01-PLAN.md -- DoorToDoorCapped variant + endogenous experiment runner (COMP-01, COMP-02)
- [x] 12-02-PLAN.md -- Section 5.2 paper update with endogenous result as primary claim (COMP-03)

### Phase 13: Paper Fixes & Literature Update
**Goal**: All old numbers are corrected throughout the paper, behavioral consistency materials are added, the missing reference is integrated, and Table 1 has confidence intervals
**Depends on**: Phase 12 (uses endogenous comparison numbers for Section 5.2 update)
**Requirements**: BEHAV-01, BEHAV-02, BEHAV-03, TEXT-01, TEXT-02, TEXT-03, LIT-01, LIT-02, ROB-01, ROB-02
**Success Criteria** (what must be TRUE):
  1. "2383.85 vs 3662.33" and "-34.9%" do not appear anywhere in the paper (grep confirms)
  2. A units/variables table exists in the paper (or appendix) with time in seconds/minutes, walk in meters, fare in CNY
  3. A worked utility example appears in the choice model section with explicit numbers
  4. A commitment assumption paragraph appears in the algorithm section
  5. Fielbaum et al. (2021) appears in references.bib and is cited in Section 2.2
  6. Table 1 has +/- notation for at least acceptance rate, vkm, and vkm/trip
**Plans**: 3 plans

Plans:
- [x] 13-01-PLAN.md -- Fix old numbers in intro.tex, conclusion.tex, abstract.tex (TEXT-01, TEXT-02, TEXT-03)
- [x] 13-02-PLAN.md -- Add notation table, worked utility example, commitment assumption (BEHAV-01, BEHAV-02, BEHAV-03)
- [x] 13-03-PLAN.md -- Fielbaum citation in Section 2.2, Table 1 +/- notation, 3-seed note (LIT-01, LIT-02, ROB-01, ROB-02)

---

## v5.0 -- Code Review Fixes & Submission Prep

### v5.0 Phases

- [x] **Phase 14: Paper & Response Letter Fixes** - Fix numeric inconsistencies in paper (Gini, cap target, weight-sensitivity table); update response_to_reviewers.tex with current numbers; remove pre-submission development artifacts (completed 2026-04-13)
- [x] **Phase 15: Code Reproducibility & Robustness** - Replace non-deterministic hash seed with SHA-256; add stop ordering warning, tolerance failure warning, empty-seeds guard, and unassigned deduplication (completed 2026-04-13)

### Phases (v6.0)

- [ ] **Phase 16: Choice Model Unification** - Remove mu_0=5.0, fix beta references, rename MNL→binary logit throughout paper
- [ ] **Phase 17: Objective Function Reconciliation** - Align paper with pre-filter-then-route code; remove Gamma from Section 3; fix ALNS description
- [ ] **Phase 18: Code Fixes & Prep for Rerun** - ALNS iterations 5→50, detour ratio guard, unit scaling documentation
- [ ] **Phase 19: Experiment Rerun** - Regenerate all CSVs, Beijing results, data-dependent figures
- [ ] **Phase 20: Table & Numerical Updates** - Update all 6 tables from new CSVs, unify baselines, fix detour ratio
- [ ] **Phase 21: MILP Section Revision** - Downgrade from "exact benchmark" to "ex-post routing diagnostic"
- [ ] **Phase 22: Beijing Results & Policy Repairs** - Add Beijing table, scope down policy claims to scenario-specific
- [ ] **Phase 23: Literature, Notation & Formatting** - Fix literature table, unify notation/units, fix spelling
- [ ] **Phase 24: Response Letter & Final Integration** - Write point-by-point response, cross-check, final PDF

### Phase Details (v5.0)

### Phase 14: Paper & Response Letter Fixes
**Goal**: Every number in the paper and response letter is internally consistent and matches the actual experiment output; all development-only annotations and comment blocks are removed before submission
**Depends on**: Phase 13 (paper state after v4.0 fixes)
**Requirements**: NUM-01, NUM-02, NUM-03, RESP-01, RESP-02, CLEAN-01, CLEAN-02, CLEAN-03
**Success Criteria** (what must be TRUE):
  1. The Gini coefficient appears as 0.1216 in all three locations (policy.tex, experiments.tex, abstract.tex) -- no instance of 0.122 remains
  2. The cap target percentage is the same value in code default (cap_share), paper paragraph text, table caption, and response letter FIX-02 section
  3. The weight-sensitivity table column headers correctly describe the denominator used (vkm/trip if per-trip, vkm if raw), and all cell values are consistent with that denominator
  4. response_to_reviewers.tex FIX-02 section cites 11.1 vs 17.1 vkm/trip (35.0%) as the primary endogenous result, with the post-hoc 74.3% demoted to a footnote reference
  5. response_to_reviewers.tex R1 body contains 15.1 vkm/trip and 21.3 vkm/trip, not the old 3022/4268 values
  6. The METRIC AUDIT comment block (experiments.tex lines 1-13), the "(provisional)" annotation (model.tex), and the internal cross-reference to subsec:vot-mapping are all removed or corrected
**Plans**: 2 plans

Plans:
- [x] 14-01-PLAN.md -- Numeric fixes: Gini in policy.tex, cap target in response letter FIX-02, verify weight-sensitivity table (NUM-01, NUM-02, NUM-03)
- [x] 14-02-PLAN.md -- Response letter + cleanup: rewrite FIX-02, fix R1 body, remove METRIC AUDIT block, remove provisional annotation, fix cross-reference (RESP-01, RESP-02, CLEAN-01, CLEAN-02, CLEAN-03)

### Phase 15: Code Reproducibility & Robustness
**Goal**: The experiment codebase produces bit-identical results across processes and platforms, and all silent failure modes are replaced with explicit warnings or errors that surface problems immediately
**Depends on**: Phase 12 (DoorToDoorCapped and endogenous experiment infrastructure)
**Requirements**: CODE-01, ROB-01, ROB-02, ROB-03, ROB-04
**Success Criteria** (what must be TRUE):
  1. Running the same experiment twice in different Python processes produces identical CSV output (SHA-256 seed replaces hash(request.id))
  2. A trip with pickup_time >= dropoff_time triggers a logged warning rather than silently returning 0.0 from max(0.0, ...)
  3. When DoorToDoorCapped mean served share is outside +/-3pp of target, a warnings.warn call is raised (not just a print statement)
  4. Calling endogenous_matched_coverage_experiment with an empty seeds list raises ValueError immediately, not a ZeroDivisionError later
  5. state.unassigned contains no duplicate request IDs after DoorToDoor._solve and DoorToDoorCapped._solve return
**Plans**: TBD

---

## Progress Table

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Problem Formulation & Model Structure | 4/4 | Complete | 2026-04-11 |
| 2. Algorithm Development & Python Implementation | 5/5 | Complete | 2026-04-12 |
| 3. Numerical Experiments | 3/3 | Complete | 2026-04-12 |
| 4. Policy Analysis & Sensitivity Analysis | 3/3 | Complete | 2026-04-12 |
| 5. Paper Writing | 5/5 | Complete | 2026-04-12 |
| 6. Academic Figures & Visualization | 3/3 | Complete | 2026-04-12 |
| 8. Pareto Experiment & New Metrics | 2/2 | Complete | 2026-04-13 |
| 10. Metric Audit & Coverage Comparison | 2/2 | Complete | 2026-04-13 |
| 11. Formalization & Policy Reframing | 2/2 | Complete | 2026-04-13 |
| 12. Endogenous Matched-Coverage Experiment | 2/2 | Complete | 2026-04-13 |
| 13. Paper Fixes & Literature Update | 3/3 | Complete | 2026-04-13 |
| 14. Paper & Response Letter Fixes | 2/2 | Complete   | 2026-04-13 |
| 15. Code Reproducibility & Robustness | 1/1 | Complete | 2026-04-13 |

---

## Coverage Map

| Requirement | Phase | Category |
|-------------|-------|----------|
| PROB-01 | Phase 1 | Problem Formulation |
| PROB-02 | Phase 1 | Problem Formulation |
| PROB-03 | Phase 1 | Problem Formulation |
| PROB-04 | Phase 1 | Problem Formulation |
| PROB-05 | Phase 1 | Problem Formulation |
| CHOICE-01 | Phase 1 | Passenger Choice |
| CHOICE-02 | Phase 1 | Passenger Choice |
| CHOICE-03 | Phase 1 | Passenger Choice |
| CHOICE-04 | Phase 1 | Passenger Choice |
| EXACT-01 | Phase 2 | Exact Algorithm |
| EXACT-02 | Phase 2 | Exact Algorithm |
| EXACT-03 | Phase 2 | Exact Algorithm |
| EXACT-04 | Phase 2 | Exact Algorithm |
| HEUR-01 | Phase 2 | Heuristic Algorithm |
| HEUR-02 | Phase 2 | Heuristic Algorithm |
| HEUR-03 | Phase 2 | Heuristic Algorithm |
| HEUR-04 | Phase 2 | Heuristic Algorithm |
| HEUR-05 | Phase 2 | Heuristic Algorithm |
| HEUR-06 | Phase 2 | Heuristic Algorithm |
| EXP-01 | Phase 3 | Experiments |
| EXP-02 | Phase 3 | Experiments |
| EXP-03 | Phase 3 | Experiments |
| EXP-04 | Phase 3 | Experiments |
| EXP-05 | Phase 3 | Experiments |
| EXP-06 | Phase 3 | Experiments |
| EXP-07 | Phase 3 | Experiments |
| EXP-08 | Phase 3 | Experiments |
| EXP-09 | Phase 3 | Experiments |
| POLICY-01 | Phase 4 | Policy Analysis |
| POLICY-02 | Phase 4 | Policy Analysis |
| POLICY-03 | Phase 4 | Policy Analysis |
| POLICY-04 | Phase 4 | Policy Analysis |
| POLICY-05 | Phase 4 | Policy Analysis |
| POLICY-06 | Phase 4 | Policy Analysis |
| PAPER-01 | Phase 5 | Paper Writing |
| PAPER-02 | Phase 5 | Paper Writing |
| PAPER-03 | Phase 5 | Paper Writing |
| PAPER-04 | Phase 5 | Paper Writing |
| PAPER-05 | Phase 5 | Paper Writing |
| PAPER-06 | Phase 5 | Paper Writing |
| PAPER-07 | Phase 5 | Paper Writing |
| PAPER-08 | Phase 5 | Paper Writing |
| PAPER-09 | Phase 5 | Paper Writing |
| PAPER-10 | Phase 5 | Paper Writing |
| FIG-01 | Phase 6 | Figures |
| FIG-02 | Phase 6 | Figures |
| FIG-03 | Phase 6 | Figures |
| FIG-04 | Phase 6 | Figures |
| FIG-05 | Phase 6 | Figures |
| FIG-06 | Phase 6 | Figures |
| REV-05 | Phase 8 | Reviewer Revision |
| REV-06 | Phase 8 | Reviewer Revision |
| REV-07 | Phase 8 | Reviewer Revision |
| REV-08 | Phase 8 | Reviewer Revision |
| METRIC-01 | Phase 10 | Codex Review Fixes |
| METRIC-02 | Phase 10 | Codex Review Fixes |
| COVER-01 | Phase 10 | Codex Review Fixes |
| COVER-02 | Phase 10 | Codex Review Fixes |
| FORM-01 | Phase 11 | Codex Review Fixes |
| FORM-02 | Phase 11 | Codex Review Fixes |
| PFRAM-01 | Phase 11 | Codex Review Fixes |
| PFRAM-02 | Phase 11 | Codex Review Fixes |
| PFRAM-03 | Phase 11 | Codex Review Fixes |
| COMP-01 | Phase 12 | GPT-5 Review Fixes |
| COMP-02 | Phase 12 | GPT-5 Review Fixes |
| COMP-03 | Phase 12 | GPT-5 Review Fixes |
| BEHAV-01 | Phase 13 | GPT-5 Review Fixes |
| BEHAV-02 | Phase 13 | GPT-5 Review Fixes |
| BEHAV-03 | Phase 13 | GPT-5 Review Fixes |
| TEXT-01 | Phase 13 | GPT-5 Review Fixes |
| TEXT-02 | Phase 13 | GPT-5 Review Fixes |
| TEXT-03 | Phase 13 | GPT-5 Review Fixes |
| LIT-01 | Phase 13 | GPT-5 Review Fixes |
| LIT-02 | Phase 13 | GPT-5 Review Fixes |
| ROB-01 (v4) | Phase 13 | GPT-5 Review Fixes |
| ROB-02 (v4) | Phase 13 | GPT-5 Review Fixes |
| NUM-01 | Phase 14 | v5.0 Paper Fixes |
| NUM-02 | Phase 14 | v5.0 Paper Fixes |
| NUM-03 | Phase 14 | v5.0 Paper Fixes |
| RESP-01 | Phase 14 | v5.0 Paper Fixes |
| RESP-02 | Phase 14 | v5.0 Paper Fixes |
| CLEAN-01 | Phase 14 | v5.0 Paper Fixes |
| CLEAN-02 | Phase 14 | v5.0 Paper Fixes |
| CLEAN-03 | Phase 14 | v5.0 Paper Fixes |
| CODE-01 | Phase 15 | v5.0 Code Fixes |
| ROB-01 | Phase 15 | v5.0 Code Fixes |
| ROB-02 | Phase 15 | v5.0 Code Fixes |
| ROB-03 | Phase 15 | v5.0 Code Fixes |
| ROB-04 | Phase 15 | v5.0 Code Fixes |

**Total mapped: 73/73 (60 v1-v4 + 13 v5.0 requirements)**

---

*Roadmap created: 2026-04-11*
*Last updated: 2026-04-11 -- Phase 1 complete (4/4 plans, all requirements PROB-01..05, CHOICE-01..04 verified)*
*Updated: 2026-04-11 -- Phase 3 planned (3 plans: 03-01, 03-02, 03-03)*
*Updated: 2026-04-12 -- Phase 6 planned (3 plans: 06-01, 06-02, 06-03)*
*Updated: 2026-04-12 -- Phase 8 planned (2 plans: 08-01, 08-02) for reviewer revision REV-05..REV-08*
*Updated: 2026-04-13 -- v3.0 phases 10-11 added (9 requirements: METRIC-01/02, COVER-01/02, FORM-01/02, PFRAM-01/02/03)*
*Updated: 2026-04-13 -- v5.0 phases 14-15 added (13 requirements: NUM-01..03, RESP-01..02, CODE-01, ROB-01..04, CLEAN-01..03)*
