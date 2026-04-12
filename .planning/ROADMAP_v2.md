# ROADMAP: Work 3 — v2.0 Reviewer Revision

**Milestone:** v2.0 — Reviewer Revision
**Goal:** Address all CRITICAL and MAJOR reviewer findings (GPT-5.2 review, Round 2) to bring the paper from 6/10 to 7–8/10 and achieve TR Part A submission-ready status.
**Granularity:** Standard
**Coverage:** 13/13 REV requirements mapped

---

## Phases

- [ ] **Phase 7: Choice Model & Algorithm Fix** — Replace multi-bundle MNL with binary logit in code and paper
- [ ] **Phase 8: Pareto Experiment & New Metrics** — Implement Gamma sweep, add social welfare metric, generate fig07_pareto
- [ ] **Phase 9: Paper Section Updates** — Clarify MILP benchmark, add VOT table, weight sensitivity, parameter plausibility

---

## Phase Details

### Phase 7: Choice Model & Algorithm Fix
**Goal**: The paper and code consistently implement binary logit single-offer acceptance, eliminating the behavioral inconsistency flagged as CRITICAL by the reviewer.
**Depends on**: v1.0 artifacts (choice.py, model.tex, algorithm.tex)
**Requirements**: REV-01, REV-02, REV-03, REV-04
**Success Criteria** (what must be TRUE):
  1. choice.py computes P_accept(b*) = exp(U_b*) / (exp(U_0) + exp(U_b*)) and all multi-bundle probability code is removed
  2. model.tex Section 4 states the single-offer mechanism and binary logit formula with clear notation
  3. algorithm.tex pseudocode shows the binary logit acceptance step explicitly at the correct position in the dispatch loop
  4. Running the existing experiment suite with updated choice.py produces valid (non-NaN, non-error) results
**Plans**: 2 plans
Plans:
- [ ] 07-01-PLAN.md — Replace choice_probability with binary logit accept_probability in choice.py
- [ ] 07-02-PLAN.md — Rewrite model.tex Section 4 and fill in algorithm.tex Algorithm 1 pseudocode

### Phase 8: Pareto Experiment & New Metrics
**Goal**: The paper presents a coverage–efficiency Pareto frontier that directly addresses the reviewer's concern that efficiency gains are partly driven by endogenous coverage reduction.
**Depends on**: Phase 7 (binary logit must be in place before running new experiments)
**Requirements**: REV-05, REV-06, REV-07, REV-08
**Success Criteria** (what must be TRUE):
  1. Gamma sweep over [0, 5, 10, 20, 50, 100] runs without error and produces a (served share, vkm/served-trip) data table for FullModel
  2. Social welfare metric W = sum_r [z_r * U_rb* - (1-z_r) * Gamma] is computed and reported alongside vkm/served-trip in the results
  3. fig07_pareto.pdf and fig07_pareto.png exist in figures/ and show a clearly labeled Pareto frontier curve
  4. experiments.tex presents the Pareto frontier figure and social welfare metric with narrative that reframes the efficiency discussion
**Plans**: TBD

### Phase 9: Paper Section Updates
**Goal**: All MAJOR and MINOR paper-level reviewer concerns are resolved: MILP benchmark scope is unambiguous, objective weights have policy-grounded VOT interpretation, and parameter values are benchmarked against literature.
**Depends on**: Phase 8 (optimality gap table requires Pareto/experiment run data; weight sensitivity uses same experiment infrastructure)
**Requirements**: REV-09, REV-10, REV-11, REV-12, REV-13
**Success Criteria** (what must be TRUE):
  1. algorithm.tex states explicitly that MILP solves deterministic routing of the realized accepted set from an ALNS run (ex-post benchmark), not a stochastic problem
  2. experiments.tex contains an MILP vs ALNS optimality gap table for n=20 and n=30 passenger instances
  3. policy.tex contains a VOT mapping table with alpha weight monetization using Chinese urban VOT values (walking ~0.5 CNY/min, waiting ~1.0 CNY/min, IVT ~0.3 CNY/min)
  4. experiments.tex contains a weight sensitivity table showing qualitative conclusions hold across efficiency-focused, equity-focused, and balanced weight configurations
  5. model.tex contains a footnote or table benchmarking implied VOT from beta parameters against Shao et al. (2017) and Li et al. (2020) ranges
**Plans**: TBD

---

## Progress Table

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 7. Choice Model & Algorithm Fix | 0/2 | Not started | - |
| 8. Pareto Experiment & New Metrics | 0/? | Not started | - |
| 9. Paper Section Updates | 0/? | Not started | - |

---

## Coverage Map

| Requirement | Phase | Description |
|-------------|-------|-------------|
| REV-01 | Phase 7 | Binary logit formula definition |
| REV-02 | Phase 7 | Update choice.py |
| REV-03 | Phase 7 | Update model.tex Section 4 |
| REV-04 | Phase 7 | Update algorithm.tex pseudocode |
| REV-05 | Phase 8 | Implement Gamma sweep experiment |
| REV-06 | Phase 8 | Add social welfare metric W |
| REV-07 | Phase 8 | Generate fig07_pareto |
| REV-08 | Phase 8 | Update experiments.tex with Pareto + W |
| REV-09 | Phase 9 | Clarify MILP benchmark scope in algorithm.tex |
| REV-10 | Phase 9 | Add MILP vs ALNS optimality gap table |
| REV-11 | Phase 9 | Add VOT mapping table to policy.tex |
| REV-12 | Phase 9 | Add weight sensitivity table to experiments.tex |
| REV-13 | Phase 9 | Add parameter plausibility footnote to model.tex |

**Mapped: 13/13 — no orphans**

---

*Roadmap created: 2026-04-12 — v2.0 reviewer revision (phases 7–9)*
*Updated: 2026-04-12 — Phase 7 planned (2 plans)*
