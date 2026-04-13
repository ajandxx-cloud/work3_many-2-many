# ROADMAP: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

**Project:** Many-to-Many DRT with Bidirectional Meeting Point Assignment and Passenger Choice
**Target:** Transportation Research Part A: Policy and Practice
**Granularity:** Standard (6 phases)
**Coverage:** 47/47 v1 requirements mapped

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
**Goal**: A complete, submission-ready draft of the full paper exists — all sections from abstract to conclusion are written in academic English at TR Part A standard, with references formatted
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
- [ ] 05-01-PLAN.md — Front matter: abstract.tex + intro.tex (PAPER-01, PAPER-02)
- [ ] 05-02-PLAN.md — Literature review: literature.tex (PAPER-03)
- [ ] 05-03-PLAN.md — Model + algorithm: model.tex + algorithm.tex (PAPER-04, PAPER-05, PAPER-06)
- [ ] 05-04-PLAN.md — Experiments + policy: experiments.tex + policy.tex (PAPER-07, PAPER-08)
- [ ] 05-05-PLAN.md — Back matter + assembly: conclusion.tex + references.bib + main.tex (PAPER-09, PAPER-10)

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
- [x] 06-01-PLAN.md — Conceptual diagrams (Wave 1): FIG-01 system overview, FIG-02 three-layer architecture, FIG-03 algorithm flowchart
- [x] 06-02-PLAN.md — Data-driven charts (Wave 1): FIG-04 baseline comparison bar charts, FIG-05 sensitivity line plots
- [x] 06-03-PLAN.md — Policy map + LaTeX integration (Wave 2): FIG-06 policy deployment map, replace all 6 figure placeholders in paper sections

### Phase 8: Pareto Experiment & New Metrics (Reviewer Revision)
**Goal**: The paper presents a coverage--efficiency Pareto frontier that directly addresses the reviewer's concern that efficiency gains are partly driven by endogenous coverage reduction
**Depends on**: Phase 3, Phase 6 (uses FullModel infrastructure and figure style)
**Requirements**: REV-05, REV-06, REV-07, REV-08
**Success Criteria** (what must be TRUE):
  1. Gamma sweep [0, 5, 10, 20, 50, 100] runs FullModel at scale=200 with 3 seeds and produces pareto_gamma_sweep.csv
  2. Social welfare W = sum_r[z_r*U_rb* - (1-z_r)*Gamma] is computed for each run and reported in the CSV
  3. fig07_pareto.pdf and fig07_pareto.png are produced at 300 dpi showing the Pareto frontier with one labeled point per Gamma value
  4. experiments.tex Section 5.1 defines W, Section 5.2 addresses the endogeneity concern, and Section 5.5 presents the frontier with Table 2 and fig07
**Plans:** 2/2 plans complete

Plans:
- [x] 08-01-PLAN.md — Gamma sweep experiment: extend metrics.py + variants.py, write pareto_sweep.py runner, write fig07_pareto.py figure script, execute sweep and generate outputs
- [x] 08-02-PLAN.md — experiments.tex update: add W definition to Section 5.1, reframe Section 5.2 efficiency discussion, add Section 5.5 with Table 2 and fig07 reference

---

## v3.0 — Codex Review Fixes

### v3.0 Phases

- [ ] **Phase 10: Metric Audit & Coverage Comparison** - Recompute vkm/trip with correct denominator throughout all paper artifacts; add matched-coverage experiment and update efficiency narrative
- [ ] **Phase 11: Formalization & Policy Reframing** - Add timing/decision diagram and ALNS objective statement; soften policy thresholds to scenario-specific findings; update reviewer response document

### Phase Details (v3.0)

### Phase 10: Metric Audit & Coverage Comparison
**Goal**: Every efficiency number in the paper uses a consistent, dimensionally correct vkm/trip denominator, and the primary efficiency claim is supported by a matched-coverage comparison that controls for served share
**Depends on**: Phase 8 (uses existing experiment infrastructure and paper sections)
**Requirements**: METRIC-01, METRIC-02, COVER-01, COVER-02
**Success Criteria** (what must be TRUE):
  1. vkm/trip is recomputed as vkm / (n_requests * acceptance_rate) in all tables, the abstract, and the policy section — no table cell uses the old denominator
  2. The three previously inconsistent numbers (abstract: 2383.85 vs 3662.33; main table: 3022 vs 4268; Gamma-sweep: 9.893) are reconciled to a single denominator and the discrepancy is resolved or explicitly explained
  3. A matched-coverage experiment runs DoorToDoor with a rejection penalty calibrated to match FullModel's ~20% served share, and produces a vkm/trip comparison at equal coverage
  4. Section 5.2 narrative uses the matched-coverage result as the primary efficiency claim, and the abstract efficiency sentence is rewritten to reflect this
**Plans**: TBD

### Phase 11: Formalization & Policy Reframing
**Goal**: The coupled decision problem is formally stated with a timing diagram and ALNS objective, and all policy thresholds are reframed as scenario-specific managerial insights rather than general prescriptions; the reviewer response document reflects all v3.0 changes
**Depends on**: Phase 10
**Requirements**: FORM-01, FORM-02, PFRAM-01, PFRAM-02, PFRAM-03
**Success Criteria** (what must be TRUE):
  1. A timing/decision diagram (figure or table) shows the Layer 1-3 sequence with explicit decision variables, information flows, and the point at which Bernoulli sampling occurs
  2. A mathematical statement in the paper specifies what ALNS minimizes online — the surrogate objective, the role of Bernoulli sampling, and how the rejection penalty enters decisions
  3. The 1000m walking threshold finding is presented with explicit caveats on generalizability (population, city type, network density) and is not stated as a universal prescription
  4. The 15-vehicle fleet ratio finding is presented with explicit caveats and framed as a scenario-specific managerial insight
  5. response_to_reviewers.tex is updated to reflect all v3.0 changes (metric correction, matched-coverage result, formalization additions, softened thresholds)
**Plans**: TBD

---

## Progress Table

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Problem Formulation & Model Structure | 4/4 | Complete | 2026-04-11 |
| 2. Algorithm Development & Python Implementation | 5/5 | Complete | 2026-04-12 |
| 3. Numerical Experiments | 3/3 | Complete | 2026-04-12 |
| 4. Policy Analysis & Sensitivity Analysis | 3/3 | Complete | 2026-04-12 |
| 5. Paper Writing | 0/5 | In progress | - |
| 6. Academic Figures & Visualization | 3/3 | Complete | 2026-04-12 |
| 8. Pareto Experiment & New Metrics | 2/2 | Complete | 2026-04-12 |
| 10. Metric Audit & Coverage Comparison | 1/2 | In Progress|  |
| 11. Formalization & Policy Reframing | 0/? | Not started | - |

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

**Total mapped: 60/60 (47 v1 + 4 reviewer revision + 9 v3.0 requirements)**

---

*Roadmap created: 2026-04-11*
*Last updated: 2026-04-11 — Phase 1 complete (4/4 plans, all requirements PROB-01..05, CHOICE-01..04 verified)*
*Updated: 2026-04-11 — Phase 3 planned (3 plans: 03-01, 03-02, 03-03)*
*Updated: 2026-04-12 — Phase 6 planned (3 plans: 06-01, 06-02, 06-03)*
*Updated: 2026-04-12 — Phase 8 planned (2 plans: 08-01, 08-02) for reviewer revision REV-05..REV-08*
*Updated: 2026-04-13 — v3.0 phases 10-11 added (9 requirements: METRIC-01/02, COVER-01/02, FORM-01/02, PFRAM-01/02/03)*
