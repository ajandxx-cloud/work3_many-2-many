---
gsd_state_version: 1.0
milestone: v2.0
milestone_name: reviewer-revision
status: complete
stopped_at: v2.0 milestone complete — all 13 REV requirements verified PASS across phases 7-9
last_updated: "2026-04-12T17:30:00.000Z"
last_activity: 2026-04-12
progress:
  total_phases: 3
  completed_phases: 3
  total_plans: 7
  completed_plans: 7
  percent: 100
---

# STATE: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

## Project Reference

**Core value:** Demonstrate that bidirectional meeting point assignment with passenger choice significantly improves DRT efficiency and equity, with actionable policy implications for TR Part A.
**Target journal:** Transportation Research Part A: Policy and Practice
**Current focus:** v2.0 COMPLETE — ready for TR Part A submission

---

## Current Position

**Status:** v2.0 milestone COMPLETE
**All phases:** 7 ✓, 8 ✓, 9 ✓
**All requirements:** 13/13 REV requirements verified PASS
**Last activity:** 2026-04-12

**v2.0 revision scope (from GPT-5.2 review, Round 2):**

- ~~CRITICAL: Replace multi-bundle MNL with binary logit~~ ✓ DONE (Phase 7)
- ~~MAJOR: Add coverage–efficiency Pareto frontier experiment~~ ✓ DONE (Phase 8)
- ~~MAJOR: Clarify MILP benchmark scope under stochastic acceptance~~ ✓ DONE (Phase 9)
- ~~MAJOR: Add objective weight VOT mapping + sensitivity table~~ ✓ DONE (Phase 9)
- ~~MINOR: Benchmark implied VOT against Chinese transit literature~~ ✓ DONE (Phase 9)

**Progress:**

[██████████] 100%
Phase 7 [██████████] 100% (Choice Model & Algorithm Fix) ✓
Phase 8 [██████████] 100% (Pareto Experiment & New Metrics) ✓
Phase 9 [██████████] 100% (Paper Section Updates) ✓
Overall v2.0 [██████████] 100% ✓

---

## Performance Metrics

| Metric | Value |
|--------|-------|
| v1.0 phases total | 6 |
| v1.0 phases complete | 6 |
| v2.0 phases total | 3 |
| v2.0 phases complete | 3 |
| v2.0 requirements total | 13 |
| v2.0 requirements complete | 13 |
| v2.0 plans written | 7 |
| v2.0 plans complete | 7 |
| Codex review Round 1 | 5/10 (weak reject) |
| Codex review Round 2 | 6/10 (weak accept) |
| Phase 7 key result | Binary logit accept_probability; REV-01..04 PASS |
| Phase 8 key result | Gamma sweep: served_share=0.183 constant (gamma post-hoc); W sensitivity shown; fig07_pareto generated; REV-05..08 PASS |
| Phase 9 key result | MILP gap table (n=20: 170%, n=30: 99%); VOT table (policy.tex); weight sensitivity (FullModel -30-31% across 3 configs); beta footnote; REV-09..13 PASS |

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

### Todos

- [x] All v2.0 revision tasks complete

### Blockers

None.

### Notes

- Dissertation timeline: Work 3 planned 2026.09–2027.04 per BUAA schedule
- Supervisor: Prof. Liu Tianliang
- Language: English (academic paper)
- Next step: TR Part A submission

---

## Session Continuity

**Last session:** 2026-04-12
**Stopped at:** v2.0 milestone complete — all 13 REV requirements verified PASS
**Next action:** TR Part A submission preparation (cover letter, response to reviewers letter)

---

*State initialized: 2026-04-11*
*Updated: 2026-04-12 — v2.0 milestone complete (phases 7-9, 13/13 requirements, 7 plans)*
