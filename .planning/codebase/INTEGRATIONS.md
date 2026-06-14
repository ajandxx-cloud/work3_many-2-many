# External Integrations

**Analysis Date:** 2026-06-14

## APIs & External Services

**Optimization Solver:**
- Gurobi Optimizer - Exact MILP solving for static many-to-many DRT assignment, routing, scheduling, acceptance, and meeting-point selection.
  - SDK/Client: `gurobipy`
  - Auth: Local Gurobi license configured outside the repo; no repo environment variable is read.
  - Implementation: `src/drt/milp.py` imports `gurobipy` inside `DRTModel.build()` and `DRTModel.solve()`, sets solver parameters, suppresses solver output, and translates Gurobi statuses into result strings.
  - Benchmark integration: `experiments/milp_gap.py` imports `drt.milp.DRTModel` inside `run_gap_experiment()` and returns `milp_status="no_gurobi"` when the solver is unavailable.

**Network APIs:**
- Not detected.
  - SDK/Client: Not applicable.
  - Auth: Not applicable.
  - Evidence: Active Python code contains no `requests`, `httpx`, `urllib.request`, `openai`, `anthropic`, `boto3`, `stripe`, `supabase`, database cloud SDK, webhook, or callback client imports.

## Data Storage

**Databases:**
- Not detected.
  - Connection: Not applicable.
  - Client: Not applicable.
  - Evidence: Active Python code contains no `sqlite3`, `sqlalchemy`, `psycopg`, `mysql`, `pymongo`, or `redis` client usage.

**File Storage:**
- Local filesystem only.
  - Experiment raw and aggregate CSV outputs are written by `experiments/runner.py` to `results/synthetic_results.csv`, `results/beijing_results.csv`, and `results/metrics_table.csv`.
  - Main experiment validation reads `results/metrics_table.csv` in `run_experiments.py`.
  - MILP benchmark JSON is written by `src/drt/milp.py` to `results/milp_benchmark.json` by default.
  - MILP gap JSON is written by `experiments/milp_gap.py` to `results/milp_gap.json`.
  - Sensitivity CSV outputs are written by `analysis/sensitivity.py` to `results/sensitivity_walk.csv` and `results/sensitivity_fleet.csv`.
  - Equity CSV output is written by `analysis/equity.py` to `results/equity_table.csv`.
  - Coverage and Pareto outputs are written by `experiments/matched_coverage.py`, `experiments/endogenous_matched_coverage.py`, and `experiments/pareto_sweep.py` under `results/`.
  - Figure scripts under `manuscript/figures/scripts/` write PDF and PNG assets under `manuscript/figures/`.

**Caching:**
- None detected.
  - There is no Redis, memcached, disk-cache package, cache directory contract, or cache invalidation code in active modules.
  - Python `__pycache__/` directories exist as interpreter artifacts, not application-managed caches.

## Authentication & Identity

**Auth Provider:**
- None.
  - Implementation: The project runs local scripts and tests. No web sessions, users, tokens, OAuth provider, JWT validation, or identity middleware exist in active code.
  - Solver licensing: Gurobi authentication is external to the repo and handled by the local Gurobi installation, not by application code.

## Monitoring & Observability

**Error Tracking:**
- None.
  - No Sentry, OpenTelemetry, Datadog, Honeycomb, New Relic, or logging service integration is detected.

**Logs:**
- Console output and local result files.
  - `run_experiments.py` prints run start, completion, and validation summaries.
  - `experiments/runner.py` prints per-variant progress and writes zero-filled error rows on timeout or exception.
  - `experiments/runner.py` prints traceback details to stderr for variant exceptions.
  - Captured historical logs live in `archive/output_logs/`; active code writes structured results under `results/`.

## CI/CD & Deployment

**Hosting:**
- None.
  - This is a local research codebase with Python package, experiment scripts, analysis scripts, and LaTeX manuscript outputs.

**CI Pipeline:**
- None detected.
  - No `.github/workflows/`, Dockerfile, docker-compose file, tox config, nox config, or pre-commit config was detected.
  - Test execution is local via `pytest`, as documented in `README.md`.

## Environment Configuration

**Required env vars:**
- None detected.
  - Active code does not call `os.environ`, `os.getenv`, or `dotenv`.
  - No `.env` file was detected at repo root.

**Secrets location:**
- Not applicable inside the repo.
  - Solver credentials or license files, if present on a developer machine, are managed by the external Gurobi installation and are not referenced by repo paths.

## Webhooks & Callbacks

**Incoming:**
- None.
  - No server framework, route handlers, HTTP listeners, webhook endpoints, or callback receivers are present.

**Outgoing:**
- None.
  - No outgoing webhooks, API callbacks, queue publishers, email clients, or notification clients are present.

---

*Integration audit: 2026-06-14*
