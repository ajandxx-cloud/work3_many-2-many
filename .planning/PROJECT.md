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

## Current Milestone: v6.0 — Round 1 Review Revision & Resubmission

**Goal:** Address all 4 CRITICAL and 4 MAJOR reviewer comments from Round 1 (GPT-5.5, score 3/10), unify model/experiment narrative, rerun key experiments, and prepare TR Part A resubmission-ready manuscript.

**Target features:**
- C1-CHOICE: Unify choice model — binary logit with U_0=0, consistent 4-tuple betas, remove mu_0=5.0, fix worked example, rename MNL→binary logit throughout paper
- C2-OBJECTIVE: Reconcile system/ALNS/welfare objectives — document pre-filter-then-route mechanism, remove Gamma from Section 3, fix ALNS description
- C3-MILP: Downgrade MILP from "exact benchmark" to "ex-post routing diagnostic" — fix claims, honest gap characterization
- C4-NUMERIC: Unify numerical baselines across all tables — consistent acceptance rates, fix detour ratio ≥1, remove "74.3% conservative lower bound"
- M1-POLICY: Scope down policy claims — 1000m threshold and fleet ratio as scenario-specific, fix daily→peak-hour
- M2-BEIJING: Add Beijing semi-realistic scenario results table to experiments section
- M3-LITERATURE: Fix literature positioning — add Fielbaum et al. 2021 to comparison table, scope "first" claims
- M4-NOTATION: Unify notation/units — add units table, fix ρ/ρ^P/ρ^D, seconds vs minutes
- MINOR: Fix British/American spelling, add missing std in tables, resolve LaTeX warnings

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

### Validated (v5.0 complete)

- [x] NUM-01: Fix Gini coefficient inconsistency — policy.tex 0.122 → 0.1216 to match experiments.tex and abstract
- [x] NUM-02: Reconcile cap target — verify actual FullModel mean served share (22.8% vs 23.5%) and align code default, paper text, table caption, and footnote
- [x] NUM-03: Fix weight-sensitivity table — verify denominator and correct column headers (vkm/trip vs raw vkm)
- [x] RESP-01: Update response_to_reviewers.tex FIX-02 section — reflect endogenous result (11.1 vs 17.1, 35.0%) as primary claim; correct 23.5% → 22.8%
- [x] RESP-02: Update response_to_reviewers.tex R1 body — replace 3022/4268 with 15.1/21.3 vkm/trip
- [x] CODE-01: Fix hash(request.id) → SHA-256 deterministic seed for cross-process reproducibility
- [x] ROB-01: Add stop ordering warning in _find_stop_info when pickup_time >= dropoff_time
- [x] ROB-02: Make tolerance failure non-silent in endogenous_matched_coverage.py
- [x] ROB-03: Add empty seeds guard (ZeroDivisionError) in endogenous_matched_coverage_experiment
- [x] ROB-04: Deduplicate state.unassigned in DoorToDoor._solve and DoorToDoorCapped._solve
- [x] CLEAN-01: Remove audit comment block from experiments.tex (lines 1-13)
- [x] CLEAN-02: Remove "(provisional)" annotation from model.tex beta parameters
- [x] CLEAN-03: Fix cross-reference robustness in model.tex footnote (subsec:vot-mapping)

### Active (v6.0)

- [ ] C1-01: Remove mu_0=5.0 from worked example in model.tex, recalculate with U_0=0
- [ ] C1-02: Delete beta_price=-0.012/beta_time=-0.008/beta_walk=-0.015 from experiments.tex, reference 12 beta values from model.tex
- [ ] C1-03: Replace "MNL" → "binary logit" in abstract, intro, model sections
- [ ] C2-01: Remove C_rej/Gamma from Section 3 system objective (model.tex Eq. 5)
- [ ] C2-02: Rewrite ALNS objective description in algorithm.tex — replace P_accept*routing_cost with pre-filter-then-route
- [ ] C2-03: Update ALNS design rationale and iteration count in algorithm.tex
- [ ] C3-01: Downgrade MILP from "exact benchmark" to "ex-post routing diagnostic" in algorithm.tex, abstract, intro, conclusion
- [ ] C3-02: Remove "small optimality gap" claims, honestly characterize 99-170% gaps
- [ ] C4-01: Unify acceptance rate baselines across all 6 tables, add configuration footnotes
- [ ] C4-02: Fix detour ratio 0.76 → actual value ≥1.0, fix "74.3% conservative lower bound"
- [ ] C4-03: Update all numerical claims in abstract, conclusion, policy from regenerated CSVs
- [ ] M1-01: Scope 1000m threshold as scenario-specific, move caveats before recommendation in policy.tex
- [ ] M1-02: Fix "daily requests" → "peak-hour requests" for fleet ratio in policy.tex, abstract, conclusion
- [ ] M2-01: Add Beijing semi-realistic scenario results table to experiments.tex
- [ ] M3-01: Add Fielbaum et al. 2021 and Alonso-Mora et al. 2017 to literature positioning table
- [ ] M3-02: Scope "first formulation" claims to specific combination in intro, conclusion
- [ ] M4-01: Add units table, fix ρ/ρ^P/ρ^D notation, unify seconds/minutes across paper
- [ ] M4-02: Unify British→American spelling throughout all sections
- [ ] MINOR-01: Add missing references (McFadden 1974, Train 2009, etc.) if not in bib
- [ ] MINOR-02: Fix LaTeX overfull/float warnings, add missing std in tables

### Active (code v6.0)

- [ ] CODE-01: Change alns_iterations 5→50 in FullModel and AblationNoChoice variants
- [ ] CODE-02: Add max(1.0, ...) guard on detour ratio in metrics.py
- [ ] CODE-03: Document unit scaling in variants.py _scale_ptype and pre-filtering mechanism
- [ ] CODE-04: Rerun all experiments — synthetic, Beijing, MILP gap, Pareto, weight sensitivity, matched coverage
- [ ] CODE-05: Regenerate data-dependent figures (fig04, fig05, fig07)
- [ ] CODE-06: Update response_to_reviewers.tex with point-by-point Round 1 responses

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
*Last updated: 2026-04-27 — v6.0 milestone started (Round 1 review revision: 4 CRITICAL + 4 MAJOR fixes, model unification, experiment rerun, resubmission prep)*
