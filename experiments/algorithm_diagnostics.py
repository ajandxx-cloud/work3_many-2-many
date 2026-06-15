"""Small Phase 04 algorithm diagnostic smoke runs.

These helpers produce algorithm-diagnostic rows only. They are not formal
runtime-quality evidence and should stay small enough for local validation.
"""
from __future__ import annotations

import json
import time

from experiments.config import ALPHA_WEIGHTS, DELTA, H_WINDOW, K_TOP, RHO_D, RHO_P
from experiments.scenarios import generate_synthetic
from src.drt.alns import RollingHorizon


def run_alns_budget_smoke(
    budgets: list[int] | None = None,
    n_requests: int = 8,
    n_vehicles: int = 3,
    seed: int = 42,
) -> list[dict]:
    """Run a tiny ALNS multi-budget diagnostic and return serializable rows."""
    budgets = budgets or [5, 20, 50]
    rows: list[dict] = []

    for budget in budgets:
        scenario = generate_synthetic(n_requests=n_requests, n_vehicles=n_vehicles, seed=seed)
        vehicles = {vehicle.id: vehicle for vehicle in scenario.vehicles}
        rh = RollingHorizon(
            vehicles=vehicles,
            meeting_points=scenario.meeting_points,
            rho_p=RHO_P,
            rho_d=RHO_D,
            k_top=K_TOP,
            H=H_WINDOW,
            delta=DELTA,
            cost_weights=tuple(ALPHA_WEIGHTS[:4]),
            travel_speed=8.33,
            alns_iterations=budget,
            seed=seed,
            collect_diagnostics=True,
        )

        arrivals = [request.earliest for request in scenario.requests]
        started = time.perf_counter()
        result = rh.run_simulation(scenario.requests, arrivals)
        runtime_s = time.perf_counter() - started
        trace = result.get("diagnostic_trace", [])
        best_objective = min(
            (entry["best_objective"] for entry in trace),
            default=result.get("cost", 0.0),
        )

        rows.append({
            "budget_iterations": budget,
            "best_objective": best_objective,
            "runtime_s": runtime_s,
            "n_accepted": result.get("n_accepted", 0),
            "n_unassigned": result.get("n_unassigned", 0),
            "operator_selection_counts": dict(result.get("operator_counts", {})),
            "improvement_counts": dict(result.get("improvement_counts", {})),
            "trace_length": len(trace),
            "evidence_family": "algorithm_diagnostic",
            "diagnostic_role": "alns_budget_smoke",
        })

    return rows


def main() -> None:
    print(json.dumps(run_alns_budget_smoke(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

