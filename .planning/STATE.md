# STATE: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

## Project Reference

**Core value:** Demonstrate that bidirectional meeting point assignment with passenger choice significantly improves DRT efficiency and equity, with actionable policy implications for TR Part A.
**Target journal:** Transportation Research Part A: Policy and Practice
**Current focus:** Phase 1 — Problem Formulation & Model Structure

---

## Current Position

**Active phase:** Phase 1 — Problem Formulation & Model Structure
**Active plan:** None (not yet started)
**Status:** Not started
**Phase goal:** Formalize the many-to-many DRT problem, notation, constraints, and three-layer coupled model with MNL passenger choice

**Progress:**
```
Phase 1 [          ] 0%
Phase 2 [          ] 0%
Phase 3 [          ] 0%
Phase 4 [          ] 0%
Phase 5 [          ] 0%
Phase 6 [          ] 0%
Overall [          ] 0%
```

---

## Performance Metrics

| Metric | Value |
|--------|-------|
| Phases total | 6 |
| Phases complete | 0 |
| Requirements total (v1) | 47 |
| Requirements complete | 0 |
| Plans written | 0 |
| Plans complete | 0 |

---

## Accumulated Context

### Key Decisions Logged

| Decision | Rationale | Phase |
|----------|-----------|-------|
| Target TR Part A not TR Part C | Policy framing differentiates from Work 1; TR Part A accepts optimization with strong policy angle | Pre-phase |
| Fix price, don't optimize it | Avoid overlap with Work 1/2; keep Work 3 focused on bidirectional spatial assignment | Pre-phase |
| Rolling horizon + ALNS as main heuristic | Standard in dynamic DRT literature 2024-2025; matches dissertation framework | Pre-phase |
| Simulation-based validation | Standard for DARP; real data hard to obtain; consistent with Work 1 approach | Pre-phase |
| FIG-01..06 assigned to Phase 6 (not Phase 5) | Figures require experiment and policy results to be final before production; decoupling avoids rework | Roadmap |

### Prior Work Context

- Work 1 (many-to-one dynamic pricing, DRPO framework): complete, submitted to TR Part C
- Work 2 (service menu design, assortment optimization): working paper
- Work 3 natural extension: bidirectional spatial service menu (pickup + dropoff) in many-to-many scenario
- Key reference: Cortenbach et al. (2024, TR Part C) — DARPmp, single-sided, Tabu Search (direct predecessor)
- Key reference: Wu et al. (2025, TR Part E) — dynamic DRT with rolling horizon (algorithm precedent)

### Todos

- [ ] Confirm Gurobi license availability for EXACT-01/02 (Phase 2)
- [ ] Select Chinese city scenario parameters for EXP-02 (Phase 3) — candidate: suburban Beijing or Shenzhen low-density district
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

**Last session:** 2026-04-11 — Roadmap initialized, STATE.md created
**Next action:** Begin Phase 1 — start with PROB-01 (define many-to-many DRT problem with bidirectional meeting points)

---

*State initialized: 2026-04-11*
*Last updated: 2026-04-11 after roadmap creation*
