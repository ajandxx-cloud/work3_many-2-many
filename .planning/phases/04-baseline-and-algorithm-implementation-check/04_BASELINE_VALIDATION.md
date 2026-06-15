# Phase 04 Baseline Validation

## Purpose

Validate that Phase 04 behavioral and diagnostic runs produce durable,
schema-consistent outputs before Phase 5 pilot smoke runs.

## Schema Contract

Raw runner rows satisfy D-22 and D-23 with:

- Run identity and provenance: `run_id`, `config_id`, `seed`, `scenario`,
  `result_schema_version`, `timestamp_utc`, `artifact_dir`, and
  `git_commit_or_code_hash`.
- Method decomposition: `method_label`, `service_design`, `choice_model`,
  `reoptimization`, `routing_solver`, `evidence_family`, and
  `diagnostic_role`.
- Status and failure handling: `status`, `detailed_reason`, `runtime_s`, and
  `error_message`.
- Counts: `n_requests`, `n_offered`, and `n_served`.

## Small Scenario Baseline Smoke

The runner smoke tests execute the configured variant registry on a synthetic
8-request scenario and verify raw CSV, metrics table, and utility component
artifacts.

## Failure Row Validation

D-24 and D-25 are covered by tests that:

- Persist exception rows with `status == "failed"` and the exception text in
  `error_message`.
- Persist timeout rows with `status == "timeout"`, a non-empty timeout reason,
  and bounded `runtime_s`.
- Avoid the previous `ThreadPoolExecutor` context-manager path that waited for
  timed-out workers to finish before returning.

## Metric Denominator Check

D-26 is covered by formal fields:

- `vkm_per_served_trip = total_vkm / n_served` when at least one request is
  served, otherwise `0.0`.
- `vkm_per_original_request = total_vkm / n_requests` when the run has original
  requests, otherwise `0.0`.

The legacy helper name `vkm_per_trip` remains only for older diagnostic scripts;
new Phase 04 runner outputs use the explicit denominator fields above.

## Evidence Family Separation

D-06 and D-27 are covered through method metadata and the Phase 04 variant map.
Behavioral rows carry `evidence_family = behavioral_main`, while deterministic
and algorithm diagnostics carry separate evidence-family values and diagnostic
roles.

## Commands

```bash
PYTHONPATH=src pytest tests/test_runner.py tests/test_metrics.py -q
```

Latest local result: 54 passed.

## Decision Trace

- D-22: Expanded raw result row fields are present.
- D-23: Provenance and count fields are present.
- D-24: Failed and timeout outcomes are durable rows.
- D-25: Timeout handling returns without waiting for the worker sleep duration.
- D-26: Formal denominator fields replace ambiguous new `vkm_per_trip` output.
- D-27: Phase 04 validation artifacts include this report, the implementation
  audit, the algorithm validation report, and the variant mapping.

