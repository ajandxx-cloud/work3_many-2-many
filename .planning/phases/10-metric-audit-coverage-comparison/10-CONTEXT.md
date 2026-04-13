# Phase 10: Metric Audit & Coverage Comparison - Context

**Gathered:** 2026-04-13
**Status:** Ready for planning
**Mode:** Auto-generated (pure computation + paper-writing phase)

<domain>
## Phase Boundary

Fix the vkm/trip metric denominator throughout the paper and add a matched-coverage experiment. Every efficiency number must use vkm / (n_requests × acceptance_rate). The three inconsistent numbers (abstract: 2383.85 vs 3662.33; main table: 3022 vs 4268; Gamma-sweep: 9.893) must be reconciled. A new matched-coverage experiment runs DoorToDoor with a rejection penalty calibrated to match FullModel's ~20% served share, and Section 5.2 + abstract are rewritten to use this as the primary efficiency claim.

</domain>

<decisions>
## Implementation Decisions

### Metric Correction
- Correct denominator: vkm / (n_requests × acceptance_rate) — NOT vkm / acceptance_rate
- With n_requests=200: FullModel = 628.5 / (200 × 0.208) = 628.5 / 41.6 ≈ 15.1 vkm/trip; DoorToDoor = 2603.7 / (200 × 0.610) = 2603.7 / 122 ≈ 21.3 vkm/trip
- Abstract numbers (2383.85 vs 3662.33) are from a different scenario — must identify which scenario and apply same correction, or remove and replace with main-table numbers
- Gamma-sweep value (9.893) must also be recomputed with correct denominator

### Matched-Coverage Experiment
- Run DoorToDoor with rejection_penalty calibrated so served_share ≈ 0.20 (matching FullModel's ~20%)
- Compare vkm/trip at equal coverage — this is the primary efficiency claim
- Add as new Table in Section 5.2 or replace existing efficiency paragraph
- Python implementation: add `matched_coverage_experiment()` to experiments/variants.py or new file

### Paper Updates
- Section 5.2: rewrite efficiency paragraph using matched-coverage result as primary claim
- Abstract: rewrite efficiency sentence with correct metric and matched-coverage result
- All tables: audit every vkm/trip cell and recompute
- response_to_reviewers.tex: note metric correction in FIX-01 response

### Claude's Discretion
All implementation choices (file structure, function naming, table formatting) are at Claude's discretion.

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `experiments/variants.py` — FullModel and DoorToDoor variant classes with `gamma` parameter
- `experiments/metrics.py` — MetricsResult dataclass with acceptance_rate, total_vkm fields
- `experiments/pareto_sweep.py` — existing sweep infrastructure (seeds, scale, CSV output)
- `results/pareto_gamma_sweep.csv` — existing results with served_share=0.183, vkm=9.893

### Established Patterns
- Experiments write CSV/JSON to `results/` directory
- Paper sections in `paper/sections/*.tex`
- Seeds: [42, 43, 44], scale: 200 requests, 15 vehicles

### Integration Points
- `paper/sections/experiments.tex` — Section 5.2 efficiency paragraph and tables
- `paper/sections/abstract.tex` — abstract efficiency claim
- `paper/response_to_reviewers.tex` — FIX-01 response section

</code_context>

<specifics>
## Specific Ideas

- The matched-coverage experiment should sweep DoorToDoor rejection_penalty until served_share ≈ 0.20 (binary search or grid search over penalty values)
- Report: at equal ~20% served share, FullModel vkm/trip vs DoorToDoor vkm/trip
- This directly answers the Codex reviewer's concern about coverage-confounded efficiency

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>
