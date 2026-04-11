---
phase: 01-problem-formulation-model-structure
plan: 01
subsystem: model
tags: [notation, problem-definition, latex, many-to-many-drt, meeting-points]
dependency_graph:
  requires: []
  provides: [notation-table, problem-definition, objective-function, decision-vector]
  affects: [01-02, 01-03, 01-04, phase-02]
tech_stack:
  added: [longtable, booktabs, amsmath]
  patterns: [latex-fragment, input-include]
key_files:
  created:
    - model/notation.tex
    - model/problem-definition.tex
  modified: []
key_decisions:
  - "Used M_r^P / M_r^D (uppercase P/D superscripts) consistently for pickup/dropoff meeting point sets"
  - "T_v^max added to Route and Schedule section (not in original CONTEXT.md) to cover vehicle shift length"
  - "Walking radius symbols rho^P and rho^D kept distinct for pickup vs dropoff sides"
  - "IVT_{rb} used in cost component C^IVT to maintain bundle-indexed notation"
metrics:
  duration_minutes: 15
  completed_date: "2026-04-11"
  tasks_completed: 2
  files_created: 2
---

# Phase 01 Plan 01: Notation Table and Problem Definition Summary

LaTeX fragments establishing the authoritative notation table (53 symbols) and four-subsection problem definition for the many-to-many DRT bidirectional meeting point paper.

## Files Created

- `model/notation.tex` — longtable with 53 symbol rows across 7 sections, ready for `\input{notation}` in model.tex
- `model/problem-definition.tex` — four subsections: Network and Input, Service Offer Bundle, System Objective, Online Decision Vector

## Symbol Count

53 data rows in the notation table, organized into 7 sections:

| Section | Symbols |
|---------|---------|
| Sets and Indices | 8 |
| Spatial and Temporal | 8 |
| Service Offer Bundle | 5 |
| Decision Variables | 4 |
| Route and Schedule | 6 |
| Cost Components | 6 |
| Passenger Choice | 11 |
| Three-Layer Model | 5 |

## Key Labels Defined

| Label | Location | Description |
|-------|----------|-------------|
| `tab:notation` | notation.tex | Notation longtable |
| `eq:objective` | problem-definition.tex | Weighted cost minimization objective |
| `eq:cop` | problem-definition.tex | Operational cost component |
| `eq:cwait` | problem-definition.tex | Waiting time cost component |
| `eq:cwalk` | problem-definition.tex | Walking distance cost component |
| `eq:civt` | problem-definition.tex | In-vehicle travel time cost component |
| `eq:crej` | problem-definition.tex | Rejection penalty cost component |
| `eq:decvec` | problem-definition.tex | Online decision vector |

## Notation Decisions

- `M_r^P` / `M_r^D` chosen over `M_r^p` / `M_r^d` for visual clarity in uppercase superscripts
- `T_v^{\max}` added to Route and Schedule section (vehicle shift length) — not in original CONTEXT.md but needed for completeness
- `\mathcal{B}_r = M_r^P \times M_r^D` defined as the Cartesian product of candidate sets
- `\text{IVT}_{rb}` used as bundle-indexed notation consistent with `\text{Walk}_{rb}` and `\text{Wait}_{rb}`

## Deviations from Plan

None — plan executed exactly as written. One minor addition: `T_v^{\max}` (maximum route duration) added to Route and Schedule section as it is referenced implicitly by feasibility constraints in downstream plans.

## Open Questions for Downstream Plans

- Plan 01-02 (constraints): `sec:constraints` label must be defined there, as `problem-definition.tex` references `\ref{sec:constraints}`
- Plan 01-03 (MNL model): `\beta_1^k` through `\beta_4^k` coefficients are declared in notation but utility function `U_{rb}` formula is deferred to that plan
- Plan 02 (algorithms): `k^{\text{top}}` candidate generation parameter is declared; exact filtering logic deferred

## Self-Check

- [x] `model/notation.tex` exists and contains `\begin{longtable}`
- [x] `model/problem-definition.tex` exists and contains `\label{eq:objective}`
- [x] Commit `76aa9e9` exists in git log
- [x] No `\documentclass` or `\begin{document}` in either file
- [x] `M_r^P` appears 3+ times in problem-definition.tex (count: 5)
- [x] `M_r^D` appears 3+ times in problem-definition.tex (count: 5)
- [x] `z_r \in \{0,1\}` present in problem-definition.tex
- [x] `\pi_r^D > \pi_r^P` present in problem-definition.tex
