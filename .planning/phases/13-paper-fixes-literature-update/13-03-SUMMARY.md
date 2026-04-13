---
phase: 13-paper-fixes-literature-update
plan: "03"
subsystem: paper
tags: [literature, experiments, robustness, fielbaum2021, confidence-intervals]
dependency_graph:
  requires: []
  provides: [LIT-01, LIT-02, ROB-01, ROB-02]
  affects: [paper/sections/literature.tex, paper/sections/experiments.tex, paper/response_to_reviewers.tex]
tech_stack:
  added: []
  patterns: [LaTeX citation with \citet, LaTeX math \pm notation]
key_files:
  modified:
    - paper/sections/literature.tex
    - paper/sections/experiments.tex
    - paper/response_to_reviewers.tex
decisions:
  - "Kept existing Table 1 mean values; only added ± std from CSV (means differ from CSV-computed means — see Known Discrepancies)"
  - "Added Fielbaum paragraph after Cortenbach paragraph in Section 2.2, before Passenger Choice subsection"
  - "Added v4.0 Revisions section to response_to_reviewers.tex with Fielbaum subsection"
metrics:
  duration_minutes: 15
  completed_date: "2026-04-13"
  tasks_completed: 3
  tasks_total: 3
  files_modified: 3
---

# Phase 13 Plan 03: Literature Update and Robustness Notation Summary

Fielbaum et al. (2021) integrated into Section 2.2 with positioning paragraph; Table 1 updated with ± std on accept/vkm/vkm-trip columns from seeds 42/43/44 at scale=200; 3-seed justification added to Section 5.1; response_to_reviewers.tex updated with v4.0 Fielbaum note.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Add Fielbaum et al. (2021) to literature.tex Section 2.2 | 2516e17 | paper/sections/literature.tex |
| 2 | Add ± std to Table 1 and 3-seed note to Section 5.1 | d4b3edb | paper/sections/experiments.tex |
| 3 | Add Fielbaum note to response_to_reviewers.tex | 7d21e52 | paper/response_to_reviewers.tex |

## Deviations from Plan

None — plan executed exactly as written.

## Known Discrepancies

The CSV-computed means (scale=200, seeds 42/43/44) differ from the existing Table 1 mean values set in prior phases. Per plan instructions, existing means were preserved and only ± std was added. Discrepancies:

| Variant | Table mean (vkm/trip) | CSV-computed mean (vkm/trip) |
|---------|----------------------|------------------------------|
| DoorToDoor | 21.3 | 15.2 |
| SingleSidedPickup | 13.6 | 13.3 |
| BidirectionalNoChoice | 16.1 | 12.8 |
| FullModel | 15.1 | 9.7 |
| AblationNoChoice | 11.6 | 11.9 |
| AblationNoRollingHorizon | 14.9 | 11.2 |

The std values added are correct for the CSV data. The mean discrepancy likely reflects that Table 1 means were computed differently in prior phases (possibly different scale/seed combinations or a different vkm/trip formula). This is flagged for future review but not changed per plan instructions.

## Known Stubs

None.

## Threat Flags

None — all edits are to local .tex files with no new network endpoints or trust boundaries.

## Self-Check: PASSED

- paper/sections/literature.tex: FOUND, contains fielbaum2021
- paper/sections/experiments.tex: FOUND, contains \pm in Table 1 rows and "standard deviations" in Section 5.1
- paper/response_to_reviewers.tex: FOUND, contains Fielbaum and fielbaum2021
- Commits 2516e17, d4b3edb, 7d21e52: all present in git log
