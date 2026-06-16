# Phase 09 Pattern Map: Manuscript Restructure for TR Part E

**Phase:** 09 - Manuscript Restructure for TR Part E
**Date:** 2026-06-16
**Status:** Pattern mapping complete

## Purpose

Map the Phase 9 manuscript-planning files to existing repository patterns,
source-of-truth contracts, and closest analog artifacts so executors can work
from local conventions instead of inventing a new manuscript workflow.

## Target Outputs and Closest Analogs

| Phase 9 output | Role | Closest local analogs | Notes |
|---|---|---|---|
| `09_TR_E_MANUSCRIPT_STRUCTURE.md` | Source-of-truth manuscript outline and section mapping | `.planning/phases/01-literature-and-novelty-audit/01_NOVELTY_POSITIONING.md`, `.planning/phases/02-experimental-contract-and-metric-standardization/02_EXPERIMENT_CONTRACT.md`, `manuscript/main.tex` | Should be a planning artifact, not final prose. It should map old sections to a TR-E evidence-chain structure and mark Phase 8 dependencies. |
| `09_REVISED_ABSTRACT.md` | Claim-gated abstract and highlights plan | `manuscript/sections/abstract.tex`, `.planning/phases/01-literature-and-novelty-audit/01_REVISED_RESEARCH_QUESTIONS.md`, `.planning/CLAIMS_AND_RISKS.md` | Must use placeholders for final claims until Phase 8 supported/unsupported claim files exist. Include TR-E highlights constraints. |
| `09_REVISED_INTRODUCTION_PLAN.md` | Research-question, contribution, and intro-flow plan | `manuscript/sections/intro.tex`, `.planning/phases/01-literature-and-novelty-audit/01_NOVELTY_POSITIONING.md`, `.planning/phases/09-manuscript-restructure-for-tr-part-e/09-CONTEXT.md` | Must replace "our method wins" with evidence gap, research questions, and contribution order. |
| `09_EXPERIMENT_SECTION_PLAN.md` | Experiment/evidence family section plan | `manuscript/sections/experiments.tex`, `.planning/phases/02-experimental-contract-and-metric-standardization/02_EXPERIMENT_CONTRACT.md`, `.planning/phases/06-formal-synthetic-experiments/06-CONTEXT.md` | Must separate experimental design, main evidence, robustness, equity, and diagnostics. |
| `09_TABLE_FIGURE_PLAN.md` | Main-text versus appendix/supplement display plan | `.planning/phases/02-experimental-contract-and-metric-standardization/02_METRICS_DEFINITIONS.md`, `.planning/phases/02-experimental-contract-and-metric-standardization/02_STATISTICAL_PLAN.md`, `manuscript/figures/scripts/` | Must use explicit denominators and avoid old ambiguous or unsupported figure narratives. |

## Source Files Executors Must Inspect

### Planning Contracts

- `.planning/phases/09-manuscript-restructure-for-tr-part-e/09-CONTEXT.md`
- `.planning/phases/09-manuscript-restructure-for-tr-part-e/09-RESEARCH.md`
- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `.planning/CLAIMS_AND_RISKS.md`

### Upstream Evidence Contracts

- `.planning/phases/02-experimental-contract-and-metric-standardization/02_EXPERIMENT_CONTRACT.md`
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_BASELINE_TAXONOMY.md`
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_METRICS_DEFINITIONS.md`
- `.planning/phases/02-experimental-contract-and-metric-standardization/02_STATISTICAL_PLAN.md`
- `.planning/phases/06-formal-synthetic-experiments/06-CONTEXT.md`

### Current Manuscript Source

- `manuscript/main.tex`
- `manuscript/sections/abstract.tex`
- `manuscript/sections/intro.tex`
- `manuscript/sections/literature.tex`
- `manuscript/sections/model.tex`
- `manuscript/sections/algorithm.tex`
- `manuscript/sections/experiments.tex`
- `manuscript/sections/policy.tex`
- `manuscript/sections/conclusion.tex`
- `manuscript/references.bib`

## Existing Patterns to Preserve

- Planning outputs live under `.planning/phases/{phase-dir}/` with the
  zero-padded phase prefix.
- Manuscript source lives under `manuscript/sections/` with `manuscript/main.tex`
  controlling section order.
- Evidence-family language comes from Phase 2, not from the old manuscript.
- Pilot/formal/claim-gate separation is a project invariant; Phase 9 must not
  turn pilot, diagnostic, or unsupported evidence into final claims.
- Current result numbers in the manuscript are legacy inputs unless Phase 8
  explicitly approves them.

## High-Risk Edits to Avoid During Phase 9 Execution

- Directly editing `manuscript/sections/*.tex` before Phase 8 claim artifacts
  exist, unless the task explicitly writes placeholders rather than final claims.
- Keeping `Transportation Research Part A` in `main.tex` when the restructure
  is intended for TR-E.
- Keeping `FullModel`, `DoorToDoor`, or diagnostic method labels as paper-facing
  conceptual evidence labels.
- Reporting `vkm_per_trip`.
- Calling gamma sensitivity a Pareto frontier.
- Describing Beijing-inspired synthetic scenarios as real Beijing evidence.
- Presenting policy prescriptions before limitations and boundary conditions.

## Recommended Plan Dependencies

- Wave 1: Create the manuscript structure and abstract/highlights planning
  artifacts. These establish the top-level story and final-claim blockers.
- Wave 2: Create introduction/literature and experiment/evidence-family plans
  using Wave 1 vocabulary.
- Wave 3: Create the table/figure and managerial-insight plan after the section
  architecture is stable.

## PATTERN MAPPING COMPLETE

