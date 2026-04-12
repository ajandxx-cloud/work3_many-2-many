# Requirements: Work 3 — v2.0 Reviewer Revision

**Defined:** 2026-04-12
**Milestone:** v2.0 — Reviewer Revision
**Core Value:** Address all CRITICAL and MAJOR reviewer findings (GPT-5.2 review, Round 2) to bring the paper from 6/10 to 7–8/10 and achieve TR Part A submission-ready status.

## v2 Requirements

### Choice Model Fix (CRITICAL)

- [ ] **REV-01**: Replace multi-bundle MNL in Layer 1 with binary logit acceptance: P_accept(b*) = exp(U_b*) / (exp(U_0) + exp(U_b*)), where b* is the single offered bundle
- [ ] **REV-02**: Update choice.py to implement binary logit; remove unused multi-bundle probability computation
- [ ] **REV-03**: Update model.tex (Section 4) to reflect binary logit formulation with clear single-offer mechanism definition
- [ ] **REV-04**: Update algorithm.tex (Section 6) pseudocode to show binary logit acceptance step explicitly

### Coverage–Efficiency Pareto Frontier (MAJOR)

- [ ] **REV-05**: Implement Pareto experiment: sweep rejection penalty Gamma over [0, 5, 10, 20, 50, 100] to generate (served share, vkm/served-trip) tradeoff curve for FullModel
- [ ] **REV-06**: Add social welfare metric W = sum_r [z_r * U_rb* - (1-z_r) * Gamma] as a headline metric alongside vkm/served-trip
- [ ] **REV-07**: Add Pareto frontier figure (fig07_pareto.pdf/png) to figures/
- [ ] **REV-08**: Update experiments.tex to present Pareto frontier and social welfare metric; reframe efficiency discussion

### MILP Benchmark Clarification (MAJOR)

- [ ] **REV-09**: Clarify in algorithm.tex that MILP solves deterministic routing of a fixed accepted set (ex-post benchmark): given realized z_r from ALNS run, solve optimal vehicle routing for that accepted set
- [ ] **REV-10**: Add MILP vs ALNS optimality gap table for small instances (n=20, 30 passengers) in experiments.tex

### Objective Weight Policy Interpretation (MAJOR)

- [ ] **REV-11**: Add VOT mapping table to policy.tex: monetize alpha weights using Chinese urban VOT literature (walking: ~0.5 CNY/min, waiting: ~1.0 CNY/min, IVT: ~0.3 CNY/min)
- [ ] **REV-12**: Add weight sensitivity table to experiments.tex: show that qualitative conclusions (bidirectional reduces vkm/served-trip) hold across 3 weight configurations (efficiency-focused, equity-focused, balanced)

### Parameter Plausibility (MINOR)

- [ ] **REV-13**: Add footnote or table in model.tex benchmarking implied VOT from beta parameters against Chinese DRT/transit literature ranges (e.g., Shao et al. 2017, Li et al. 2020)

## Out of Scope (v2.0)

| Feature | Reason |
|---------|--------|
| New algorithm development | v2.0 is a paper revision, not a new algorithm |
| Real data validation | Deferred to future work (acknowledged in conclusion) |
| Latent consideration set MNL | Binary logit is cleaner and sufficient; latent set requires additional behavioral assumptions |
| New experiment scenarios | Existing synthetic + Beijing scenarios sufficient; Pareto sweep uses same infrastructure |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| REV-01 | Phase 7 — Choice Model & Algorithm Fix | Pending |
| REV-02 | Phase 7 — Choice Model & Algorithm Fix | Pending |
| REV-03 | Phase 7 — Choice Model & Algorithm Fix | Pending |
| REV-04 | Phase 7 — Choice Model & Algorithm Fix | Pending |
| REV-05 | Phase 8 — Pareto Experiment & New Metrics | Pending |
| REV-06 | Phase 8 — Pareto Experiment & New Metrics | Pending |
| REV-07 | Phase 8 — Pareto Experiment & New Metrics | Pending |
| REV-08 | Phase 8 — Pareto Experiment & New Metrics | Pending |
| REV-09 | Phase 9 — Paper Section Updates | Pending |
| REV-10 | Phase 9 — Paper Section Updates | Pending |
| REV-11 | Phase 9 — Paper Section Updates | Pending |
| REV-12 | Phase 9 — Paper Section Updates | Pending |
| REV-13 | Phase 9 — Paper Section Updates | Pending |

**Coverage:**
- v2 requirements: 13 total
- Mapped to phases: 13
- Unmapped: 0 ✓

---
*Requirements defined: 2026-04-12 — v2.0 reviewer revision*
