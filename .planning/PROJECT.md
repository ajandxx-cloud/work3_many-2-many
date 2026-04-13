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

## Current Milestone: v5.0 — Code Review Fixes & Submission Prep

**Goal:** Address all outstanding code review findings from phases 12-13 to achieve final submission readiness for TR Part A.

**Target features:**
- FIX-NUM: Fix paper numeric inconsistencies — Gini 0.1216 vs 0.122; 22.8% vs 23.5% cap target; weight-sensitivity table vkm/trip vs raw vkm
- FIX-RESP: Update response_to_reviewers.tex — FIX-02 section stale description; R1 body old numbers 3022/4268
- FIX-CODE: Fix code reproducibility — replace hash(request.id) with SHA-256 deterministic seed
- FIX-ROBUST: Code robustness fixes — stop ordering warning, tolerance failure non-silent, division-by-zero guard, unassigned deduplication
- FIX-CLEAN: Pre-submission cleanup — remove audit comment blocks, provisional annotations, internal development notes

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

### Validated (v4.0 complete)

- [x] FIX-A: Endogenous matched-coverage comparison — DoorToDoorCapped with acceptance cap + re-routing; FullModel 11.1 vs DoorToDoor 17.1 vkm/trip (35.0%) at matched ~23% served share (Validated in Phase 12)
- [x] FIX-B: Behavioral consistency check — notation table (tab:notation), worked utility example (Section 4.2), commitment assumption paragraph (algorithm.tex) added (Validated in Phase 13)
- [x] FIX-C: Fix old numbers — "2383.85/3662.33/-34.9%" replaced with v3.0 numbers throughout intro, conclusion, abstract (Validated in Phase 13)
- [x] FIX-D: Fielbaum et al. (2021) added to Section 2.2 with positioning sentence (Validated in Phase 13)
- [x] FIX-E: ± std added to Table 1; commitment assumption clarified; 3-seed note with \citep{wu2025} in Section 5.1 (Validated in Phase 13)

### Active (v5.0)

- [ ] NUM-01: Fix Gini coefficient inconsistency — policy.tex 0.122 → 0.1216 to match experiments.tex and abstract
- [ ] NUM-02: Reconcile cap target — verify actual FullModel mean served share (22.8% vs 23.5%) and align code default, paper text, table caption, and footnote
- [ ] NUM-03: Fix weight-sensitivity table — verify denominator and correct column headers (vkm/trip vs raw vkm)
- [ ] RESP-01: Update response_to_reviewers.tex FIX-02 section — reflect endogenous result (11.1 vs 17.1, 35.0%) as primary claim; correct 23.5% → 22.8%
- [ ] RESP-02: Update response_to_reviewers.tex R1 body — replace 3022/4268 with 15.1/21.3 vkm/trip
- [ ] CODE-01: Fix hash(request.id) → SHA-256 deterministic seed for cross-process reproducibility
- [ ] ROB-01: Add stop ordering warning in _find_stop_info when pickup_time >= dropoff_time
- [ ] ROB-02: Make tolerance failure non-silent in endogenous_matched_coverage.py
- [ ] ROB-03: Add empty seeds guard (ZeroDivisionError) in endogenous_matched_coverage_experiment
- [ ] ROB-04: Deduplicate state.unassigned in DoorToDoor._solve and DoorToDoorCapped._solve
- [ ] CLEAN-01: Remove audit comment block from experiments.tex (lines 1-13)
- [ ] CLEAN-02: Remove "(provisional)" annotation from model.tex beta parameters
- [ ] CLEAN-03: Fix cross-reference robustness in model.tex footnote (subsec:vot-mapping)

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
*Last updated: 2026-04-13 — v5.0 milestone started (code review fixes: numeric inconsistencies, response letter updates, code reproducibility, robustness, pre-submission cleanup)*
