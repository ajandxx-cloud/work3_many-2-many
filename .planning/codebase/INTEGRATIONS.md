# External Integrations

**Analysis Date:** 2026-06-16

## APIs & External Services

**Optimization Solver:**
- Gurobi Optimizer - Exact MILP solving for static many-to-many DRT assignment, vehicle assignment, pickup/dropoff meeting-point selection, scheduling, and acceptance decisions.
  - SDK/Client: `gurobipy`
  - Auth: Local Gurobi license configured outside the repository; no repo `.env` file or explicit environment variable is read by `src/drt/milp.py`.
  - Implementation: `src/drt/milp.py` imports `gurobipy` inside `DRTModel.build()` and `DRTModel.solve()`, sets `TimeLimit`, `MIPGap`, and `OutputFlag`, solves the model, and maps Gurobi statuses to `optimal`, `feasible`, `infeasible`, `timeout`, or `unknown`.
  - Diagnostic integration: `experiments/milp_gap.py` imports `drt.milp.DRTModel` inside `run_gap_experiment()` and returns `milp_status="no_gurobi"` when Gurobi is unavailable or unlicensed.
  - Test behavior: `tests/test_milp.py` uses `pytest.importorskip("gurobipy")` and skips licensed solver tests when Gurobi is unavailable.

**Version Metadata:**
- Git CLI - Used to stamp experiment artifacts with a short commit hash.
  - SDK/Client: `subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])`
  - Auth: Local repository access only; no remote GitHub API integration detected.
  - Implementation: `experiments/runner.py`, `experiments/formal_statistics.py`, `experiments/phase06_formal.py`, `experiments/phase06_coverage_controls.py`, and `experiments/phase06_robustness.py`.
  - Failure mode: Helpers return `"unknown"` or catch exceptions when Git metadata is unavailable.

**Network APIs:**
- Not detected.
  - SDK/Client: Not applicable.
  - Auth: Not applicable.
  - Evidence: Active Python code contains no detected imports or clients for `requests`, `httpx`, `urllib.request`, `openai`, `anthropic`, `boto3`, `stripe`, `supabase`, cloud database SDKs, webhook clients, or callback clients.

## Data Storage

**Databases:**
- Not detected.
  - Connection: Not applicable.
  - Client: Not applicable.
  - Evidence: Active Python code contains no detected `sqlite3`, `sqlalchemy`, `psycopg`, `mysql`, `pymongo`, or `redis` usage.

**File Storage:**
- Local filesystem only.
  - Core experiment raw and aggregate CSV outputs are written by `experiments/runner.py` to `results/synthetic_results.csv`, `results/beijing_results.csv`, `results/metrics_table.csv`, and `results/utility_components.csv`.
  - Root validation runner `run_experiments.py` reads `results/metrics_table.csv`.
  - MILP benchmark output is written by `src/drt/milp.py` to `results/milp_benchmark.json` by default.
  - MILP gap diagnostics are written by `experiments/milp_gap.py` to `results/milp_gap.json`.
  - Phase 5 and Phase 6 experiment modules write structured artifacts under `results/pilot/phase05/` and `results/formal/phase06/`, including CSV, JSON, plot PNG files, and manifest files.
  - Analysis modules write post-hoc CSV/Markdown outputs under `results/`: `analysis/sensitivity.py`, `analysis/equity.py`, and `analysis/policy.py`.
  - Figure scripts under `manuscript/figures/scripts/` write PDF and PNG assets under `manuscript/figures/`.
  - Manuscript source and compiled output live under `manuscript/`, including `manuscript/main.tex` and `manuscript/main.pdf`.
  - Archived outputs and debug artifacts live under `archive/`, including `archive/pre_revision_results/`, `archive/debug_scripts/`, `archive/adhoc_tests/`, and `archive/output_logs/`.

**Caching:**
- No external cache detected.
- Local Python bytecode caches are present under `__pycache__/` and `src/drt/__pycache__/`.
- Pytest cache is present under `.pytest_cache/`.

## Authentication & Identity

**Auth Provider:**
- Not detected.
  - Implementation: No web app, user model, login flow, session storage, OAuth/OIDC provider, API token exchange, or identity SDK usage detected.
  - Solver licensing: Gurobi authentication/licensing is external to this repository and is only consumed indirectly by `gurobipy` in `src/drt/milp.py`.

## Monitoring & Observability

**Error Tracking:**
- None detected.

**Logs:**
- Console logging with `print()` and `stderr` is used in `run_experiments.py`, `experiments/runner.py`, `experiments/milp_gap.py`, `experiments/phase06_formal.py`, `experiments/phase06_coverage_controls.py`, and `experiments/phase06_robustness.py`.
- Structured failure rows are emitted into CSV/JSON artifacts by experiment runners. Examples include timeout/error rows in `experiments/runner.py` and validation reports under `results/formal/phase06/`.
- Captured historical run logs exist as local files such as `smoke_test_output.txt`, `test_fix_output.txt`, `test_scale100_output.txt`, `results/runner_output.txt`, and `results/targeted_run_log.txt`.

## CI/CD & Deployment

**Hosting:**
- Not applicable. No deployed application, hosting provider config, Dockerfile, Compose file, Procfile, or server entry point detected.

**CI Pipeline:**
- None detected.
  - No `.github/workflows/`, GitLab CI, CircleCI, Azure Pipelines, or other CI configuration detected in the repository file list.
  - Verification is local via `pytest`, experiment scripts, and generated validation reports.

## Environment Configuration

**Required env vars:**
- None detected for normal package import, synthetic/Beijing scenario generation, heuristic runs, analysis, or file-based artifact generation.
- Gurobi may require external license configuration depending on the local installation, but the repository does not read a named Gurobi environment variable directly.
- Some phase verification examples use shell-level `PYTHONPATH=src` to resolve imports; editable install with `pip install -e .` is the documented alternative.

**Secrets location:**
- Not detected.
- No `.env*` files detected at repository root.
- Do not commit Gurobi license files, cloud credentials, package tokens, or private keys into this repository.

## Webhooks & Callbacks

**Incoming:**
- None detected.
  - No HTTP server, route handlers, API endpoint files, webhook receivers, or callback handlers detected.

**Outgoing:**
- None detected.
  - No network callback clients, webhook POSTs, or cloud API calls detected.

---

*Integration audit: 2026-06-16*
