---
gsd_state_version: 1.0
milestone: v1.0
milestone_name: milestone
status: completed
stopped_at: Completed 08-pareto-experiment-new-metrics-01-PLAN.md
last_updated: "2026-04-12T16:09:09.452Z"
last_activity: 2026-04-12
progress:
  total_phases: 7
  completed_phases: 6
  total_plans: 25
  completed_plans: 24
  percent: 96
---

# STATE: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

## Project Reference

**Core value:** Demonstrate that bidirectional meeting point assignment with passenger choice significantly improves DRT efficiency and equity, with actionable policy implications for TR Part A.
**Target journal:** Transportation Research Part A: Policy and Practice
**Current focus:** Phase 8 — pareto-experiment-new-metrics

---

## Current Position

Phase: 8 (pareto-experiment-new-metrics) — NEXT
**Active phase:** Phase 8
**Status:** Phase 7 complete; advancing to Phase 8
**Last activity:** 2026-04-12

**v2.0 revision scope (from GPT-5.2 review, Round 2):**

- ~~CRITICAL: Replace multi-bundle MNL with binary logit~~ ✓ DONE (Phase 7)
- MAJOR: Add coverage–efficiency Pareto frontier experiment
- MAJOR: Clarify MILP benchmark scope under stochastic acceptance
- MAJOR: Add objective weight VOT mapping + sensitivity table
- MINOR: Benchmark implied VOT against Chinese transit literature

**Progress:**

[██████████] 96%
Phase 7 [██████████] 100% (Choice Model & Algorithm Fix) ✓
Phase 8 [          ] 0% (Pareto Experiment & New Metrics)
Phase 9 [          ] 0% (Paper Section Updates)
Overall v2.0 [███       ] 33%

---

## Performance Metrics (v1.0 final)

| Metric | Value |
|--------|-------|
| v1.0 phases total | 6 |
| v1.0 phases complete | 6 |
| v1.0 requirements total | 47 |
| v1.0 requirements complete | 47 |
| v1.0 plans written | 23 |
| v1.0 plans complete | 23 |
| Codex review Round 1 | 5/10 (weak reject) |
| Codex review Round 2 | 6/10 (weak accept) |
| Phase 3 key result | FullModel vkm/acceptance = 2383.85 vs DoorToDoor 3662.33 (-34.9% efficiency gain) |
| Phase 4 key result | Equity Gini=0.1216; walk_sensitive=20.2%, time_sensitive=14.4%; 5 policy recommendations |
| Phase 5 key result | 8 section files + 59 BibTeX entries; full paper draft complete |
| Phase 6 key result | 6 publication-quality figures (PDF + PNG, matplotlib) |
| Phase 7 key result | Binary logit accept_probability in choice.py; model.tex §4.2 + algorithm.tex Algorithm 1 updated; REV-01..04 PASS |
| Phase 08-pareto-experiment-new-metrics P01 | 3 | 3 tasks | 7 files |

## Accumulated Context

### Key Decisions Logged

| Decision | Rationale | Phase |
|----------|-----------|-------|
| Target TR Part A not TR Part C | Policy framing differentiates from Work 1; TR Part A accepts optimization with strong policy angle | Pre-phase |
| Fix price, don't optimize it | Avoid overlap with Work 1/2; keep Work 3 focused on bidirectional spatial assignment | Pre-phase |
| Rolling horizon + ALNS as main heuristic | Standard in dynamic DRT literature 2024-2025; matches dissertation framework | Pre-phase |
| Simulation-based validation | Standard for DARP; real data hard to obtain; consistent with Work 1 approach | Pre-phase |
| Gurobi solver for MILP | Industry standard, best performance for DARP-scale MILPs | Phase 2 |
| src/drt/ single package | Clean module separation; feasibility.py reused by MILP and ALNS | Phase 2 |
| pytest for unit tests | Catches bugs early; required for HEUR-06 response-time benchmark | Phase 2 |
| Local PRNG random.Random(seed) in generators | Prevents cross-contamination between generator calls; essential for multi-seed experiments | Phase 3 |
| O(n log n) sorted-array Gini formula | Equivalent to pairwise O(n^2) formula but faster at n=500 scale | Phase 3 |
| Beijing MPs follow 9x9 grid formula (1875m spacing) | Plan formula gives 1875m not 500m; formula is authoritative over prose description | Phase 3 |
| Binary logit for single-offer acceptance | Reviewer CRITICAL: multi-bundle MNL behaviorally inconsistent with single-offer mechanism | Phase 7 |
| Pareto frontier over rejection cost Gamma | Reviewer MAJOR: efficiency gains partly driven by endogenous coverage reduction | v2.0 |

### Prior Work Context

- Work 1 (many-to-one dynamic pricing, DRPO framework): complete, submitted to TR Part C
- Work 2 (service menu design, assortment optimization): working paper
- Work 3 natural extension: bidirectional spatial service menu (pickup + dropoff) in many-to-many scenario
- Key reference: Cortenbach et al. (2024, TR Part C) — DARPmp, single-sided, Tabu Search (direct predecessor)
- Key reference: Wu et al. (2025, TR Part E) — dynamic DRT with rolling horizon (algorithm precedent)

### Todos

- [x] Update choice.py to binary logit (done Phase 7)
- [x] Update model.tex §4.2 binary logit + algorithm.tex Algorithm 1 (done Phase 7)
- [ ] Run Pareto sweep experiment (Gamma ∈ {0,5,10,20,50,100}) and generate fig07_pareto
- [ ] Add social welfare metric W = sum_r [z_r * U_rb* - (1-z_r) * Gamma]
- [ ] Update experiments.tex with Pareto frontier + W narrative
- [ ] Clarify MILP benchmark scope (algorithm.tex) + optimality gap table
- [ ] Add VOT mapping table (policy.tex) + weight sensitivity table (experiments.tex)
- [ ] Add parameter plausibility footnote (model.tex)

### Blockers

None currently.

### Notes

- Dissertation timeline: Work 3 planned 2026.09–2027.04 per BUAA schedule
- Supervisor: Prof. Liu Tianliang
- Language: English (academic paper)
- v2.0 phases 7–9 depend on v1.0 artifacts (paper sections, Python code, figures)

---

## Session Continuity

**Last session:** 2026-04-12T16:09:09.450Z
**Stopped at:** Completed 08-pareto-experiment-new-metrics-01-PLAN.md
**Next action:** `/gsd-plan-phase 8` — plan Phase 8 (Pareto Experiment & New Metrics)

---

*State initialized: 2026-04-11*
*Updated: 2026-04-12 — Phase 7 complete (REV-01..04 PASS); advancing to Phase 8*
