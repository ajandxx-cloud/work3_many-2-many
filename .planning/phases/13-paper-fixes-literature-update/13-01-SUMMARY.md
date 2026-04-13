---
phase: 13-paper-fixes-literature-update
plan: "01"
subsystem: paper-text
tags: [text-fix, numbers, v4.0, intro, conclusion, abstract]
dependency_graph:
  requires: []
  provides: [corrected-v3.0-numbers-in-intro-conclusion-abstract]
  affects: [paper/sections/intro.tex, paper/sections/conclusion.tex, paper/sections/abstract.tex]
tech_stack:
  added: []
  patterns: [LaTeX text replacement]
key_files:
  created: []
  modified:
    - paper/sections/intro.tex
    - paper/sections/conclusion.tex
    - paper/sections/abstract.tex
decisions:
  - "35.0% endogenous matched-coverage is primary claim; 74.3% post-hoc demoted to parenthetical lower bound"
  - "Both 35.0% (endogenous) and 29.2% (unconstrained) reported in all three files for consistency"
metrics:
  duration: "~5 minutes"
  completed: "2026-04-13"
  tasks_completed: 3
  tasks_total: 3
  files_modified: 3
---

# Phase 13 Plan 01: Fix Stale Numbers in intro/conclusion/abstract Summary

One-liner: Replaced stale "2383.85 vs 3662.33 / -34.9%" figures with v3.0 endogenous matched-coverage numbers (35.0% primary, 29.2% secondary) across intro.tex, conclusion.tex, and abstract.tex; paper-wide grep confirms old numbers absent from rendered content.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Fix intro.tex contribution item 3 | f287709 | paper/sections/intro.tex |
| 2 | Fix conclusion.tex old numbers | 3838f15 | paper/sections/conclusion.tex |
| 3 | Update abstract.tex primary claim + grep-verify | 831c3d9 | paper/sections/abstract.tex |

## What Was Done

Task 1 replaced the contribution item 3 in intro.tex: the old `-34.9%` / `2383.85 vs 3662.33` wording was replaced with the v3.0 endogenous matched-coverage result (35.0%, FullModel 11.1 vs DoorToDoor(capped) 17.1 vkm/trip) plus the unconstrained comparison (29.2%, 15.1 vs 21.3 vkm/trip).

Task 2 updated two locations in conclusion.tex: the opening paragraph (Location A) and contribution item 3 (Location B), both now using the same dual-comparison framing.

Task 3 rewrote the abstract results block to lead with the endogenous 35.0% result at equal served share (~22.8%), with the unconstrained 29.2% as secondary and the post-hoc 74.3% demoted to a parenthetical conservative lower bound.

## Verification

- `grep -n "35\.0" paper/sections/intro.tex` — match at line 83 (contribution item 3)
- `grep -n "35\.0" paper/sections/conclusion.tex` — matches at lines 13 and 30 (opening paragraph + contribution item 3)
- `grep -n "35\.0" paper/sections/abstract.tex` — match at line 17 (primary claim)
- `grep -rn "2383\|3662" paper/` — one match in experiments.tex line 5, which is a LaTeX comment (`%`) and not rendered content
- `grep -rn "34\.9" paper/` — zero matches

## Deviations from Plan

None — plan executed exactly as written. The only note: `experiments.tex` line 5 contains `2383.85 vs 3662.33` inside a `%` comment (historical note left by a prior author). This is not rendered LaTeX and does not affect the paper output. No fix needed.

## Known Stubs

None.

## Threat Flags

None. All edits are local `.tex` file replacements with no new network endpoints, auth paths, or schema changes.

## Self-Check: PASSED

- paper/sections/intro.tex — FOUND, contains 35.0
- paper/sections/conclusion.tex — FOUND, contains 35.0 (2 occurrences)
- paper/sections/abstract.tex — FOUND, contains 35.0
- Commit f287709 — FOUND
- Commit 3838f15 — FOUND
- Commit 831c3d9 — FOUND
