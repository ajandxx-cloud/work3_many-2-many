# Phase 12: Endogenous Matched-Coverage Experiment - Context

**Gathered:** 2026-04-13
**Status:** Ready for planning

<domain>
## Phase Boundary

Implement `DoorToDoorCapped` — a DoorToDoor variant with an endogenous acceptance cap — run it for seeds 42/43/44 at n=200/15 vehicles, and update Section 5.2 to present the endogenous result as the primary efficiency claim. The post-hoc 74.3% result is retained as a supplementary lower-bound footnote.

This replaces the post-hoc random rejection approach in `experiments/matched_coverage.py` with a credible endogenous comparison where DoorToDoor re-routes with a served-share cap.

</domain>

<decisions>
## Implementation Decisions

### DoorToDoorCapped Implementation Strategy
- Implement as a new class in `experiments/variants.py` — consistent with all other variants (DoorToDoor, SingleSidedPickup, etc.)
- Cap enforcement: count accepted requests; once `accepted_count / n_requests >= cap_share`, reject all subsequent requests without route insertion (ALNS continues optimizing routes for already-accepted passengers)
- Cap target: computed dynamically at runtime — run FullModel first (seeds 42/43/44), compute mean served_share, pass as `cap_share` to DoorToDoorCapped
- Re-routing after cap: Yes — ALNS continues optimizing routes for already-accepted passengers; only new requests are rejected

### Experiment Runner & Output
- New file: `experiments/endogenous_matched_coverage.py` — mirrors `matched_coverage.py` structure
- Output columns: `variant, seed, served_share, vkm_per_trip` (no `rejection_penalty` — not applicable to endogenous approach)
- Output path: `results/endogenous_matched_coverage.csv` — distinct from existing `matched_coverage.csv`
- Cap computation: run FullModel first for all seeds, compute mean served_share, pass dynamically to DoorToDoorCapped

### Section 5.2 Paper Update
- Endogenous result is the primary claim — replace post-hoc 74.3% as the main evidence; move post-hoc to footnote as "conservative lower bound"
- Update `tab:matched-coverage` in `paper/sections/experiments.tex`: replace `DoorToDoor (matched)` row with `DoorToDoor (capped)` row using new numbers
- Assert ±3pp tolerance in experiment script: `abs(mean_dtd_share - mean_fm_share) <= 0.03`; warn if outside but still write CSV
- If outside ±3pp: warn in script output, still write CSV, note in paper that cap converged to within X pp

### Claude's Discretion
- Exact class signature for `DoorToDoorCapped.__init__` (e.g., `cap_share: float` parameter)
- Whether to add `DoorToDoorCapped` to the variant name registry assertion in `variants.py`
- Exact wording of the footnote for the post-hoc 74.3% result in experiments.tex

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `DoorToDoor` class in `experiments/variants.py` — base implementation to extend; uses `greedy_insertion` with synthetic MPs at origin/destination
- `ALNSState`, `RollingHorizon`, `greedy_insertion` in `src/drt/alns.py` — ALNS infrastructure
- `experiments/matched_coverage.py` — existing post-hoc experiment structure to mirror for the new endogenous version
- `experiments/config.py` — `SEEDS = [42, 43, 44]`, `VEHICLE_COUNTS = {200: 15}`, `SCALES`
- `experiments/metrics.py` — `vkm_per_trip()` helper, `SimulationResult`, `PassengerRecord`
- `experiments/scenarios.py` — `generate_synthetic()` for scenario generation

### Established Patterns
- All variants inherit from `BaseVariant` and implement `run(scenario) -> SimulationResult`
- Variant names are asserted unique at module load (Threat T-03-07 mitigation)
- Experiment scripts follow: run baseline → calibrate/configure variant → write CSV → print summary
- `vkm_per_trip(total_vehicle_km, n_requests, acceptance_rate)` is the correct metric denominator

### Integration Points
- `experiments/variants.py` — add `DoorToDoorCapped` class here
- `experiments/endogenous_matched_coverage.py` — new experiment script (new file)
- `results/endogenous_matched_coverage.csv` — output (new file)
- `paper/sections/experiments.tex` — update Section 5.2 and `tab:matched-coverage`

</code_context>

<specifics>
## Specific Ideas

- FullModel mean served_share from existing results: seeds 42/43/44 at n=200 → 22.5%, 25.5%, 22.5% → mean ≈ 23.5% (from `results/matched_coverage.csv`)
- Existing post-hoc result for reference: FullModel 10.9 vkm/trip, DoorToDoor_matched 42.3 vkm/trip (74.3% improvement at ~23.5% share)
- Success criterion: mean served_share of DoorToDoorCapped within ±3pp of FullModel mean (~23.5%)
- The cap mechanism: DoorToDoor processes requests sequentially; once `accepted_count / total_requests >= cap_share`, subsequent requests are rejected without insertion attempt

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>
```

---

*Phase: 12-endogenous-matched-coverage-experiment*
*Context gathered: 2026-04-13 via smart discuss (autonomous mode)*
