---
phase: 09-paper-section-updates
plan: "02"
subsystem: paper
tags: [vot, mnl, policy, reviewer-response, latex]
dependency_graph:
  requires: []
  provides: [tab:vot-mapping, subsec:vot-mapping, model-footnote-vot]
  affects: [paper/sections/policy.tex, paper/sections/model.tex, paper/references.bib]
tech_stack:
  added: []
  patterns: [VOT derivation from MNL beta ratios, LaTeX multirow table]
key_files:
  created: []
  modified:
    - paper/sections/policy.tex
    - paper/sections/model.tex
    - paper/references.bib
decisions:
  - "Walk VOT values honestly reported as above literature range with unit-mismatch explanation; wait/IVT VOT used as primary policy benchmarks"
  - "Walk-sensitive type identified as most policy-relevant comparator for bidirectional DRT"
metrics:
  duration: ~10min
  completed: 2026-04-12
  tasks_completed: 2
  files_modified: 3
---

# Phase 09 Plan 02: VOT Mapping Table and Beta Plausibility Footnote Summary

VOT mapping table (REV-11) and MNL parameter plausibility footnote (REV-13) added, grounding the paper's objective weights and beta parameters in Chinese urban VOT literature (Shao et al. 2017, Li et al. 2020).

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Add VOT mapping table to policy.tex (REV-11) | 8ba713e | paper/sections/policy.tex |
| 2 | Add VOT plausibility footnote to model.tex (REV-13) | 8ba713e | paper/sections/model.tex, paper/references.bib |

## What Was Built

**policy.tex** — new `\subsection{Objective Weight Interpretation via Value of Time}\label{subsec:vot-mapping}` appended after the Deployment summary paragraph. Contains:
- VOT derivation equation (Eq. eq:vot-formula) for wait, IVT, and walk attributes
- Table `tab:vot-mapping`: 3-passenger-type implied VOT vs. literature benchmark (Shao et al. 2017; Li et al. 2020)
- Interpretation paragraph honestly noting that walk VOT exceeds literature range due to unit mismatch (beta_1 in utility/meter vs. literature in CNY/min), and directing operators to use wait/IVT VOT as primary benchmarks

**model.tex** — footnote appended to the sentence ending "...low-density urban areas" in the Passenger Heterogeneity subsection. Footnote reports VOT_wait=0.80 and VOT_IVT=0.40 CNY/min for walk-sensitive type (within literature range), explains walk VOT inflation, and cross-references tab:vot-mapping.

**references.bib** — added `shao2017` and `li2020drt` entries (no pre-existing keys, no duplicates).

## VOT Arithmetic (verified, threat T-09-04)

| Type | Walk (CNY/min) | Wait (CNY/min) | IVT (CNY/min) |
|------|---------------|----------------|---------------|
| Price-sensitive | (0.005/0.15)×80 = 2.667 | 0.04/0.15 = 0.267 | 0.02/0.15 = 0.133 |
| Time-sensitive  | (0.005/0.03)×80 = 13.333 | 0.10/0.03 = 3.333 | 0.08/0.03 = 2.667 |
| Walk-sensitive  | (0.020/0.05)×80 = 32.000 | 0.04/0.05 = 0.800 | 0.02/0.05 = 0.400 |
| Literature (Shao 2017 / Li 2020) | 0.4–0.6 | 0.8–1.2 | 0.2–0.4 |

## Deviations from Plan

None — plan executed exactly as written. The plan's own note about high walk VOT was incorporated honestly into the interpretation paragraph and footnote.

## Known Stubs

None. Both additions are complete analytical content with no placeholder text.

## Self-Check: PASSED
