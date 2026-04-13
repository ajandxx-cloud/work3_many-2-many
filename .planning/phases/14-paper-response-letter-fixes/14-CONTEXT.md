# Phase 14: Paper & Response Letter Fixes - Context

**Gathered:** 2026-04-13
**Status:** Ready for planning
**Mode:** Auto-generated (infrastructure phase — all fixes predetermined by success criteria)

<domain>
## Phase Boundary

Fix all numeric inconsistencies in the paper and response letter so every number matches actual experiment output, and remove all development-only annotations and comment blocks before submission. Specific targets:
- Gini coefficient: 0.1216 in policy.tex, experiments.tex, abstract.tex (no 0.122 anywhere)
- Cap target percentage: consistent across cap_share default, paper text, table caption, response letter FIX-02
- Weight-sensitivity table: column headers correctly describe denominator (vkm/trip vs raw vkm)
- response_to_reviewers.tex FIX-02: cite 11.1 vs 17.1 vkm/trip (35.0%) as primary; 74.3% as footnote
- response_to_reviewers.tex R1 body: 15.1 and 21.3 vkm/trip (not old 3022/4268 values)
- Remove METRIC AUDIT comment block (experiments.tex lines 1-13)
- Remove "(provisional)" annotation (model.tex)
- Remove/correct internal cross-reference to subsec:vot-mapping

</domain>

<decisions>
## Implementation Decisions

### Claude's Discretion
All implementation choices are at Claude's discretion — pure infrastructure phase. All target values and file locations are specified in the success criteria. Use grep to locate exact occurrences before editing.

</decisions>

<code_context>
## Existing Code Insights

### Paper Files
- paper/sections/abstract.tex — abstract (check Gini)
- paper/sections/experiments.tex — experiments section (METRIC AUDIT block lines 1-13, Gini, weight-sensitivity table)
- paper/sections/policy.tex — policy section (Gini)
- paper/sections/model.tex — model section ("(provisional)" annotation, subsec:vot-mapping cross-reference)
- paper/response_to_reviewers.tex — response letter (FIX-02 section, R1 body with old 3022/4268 values)

### Code Files
- src/drt/ — Python experiment code (cap_share default value)

### Integration Points
- All fixes are in paper/ directory and src/ directory
- No new files needed — pure editing

</code_context>

<specifics>
## Specific Ideas

All fixes are fully specified by the success criteria. No additional requirements.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>
