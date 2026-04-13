# Phase 13: Paper Fixes & Literature Update - Context

**Gathered:** 2026-04-13
**Status:** Ready for planning

<domain>
## Phase Boundary

Fix all stale numbers throughout the paper (intro, abstract, conclusion), add behavioral consistency materials (units/variables table, worked utility example, commitment assumption paragraph), integrate Fielbaum et al. (2021) into the literature review, and add ± notation to Table 1. All changes are pure LaTeX edits — no new experiments required.

</domain>

<decisions>
## Implementation Decisions

### Text Fixes (Old Numbers + Abstract)
- Replace old numbers in intro.tex: use v3.0 numbers — "15.1 vs 21.3 vkm/trip (29.2% improvement)" for unconstrained comparison; "11.1 vs 17.1 vkm/trip (35.0% improvement) at equal ~23% served share" for endogenous comparison
- Update abstract (paper/sections/abstract.tex): lead with endogenous 35.0% as primary claim; post-hoc 74.3% moves to a parenthetical or footnote reference
- Fix conclusion.tex: replace "2383.85 vs 3662.33" and "34.9%" with v3.0 numbers throughout
- Grep-verify after all fixes: confirm "2383.85", "3662.33", "34.9" do not appear anywhere in paper/

### Behavioral Consistency Materials
- Units/variables table: add as appendix in paper/main.tex (tab:notation); already referenced in model.tex:465 — create the actual table content
- Worked utility example: add at end of Section 4.2 in paper/sections/model.tex, after the beta parameter equations (after line ~290); use concrete numbers from the parameter table
- Commitment assumption paragraph: add in paper/sections/algorithm.tex after the "committed nodes" sentence (around line 174-177); clarify that accepted offers are committed and not re-optimized after acceptance
- Table 1 ± notation: add ± std to acceptance rate, vkm, and vkm/trip columns; compute std from seeds 42/43/44 using results/synthetic_results.csv

### Literature Update (Fielbaum et al. 2021)
- Cite Fielbaum et al. (2021) in paper/sections/literature.tex, Section 2.2 (meeting-point DRT subsection), after the Cortenbach 2024 discussion
- Positioning sentence: "Fielbaum et al. (2021) studied bidirectional walking flexibility in ridepooling, showing that allowing passengers to walk to both pickup and dropoff points reduces vehicle detours; our work extends this to the many-to-many DRT setting with explicit passenger choice and online re-optimization."
- Update paper/response_to_reviewers.tex: add a note that Fielbaum et al. (2021) has been added to Section 2.2 in response to the GPT-5 review
- Add 3-seed justification note in Section 5.1 of experiments.tex: one sentence — "Results are averaged over three random seeds (42, 43, 44); standard deviations are reported in Table~\ref{tab:results}."

### Claude's Discretion
- Exact wording of the worked utility example (use beta values already in model.tex)
- Exact column format for ± in Table 1 (e.g., "0.208 ± 0.012" or "$0.208 \pm 0.012$")
- Whether to add a brief appendix header or integrate notation table inline

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `paper/sections/intro.tex` — contains old numbers at lines 83-84 (2383.85, 3662.33, -34.9%)
- `paper/sections/conclusion.tex` — contains old numbers at lines 14-15, 28
- `paper/sections/abstract.tex` — contains post-hoc 74.3%/10.9/42.3 as primary claim
- `paper/sections/experiments.tex` — Table 1 at lines 86-99; Section 5.1 for 3-seed note; Section 5.2 already updated with endogenous numbers
- `paper/sections/model.tex` — beta parameters at lines ~263-290; notation table reference at line 465
- `paper/sections/algorithm.tex` — committed nodes sentence at lines 174-177
- `paper/sections/literature.tex` — Section 2.2 for Fielbaum citation (currently absent)
- `paper/references.bib` — Fielbaum 2021 entry already exists at line 309
- `results/synthetic_results.csv` — per-seed data for computing ± std values

### Established Patterns
- LaTeX citation style: `\citet{key}` for inline, `\citep{key}` for parenthetical
- Table format: `\begin{tabular}{lccccccc}` with `\toprule/\midrule/\bottomrule`
- ± notation: `$X \pm Y$` format used in MILP table (line 122-123 of experiments.tex)
- Appendix: main.tex likely has `\appendix` section

### Integration Points
- `paper/sections/abstract.tex` — update primary claim numbers
- `paper/sections/intro.tex` — fix old numbers (lines 83-84)
- `paper/sections/conclusion.tex` — fix old numbers (lines 14-15, 28)
- `paper/sections/model.tex` — add worked utility example + notation table
- `paper/sections/algorithm.tex` — add commitment assumption paragraph
- `paper/sections/literature.tex` — add Fielbaum citation in Section 2.2
- `paper/sections/experiments.tex` — add ± to Table 1, add 3-seed note in Section 5.1
- `paper/response_to_reviewers.tex` — note Fielbaum addition

</code_context>

<specifics>
## Specific Ideas

- v3.0 correct numbers: FullModel 15.1 vkm/trip, DoorToDoor 21.3 vkm/trip (29.2% unconstrained); FullModel 11.1 vkm/trip, DoorToDoor(capped) 17.1 vkm/trip (35.0% endogenous at ~23% served share)
- Old numbers to eliminate: "2383.85", "3662.33", "34.9%", "-34.9%"
- Fielbaum bib key: `fielbaum2021` (confirmed in references.bib line 309)
- Beta values for worked example: walk-sensitive type has β_walk=-0.020, β_wait=-0.04, β_ivt=-0.02, β_price=-0.05 (from model.tex lines 275-276)
- Seeds for std computation: 42, 43, 44 — data in results/synthetic_results.csv

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 13-paper-fixes-literature-update*
*Context gathered: 2026-04-13 via smart discuss (autonomous mode)*
