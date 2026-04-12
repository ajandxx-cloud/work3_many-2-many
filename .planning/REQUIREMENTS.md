# Requirements: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

**Defined:** 2026-04-11
**Core Value:** Demonstrate that bidirectional meeting point assignment with passenger choice significantly improves DRT efficiency and equity, with actionable policy implications for TR Part A.

## v1 Requirements

### Problem Formulation

- [ ] **PROB-01**: Define many-to-many DRT problem with bidirectional meeting points (pickup set M_r^P + dropoff set M_r^D per request)
- [ ] **PROB-02**: Formalize service offer bundle b = (m_r^P, m_r^D, τ_r, p_r) as the decision unit
- [ ] **PROB-03**: Define system objective: min C^op + C^wait + C^walk + C^IVT + C^rej
- [ ] **PROB-04**: Specify constraints: vehicle capacity, time windows, ride time, route duration, walking radius, precedence (pickup before dropoff)
- [ ] **PROB-05**: Define online decision vector (z_r, m_r^P, m_r^D, v_r, π_r^P, π_r^D) per request

### Passenger Choice Model

- [ ] **CHOICE-01**: MNL utility function U_rb = β1·Walk_rb + β2·Wait_rb + β3·IVT_rb + β4·p_r + ε
- [ ] **CHOICE-02**: Outside option (reject all offers) included in choice set
- [ ] **CHOICE-03**: Passenger heterogeneity: at least 2-3 passenger types (price-sensitive, time-sensitive, walk-sensitive)
- [ ] **CHOICE-04**: Choice probability formula P_rb = exp(U_rb) / (exp(U_r0) + Σ exp(U_rb))

### Small-Scale Exact Algorithm

- [ ] **EXACT-01**: MILP formulation for static snapshot / batch window (small-scale benchmark)
- [ ] **EXACT-02**: Solve instances up to ~30-50 passengers, ~5-8 vehicles using Gurobi/CPLEX
- [ ] **EXACT-03**: Report optimality gap and solve time for benchmark instances
- [ ] **EXACT-04**: Use exact solution as quality benchmark for heuristic validation

### Large-Scale Heuristic Algorithm

- [ ] **HEUR-01**: Candidate generation: for each request, generate top-k pickup candidates and top-k dropoff candidates (walking radius filter)
- [ ] **HEUR-02**: Online insertion evaluation: for each candidate pair (m^P, m^D), enumerate vehicles and insertion positions, compute feasibility + incremental cost
- [ ] **HEUR-03**: Fast feasibility check: constant-time or near-constant-time schedule feasibility test
- [ ] **HEUR-04**: Rolling horizon re-optimization: every Δ minutes, run ALNS on active requests in window [t, t+H]
- [ ] **HEUR-05**: ALNS destroy/repair operators: request reassignment, pickup/dropoff pair swap, insertion position exchange, route segment reconstruction
- [ ] **HEUR-06**: Response time guarantee: average decision time < 1 second per request for large-scale instances

### Numerical Experiments

- [x] **EXP-01**: Synthetic scenario: grid/random network, 100-500 requests, 10-30 vehicles
- [x] **EXP-02**: Semi-realistic case: Chinese city scenario (e.g., suburban area, low-density district)
- [x] **EXP-03**: Baseline 1 — Door-to-door DARP (no meeting points)
- [x] **EXP-04**: Baseline 2 — Single-sided meeting point (pickup flexible, dropoff fixed)
- [x] **EXP-05**: Baseline 3 — Bidirectional meeting points, no passenger choice (system assigns directly)
- [x] **EXP-06**: Full model — Bidirectional meeting points + passenger choice + rolling horizon
- [x] **EXP-07**: Ablation 1 — Remove rolling horizon (myopic insertion only)
- [x] **EXP-08**: Ablation 2 — Remove passenger choice (system assigns best option directly)
- [x] **EXP-09**: Performance metrics: acceptance rate, vehicle-km, avg/95th-pct waiting time, avg walking distance, avg IVT, detour ratio, fairness index, CPU time

### Policy Analysis (TR Part A Requirement)

- [ ] **POLICY-01**: Sensitivity analysis: demand density × bidirectional meeting point benefit
- [ ] **POLICY-02**: Sensitivity analysis: walking tolerance threshold × system performance
- [ ] **POLICY-03**: Sensitivity analysis: fleet size × service quality tradeoff
- [ ] **POLICY-04**: Equity analysis: service quality distribution across passenger types (price-sensitive vs. time-sensitive)
- [x] **POLICY-05**: Policy recommendations: when/where to deploy bidirectional DRT in Chinese cities
- [ ] **POLICY-06**: Comparison of Chinese city tiers (high-density vs. low-density scenarios)

### Paper Writing

- [ ] **PAPER-01**: Abstract (250 words)
- [ ] **PAPER-02**: Introduction: motivation, research gap, contributions (3-4 bullet points)
- [ ] **PAPER-03**: Literature review: DARP/DRT, meeting points, passenger choice in DRT, dynamic scheduling
- [ ] **PAPER-04**: Problem formulation section
- [ ] **PAPER-05**: Model section: three-layer coupled model
- [ ] **PAPER-06**: Algorithm section: exact + heuristic
- [ ] **PAPER-07**: Numerical experiments section
- [ ] **PAPER-08**: Policy implications section (TR Part A requirement)
- [ ] **PAPER-09**: Conclusion
- [ ] **PAPER-10**: References (50-80 citations, consistent with dissertation reference list)

### Academic Figures

- [ ] **FIG-01**: System overview diagram (many-to-many DRT with bidirectional meeting points)
- [ ] **FIG-02**: Three-layer model architecture diagram
- [ ] **FIG-03**: Algorithm flowchart (online insertion + rolling horizon + ALNS)
- [ ] **FIG-04**: Experiment result charts (bar/line charts comparing baselines)
- [ ] **FIG-05**: Sensitivity analysis heatmaps or line plots
- [ ] **FIG-06**: Policy insight visualization (e.g., benefit map by demand density × walking tolerance)

## v2 Requirements

### Extensions (Post-submission)

- **EXT-01**: Anticipatory/multiple-plan enhancement (light lookahead)
- **EXT-02**: Time-dependent travel times
- **EXT-03**: Electric vehicle charging constraints
- **EXT-04**: Real data validation (if Didi/city DRT data becomes available)

## Out of Scope

| Feature | Reason |
|---------|--------|
| Dynamic pricing as core decision | Overlap with Work 1/2; keep price fixed or use Work 1 mechanism |
| Reinforcement learning as main method | Would shift paper to algorithm paper, away from problem innovation |
| TR Part D environmental framing | Not target journal; would require adding carbon/emissions analysis |
| Real GPS/smart card data | Not available; simulation standard for DARP literature |
| Work 4 planning-operations integration | Separate paper; out of scope for Work 3 |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| PROB-01 | Phase 1 — Problem Formulation & Model Structure | Pending |
| PROB-02 | Phase 1 — Problem Formulation & Model Structure | Pending |
| PROB-03 | Phase 1 — Problem Formulation & Model Structure | Pending |
| PROB-04 | Phase 1 — Problem Formulation & Model Structure | Pending |
| PROB-05 | Phase 1 — Problem Formulation & Model Structure | Pending |
| CHOICE-01 | Phase 1 — Problem Formulation & Model Structure | Pending |
| CHOICE-02 | Phase 1 — Problem Formulation & Model Structure | Pending |
| CHOICE-03 | Phase 1 — Problem Formulation & Model Structure | Pending |
| CHOICE-04 | Phase 1 — Problem Formulation & Model Structure | Pending |
| EXACT-01 | Phase 2 — Algorithm Development & Python Implementation | Pending |
| EXACT-02 | Phase 2 — Algorithm Development & Python Implementation | Pending |
| EXACT-03 | Phase 2 — Algorithm Development & Python Implementation | Pending |
| EXACT-04 | Phase 2 — Algorithm Development & Python Implementation | Pending |
| HEUR-01 | Phase 2 — Algorithm Development & Python Implementation | Pending |
| HEUR-02 | Phase 2 — Algorithm Development & Python Implementation | Pending |
| HEUR-03 | Phase 2 — Algorithm Development & Python Implementation | Pending |
| HEUR-04 | Phase 2 — Algorithm Development & Python Implementation | Pending |
| HEUR-05 | Phase 2 — Algorithm Development & Python Implementation | Pending |
| HEUR-06 | Phase 2 — Algorithm Development & Python Implementation | Pending |
| EXP-01 | Phase 3 — Numerical Experiments | Complete |
| EXP-02 | Phase 3 — Numerical Experiments | Complete |
| EXP-03 | Phase 3 — Numerical Experiments | Complete |
| EXP-04 | Phase 3 — Numerical Experiments | Complete |
| EXP-05 | Phase 3 — Numerical Experiments | Complete |
| EXP-06 | Phase 3 — Numerical Experiments | Complete |
| EXP-07 | Phase 3 — Numerical Experiments | Complete |
| EXP-08 | Phase 3 — Numerical Experiments | Complete |
| EXP-09 | Phase 3 — Numerical Experiments | Complete |
| POLICY-01 | Phase 4 — Policy Analysis & Sensitivity Analysis | Pending |
| POLICY-02 | Phase 4 — Policy Analysis & Sensitivity Analysis | Pending |
| POLICY-03 | Phase 4 — Policy Analysis & Sensitivity Analysis | Pending |
| POLICY-04 | Phase 4 — Policy Analysis & Sensitivity Analysis | Pending |
| POLICY-05 | Phase 4 — Policy Analysis & Sensitivity Analysis | Complete |
| POLICY-06 | Phase 4 — Policy Analysis & Sensitivity Analysis | Pending |
| PAPER-01 | Phase 5 — Paper Writing | Pending |
| PAPER-02 | Phase 5 — Paper Writing | Pending |
| PAPER-03 | Phase 5 — Paper Writing | Pending |
| PAPER-04 | Phase 5 — Paper Writing | Pending |
| PAPER-05 | Phase 5 — Paper Writing | Pending |
| PAPER-06 | Phase 5 — Paper Writing | Pending |
| PAPER-07 | Phase 5 — Paper Writing | Pending |
| PAPER-08 | Phase 5 — Paper Writing | Pending |
| PAPER-09 | Phase 5 — Paper Writing | Pending |
| PAPER-10 | Phase 5 — Paper Writing | Pending |
| FIG-01 | Phase 6 — Academic Figures & Visualization | Pending |
| FIG-02 | Phase 6 — Academic Figures & Visualization | Pending |
| FIG-03 | Phase 6 — Academic Figures & Visualization | Pending |
| FIG-04 | Phase 6 — Academic Figures & Visualization | Pending |
| FIG-05 | Phase 6 — Academic Figures & Visualization | Pending |
| FIG-06 | Phase 6 — Academic Figures & Visualization | Pending |

**Coverage:**
- v1 requirements: 47 total
- Mapped to phases: 47
- Unmapped: 0 ✓

---
*Requirements defined: 2026-04-11*
*Last updated: 2026-04-11 — traceability updated after roadmap creation (FIG-01..06 moved to Phase 6)*
