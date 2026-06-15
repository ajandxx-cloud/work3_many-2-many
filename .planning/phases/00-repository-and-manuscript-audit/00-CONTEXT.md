# Phase 0 Context: Repository and Manuscript Audit

**Phase Goal:** Understand the current code, manuscript, data, and experiment outputs before any new experiments are run.

## Known Context

The repository is an existing DRT simulation/manuscript project. It already contains:

- Core Python package under `src/drt/`
- Experiment runners under `experiments/`
- Analysis scripts under `analysis/`
- Current outputs under `results/`
- Current manuscript under `manuscript/`
- Review/discussion notes under `docs/`
- Codebase maps under `.planning/codebase/`

The rebuild brief requires Phase 0 to produce:

1. `00_REPOSITORY_AUDIT.md`
2. `00_MANUSCRIPT_CLAIM_AUDIT.md`
3. `00_CURRENT_EXPERIMENT_MAP.md`
4. initial `ROADMAP.md`
5. initial `REQUIREMENTS.md`
6. initial `STATE.md`

These have been initialized, but the audit files still need row-level verification before Phase 0 can be considered complete.

## Key Risks From Review Note

- Novelty overclaim around bidirectional meeting points.
- Passenger-choice parameters lack calibration.
- Headline vkm/trip comparison is coverage-confounded.
- Baselines mix all-feasible acceptance and binary-logit response.
- ALNS validation is weak and MILP gap is large.
- MILP formulation scope may be incomplete.
- Formal seed count is too low.
- Beijing-inspired scenario is synthetic and cannot support real-city policy claims.
- Gamma sweep is post-hoc welfare accounting, not a true Pareto frontier.
- Equity analysis is useful but currently overinterpreted.

## Expected Files / Modules To Inspect

- `manuscript/sections/abstract.tex`
- `manuscript/sections/intro.tex`
- `manuscript/sections/literature.tex`
- `manuscript/sections/model.tex`
- `manuscript/sections/algorithm.tex`
- `manuscript/sections/experiments.tex`
- `manuscript/sections/policy.tex`
- `manuscript/sections/conclusion.tex`
- `manuscript/references.bib`
- `experiments/*.py`
- `analysis/*.py`
- `src/drt/*.py`
- `results/*.csv`
- `results/*.json`
- `manuscript/figures/scripts/*.py`
- `docs/工作3讨论-6.14.md`

## Outputs

- Complete and verify the three Phase 0 audit markdown files.
- Keep `.planning/STATE.md` current.
- Do not run new experiments.

## Open Questions For Later

- Should the paper target TR Part E or stay closer to the current TR Part A framing?
- Should the encoded discussion note be repaired from an original source, or is the extracted risk content sufficient?
- Which result tables should be archived as exploratory before formal rebuild begins?
