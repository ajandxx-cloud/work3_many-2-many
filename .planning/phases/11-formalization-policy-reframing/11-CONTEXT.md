# Phase 11: Formalization & Policy Reframing - Context

**Gathered:** 2026-04-13
**Status:** Ready for execution
**Mode:** Auto-generated (pure LaTeX text insertion phase)

<domain>
## Phase Boundary

Add two formalization elements (timing/decision diagram, ALNS objective statement) and soften two policy thresholds to scenario-specific findings. Update the reviewer response document with all v3.0 changes. All changes are pure LaTeX text insertions — no Python, no figures, no compilation required.

</domain>

<decisions>
## Implementation Decisions

### FORM-01: Timing/Decision Table
- Use LaTeX table (not figure) — no Python/matplotlib dependency
- Insert after `\end{table}` of `tab:layer-coupling`, before "The three-layer architecture captures..."
- 5 columns: Event / Layer / Decision Variables / Information Flow / Bernoulli Sampling?
- 5 rows covering the full planning cycle
- Add cross-reference sentence after table

### FORM-02: ALNS Objective Paragraph
- Use `\paragraph{Online Objective.}` (not a new \subsubsection)
- Insert between subsection intro sentence and `\subsubsection{Candidate Generation}`
- Equation `eq:alns-objective`: E[ΔC | b, x_r] = P_accept(b*) × ΔC_routing
- Three enumerated bullets: (1) Bernoulli after selection, (2) Γ excluded from bundle selection, (3) rolling horizon objective

### PFRAM-01/02: Policy Caveats
- Add `\paragraph{Generalizability caveat.}` after each Policy implication paragraph
- R1 caveat: names synthetic scenario dimensions, MNL calibration, pedestrian infrastructure, local surveys
- R2 caveat: "order-of-magnitude guideline", demand clustering, temporal patterns

### PFRAM-03: Reviewer Response
- Add `\section*{v3.0 Revisions (Second Round)}` with five `\subsection*{FIX-NN}` entries
- Insert between v2.0 closing sentence and `\bigskip\bigskip` before author block
- Do NOT use `\ref{tab:timing-diagram}` in standalone document — use prose "Table~5 in the revised manuscript"

### Claude's Discretion
All formatting details (table column widths, spacing) are at Claude's discretion.

</decisions>

<code_context>
## Existing Code Insights

### Key Phase 10 Results (already in the paper)
- Corrected vkm/trip: FullModel 15.1, DoorToDoor 21.3 (29.2% improvement, unconstrained)
- Matched-coverage: FullModel 10.9 vs DoorToDoor 42.3 vkm/trip at equal ~23.5% served share (74.3% improvement)
- `experiments/matched_coverage.py` — post-hoc rejection calibration
- `results/matched_coverage.csv` — 6 rows (3 seeds × 2 variants)

### Integration Points
- `paper/sections/model.tex` — Three-layer model section (tab:layer-coupling at ~line 401–414)
- `paper/sections/algorithm.tex` — Rolling Horizon ALNS subsection (~line 74–144)
- `paper/sections/policy.tex` — R1 (lines 16–40), R2 (lines 43–66)
- `paper/response_to_reviewers.tex` — Summary of Changes section at ~line 107, author block at ~line 126

</code_context>
