# ROADMAP: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

**Project:** Many-to-Many DRT with Bidirectional Meeting Point Assignment and Passenger Choice
**Target:** Transportation Research Part A: Policy and Practice
**Granularity:** Standard (6 phases)
**Coverage:** 47/47 v1 requirements mapped

---

## Phases

- [x] **Phase 1: Problem Formulation & Model Structure** - Define the many-to-many DRT problem, notation, constraints, and three-layer coupled model with MNL passenger choice
- [ ] **Phase 2: Algorithm Development & Python Implementation** - Build exact MILP benchmark and large-scale rolling horizon + ALNS heuristic; implement and validate in Python
- [ ] **Phase 3: Numerical Experiments** - Run synthetic and semi-realistic Chinese city experiments; compare all baselines and ablations; collect performance metrics
- [ ] **Phase 4: Policy Analysis & Sensitivity Analysis** - Conduct sensitivity sweeps and equity analysis; derive actionable policy recommendations for TR Part A
- [ ] **Phase 5: Paper Writing** - Write all paper sections (abstract through conclusion) in submission-ready form
- [ ] **Phase 6: Academic Figures & Visualization** - Produce all publication-quality figures (system diagrams, flowcharts, result charts, policy maps)

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
- [ ] 02-01-PLAN.md — Project scaffold + data types (pyproject.toml, types.py, choice.py)
- [ ] 02-02-PLAN.md — Candidate generation + feasibility checker (candidate.py, feasibility.py)
- [ ] 02-03-PLAN.md — Online insertion evaluator (insertion.py)
- [ ] 02-04-PLAN.md — MILP formulation with Gurobi (milp.py)
- [ ] 02-05-PLAN.md — ALNS rolling horizon (alns.py)

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
**Plans**: TBD

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
**Plans**: TBD

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
**Plans**: TBD
**UI hint**: yes

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
**Plans**: TBD
**UI hint**: yes

---

## Progress Table

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Problem Formulation & Model Structure | 4/4 | Complete | 2026-04-11 |
| 2. Algorithm Development & Python Implementation | 0/5 | Planned | - |
| 3. Numerical Experiments | 0/? | Not started | - |
| 4. Policy Analysis & Sensitivity Analysis | 0/? | Not started | - |
| 5. Paper Writing | 0/? | Not started | - |
| 6. Academic Figures & Visualization | 0/? | Not started | - |

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

**Total mapped: 47/47 ✓**

---

*Roadmap created: 2026-04-11*
*Last updated: 2026-04-11 — Phase 1 complete (4/4 plans, all requirements PROB-01..05, CHOICE-01..04 verified)*
