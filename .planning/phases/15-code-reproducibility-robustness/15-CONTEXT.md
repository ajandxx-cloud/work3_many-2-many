# Phase 15: Code Reproducibility & Robustness - Context

**Gathered:** 2026-04-13
**Status:** Ready for planning
**Mode:** Auto-generated (infrastructure phase — all fixes predetermined by success criteria)

<domain>
## Phase Boundary

Fix five code robustness and reproducibility issues in the experiment codebase:
- CODE-01: SHA-256 seed replaces hash(request.id) in _mnl_filter_requests (experiments/variants.py:147)
- ROB-01: Stop ordering warning when pickup_time >= dropoff_time (experiments/variants.py:249)
- ROB-02: DoorToDoorCapped tolerance warning via warnings.warn (experiments/endogenous_matched_coverage.py:114)
- ROB-03: Empty seeds guard raises ValueError (experiments/endogenous_matched_coverage.py:84)
- ROB-04: Unassigned deduplication in DoorToDoor._solve and DoorToDoorCapped._solve

</domain>

<decisions>
## Implementation Decisions

### Claude's Discretion
All implementation choices are at Claude's discretion — pure infrastructure phase.
All target locations and behaviors are specified in the success criteria.

</decisions>

<code_context>
## Existing Code Insights

### Target Files
- experiments/variants.py — _mnl_filter_requests (line 147: hash seed), _build_records (line 249: stop ordering), DoorToDoor._solve (line 385: unassigned extend), DoorToDoorCapped._solve (line 464: unassigned extend)
- experiments/endogenous_matched_coverage.py — endogenous_matched_coverage_experiment (line 84: seeds guard, line 114: tolerance warning)

### Integration Points
- No new files needed — pure editing
- hashlib is stdlib; warnings is stdlib — no new dependencies

</code_context>

<specifics>
## Specific Ideas

All fixes are fully specified by the success criteria. No additional requirements.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>
