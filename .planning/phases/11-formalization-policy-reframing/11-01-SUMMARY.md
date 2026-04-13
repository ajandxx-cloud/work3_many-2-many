---
phase: 11-formalization-policy-reframing
plan: 01
subsystem: paper/model-and-algorithm
tags: [latex, formalization, timing-diagram, alns-objective, bernoulli]
dependency_graph:
  requires: []
  provides: [tab:timing-diagram, eq:alns-objective]
  affects: [paper/sections/model.tex, paper/sections/algorithm.tex]
tech_stack:
  added: []
  patterns: [pure-latex-insertion]
key_files:
  created: []
  modified:
    - paper/sections/model.tex
    - paper/sections/algorithm.tex
decisions:
  - "Insert timing/decision table as pure LaTeX after tab:layer-coupling table without deleting existing text"
  - "ALNS Online Objective paragraph placed between subsection intro and Candidate Generation subsubsection"
metrics:
  duration_minutes: 10
  completed_date: "2026-04-13"
  tasks_completed: 2
  tasks_total: 2
  files_changed: 2
---

# Phase 11 Plan 01: Timing Diagram and ALNS Objective Statement Summary

**One-liner:** Added tab:timing-diagram (5-event Layer 1-3 sequence with explicit Bernoulli sampling point) to model.tex and eq:alns-objective surrogate cost equation with three design-choice bullets to algorithm.tex.

## What Was Built

Two pure LaTeX text insertions addressing Codex reviewer MAJOR issues about implicit formalization:

1. **Task 1 (FORM-01) — model.tex:** Inserted `tab:timing-diagram` table immediately after the `tab:layer-coupling` table in the Layer Coupling Summary subsection. The table has 5 columns (Event / Layer / Decision Variables / Information Flow / Bernoulli?) and 5 rows covering the full request lifecycle within one planning cycle. A cross-reference sentence was appended clarifying that Bernoulli sampling occurs exclusively in Layer 2.

2. **Task 2 (FORM-02) — algorithm.tex:** Inserted a `\paragraph{Online Objective.}` block between the Rolling Horizon ALNS subsection introduction and the `\subsubsection{Candidate Generation}` heading. The paragraph contains `eq:alns-objective` (surrogate expected routing cost equation) and three enumerated design choices: (1) Bernoulli sampling after bundle selection, (2) rejection penalty Gamma excluded from bundle selection, (3) rolling horizon re-optimization minimizes the same routing cost.

## Commits

| Task | Commit | Files |
|------|--------|-------|
| FORM-01 + FORM-02 | 256fcbf | paper/sections/model.tex, paper/sections/algorithm.tex |

## Verification Results

```
model.tex FORM-01: all assertions passed
  tab:timing-diagram occurrences: 2
  Bernoulli occurrences: 5
  tab:layer-coupling occurrences: 2

algorithm.tex FORM-02: all assertions passed
  eq:alns-objective occurrences: 1
  Online Objective occurrences: 1
  Candidate Generation occurrences: 1
```

## Deviations from Plan

None - plan executed exactly as written.

## Known Stubs

None. Both insertions are complete LaTeX content with no placeholder text.

## Threat Flags

None. Both changes are pure insertions between known anchors; no new network endpoints, auth paths, or schema changes introduced.

## Self-Check: PASSED

- paper/sections/model.tex modified: confirmed (256fcbf, +80 lines)
- paper/sections/algorithm.tex modified: confirmed (256fcbf, +80 lines)
- tab:timing-diagram label present in model.tex: confirmed (2 occurrences)
- tab:layer-coupling preserved: confirmed (2 occurrences)
- Bernoulli count >= 2 in model.tex: confirmed (5 occurrences)
- eq:alns-objective present in algorithm.tex: confirmed
- Online Objective paragraph present: confirmed
- Candidate Generation subsubsection preserved: confirmed
