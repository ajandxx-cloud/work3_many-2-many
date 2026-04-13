---
gsd_state_version: 1.0
milestone: v3.0
milestone_name: — Codex Review Fixes
status: v4.0 milestone started; phases 12-13 planned; no plans executed yet
last_updated: "2026-04-13T05:17:17.214Z"
last_activity: 2026-04-13
progress:
  total_phases: 7
  completed_phases: 7
  total_plans: 25
  completed_plans: 25
  percent: 100
---

# STATE: Work 3 — Many-to-Many DRT Bidirectional Meeting Point Paper

## Project Reference

**Core value:** Demonstrate that bidirectional meeting point assignment with passenger choice significantly improves DRT efficiency and equity, with actionable policy implications for TR Part A.
**Target journal:** Transportation Research Part A: Policy and Practice
**Current focus:** v4.0 — GPT-5 Review Fixes (2 blocking issues)

---

## Current Position

Phase: 8
Plan: Not started
Status: v4.0 milestone started; phases 12-13 planned; no plans executed yet
Last activity: 2026-04-13

**v4.0 revision scope (from GPT-5 MCP review, 2026-04-13, score 5/10):**

- [ ] Phase 12: Endogenous Matched-Coverage Experiment
  - [ ] COMP-01: Implement DoorToDoorCapped variant with acceptance cap + re-routing
  - [ ] COMP-02: Run experiment (seeds 42/43/44, n=200, 15 vehicles)
  - [ ] COMP-03: Update Section 5.2 with endogenous result as primary claim
- [ ] Phase 13: Paper Fixes & Literature Update
  - [ ] BEHAV-01: Add units/variables reference table
  - [ ] BEHAV-02: Add worked utility example with explicit unit conversions
  - [ ] BEHAV-03: Add commitment assumption paragraph
  - [ ] TEXT-01: Fix intro.tex old numbers (2383.85 vs 3662.33, -34.9%)
  - [ ] TEXT-02: Fix conclusion old numbers
  - [ ] TEXT-03: Grep-verify no old numbers remain
  - [ ] LIT-01: Add Fielbaum et al. (2021) to references.bib
  - [ ] LIT-02: Add positioning sentences in Section 2.2
  - [ ] ROB-01: Add ± notation to Table 1
  - [ ] ROB-02: Add 3-seed justification note in Section 5.1

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

### v3.0 Results (for reference)

| Metric | Value |
|--------|-------|
| v3.0 phases complete | 2/2 (Phases 10-11) |
| v3.0 requirements complete | 9/9 |
| GPT-5 review score (post-v3.0) | 5/10 (borderline Major Revisions) |
| Corrected vkm/trip | FullModel 15.1, DoorToDoor 21.3 (29.2% improvement, unconstrained) |
| Post-hoc matched-coverage | FullModel 10.9, DoorToDoor 42.3 vkm/trip (74.3% at equal ~23.5% share) |
| GPT-5 verdict | "Not fully sufficient as main proof" — needs endogenous re-routing |

### Blockers

None. Phase 12 (DoorToDoorCapped implementation) is ready to start.

### Notes

- Dissertation timeline: Work 3 planned 2026.09–2027.04 per BUAA schedule
- Supervisor: Prof. Liu Tianliang
- Language: English (academic paper)
- GPT-5 review thread ID: 019d84ab-c6a4-7fd1-b91f-01109b57c1f2 (for Round 3 if needed)

---

*State initialized: 2026-04-11*
*Updated: 2026-04-13 — v3.0 milestone complete (Phases 10-11, 9 requirements)*
*Updated: 2026-04-13 — v4.0 milestone started (GPT-5 review fixes, Phases 12-13, 13 requirements)*
