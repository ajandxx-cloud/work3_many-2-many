---
gsd_state_version: 1.0
milestone: v2.0
milestone_name: reviewer-revision
status: in_progress
stopped_at: Roadmap written — phases 7–9 defined, ready to plan Phase 7
last_updated: "2026-04-12T17:00:00.000Z"
progress:
  total_phases: 3
  completed_phases: 0
  total_plans: 0
  completed_plans: 0
  percent: 0
---

# STATE: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

## Project Reference

**Core value:** Demonstrate that bidirectional meeting point assignment with passenger choice significantly improves DRT efficiency and equity, with actionable policy implications for TR Part A.
**Target journal:** Transportation Research Part A: Policy and Practice
**Current focus:** v2.0 — Reviewer Revision (phases 7–9)

---

## Current Position

Phase: Phase 7 — Choice Model & Algorithm Fix (not started)
Plan: —
**Active phase:** Phase 7
**Status:** Roadmap complete — ready to plan Phase 7
**Last activity:** 2026-04-12 — ROADMAP_v2.md written (phases 7–9, 13 requirements mapped)

**v2.0 revision scope (from GPT-5.2 review, Round 2):**
- CRITICAL: Replace multi-bundle MNL with binary logit (single-offer behavioral consistency)
- MAJOR: Add coverage–efficiency Pareto frontier experiment
- MAJOR: Clarify MILP benchmark scope under stochastic acceptance
- MAJOR: Add objective weight VOT mapping + sensitivity table
- MINOR: Benchmark implied VOT against Chinese transit literature

**Progress:**

[          ] 0%
Phase 7 [          ] 0% (Choice Model & Algorithm Fix)
Phase 8 [          ] 0% (Pareto Experiment & New Metrics)
Phase 9 [          ] 0% (Paper Section Updates)
Overall v2.0 [          ] 0%

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
| Binary logit for single-offer acceptance | Reviewer CRITICAL: multi-bundle MNL behaviorally inconsistent with single-offer mechanism | v2.0 |
| Pareto frontier over rejection cost Gamma | Reviewer MAJOR: efficiency gains partly driven by endogenous coverage reduction | v2.0 |

### Prior Work Context

- Work 1 (many-to-one dynamic pricing, DRPO framework): complete, submitted to TR Part C
- Work 2 (service menu design, assortment optimization): working paper
- Work 3 natural extension: bidirectional spatial service menu (pickup + dropoff) in many-to-many scenario
- Key reference: Cortenbach et al. (2024, TR Part C) — DARPmp, single-sided, Tabu Search (direct predecessor)
- Key reference: Wu et al. (2025, TR Part E) — dynamic DRT with rolling horizon (algorithm precedent)

### Todos

- [ ] Confirm MNL/binary-logit parameter values (β1..β4) from Work 1/2 calibration or literature
- [ ] Run Pareto sweep experiment (Gamma sweep) and generate fig07_pareto
- [ ] Update choice.py to binary logit
- [ ] Update model.tex, algorithm.tex, experiments.tex, policy.tex per reviewer fixes

### Blockers

None currently.

### Notes

- Dissertation timeline: Work 3 planned 2026.09–2027.04 per BUAA schedule
- Supervisor: Prof. Liu Tianliang
- Language: English (academic paper)
- v2.0 phases 7–9 depend on v1.0 artifacts (paper sections, Python code, figures)

---

## Session Continuity

**Last session:** 2026-04-12
**Stopped at:** Roadmap written — ROADMAP_v2.md created with phases 7–9, 13/13 REV requirements mapped
**Next action:** `/gsd-plan-phase 7` — plan Phase 7 (Choice Model & Algorithm Fix)

---

*State initialized: 2026-04-11*
*Updated: 2026-04-12 — v2.0 roadmap written (phases 7–9, 13 requirements, 3 phases)*
