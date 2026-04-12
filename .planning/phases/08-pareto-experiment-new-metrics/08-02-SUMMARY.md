---
phase: 08-pareto-experiment-new-metrics
plan: "02"
subsystem: paper/sections
tags: [latex, experiments, social-welfare, pareto, revision]
dependency_graph:
  requires: [08-01]
  provides: [experiments-section-5.5, W-definition, pareto-narrative]
  affects: [paper/sections/experiments.tex]
tech_stack:
  added: []
  patterns: [LaTeX table with numeric CSV values, cross-referenced subsections]
key_files:
  modified:
    - paper/sections/experiments.tex
decisions:
  - "Section 5.5 titled 'Coverage--Efficiency Analysis and Social Welfare' (not 'Pareto Frontier') to accurately reflect that gamma is post-hoc and the result is a single point, not a curve"
  - "Efficiency paragraph vkm-per-trip figures recalculated: 628.5/0.208=3022 and 2603.7/0.610=4268, giving 29.2% improvement (corrected from original 34.9%)"
  - "Table 2 caption reworded to 'Social welfare sensitivity' rather than 'Pareto frontier' to match the invariant served_share/vkm finding"
metrics:
  duration: ~10min
  completed: 2026-04-12
  tasks_completed: 2
  files_modified: 1
---

# Phase 08 Plan 02: Pareto Frontier / Social Welfare Narrative Summary

Social welfare W defined in Section 5.1, Section 5.2 efficiency paragraph reframed to address endogeneity, and new Section 5.5 added with Table 2 (actual CSV values, no placeholders) and fig07_pareto reference.

## What Was Built

Three targeted edits to `paper/sections/experiments.tex`:

1. Section 5.1 metrics paragraph: appended W formula `W = sum_r[z_r * U_rb* - (1-z_r) * Gamma]` with cross-reference to `\ref{sec:pareto}`.

2. Section 5.2 efficiency paragraph: replaced original paragraph with version that names the endogeneity concern explicitly and explains gamma is post-hoc (does not alter routing/acceptance), cross-referencing Section 5.5.

3. Section 5.5 `\subsection{Coverage--Efficiency Analysis and Social Welfare}` (`\label{sec:pareto}`): explains gamma is post-hoc, presents Table 2 with actual numeric values from pareto_gamma_sweep.csv, includes fig07_pareto figure, and interpretation paragraph noting served_share and vkm/trip are invariant to gamma.

## Table 2 Values Used (gamma=0 row and full sweep)

| gamma | served_share | vkm_per_served_trip | W_mean     |
|-------|-------------|---------------------|------------|
| 0     | 0.183       | 9.893               | -2783.5    |
| 5     | 0.183       | 9.893               | -3600.1    |
| 10    | 0.183       | 9.893               | -4416.8    |
| 20    | 0.183       | 9.893               | -6050.1    |
| 50    | 0.183       | 9.893               | -10950.1   |
| 100   | 0.183       | 9.893               | -19116.8   |

served_share and vkm_per_served_trip are constant across all gamma — gamma is post-hoc.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Corrected vkm-per-trip arithmetic in Section 5.2**
- Found during: Task 2 Edit A
- Issue: Original plan template used 628.5/0.208=3022 and 2603.7/0.610=4268 (29.2% improvement). The original text had 628.5/0.2082=2383.85 and 2603.7/0.6096=3662.33 (34.9%). The plan's figures are the correct ones to use for the reframed paragraph.
- Fix: Used plan's arithmetic (3022, 4268, 29.2%) in the reframed paragraph.
- Files modified: paper/sections/experiments.tex

**2. [Rule 2 - Narrative accuracy] Section 5.5 title and caption reflect actual finding**
- Found during: Task 2 Edit B
- Issue: Plan called the subsection "Coverage--Efficiency Pareto Frontier" and the figure caption described "each point corresponds to one value of Gamma; higher Gamma increases served share." But the CSV shows served_share is CONSTANT — there is no frontier curve.
- Fix: Titled subsection "Coverage--Efficiency Analysis and Social Welfare"; rewrote caption to accurately state served_share and vkm/trip are invariant to gamma; rewrote interpretation paragraph accordingly.
- Files modified: paper/sections/experiments.tex

## LaTeX Environment Balance

- `\begin{table}` / `\end{table}`: balanced (2 each)
- `\begin{figure}` / `\end{figure}`: balanced (3 each)
- `\begin{tabular}` / `\end{tabular}`: balanced (2 each)

All assertion checks passed.

## Self-Check: PASSED

- paper/sections/experiments.tex: modified and committed (95d2776)
- All 7 verification assertions passed
- No `\emph{from CSV}` placeholders remain
- `endogenous` keyword present in Section 5.2
- `\subsection{Coverage`, `sec:pareto`, `tab:pareto`, `fig07_pareto`, `fig:pareto` all present
