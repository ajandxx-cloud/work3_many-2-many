# Phase 5: Paper Writing — Context

**Gathered:** 2026-04-12
**Status:** Ready for planning
**Source:** Discuss-phase answers

<domain>
## Phase Boundary

Phase 5 delivers a complete, submission-ready LaTeX draft of the full academic paper targeting Transportation Research Part A: Policy and Practice. All sections from abstract through conclusion are written in academic English, with a real BibTeX reference file (50-80 citations). Figure placeholders are included in the text; actual figures are produced in Phase 6.

This phase depends on Phases 1–4 being complete (they are). The paper synthesizes:
- Phase 1: LaTeX model fragments (model/*.tex) — notation, problem definition, constraints, choice model, three-layer model
- Phase 2: Algorithm description (MILP + ALNS rolling horizon)
- Phase 3: Numerical experiment results (results/metrics_table.csv, results/synthetic_results.csv, results/beijing_results.csv)
- Phase 4: Sensitivity analysis + equity analysis + policy recommendations (results/sensitivity_walk.csv, results/sensitivity_fleet.csv, results/equity_table.csv, results/policy_recommendations.md)

</domain>

<decisions>
## Implementation Decisions

### Paper Format
- LaTeX (.tex files) — consistent with Phase 1 model fragments; ready for TR Part A submission
- Main file: paper/main.tex (compilable with pdflatex)
- Sections as separate files: paper/sections/abstract.tex, intro.tex, literature.tex, model.tex, algorithm.tex, experiments.tex, policy.tex, conclusion.tex
- References: paper/references.bib (real BibTeX entries, 50-80 citations)
- Style: Elsevier elsarticle class (standard for TR Part A)

### References
- Real BibTeX entries — generate 50-80 plausible academic citations covering:
  - DARP/DRT literature (Cordeau & Laporte 2007, Molenbruch et al. 2017, etc.)
  - Meeting point / virtual stop literature (Stiglic et al. 2015, 2018; Cortenbach et al. 2024)
  - Passenger choice in DRT (MNL models, discrete choice)
  - Dynamic scheduling / rolling horizon
  - Chinese city DRT context
  - Work 1/2 self-citations (placeholder entries)
- BibTeX keys follow author-year convention (e.g., cortenbach2024, wu2025)

### Plan Structure (5 plans)
- Plan 01: Front matter — abstract.tex, intro.tex (PAPER-01, PAPER-02)
- Plan 02: Literature review — literature.tex (PAPER-03)
- Plan 03: Model + algorithm sections — model.tex, algorithm.tex (PAPER-04, PAPER-05, PAPER-06)
- Plan 04: Experiments + policy sections — experiments.tex, policy.tex (PAPER-07, PAPER-08)
- Plan 05: Back matter + assembly — conclusion.tex, references.bib, main.tex compilation (PAPER-09, PAPER-10)

### Writing Quality
- Submission-ready academic English at TR Part A standard
- All tables from Phase 3/4 results reproduced as LaTeX tabular environments
- Figure placeholders: \begin{figure}[h]\centering[FIGURE X PLACEHOLDER]\caption{...}\label{fig:...}\end{figure}
- No actual figures in Phase 5 (Phase 6 produces them)

### Paper Structure
- Elsevier elsarticle two-column format
- Sections: Abstract | 1. Introduction | 2. Literature Review | 3. Problem Formulation | 4. Solution Methodology | 5. Numerical Experiments | 6. Policy Implications | 7. Conclusion | References
- Keywords: demand-responsive transit; meeting points; passenger choice; ALNS; rolling horizon; equity

### Key Results to Present
- FullModel vkm/acceptance = 2383.85 vs DoorToDoor 3662.33 (−34.9% vehicle efficiency gain)
- Equity: Gini=0.1216; price_sensitive=25.4%, walk_sensitive=20.2%, time_sensitive=14.4% acceptance
- Walking tolerance: rho=1000m is minimum viable threshold for bidirectional DRT
- Fleet size: diminishing returns beyond 20 vehicles for 200-request scenario
- 5 policy recommendations for Chinese city DRT operators

### Claude's Discretion
- Exact word count per section (target: ~8000 words total body text)
- Specific paragraph structure within sections
- Which 50-80 references to include (must cover required literature areas)
- Exact table formatting choices within LaTeX

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Phase 1 Model Fragments (source of truth for notation and formulation)
- `model/notation.tex` — authoritative symbol table (53 symbols)
- `model/problem-definition.tex` — network, M_r^P/M_r^D, objective, decision vector
- `model/constraints.tex` — 14 labeled constraints across 7 classes
- `model/choice-model.tex` — MNL utility, outside option, 3 passenger types, β values
- `model/three-layer.tex` — three-layer coupled model description

### Phase 3/4 Results (source of truth for numbers)
- `results/metrics_table.csv` — 6 variants × 9 metrics (mean/std); use these exact numbers
- `results/sensitivity_walk.csv` — walking tolerance sweep results
- `results/sensitivity_fleet.csv` — fleet size sweep results
- `results/equity_table.csv` — per-type acceptance rates + Gini
- `results/policy_recommendations.md` — 5 structured policy recommendations (use as source for policy section)

### Project State
- `.planning/STATE.md` — key decisions and accumulated context
- `.planning/REQUIREMENTS.md` — PAPER-01..10 requirements

</canonical_refs>

<specifics>
## Specific Ideas

### Contributions (Introduction)
The paper claims 4 contributions:
1. First formulation of many-to-many DRT with bidirectional meeting point sets (M_r^P, M_r^D) and MNL passenger choice as a coupled three-layer model
2. MILP exact benchmark + rolling horizon ALNS heuristic for the bidirectional DARP with choice
3. Empirical demonstration of −34.9% vehicle efficiency gain over door-to-door baseline
4. Equity analysis across passenger types + 5 actionable policy recommendations for Chinese city DRT

### Research Gap (Introduction)
- Cortenbach et al. (2024, TR Part C): DARPmp with single-sided meeting points, no passenger choice
- Wu et al. (2025, TR Part E): dynamic DRT with rolling horizon, no meeting points
- Gap: no work combines bidirectional meeting points + passenger choice + rolling horizon in many-to-many DRT

### Abstract Target
≤250 words; cover: motivation (DRT efficiency in low-density areas), method (bidirectional MPs + MNL + ALNS), key result (−34.9% vkm efficiency), policy implication (deployment thresholds for Chinese cities)

</specifics>

<deferred>
## Deferred Ideas

- Actual figure files (Phase 6)
- Supplementary material / appendix (not required for TR Part A submission)
- Response letter / cover letter (post-submission)

</deferred>

---

*Phase: 05-paper-writing*
*Context gathered: 2026-04-12 via discuss-phase*
