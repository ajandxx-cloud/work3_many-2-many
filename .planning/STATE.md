---
gsd_state_version: 1.0
milestone: v3.0
milestone_name: — Codex Review Fixes
status: in-progress
last_updated: "2026-04-13T02:30:00.000Z"
last_activity: 2026-04-13 — Phase 11 Plan 01 executed (timing diagram + ALNS objective)
progress:
  total_phases: 9
  completed_phases: 7
  total_plans: 27
  completed_plans: 27
  percent: 100
---

# STATE: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

## Project Reference

**Core value:** Demonstrate that bidirectional meeting point assignment with passenger choice significantly improves DRT efficiency and equity, with actionable policy implications for TR Part A.
**Target journal:** Transportation Research Part A: Policy and Practice
**Current focus:** v3.0 — Codex review fixes (4 CRITICAL/MAJOR issues)

---

## Current Position

Phase: Phase 11 — Formalization & Policy Reframing (in progress)
Plan: 01 complete
Status: Plan 11-01 complete; Plans 11-02 through 11-05 (PFRAM-01–03) remaining
Last activity: 2026-04-13 — Plan 11-01 executed (timing diagram + ALNS objective)

**v3.0 revision scope (from Codex review, 2026-04-13):**

- [x] Phase 10: Metric Audit & Coverage Comparison
  - [x] METRIC-01: Recompute vkm/trip throughout all tables, abstract, policy section
  - [x] METRIC-02: Reconcile inconsistent efficiency numbers to single denominator
  - [x] COVER-01: Add matched-coverage experiment (DoorToDoor at equal served share)
  - [x] COVER-02: Update Section 5.2 narrative and abstract efficiency claim
- [ ] Phase 11: Formalization & Policy Reframing
  - [x] FORM-01: Add timing/decision diagram (Layer 1-3 sequence + Bernoulli sampling point)
  - [x] FORM-02: Add mathematical statement of ALNS online objective
  - [ ] PFRAM-01: Reframe 1000m walking threshold as scenario-specific finding
  - [ ] PFRAM-02: Reframe 15-vehicle fleet ratio as scenario-specific finding
  - [ ] PFRAM-03: Update response_to_reviewers.tex for all v3.0 changes

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
| Correct vkm/trip denominator | Codex CRITICAL: dividing by acceptance rate (not trip count) gives dimensionally wrong metric | Phase 10 |
| Matched-coverage comparison | Codex CRITICAL: 20.8% vs 61% served share confounds efficiency comparison | Phase 10 |
| Formalize ALNS decision problem | Codex MAJOR: unclear what ALNS optimizes (expected cost vs Bernoulli realizations) | Phase 11 |
| Soften policy thresholds | Codex MAJOR: 1000m/15-vehicle thresholds too strong for synthetic-only evidence | Phase 11 |

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
*Updated: 2026-04-13 — v3.0 roadmap created (Phases 10-11, 9 requirements)*
