# Codebase Structure

**Analysis Date:** 2026-06-16

## Directory Layout

```text
3.working-root/
+-- README.md                 # Project overview, run instructions, known repository notes
+-- CLAUDE.md                 # GSD/project context and workflow constraints
+-- pyproject.toml            # Python package metadata for package `drt`
+-- run_experiments.py        # Root script for the generic full experiment run
+-- .planning/                # GSD planning state and codebase maps
+-- src/
|   +-- drt/                  # Core reusable DRT package
|       +-- __init__.py       # Public package re-exports
|       +-- types.py          # Domain dataclasses
|       +-- candidate.py      # Meeting-point candidate filtering
|       +-- feasibility.py    # Insertion feasibility checks
|       +-- insertion.py      # Greedy insertion evaluator
|       +-- choice.py         # MNL/binary-logit choice model
|       +-- alns.py           # ALNS operators and rolling horizon controller
|       +-- milp.py           # Gurobi static snapshot diagnostic model
+-- experiments/              # Scenario, variant, runner, phase, and validation scripts
+-- analysis/                 # Post-hoc sensitivity, equity, and policy analysis
+-- tests/                    # Pytest coverage for algorithms, variants, runners, phases
+-- results/                  # Generated experiment outputs and formal artifacts
+-- manuscript/               # Current LaTeX paper, figures, figure scripts, sections
+-- docs/                     # Human-written notes and project documents
+-- archive/                  # Historical drafts, output logs, debug scripts, ad-hoc tests
```

## Directory Purposes

**`src/drt/`:**
- Purpose: Reusable many-to-many DRT algorithm package.
- Contains: Dataclasses, candidate filtering, feasibility checks, insertion logic, choice model, ALNS/rolling horizon, exact MILP diagnostics.
- Key files: `src/drt/types.py`, `src/drt/choice.py`, `src/drt/insertion.py`, `src/drt/alns.py`, `src/drt/milp.py`.
- Add only source code that can be imported without depending on `results/`, `manuscript/`, or phase-specific planning files.

**`experiments/`:**
- Purpose: Experiment orchestration and evidence generation.
- Contains: Shared constants, scenario generators, variant definitions, generic runner, Phase 05/06 harnesses, controls, robustness diagnostics, formal validation/statistics, auxiliary experiments.
- Key files: `experiments/config.py`, `experiments/scenarios.py`, `experiments/variants.py`, `experiments/runner.py`, `experiments/phase06_formal.py`, `experiments/formal_statistics.py`.
- Add new runnable experiment behavior here, not in `run_experiments.py`.

**`analysis/`:**
- Purpose: Post-hoc analysis that reads completed result artifacts.
- Contains: Sensitivity sweeps, equity analysis, policy recommendation generation, and one local test module.
- Key files: `analysis/sensitivity.py`, `analysis/equity.py`, `analysis/policy.py`, `analysis/test_sensitivity.py`.
- Add analysis that consumes existing CSV/JSON outputs and writes derived reports.

**`tests/`:**
- Purpose: Pytest suite for core algorithms, scenario generators, variants, runner behavior, phase harnesses, controls, and robustness packages.
- Contains: `test_*.py` files co-located in one top-level test directory.
- Key files: `tests/test_insertion.py`, `tests/test_choice.py`, `tests/test_alns.py`, `tests/test_runner.py`, `tests/test_phase06_formal.py`.
- Add tests for any behavior added under `src/drt/`, `experiments/`, or `analysis/`.

**`results/`:**
- Purpose: Generated experiment outputs and validation artifacts.
- Contains: Root generic CSV/JSON outputs, pilot results under `results/pilot/phase05`, formal Phase 06 outputs under `results/formal/phase06`, plots, tables, manifests, validation reports.
- Key files: `results/formal/phase06/main_behavioral/raw_results.csv`, `results/formal/phase06/tables/main_behavioral_table.csv`, `results/formal/phase06/phase06_result_manifest.json`.
- Treat this directory as generated evidence/output, not application source.

**`manuscript/`:**
- Purpose: Current publication source.
- Contains: `main.tex`, section `.tex` files, bibliography, cover/response letters, compiled `main.pdf`, figures, and figure generation scripts.
- Key files: `manuscript/main.tex`, `manuscript/sections/experiments.tex`, `manuscript/figures/scripts/fig01_system_overview.py`.
- Add paper text in `manuscript/sections/` and plotting scripts in `manuscript/figures/scripts/`.

**`docs/`:**
- Purpose: Human-written notes, proposal material, and dataset notes.
- Contains: Markdown and text documents, including Chinese-language notes.
- Key files: `docs/开题报告-3.30.md`, `docs/工作3讨论-6.14.md`, `docs/工作3公开数据集.txt`.
- Add explanatory project notes here when they are not active manuscript source or executable plans.

**`archive/`:**
- Purpose: Historical and superseded artifacts kept for reference.
- Contains: Early model drafts, pre-revision results, debug scripts, ad-hoc tests, output logs, and old paper text.
- Key files: `archive/model_draft/model.tex`, `archive/debug_scripts/debug_rh.py`, `archive/adhoc_tests/smoke_test.py`, `archive/output_logs/full_run_output.txt`.
- Do not add active source here unless explicitly archiving old material.

**`.planning/`:**
- Purpose: GSD workflow state, phase artifacts, and codebase documentation.
- Contains: `codebase/` documents and phase/ledger artifacts.
- Key files: `.planning/codebase/ARCHITECTURE.md`, `.planning/codebase/STRUCTURE.md`.
- Add planning artifacts through GSD workflows; do not mix source code into this directory.

## Key File Locations

**Entry Points:**
- `run_experiments.py`: Root convenience script for the generic full experiment run.
- `experiments/runner.py`: Generic experiment matrix runner and CSV writer.
- `experiments/phase05_pilot.py`: Phase 05 pilot-only behavioral run.
- `experiments/phase06_formal.py`: Phase 06 formal main run, manifest, validation CLI.
- `experiments/phase06_coverage_controls.py`: Phase 06 matched-coverage and fixed-accepted-set controls.
- `experiments/phase06_robustness.py`: Phase 06 robustness, sensitivity, equity, and algorithm diagnostics.
- `experiments/formal_statistics.py`: Phase 06 closeout tables, plots, manifests, and reports.
- `analysis/sensitivity.py`: Post-hoc walking/fleet sensitivity analysis.
- `analysis/equity.py`: Post-hoc equity summary generation.
- `analysis/policy.py`: Policy recommendation report generation.

**Configuration:**
- `pyproject.toml`: Package name, Python version, dependencies, optional dev dependencies, `src` package discovery.
- `experiments/config.py`: Shared experiment constants: seeds, scales, vehicle counts, walking radii, top-k, rolling-horizon window, ALNS iterations, cost weights, choice parameters.
- `experiments/phase06_formal.py`: Formal scales, formal seed sets, output roots, artifact aliases, rerun ledger path.
- `experiments/phase06_coverage_controls.py`: Coverage-control package names, schemas, timeout, method label mappings.
- `experiments/phase06_robustness.py`: Robustness package names, default seeds/scales/methods, output schemas.

**Core Logic:**
- `src/drt/types.py`: Dataclasses and passenger-type constants.
- `src/drt/candidate.py`: `euclidean()` and `generate_candidates()`.
- `src/drt/feasibility.py`: `check_feasibility()`.
- `src/drt/insertion.py`: `InsertionResult` and `evaluate_insertion()`.
- `src/drt/choice.py`: `mnl_utility()`, `accept_probability()`, `evaluate_single_offer()`, `assign_passenger_type()`.
- `src/drt/alns.py`: `ALNSState`, ALNS destroy/repair operators, `RollingHorizon`, benchmark helper.
- `src/drt/milp.py`: `DRTModel` static snapshot exact solver.
- `experiments/scenarios.py`: `Scenario`, `generate_synthetic()`, `generate_beijing()`.
- `experiments/variants.py`: `BaseVariant`, all service-design variants, `ALL_VARIANTS`.
- `experiments/metrics.py`: `PassengerRecord`, `SimulationResult`, `MetricsResult`, `compute_metrics()`.

**Formal Evidence and Validation:**
- `experiments/formal_validation.py`: Phase 06 main output validators and failure ledger helpers.
- `experiments/phase06_formal.py`: Formal run wrapper, seed/config/run manifests, artifact aliases.
- `experiments/phase06_coverage_controls.py`: Coverage-control runners, validators, summaries.
- `experiments/phase06_robustness.py`: Robustness package runners, validators, summaries.
- `experiments/formal_statistics.py`: Statistical tables, plots, result manifest, verification markdown.

**Publication:**
- `manuscript/main.tex`: Manuscript master document.
- `manuscript/sections/`: Current paper section files.
- `manuscript/references.bib`: Bibliography.
- `manuscript/figures/`: Generated figure assets.
- `manuscript/figures/scripts/`: Python scripts that create individual figures.

**Testing:**
- `tests/test_candidate.py`: Candidate generation behavior.
- `tests/test_feasibility.py`: Feasibility constraint checks.
- `tests/test_insertion.py`: Insertion result behavior.
- `tests/test_choice.py`: Choice model and utility behavior.
- `tests/test_alns.py`: ALNS and rolling-horizon behavior.
- `tests/test_milp.py`: MILP import/build/diagnostic behavior.
- `tests/test_runner.py`: Runner rows, timeout/error behavior, CSV writing.
- `tests/test_variants.py`: Variant metadata and behavior.
- `tests/test_scenarios.py`: Scenario generation constraints.
- `tests/test_phase05_pilot.py`: Phase 05 pilot selection/output behavior.
- `tests/test_phase06_formal.py`: Phase 06 formal run/manifest/validation behavior.
- `tests/test_phase06_coverage_controls.py`: Coverage-control package behavior.
- `tests/test_phase06_robustness.py`: Robustness package behavior.

## Naming Conventions

**Files:**
- Core package modules are lowercase single-purpose names: `src/drt/choice.py`, `src/drt/alns.py`, `src/drt/milp.py`.
- Experiment modules are lowercase descriptive names with underscores: `experiments/phase06_coverage_controls.py`, `experiments/formal_statistics.py`.
- Tests use `test_<subject>.py`: `tests/test_runner.py`, `tests/test_phase06_formal.py`.
- Manuscript figure scripts use `figNN_subject.py`: `manuscript/figures/scripts/fig04_baseline_comparison.py`.
- Generated formal artifacts use explicit evidence names: `raw_results.csv`, `processed_results.csv`, `utility_logs.csv`, `validation_report.json`, `run_manifest.json`.

**Directories:**
- Source package code lives under `src/drt/`.
- Experiment code lives under `experiments/`.
- Formal evidence is grouped by phase and package under `results/formal/phase06/`.
- Active manuscript material lives under `manuscript/`.
- Historical material lives under `archive/`.

**Classes:**
- Domain dataclasses use PascalCase nouns: `Request`, `Vehicle`, `MeetingPoint`, `OfferAttributes`, `ChoiceEvaluation`.
- Variant classes use PascalCase method names: `DoorToDoor`, `SingleSidedPickup`, `FullModel`, `AblationNoChoice`.
- Internal control subclasses in Phase 06 coverage controls use leading underscores: `_MatchedDoorToDoor`, `_FixedBidirectionalRH`.

**Functions:**
- Public functions use snake_case verbs/nouns: `generate_synthetic()`, `evaluate_insertion()`, `compute_metrics()`, `run_phase06_main()`.
- Private helpers use leading underscores: `_write_json()`, `_run_variant_with_timeout()`, `_validate_scales()`.
- CLI modules expose `main()` or `main(argv: list[str] | None = None)`.

**Constants:**
- Configuration constants are uppercase: `RHO_P`, `RHO_D`, `K_TOP`, `H_WINDOW`, `FORMAL_SCALES`.
- Package IDs and method-label sets are uppercase: `MATCHED_PACKAGE`, `PACKAGE_NAMES`, `FORMAL_MAIN_METHOD_LABELS`.

## Where to Add New Code

**New core algorithm primitive:**
- Primary code: `src/drt/<primitive>.py`
- Public exports: update `src/drt/__init__.py` only for stable public APIs.
- Tests: `tests/test_<primitive>.py`
- Use `src/drt/types.py` dataclasses instead of ad-hoc dicts for domain objects.

**New service design or algorithm variant:**
- Primary code: add a `BaseVariant` subclass in `experiments/variants.py`.
- Registry: add an instance to `ALL_VARIANTS` in `experiments/variants.py` only if the generic runner should include it.
- Tests: `tests/test_variants.py` and, when runner output changes, `tests/test_runner.py`.
- Set `method_label`, `service_design`, `choice_model`, `reoptimization`, `routing_solver`, `evidence_family`, and `diagnostic_role`.

**New generic experiment matrix behavior:**
- Primary code: `experiments/runner.py` for generic execution mechanics.
- Configuration: `experiments/config.py` for shared constants.
- Tests: `tests/test_runner.py`.
- Do not hardcode Phase 05/06 evidence rules into the generic runner.

**New scenario generator:**
- Primary code: `experiments/scenarios.py`.
- Tests: `tests/test_scenarios.py`.
- Return the existing `Scenario` dataclass and preserve deterministic seeded generation.

**New metric:**
- Primary code: `experiments/metrics.py`.
- Runner schema: update `_METRIC_COLS` and row writing in `experiments/runner.py` if the metric is persisted.
- Tests: `tests/test_metrics.py` and `tests/test_runner.py`.

**New Phase 06 main evidence behavior:**
- Primary code: `experiments/phase06_formal.py`.
- Validation: `experiments/formal_validation.py`.
- Closeout/reporting: `experiments/formal_statistics.py`.
- Tests: `tests/test_phase06_formal.py`.
- Output root: `results/formal/phase06/main_behavioral`.

**New Phase 06 coverage control:**
- Primary code: `experiments/phase06_coverage_controls.py`.
- Tests: `tests/test_phase06_coverage_controls.py`.
- Output root: `results/formal/phase06/coverage_controls/<package_id>`.
- Add schema columns and validation paths in the same file.

**New Phase 06 robustness package:**
- Primary code: `experiments/phase06_robustness.py`.
- Tests: `tests/test_phase06_robustness.py`.
- Output root: `results/formal/phase06/robustness/<package_id>`.
- Add the package ID to `PACKAGE_NAMES` and provide run, validate, and summary paths.

**New post-hoc analysis report:**
- Primary code: `analysis/<topic>.py`.
- Tests: `analysis/test_<topic>.py` or `tests/test_<topic>.py`.
- Outputs: `results/<topic>.csv`, `results/<topic>.md`, or an isolated formal subdirectory when tied to Phase 06.

**New manuscript figure:**
- Primary script: `manuscript/figures/scripts/figNN_subject.py`.
- Outputs: `manuscript/figures/figNN_subject.png` and/or `.pdf`.
- Source data: read from `results/` or `results/formal/phase06/`; do not run simulations from figure scripts.

**New manuscript text:**
- Primary code: `manuscript/sections/<section>.tex`.
- Master include: update `manuscript/main.tex`.
- Bibliography: `manuscript/references.bib`.

**New documentation or notes:**
- Current project notes: `docs/`.
- GSD planning artifacts: `.planning/`.
- Do not place active implementation notes in `archive/`.

## Special Directories

**`results/`:**
- Purpose: Generated experiment outputs, validation reports, tables, and plots.
- Generated: Yes.
- Committed: Some outputs are present in the repository.
- Guidance: Prefer isolated subdirectories for new formal evidence. Avoid overwriting root result files for phase work.

**`results/formal/phase06/`:**
- Purpose: Current formal Phase 06 evidence tree.
- Generated: Yes.
- Committed: Present in repository.
- Guidance: Keep main behavioral, coverage controls, robustness, tables, plots, and smoke outputs separated.

**`manuscript/figures/`:**
- Purpose: Publication-ready figure assets.
- Generated: Yes for `.png`/`.pdf`; source scripts live in `manuscript/figures/scripts/`.
- Committed: Present in repository.
- Guidance: Regenerate assets from scripts when source data changes.

**`manuscript/figures/scripts/`:**
- Purpose: Figure source code.
- Generated: No.
- Committed: Yes.
- Guidance: Keep scripts plotting-focused; place data processing in `experiments/formal_statistics.py` or `analysis/`.

**`archive/`:**
- Purpose: Superseded model drafts, pre-revision results, debug scripts, ad-hoc tests, and output logs.
- Generated: Mixed.
- Committed: Present in repository.
- Guidance: Do not import from `archive/` in active code.

**`.planning/codebase/`:**
- Purpose: Machine-consumed codebase maps for GSD planning/execution.
- Generated: Yes.
- Committed: Yes.
- Guidance: Update via codebase mapping, not by hand during unrelated implementation phases.

**`.pytest_cache/` and `__pycache__/`:**
- Purpose: Runtime/test caches.
- Generated: Yes.
- Committed: No intended source value.
- Guidance: Ignore for architecture and implementation decisions.

---

*Structure analysis: 2026-06-16*
