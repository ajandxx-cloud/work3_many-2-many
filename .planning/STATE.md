---
gsd_state_version: 1.0
milestone: v1.0
milestone_name: milestone
status: executing
stopped_at: Completed 04-policy-analysis-sensitivity-analysis 04-03-PLAN.md
last_updated: "2026-04-12T13:25:30.088Z"
progress:
  total_phases: 6
  completed_phases: 4
  total_plans: 15
  completed_plans: 15
  percent: 100
---

# STATE: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

## Project Reference

**Core value:** Demonstrate that bidirectional meeting point assignment with passenger choice significantly improves DRT efficiency and equity, with actionable policy implications for TR Part A.
**Target journal:** Transportation Research Part A: Policy and Practice
**Current focus:** Phase 4 — Policy Analysis & Sensitivity Analysis

---

## Current Position

**Active phase:** Phase 4 — Policy Analysis & Sensitivity Analysis
**Active plan:** Plan 02 (04-01 complete)
**Status:** Executing
**Phase goal:** Sensitivity sweeps across demand density, walking tolerance, and fleet size; equity analysis; policy recommendations for TR Part A

**Progress:**

[██████████] 100%
Phase 1 [██████████] 100% ✓
Phase 2 [██████████] 100% ✓
Phase 3 [██████████] 100% ✓
Phase 4 [███       ] 33% (1/3 plans)
Phase 5 [          ] 0%
Phase 6 [          ] 0%
Overall [█████     ] 53%

```

---

## Performance Metrics

| Metric | Value |
|--------|-------|
| Phases total | 6 |
| Phases complete | 3 |
| Requirements total (v1) | 47 |
| Requirements complete | 28 |
| Plans written | 12 |
| Plans complete | 12 |
| Phase 3 key result | FullModel vkm/acceptance = 2383.85 vs DoorToDoor 3662.33 (-34.9% efficiency gain) |

---
| Phase 04-policy-analysis-sensitivity-analysis P03 | 25 | 1 tasks | 2 files |

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

### Prior Work Context

- Work 1 (many-to-one dynamic pricing, DRPO framework): complete, submitted to TR Part C
- Work 2 (service menu design, assortment optimization): working paper
- Work 3 natural extension: bidirectional spatial service menu (pickup + dropoff) in many-to-many scenario
- Key reference: Cortenbach et al. (2024, TR Part C) — DARPmp, single-sided, Tabu Search (direct predecessor)
- Key reference: Wu et al. (2025, TR Part E) — dynamic DRT with rolling horizon (algorithm precedent)

### Todos

- [x] Gurobi license: not available on dev machine — scale test (EXACT-02) uses skipif guard; will need license for actual benchmark runs
- [x] Select Chinese city scenario parameters for EXP-02 (Phase 3) — Beijing suburban 15km×15km, 80 MPs, morning peak 7-9am (implemented in generate_beijing)
- [ ] Confirm MNL parameter values (β1..β4) from Work 1/2 calibration or literature

### Blockers

None currently.

### Notes

- Dissertation timeline: Work 3 planned 2026.09–2027.04 per BUAA schedule
- Supervisor: Prof. Liu Tianliang
- Language: English (academic paper)
- Phase 5 (Paper Writing) depends on Phases 1-4 all being complete
- Phase 6 (Figures) depends on Phases 3, 4, and 5 being complete

---

## Session Continuity

**Last session:** 2026-04-12T13:25:30.085Z
**Stopped at:** Completed 04-policy-analysis-sensitivity-analysis 04-03-PLAN.md
**Next action:** Phase 4 Plan 02 — equity analysis

---

*State initialized: 2026-04-11*
*Last updated: 2026-04-12 after Phase 4 plan 01 completion*
