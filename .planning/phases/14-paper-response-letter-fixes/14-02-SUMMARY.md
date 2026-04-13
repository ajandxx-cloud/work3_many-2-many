---
phase: 14-paper-response-letter-fixes
plan: "02"
subsystem: paper
tags: [response-letter, cleanup, tex-edits]
dependency_graph:
  requires: ["14-01"]
  provides: ["clean-response-letter", "clean-experiments", "clean-model"]
  affects: ["paper/response_to_reviewers.tex", "paper/sections/experiments.tex", "paper/sections/model.tex"]
tech_stack:
  added: []
  patterns: ["LaTeX text substitution", "grep-verified edits"]
key_files:
  modified:
    - paper/response_to_reviewers.tex
    - paper/sections/experiments.tex
    - paper/sections/model.tex
decisions:
  - "11.1 vs 17.1 vkm/trip (35.0%) is the primary efficiency claim; 74.3% post-hoc figure demoted to footnote"
  - "sec:policy replaces subsec:vot-mapping as the cross-reference target in model.tex footnote"
metrics:
  duration: "~10 minutes"
  completed: "2026-04-13"
  tasks_completed: 3
  tasks_total: 3
  files_modified: 3
requirements:
  - RESP-01
  - RESP-02
  - CLEAN-01
  - CLEAN-02
  - CLEAN-03
---

# Phase 14 Plan 02: Response Letter Fixes and Pre-Submission Cleanup Summary

Five targeted edits across three files to produce a clean, internally consistent submission package.

## Tasks Completed

| Task | Description | Commit | Requirements |
|------|-------------|--------|--------------|
| 1 | Fix R1 body (15.1/21.3 vkm/trip) and rewrite FIX-02 block (11.1 vs 17.1, 35.0% primary; 74.3% to footnote) | 497aa33 | RESP-01, RESP-02 |
| 2 | Remove METRIC AUDIT comment block from experiments.tex | 24f57d7 | CLEAN-01 |
| 3 | Remove "(provisional)" annotation and fix subsec:vot-mapping → sec:policy in model.tex | ded3957 | CLEAN-02, CLEAN-03 |

## Verification Results

| Check | Result |
|-------|--------|
| `grep "3{,}022\|4{,}268" response_to_reviewers.tex` | 0 matches (PASS) |
| `grep "11\.1" response_to_reviewers.tex` | line 161 in FIX-02 block (PASS) |
| `grep "35\.0" response_to_reviewers.tex` | line 163 in FIX-02 block (PASS) |
| `grep "15\.1" response_to_reviewers.tex` | line 63 in R1 body (PASS) |
| `grep "74\.3" response_to_reviewers.tex` | line 169 — footnote only (PASS) |
| `grep "METRIC AUDIT" experiments.tex` | 0 matches (PASS) |
| `head -1 experiments.tex` | `\section{Numerical Experiments}` (PASS) |
| `grep "provisional" model.tex` | 0 matches (PASS) |
| `grep "subsec:vot-mapping" model.tex` | 0 matches (PASS) |
| `grep "sec:policy" model.tex` | line 300 (PASS) |

## Deviations from Plan

None — plan executed exactly as written.

## Known Stubs

None.

## Threat Flags

None — all edits are static .tex substitutions with no new network endpoints, auth paths, or schema changes.

## Self-Check: PASSED

- paper/response_to_reviewers.tex: modified (commits 497aa33)
- paper/sections/experiments.tex: modified (commit 24f57d7)
- paper/sections/model.tex: modified (commit ded3957)
- All three commits confirmed in git log
