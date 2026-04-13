---
gsd_state_version: 1.0
milestone: v3.0
milestone_name: codex-review-fixes
status: in_progress
stopped_at: Milestone v3.0 started — defining requirements
last_updated: "2026-04-13T00:00:00.000Z"
last_activity: 2026-04-13
progress:
  total_phases: 0
  completed_phases: 0
  total_plans: 0
  completed_plans: 0
  percent: 0
---

# STATE: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

## Project Reference

**Core value:** Demonstrate that bidirectional meeting point assignment with passenger choice significantly improves DRT efficiency and equity, with actionable policy implications for TR Part A.
**Target journal:** Transportation Research Part A: Policy and Practice
**Current focus:** v3.0 — Codex review fixes (4 CRITICAL/MAJOR issues)

---

## Current Position

Phase: Not started (defining requirements)
Plan: —
Status: Defining requirements
Last activity: 2026-04-13 — Milestone v3.0 started

**v3.0 revision scope (from Codex review, 2026-04-13):**

- [ ] FIX-01 [CRITICAL]: Correct vkm/trip metric — recompute as vkm ÷ accepted_trip_count
- [ ] FIX-02 [CRITICAL]: Add matched-coverage comparison
- [ ] FIX-03 [MAJOR]: Formalize coupled decision problem
- [ ] FIX-04 [MAJOR]: Soften policy thresholds

---

## Accumulated Context

### Key Decisions Logged

| Decision | Rationale | Phase |
|----------|-----------|-------|
| Target TR Part A not TR Part C | Policy framing differentiates from Work 1; TR Part A accepts optimization with strong policy angle | Pre-phase |
| Fix price, don't optimize it | Avoid overlap with Work 1/2; keep Work 3 focused on bidirectional spatial assignment | Pre-phase |
| Rolling horizon + ALNS as main heuristic | Standard in dynamic DRT literature 2024-2025; matches dissertation framework | Pre-phase |
| Simulation-based validation | Standard for DARP; real data hard to obtain; consistent with Work 1 approach | Pre-phase |
| Gurobi solver for MILP | Industry standard, best performance for DARP-scale MILPs | Phase 2 |
| Binary logit for single-offer acceptance | Reviewer CRITICAL: multi-bundle MNL behaviorally inconsistent with single-offer mechanism | Phase 7 |
| Pareto frontier reframed as welfare sensitivity | gamma is post-hoc; served_share constant; narrative shows structural efficiency gain | Phase 8 |
| MILP gap large (99-170%) explained honestly | Small accepted sets (4-7 pax) at n=20/30; gap expected to narrow at scale | Phase 9 |

### Prior Work Context

- Work 1 (many-to-one dynamic pricing, DRPO framework): complete, submitted to TR Part C
- Work 2 (service menu design, assortment optimization): working paper
- Work 3 natural extension: bidirectional spatial service menu (pickup + dropoff) in many-to-many scenario

### v2.0 Results (for reference)

| Metric | Value |
|--------|-------|
| v2.0 phases complete | 3/3 |
| v2.0 requirements complete | 13/13 |
| Codex review (post-v2.0) Round 1 | 4/10 → 5/10 after revisions |
| Phase 7 key result | Binary logit accept_probability; REV-01..04 PASS |
| Phase 8 key result | Gamma sweep: served_share=0.183 constant; fig07_pareto generated |
| Phase 9 key result | MILP gap table; VOT table; weight sensitivity -30-31% |

### Blockers

None.

### Notes

- Dissertation timeline: Work 3 planned 2026.09–2027.04 per BUAA schedule
- Supervisor: Prof. Liu Tianliang
- Language: English (academic paper)

---

*State initialized: 2026-04-11*
*Updated: 2026-04-13 — v3.0 milestone started (Codex review fixes)*
