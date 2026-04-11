# Phase 1: Problem Formulation & Model Structure - Context

**Gathered:** 2026-04-11
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 1 delivers the complete mathematical foundation of the paper: the many-to-many DRT problem with bidirectional meeting points (M_r^P, M_r^D) is formally defined, notation is fixed and consistent throughout, all operational constraints are enumerated with corresponding mathematical expressions, and the three-layer coupled model (service generation → passenger response → dynamic dispatch) is documented in a self-contained LaTeX model writeup ready to hand off to the algorithm phase.

</domain>

<decisions>
## Implementation Decisions

### Spatial & Network Representation
- Euclidean distance model for travel times and walking distances — avoids network data dependency, standard for DARP literature
- Pre-defined fixed meeting point set (bus stops, landmarks) — more realistic for Chinese DRT practice, discrete candidate sets align with PROB-01 formulation
- Continuous time representation — standard for DARP exact formulations; allows precise time window constraints
- Directed graph for vehicle routing — more realistic for urban road networks with asymmetric travel times

### Model Formalization Output
- Primary output format: LaTeX (.tex) — directly usable in paper, standard for academic math typesetting
- Document structure: standalone model document (model.tex) that feeds into paper Sections 3–4 — clean separation, avoids premature section-level organization before algorithms are fixed
- Include a full notation table/glossary — essential for cross-phase consistency; Phase 2 (algorithm) will reference these symbols directly
- Full mathematical expressions for all constraints (capacity, time windows, ride time, walking radius, precedence) — required for clean MILP formulation in Phase 2

### Three-Layer Model Architecture
- Sequential coupling with feedback loop: service generation → passenger response → dispatch, with re-optimization — matches rolling horizon architecture committed to in REQUIREMENTS
- Service generation: top-k candidates filtered by walking radius and time window — computationally tractable; directly maps to HEUR-01
- Passenger response: probabilistic MNL (core dissertation thread, non-negotiable per REQUIREMENTS and CLAUDE.md)
- Dispatch trigger: periodic rolling horizon (every Δ minutes) — matches HEUR-04, standard in 2024–2025 dynamic DRT literature (Wu et al.)

### Notation & Indexing Conventions
- Request index: r — consistent with REQUIREMENTS.md notation already established (M_r^P, M_r^D, v_r, π_r^P, π_r^D)
- Pickup/dropoff superscripts: P/D — already used throughout REQUIREMENTS.md; maintain consistency
- Vehicle index: v — already used in decision vector (v_r) in REQUIREMENTS.md
- Time window notation: [e_r, l_r] (earliest, latest) — standard DARP notation

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- No existing codebase — this is a new academic paper project starting from scratch
- Work 1 (DRPO framework, TR Part C) and Work 2 (service menu design) are prior works in the dissertation series; their notation conventions should be reviewed for consistency

### Established Patterns
- REQUIREMENTS.md already establishes core notation: M_r^P, M_r^D, b = (m_r^P, m_r^D, τ_r, p_r), objective C^op + C^wait + C^walk + C^IVT + C^rej, decision vector (z_r, m_r^P, m_r^D, v_r, π_r^P, π_r^D)
- MNL utility: U_rb = β1·Walk_rb + β2·Wait_rb + β3·IVT_rb + β4·p_r + ε (from CHOICE-01)
- Choice probability: P_rb = exp(U_rb) / (exp(U_r0) + Σ exp(U_rb)) (from CHOICE-04)
- Key references already identified: Cortenbach et al. (2024, TR Part C), Wu et al. (2025, TR Part E)

### Integration Points
- Phase 2 (Algorithm) will import the model.tex notation table and constraint formulations directly
- Phase 5 (Paper Writing) will incorporate model.tex into Section 3 (Problem Formulation) and Section 4 (Model)
- The three-layer model architecture description feeds directly into the algorithm flowchart (FIG-03, Phase 6)

</code_context>

<specifics>
## Specific Ideas

- Passenger heterogeneity: at least 2-3 types (price-sensitive, time-sensitive, walk-sensitive) as specified in CHOICE-03 — these types should be named and their β parameter profiles sketched in Phase 1 so Phase 2 can simulate them correctly
- Outside option: U_r0 (reject all offers) must be formally included in the choice set — critical for realistic acceptance rate modeling
- The service offer bundle b = (m_r^P, m_r^D, τ_r, p_r) is the central object — formalize this as a tuple with clear domains for each component
- Precedence constraint: pickup node must appear before dropoff node in every route — ensure this is listed explicitly among Phase 1 constraints

</specifics>

<deferred>
## Deferred Ideas

- Anticipatory/lookahead extensions — noted in REQUIREMENTS as EXT-01, out of scope for Phase 1
- Electric vehicle charging constraints — EXT-03, post-submission extension
- Real data validation scenarios — EXT-04, out of scope

</deferred>
