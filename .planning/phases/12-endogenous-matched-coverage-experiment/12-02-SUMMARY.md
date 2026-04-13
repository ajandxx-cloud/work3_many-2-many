---
phase: 12-endogenous-matched-coverage-experiment
plan: "02"
subsystem: paper
tags: [experiments-tex, matched-coverage, DoorToDoorCapped, section-5-2, endogenous]
dependency_graph:
  requires: [12-01]
  provides: [updated-section-5-2, endogenous-primary-claim]
  affects: [paper/sections/experiments.tex]
tech_stack:
  added: []
  patterns: [endogenous-cap-comparison, footnote-demotion]
key_files:
  created: []
  modified:
    - paper/sections/experiments.tex
decisions:
  - "Endogenous DoorToDoorCapped result (35.0% improvement, 11.1 vs 17.1 vkm/trip) is the primary efficiency claim in Section 5.2"
  - "Post-hoc 74.3% result retained in footnote as conservative lower bound, not removed"
  - "tab:matched-coverage updated to lcc (2 data columns) — Rejection fraction column removed as not applicable to endogenous approach"
  - "Served share reported as 22.8% (FullModel mean) and 23.0% (DoorToDoorCapped mean) from actual CSV results"
metrics:
  completed_date: "2026-04-13"
  tasks_completed: 1
  tasks_total: 1
  files_created: 0
  files_modified: 1
---

# Phase 12 Plan 02: Section 5.2 Endogenous Comparison Update Summary

Section 5.2 of experiments.tex updated to present DoorToDoorCapped endogenous comparison (FullModel 11.1 vs DoorToDoorCapped 17.1 vkm/trip, 35.0% improvement) as primary efficiency claim, with post-hoc 74.3% result demoted to supplementary footnote.

## Numbers Applied

Numbers sourced from `results/endogenous_matched_coverage.csv` via `12-01-SUMMARY.md`:

| Metric | FullModel | DoorToDoorCapped |
|--------|-----------|-----------------|
| Mean vkm/trip | 11.1 | 17.1 |
| Mean served_share | 22.8% | 23.0% |
| Improvement | — | 35.0% |

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Update Section 5.2 paragraph and tab:matched-coverage in experiments.tex | 4b1ec81 | paper/sections/experiments.tex |

## Changes Made to experiments.tex

**Paragraph (lines 142-168):**
- Replaced post-hoc `matched-coverage` framing with endogenous `DoorToDoor\,(capped)` mechanism description
- New primary claim: FullModel 11.1 vs DoorToDoor\,(capped) 17.1 vkm/trip (35.0% improvement)
- Retained unconstrained comparison (15.1 vs 21.3 vkm/trip, 29.2%) as structural consistency check
- Moved 74.3% post-hoc result into `\footnote{}` as conservative lower bound reference

**Table tab:matched-coverage (lines 170-182):**
- Caption updated: "Endogenous matched-coverage comparison: FullModel vs. DoorToDoor\,(capped)"
- Column spec changed from `{lccc}` to `{lcc}` (Rejection fraction column removed)
- Row label changed from `DoorToDoor (matched)` to `DoorToDoor\,(capped)`
- Numbers updated to actual experiment results from CSV

## Acceptance Criteria Verified

| Criterion | Result |
|-----------|--------|
| `DoorToDoor\,(capped)` appears >= 2 times | 4 occurrences (paragraph x2, caption, table row) |
| `74.3` appears exactly 1 line, inside `\footnote{}` | PASS — line 166, inside footnote block |
| `post-hoc` appears inside `\footnote{}` | PASS — lines 164, 168 in footnote |
| `Rejection fraction` appears 0 times | PASS — 0 occurrences |
| `tab:matched-coverage` appears >= 2 times | PASS — lines 152, 174 |
| `endogenous` appears >= 2 times in main paragraph | PASS — 4 occurrences |
| `DoorToDoor.*matched` appears 0 times | PASS — 0 occurrences |
| Table uses `{lcc}` column spec | PASS — line 175 |

## Deviations from Plan

None — plan executed exactly as written. The actual numbers from the CSV (11.1/17.1/35.0%/22.8%/23.0%) were substituted for all ACTUAL_* placeholders as specified.

## Known Stubs

None. All numbers are wired from actual simulation results in `results/endogenous_matched_coverage.csv`.

## Threat Flags

None. No new network endpoints, auth paths, or trust boundaries introduced. LaTeX number substitution verified via grep patterns (T-12-04 mitigated).

## Self-Check: PASSED

- paper/sections/experiments.tex: modified, DoorToDoor\,(capped) present (4 occurrences)
- Commit 4b1ec81: exists (Task 1)
- 74.3 confined to footnote: verified
- Rejection fraction column: removed (0 occurrences)
- Table column spec: {lcc} confirmed at line 175
