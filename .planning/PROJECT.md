# Work 3: Many-to-Many DRT Bidirectional Meeting Point Paper

## What This Is

A full academic paper targeting Transportation Research Part A: Policy and Practice, studying the online co-optimization of bidirectional meeting-point assignment and dynamic routing for many-to-many demand-responsive transit (DRT) with passenger choice. The paper extends Work 1 (many-to-one, dynamic pricing) and Work 2 (service menu design) to the many-to-many scenario, with policy framing around DRT service design for low-density urban areas in China.

## Core Value

Demonstrate that jointly optimizing pickup AND dropoff meeting points — while explicitly modeling passenger choice — significantly improves DRT operational efficiency and service equity compared to door-to-door or single-sided meeting point approaches, with actionable policy implications for DRT operators and urban planners.

## Target Journal

Transportation Research Part A: Policy and Practice (TR Part A)

**Policy framing angle:**
- How should DRT operators design bidirectional meeting point systems?
- What are the equity and accessibility implications of different meeting point policies?
- Under what urban conditions (demand density, fleet size, walking tolerance) does bidirectional meeting point assignment deliver the most benefit?
- Policy recommendations for Chinese city DRT deployment

## Current Milestone: v4.0 — GPT-5 Review Fixes (Third Round)

**Goal:** Address the two blocking issues identified by GPT-5 (high reasoning) review to move from 5/10 to ≥7/10 and achieve genuine submission readiness for TR Part A.

**Target features:**
- FIX-A [BLOCKING]: Endogenous matched-coverage comparison — implement DoorToDoor variant with acceptance cap + re-routing so served share ≈ FullModel's ~23.5%; replace post-hoc random rejection with endogenous comparison
- FIX-B [BLOCKING]: Behavioral consistency check — add units/variables table, one worked utility example, reconcile offer-stage attributes vs realized attributes vs aggregate acceptance rates
- FIX-C [MAJOR]: Fix old numbers in intro.tex and conclusion — replace "2383.85 vs 3662.33" and "-34.9%" with v3.0 numbers throughout
- FIX-D [MAJOR]: Add missing reference — Fielbaum, Bai & Alonso-Mora (2021) on bidirectional walking flexibility in ridepooling; position relative to this paper
- FIX-E [MINOR]: Add confidence intervals to main results table; clarify commitment assumption for accepted offers after rolling-horizon re-optimization

## Requirements

### Validated (v1.0 complete)

- [x] Problem formulation: many-to-many DRT with bidirectional meeting points + passenger choice
- [x] Mathematical model: three-layer coupled model (service generation → passenger response → dynamic dispatch)
- [x] Small-scale exact algorithm (MILP/branch-and-cut) for benchmark validation
- [x] Large-scale heuristic: online insertion + rolling horizon + ALNS
- [x] Numerical experiments: synthetic scenario + semi-realistic case (Chinese city)
- [x] Comparison baselines: door-to-door, single-sided meeting point, no passenger choice, full model
- [x] Policy analysis: sensitivity to demand density, walking tolerance, fleet size, city type
- [x] Paper writing: all sections (intro, literature, model, algorithm, experiments, conclusion)
- [x] Academic figures: system diagram, algorithm flowchart, result charts (Python/matplotlib)

### Validated (v2.0 complete)

- [x] Binary logit acceptance model replacing multi-bundle MNL in single-offer mechanism
- [x] Coverage–efficiency Gamma sweep (served share vs welfare sensitivity)
- [x] MILP benchmark scope defined: ex-post routing of fixed accepted set + optimality gap
- [x] Objective weight policy interpretation: VOT mapping + weight sensitivity table
- [x] Parameter plausibility: implied VOT benchmarked against Chinese DRT/transit literature

### Validated (v3.0 complete)

- [x] FIX-01: Correct vkm/trip metric — recomputed as vkm ÷ accepted_trip_count; all tables, abstract, policy section updated
- [x] FIX-02: Matched-coverage comparison (post-hoc) — FullModel 10.9 vs DoorToDoor 42.3 vkm/trip at ~23.5% served share (74.3%); acknowledged as conservative lower bound
- [x] FIX-03: Formalize coupled decision problem — timing/decision diagram (tab:timing-diagram) + ALNS online objective (eq:alns-objective) added
- [x] FIX-04: Soften policy thresholds — generalizability caveats added to R1 (1000m) and R2 (15-vehicle ratio)

### Active (v4.0 revision)

- [ ] FIX-A: Endogenous matched-coverage comparison — DoorToDoor with acceptance cap + re-routing; served share ≈ FullModel ~23.5%; replaces post-hoc random rejection
- [ ] FIX-B: Behavioral consistency check — units/variables table, worked utility example, reconcile offer-stage vs realized attributes vs acceptance rates
- [ ] FIX-C: Fix old numbers in intro.tex and conclusion — replace "2383.85 vs 3662.33" and "-34.9%" with v3.0 numbers
- [ ] FIX-D: Add Fielbaum et al. (2021) to literature review — position bidirectional walking flexibility relative to this paper
- [ ] FIX-E: Add confidence intervals to main results table; clarify commitment assumption for accepted offers after rolling-horizon re-optimization

### Out of Scope

- Pricing as core decision variable — price is fixed or uses Work 1's mechanism (avoid overlap with Work 1/2)
- Reinforcement learning as main method — keep as extension discussion only
- Real GPS/smart card data — simulation-based validation is standard for this problem type
- TR Part D environmental framing — not the target journal

## Context

**Dissertation position:** Work 3 of 4 in PhD dissertation "Optimization of DRT Systems with Passenger Boarding Location Choice" (BUAA, supervisor: Prof. Liu Tianliang). Work 1 (many-to-one dynamic pricing, DRPO framework) is complete and submitted to TR Part C. Work 2 (service menu design, assortment optimization) is working paper.

**Work 3 natural extension:** Work 1 = single-sided meeting point + pricing. Work 2 = spatiotemporal service menu. Work 3 = bidirectional spatial service menu (pickup + dropoff) in many-to-many scenario.

**Key prior work to build on:**
- Cortenbach et al. (2024, TR Part C): DARPmp — meeting point selection endogenized, single-sided, Tabu Search
- Wu et al. (2025, TR Part E): Dynamic DRT with time-dependent travel times, rolling horizon
- Equity-aware DARP BCP (2025, TR Part B): exact algorithm benchmark for ~55 passengers

**Data approach:** Simulation-based (synthetic + semi-realistic). No primary survey data needed. Standard for DARP/DRT literature.

## Constraints

- **Timeline**: Work 3 planned 2026.09–2027.04 per dissertation schedule
- **Method**: Must include both exact (small-scale) and heuristic (large-scale) algorithms
- **Passenger choice**: Must retain MNL/binary-logit passenger choice model — core dissertation thread
- **Policy framing**: TR Part A requires policy implications beyond pure optimization
- **Language**: English (academic paper)

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Target TR Part A not TR Part C | Policy framing differentiates from Work 1 (TR Part C); TR Part A accepts optimization papers with strong policy angle | Confirmed |
| Fix price, don't optimize it | Avoid overlap with Work 1/2; keep Work 3 focused on bidirectional spatial assignment | Confirmed |
| Rolling horizon + ALNS as main heuristic | Standard in dynamic DRT literature 2024-2025; matches dissertation framework | Confirmed |
| Simulation-based validation | Standard for DARP; real data hard to obtain; consistent with Work 1 approach | Confirmed |
| Binary logit for single-offer acceptance | Reviewer CRITICAL: multi-bundle MNL behaviorally inconsistent with single-offer mechanism | v2.0 |
| Pareto frontier over rejection cost | Reviewer MAJOR: efficiency gains partly driven by endogenous coverage reduction | v2.0 |
| Correct vkm/trip denominator | Codex CRITICAL: dividing by acceptance rate (not trip count) gives dimensionally wrong metric | v3.0 |
| Matched-coverage comparison | Codex CRITICAL: 20.8% vs 61% served share confounds efficiency comparison | v3.0 |
| Formalize ALNS decision problem | Codex MAJOR: unclear what ALNS optimizes (expected cost vs Bernoulli realizations) | v3.0 |
| Endogenous matched-coverage comparison | GPT-5 BLOCKING: post-hoc random rejection not credible; DoorToDoor with acceptance cap + re-routing required | v4.0 |
| Add Fielbaum et al. (2021) to literature | GPT-5 MAJOR: bidirectional walking flexibility in ridepooling is prior art; must position relative to it | v4.0 |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition:**
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-13 — v3.0 milestone started (Codex review fixes)*
