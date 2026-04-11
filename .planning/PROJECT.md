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

## Requirements

### Validated

(None yet — paper not started)

### Active

- [ ] Problem formulation: many-to-many DRT with bidirectional meeting points + passenger choice
- [ ] Mathematical model: three-layer coupled model (service generation → passenger response → dynamic dispatch)
- [ ] Small-scale exact algorithm (MILP/branch-and-cut) for benchmark validation
- [ ] Large-scale heuristic: online insertion + rolling horizon + ALNS
- [ ] Numerical experiments: synthetic scenario + semi-realistic case (Chinese city)
- [ ] Comparison baselines: door-to-door, single-sided meeting point, no passenger choice, full model
- [ ] Policy analysis: sensitivity to demand density, walking tolerance, fleet size, city type
- [ ] Paper writing: all sections (intro, literature, model, algorithm, experiments, conclusion)
- [ ] Academic figures: system diagram, algorithm flowchart, result charts (Python/matplotlib)

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
- **Passenger choice**: Must retain MNL passenger choice model — core dissertation thread
- **Policy framing**: TR Part A requires policy implications beyond pure optimization
- **Language**: English (academic paper)

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Target TR Part A not TR Part C | Policy framing differentiates from Work 1 (TR Part C); TR Part A accepts optimization papers with strong policy angle | — Pending |
| Fix price, don't optimize it | Avoid overlap with Work 1/2; keep Work 3 focused on bidirectional spatial assignment | — Pending |
| Rolling horizon + ALNS as main heuristic | Standard in dynamic DRT literature 2024-2025; matches dissertation framework | — Pending |
| Simulation-based validation | Standard for DARP; real data hard to obtain; consistent with Work 1 approach | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition:**
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions

---
*Last updated: 2026-04-11 after initialization*
