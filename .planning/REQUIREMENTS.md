# Requirements: TR_E_Bidirectional_MeetingPoint_DRT_Experiment_Rebuild

**Defined:** 2026-06-15
**Core Value:** Produce reproducible, reviewer-resistant evidence for defensible conditional claims about bidirectional meeting-point DRT.

## v1 Requirements

### Audit

- [x] **AUD-01**: Every current manuscript result is mapped to a script, data file, result artifact, or marked as not reproducible.
- [x] **AUD-02**: Every current manuscript claim is classified as supported, weakly supported, exploratory, unsupported, or contradicted.
- [x] **AUD-03**: Current weaknesses from the review note are translated into explicit risks and phase gates.

### Positioning

- [x] **POS-01**: Literature and novelty audit verifies whether prior DARPmp and ridepooling work already covers pickup/dropoff walking locations.
- [x] **POS-02**: Contribution framing avoids unverified "first" claims and centers the integrated choice-aware dynamic service-design framework.
- [x] **POS-03**: Target-journal positioning conflict between current Part A framing and requested TR-E-level framing is resolved.

### Experiments

- [ ] **EXP-01**: Method definitions separate service design, passenger response, routing algorithm, and diagnostic role.
- [ ] **EXP-02**: Behavioral choice-based comparisons use consistent passenger response assumptions across all service variants.
- [ ] **EXP-03**: Deterministic feasibility/routing diagnostics are reported separately from behavioral comparisons.
- [ ] **EXP-04**: Coverage-confounding controls include unconstrained behavioral, matched-coverage, and fixed accepted-set designs.
- [ ] **EXP-05**: Formal experiments use paired seeds, at least 20 synthetic seeds, saved configs, raw rows, logs, and failure rows.
Formal experiments must be split into main-evidence experiments and supplementary diagnostic experiments. The main-evidence experiment should be small enough to guarantee paired-seed completion and should focus on the central claim: whether bidirectional pickup/dropoff meeting-point service design improves operating efficiency under consistent passenger-response assumptions. Supplementary experiments, including matched coverage, fixed accepted-set routing, utility sensitivity, meeting-point density, fleet-demand stress tests, equity analysis, and ALNS/MILP diagnostics, must be executed as separate subphases. No supplementary result may be used to support a headline claim unless its corresponding subphase passes its own reproducibility and validity gate.


### Metrics

- [ ] **MET-01**: Metric definitions include formulas, units, denominators, and valid value ranges.
- [ ] **MET-02**: Served share, behavioral acceptance rate, feasibility rejection rate, choice rejection rate, and deterministic inserted share are distinct.
- [ ] **MET-03**: Main tables report total vkm, vkm per served trip, vkm per original request, and served share together.
- [ ] **MET-04**: Equity metrics include type-level outcomes and, where possible, individual-level burden distributions.

### Choice

- [ ] **CHO-01**: Passenger utility model includes service ASC or equivalent service-attractiveness constant.
- [ ] **CHO-02**: Outside-option utility is explicit and tested through sensitivity analysis.
- [ ] **CHO-03**: Passenger-type parameters are sourced from literature/data or labeled as simulation ranges.
- [ ] **CHO-04**: Utility-component logging explains acceptance outcomes under each parameter setting.

### Algorithms

- [ ] **ALG-01**: Feasibility checks cover capacity, pickup windows, ride time, precedence, walking radius, route-time consistency, and committed nodes.
- [ ] **ALG-02**: ALNS is compared against greedy insertion, no-reoptimization, and exact/MILP diagnostics on fixed accepted sets.
- [ ] **ALG-03**: ALNS convergence diagnostics include objective vs iteration, runtime-quality trade-offs, and operator contribution.
- [ ] **ALG-04**: MILP/exact diagnostic scope is documented honestly and not presented as a full online stochastic benchmark unless implemented as such.

### Claims

- [ ] **CLM-01**: Every final manuscript claim links to formal evidence.
- [ ] **CLM-02**: Claims are graded strong, moderate, exploratory, or unsupported.
- [ ] **CLM-03**: Unsupported claims are removed or rewritten before manuscript restructuring.

### Reproducibility

- [ ] **REP-01**: Reproducibility package records commands, dependencies, configs, seeds, code revision, and result manifests.
- [ ] **REP-02**: Main tables and figures can be regenerated from saved artifacts.
- [ ] **REP-03**: Failed, timeout, and infeasible runs are durable rows with status, error message, runtime, config ID, seed, method, and scenario.

## v2 Requirements

### Case Study

- **CASE-01**: If data are available, add a semi-real case study with real or semi-real OD, road network, and meeting-point data.
- **CASE-02**: If real/semi-real data are unavailable, keep the case as Beijing-inspired synthetic and write limitations accordingly.

### Manuscript

- **MS-01**: Rewrite manuscript sections after formal evidence synthesis.
- **MS-02**: Redesign tables and figures after metrics and claims stabilize.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Running new experiments in Phase 0 | Phase 0 is audit-only by the user-provided protocol |
| Treating pilot runs as formal evidence | Formal claims require preregistered paired-seed experiments |
| Calling a post-hoc gamma sweep a Pareto frontier | Gamma currently does not affect routing or acceptance |
| Universal city policy recommendations from synthetic grids | Synthetic scenarios do not establish real city external validity |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| AUD-01 | Phase 0 | Complete |
| AUD-02 | Phase 0 | Complete |
| AUD-03 | Phase 0 | Complete |
| POS-01 | Phase 1 | Complete |
| POS-02 | Phase 1 | Complete |
| POS-03 | Phase 1 | Complete |
| EXP-01 | Phase 2 | Pending |
| EXP-02 | Phase 2 | Pending |
| EXP-03 | Phase 2 | Pending |
| EXP-04 | Phase 2 | Pending |
| EXP-05 | Phase 6 | Pending |
| MET-01 | Phase 2 | Pending |
| MET-02 | Phase 2 | Pending |
| MET-03 | Phase 2 | Pending |
| MET-04 | Phase 8 | Pending |
| CHO-01 | Phase 3 | Pending |
| CHO-02 | Phase 3 | Pending |
| CHO-03 | Phase 3 | Pending |
| CHO-04 | Phase 3 | Pending |
| ALG-01 | Phase 4 | Pending |
| ALG-02 | Phase 4 | Pending |
| ALG-03 | Phase 4 | Pending |
| ALG-04 | Phase 4 | Pending |
| CLM-01 | Phase 8 | Pending |
| CLM-02 | Phase 8 | Pending |
| CLM-03 | Phase 8 | Pending |
| REP-01 | Phase 10 | Pending |
| REP-02 | Phase 10 | Pending |
| REP-03 | Phase 5 | Pending |

**Coverage:**
- v1 requirements: 27 total
- Mapped to phases: 27
- Unmapped: 0

---
*Requirements defined: 2026-06-15*
*Last updated: 2026-06-15 after Phase 0 audit completion*
