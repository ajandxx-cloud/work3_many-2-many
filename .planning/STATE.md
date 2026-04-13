---
gsd_state_version: 1.0
milestone: v5.0
milestone_name: — Code Review Fixes & Submission Prep
status: Complete
last_updated: "2026-04-13T00:00:00.000Z"
last_activity: 2026-04-13
progress:
  total_phases: 2
  completed_phases: 2
  total_plans: 3
  completed_plans: 3
  percent: 100
---

# STATE: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

## Project Reference

**Core value:** Demonstrate that bidirectional meeting point assignment with passenger choice significantly improves DRT efficiency and equity, with actionable policy implications for TR Part A.
**Target journal:** Transportation Research Part A: Policy and Practice
**Current focus:** v5.0 — Code Review Fixes & Submission Prep (COMPLETE)

---

## Current Position

Phase: Phase 15 (complete)
Plan: 15-01 (complete)
Status: v5.0 milestone complete — all 13 requirements satisfied
Last activity: 2026-04-13 — Phase 15 verified (5/5 criteria pass)

**v5.0 scope (13 requirements across 2 phases):**

- [x] Phase 14: Paper & Response Letter Fixes (NUM-01..03, RESP-01..02, CLEAN-01..03) — completed 2026-04-13
- [x] Phase 15: Code Reproducibility & Robustness (CODE-01, ROB-01..04) — completed 2026-04-13

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
| Matched-coverage comparison (post-hoc) | Codex CRITICAL: 20.8% vs 61% served share confounds efficiency comparison | Phase 10 |
| Formalize ALNS decision problem | Codex MAJOR: unclear what ALNS optimizes (expected cost vs Bernoulli realizations) | Phase 11 |
| Soften policy thresholds | Codex MAJOR: 1000m/15-vehicle thresholds too strong for synthetic-only evidence | Phase 11 |
| Endogenous matched-coverage required | GPT-5 BLOCKING: post-hoc random rejection not credible as primary evidence; DoorToDoor with acceptance cap + re-routing needed | Phase 12 |
| Add Fielbaum et al. (2021) | GPT-5 MAJOR: bidirectional walking flexibility in ridepooling is prior art that must be acknowledged | Phase 13 |

### Prior Work Context

- Work 1 (many-to-one dynamic pricing, DRPO framework): complete, submitted to TR Part C
- Work 2 (service menu design, assortment optimization): working paper
- Work 3 natural extension: bidirectional spatial service menu (pickup + dropoff) in many-to-many scenario

### v4.0 Results (for reference)

| Metric | Value |
|--------|-------|
| v4.0 phases complete | 2/2 (Phases 12-13) |
| v4.0 requirements complete | 13/13 |
| Endogenous matched-coverage | FullModel 11.1 vs DoorToDoor 17.1 vkm/trip (35.0% improvement at ~23% matched share) |
| Unconstrained comparison | FullModel 15.1 vs DoorToDoor 21.3 vkm/trip (29.2% improvement) |
| Post-hoc lower bound | FullModel 10.9 vs DoorToDoor 42.3 vkm/trip (74.3% at ~23.5% share, footnote) |

### v5.0 Scope Summary

| Phase | Requirements | Focus |
|-------|-------------|-------|
| Phase 14 | NUM-01..03, RESP-01..02, CLEAN-01..03 | Paper numeric fixes, response letter update, pre-submission cleanup |
| Phase 15 | CODE-01, ROB-01..04 | SHA-256 seed, stop ordering warning, tolerance warning, empty-seeds guard, unassigned dedup |

### Blockers

None. Roadmap defined, ready to plan.

### Notes

- Dissertation timeline: Work 3 planned 2026.09-2027.04 per BUAA schedule
- Supervisor: Prof. Liu Tianliang
- Language: English (academic paper)
- GPT-5 review thread ID: 019d84ab-c6a4-7fd1-b91f-01109b57c1f2 (for Round 3 if needed)

---

*State initialized: 2026-04-11*
*Updated: 2026-04-13 — v3.0 milestone complete (Phases 10-11, 9 requirements)*
*Updated: 2026-04-13 — v4.0 milestone complete (Phases 12-13, 13 requirements)*
*Updated: 2026-04-13 — v5.0 milestone started (code review fixes, 13 requirements)*
*Updated: 2026-04-13 — v5.0 roadmap created (Phases 14-15, 13 requirements, 100% coverage)*
