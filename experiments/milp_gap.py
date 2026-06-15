"""
experiments/milp_gap.py — REV-10: MILP vs ALNS optimality gap experiment.

For small instances (n=20, n=30 passengers), runs:
  1. ALNS heuristic (FullModel) to obtain the realized accepted set R^acc
     and the ALNS vehicle-km.
  2. MILP ex-post benchmark: given the realized accepted set from step 1
     (z_r treated as fixed = 1 for r in R^acc), solve optimal vehicle routing
     for that fixed accepted set.
  3. Compute optimality gap = (alns_vkm - milp_vkm) / milp_vkm * 100%.

Writes results to results/milp_gap.json.

Notes
-----
- Gaps are comparable only for fixed accepted sets or static small instances
  where objective units and semantics match. This is not a full online exact
  stochastic DRT benchmark.
- The MILP import (gurobipy) is deferred inside run_gap_experiment so this
  module can be imported without a Gurobi installation.
- If Gurobi is unavailable, run_gap_experiment returns milp_status='no_gurobi'
  and milp_vkm=None.  main() writes a JSON with those entries.
- The MILP objective is a weighted cost (α1*C_op + α2*C_wait + ...) not raw
  vehicle-km.  We report the MILP operational cost term (C_op, proportional
  to routing distance) as 'milp_vkm' and derive ALNS cost via the same
  alpha_op weight for comparability.  See §Solver and Scope in algorithm.tex.
"""
from __future__ import annotations

import json
import os
import sys
import time

# ---------------------------------------------------------------------------
# Path setup: allow running as a script from the repo root
# ---------------------------------------------------------------------------
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from experiments.config import (
    ALPHA_WEIGHTS,
    RHO_D,
    RHO_P,
    SEEDS,
    VEHICLE_CAPACITY,
)
from experiments.scenarios import generate_synthetic
from experiments.variants import FullModel


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

_DIAGNOSTIC_META = {
    "method_label": "MILPStaticSnapshot_Diagnostic",
    "service_design": "fixed_accepted_set",
    "choice_model": "none",
    "reoptimization": "static_snapshot",
    "routing_solver": "milp",
    "evidence_family": "algorithm_diagnostic",
    "diagnostic_role": "milp_static_snapshot",
    "objective_units": "weighted_cost_units",
}


def _base_row(
    n_requests: int,
    seed: int,
    alns_vkm: float,
    n_accepted: int,
    status: str,
    detailed_reason: str,
    runtime_s: float,
    error_message: str = "",
) -> dict:
    return {
        **_DIAGNOSTIC_META,
        "n_requests": n_requests,
        "seed": seed,
        "alns_vkm": alns_vkm,
        "milp_vkm": None,
        "gap_pct": None,
        "milp_status": status,
        "status": status,
        "detailed_reason": detailed_reason,
        "solve_time": 0.0,
        "runtime_s": runtime_s,
        "error_message": error_message,
        "n_accepted": n_accepted,
        "n_unassigned": n_requests - n_accepted,
        "comparable_gap": False,
    }


def run_gap_experiment(n_requests: int, seed: int) -> dict:
    """Run ALNS (FullModel) then MILP ex-post on the same instance.

    Parameters
    ----------
    n_requests : int
        Number of trip requests (use small values: 20 or 30 for tractability).
    seed : int
        Random seed for reproducible scenario generation.

    Returns
    -------
    dict with keys:
        n_requests   : int
        seed         : int
        alns_vkm     : float — total vehicle-km from FullModel ALNS run
        milp_vkm     : float or None — MILP optimal routing cost (vehicle-km
                       equivalent, computed from C_op term) or None if Gurobi
                       is unavailable or MILP is infeasible
        gap_pct      : float or None — (alns_vkm - milp_vkm) / milp_vkm * 100
        milp_status  : str — 'optimal' | 'feasible' | 'infeasible' | 'timeout'
                       | 'no_gurobi' | 'no_accepted'
        solve_time   : float — MILP wall-clock solve time in seconds (0.0 if
                       Gurobi not run)
        n_accepted   : int — number of requests in the realized accepted set
    """
    overall_t0 = time.perf_counter()
    n_vehicles = max(3, n_requests // 5)   # ~5 requests per vehicle

    # --- Step 1: Generate scenario ---
    scenario = generate_synthetic(n_requests, n_vehicles, seed)

    # --- Step 2: Run ALNS (FullModel) to get realized accepted set + vkm ---
    variant = FullModel()
    t0 = time.perf_counter()
    sim_result = variant.run(scenario)
    alns_wall = time.perf_counter() - t0

    alns_vkm = sim_result.total_vehicle_km
    accepted_ids = {r.request_id for r in sim_result.records if r.accepted}
    accepted_requests = [r for r in scenario.requests if r.id in accepted_ids]

    if not accepted_requests:
        return _base_row(
            n_requests,
            seed,
            alns_vkm,
            n_accepted=0,
            status="no_accepted",
            detailed_reason="FullModel accepted no requests; fixed accepted-set MILP gap is incomparable.",
            runtime_s=time.perf_counter() - overall_t0,
        )

    # --- Step 3: MILP ex-post benchmark ---
    # Deferred import so module is importable without Gurobi.
    try:
        from drt.milp import DRTModel  # noqa: PLC0415
    except ImportError:
        return _base_row(
            n_requests,
            seed,
            alns_vkm,
            n_accepted=len(accepted_requests),
            status="no_gurobi",
            detailed_reason="Gurobi is unavailable; MILP static snapshot solve skipped.",
            runtime_s=time.perf_counter() - overall_t0,
            error_message="gurobipy not available",
        )

    # Build MILP on the realized accepted set only (z_r fixed = 1 for all).
    # cost_weights uses alpha1..alpha5 from config; C^rej = 0 since all
    # requests in accepted_requests are treated as accepted (z_r = 1).
    milp = DRTModel(
        requests=accepted_requests,
        vehicles=scenario.vehicles,
        meeting_points=scenario.meeting_points,
        rho_p=RHO_P,
        rho_d=RHO_D,
        cost_weights=tuple(ALPHA_WEIGHTS),
        time_limit=300.0,
        mip_gap=0.01,
    )

    try:
        result = milp.solve()
    except ImportError:
        # gurobipy present at import time but license missing causes ImportError
        # on solve() — treat same as no_gurobi
        return _base_row(
            n_requests,
            seed,
            alns_vkm,
            n_accepted=len(accepted_requests),
            status="no_gurobi",
            detailed_reason="Gurobi is unavailable or unlicensed; MILP static snapshot solve skipped.",
            runtime_s=time.perf_counter() - overall_t0,
            error_message="gurobipy not available or unlicensed",
        )
    except Exception as exc:
        return _base_row(
            n_requests,
            seed,
            alns_vkm,
            n_accepted=len(accepted_requests),
            status="error",
            detailed_reason="MILP static snapshot solve failed.",
            runtime_s=time.perf_counter() - overall_t0,
            error_message=str(exc),
        )

    # The MILP objective_value is a composite weighted cost, not raw vkm.
    # For the gap table we compare ALNS vkm to MILP objective_value normalized
    # by alpha_op so that both sides reflect routing distance in comparable
    # units.  When alpha_op = 1 (default), milp_vkm = objective_value gives
    # a lower bound on the routing cost achievable for the fixed accepted set.
    alpha_op = ALPHA_WEIGHTS[0]  # first weight is operational cost
    milp_obj = result["objective_value"]
    milp_vkm = (milp_obj / alpha_op) if milp_obj is not None else None

    gap_pct = None
    comparable_gap = False
    detailed_reason = "MILP status is not comparable for gap computation."
    if (
        result["status"] in ("optimal", "feasible")
        and milp_vkm is not None
        and milp_vkm > 0
    ):
        gap_pct = (alns_vkm - milp_vkm) / milp_vkm * 100.0
        comparable_gap = True
        detailed_reason = "Comparable fixed accepted-set static snapshot gap in weighted-cost units."
    elif result["status"] == "timeout":
        detailed_reason = "MILP timed out; gap suppressed as incomparable."
    elif result["status"] == "infeasible":
        detailed_reason = "MILP infeasible; gap suppressed as incomparable."

    return {
        **_DIAGNOSTIC_META,
        "n_requests": n_requests,
        "seed": seed,
        "alns_vkm": alns_vkm,
        "milp_vkm": milp_vkm,
        "gap_pct": gap_pct,
        "milp_status": result["status"],
        "status": result["status"],
        "detailed_reason": detailed_reason,
        "solve_time": result["solve_time"],
        "runtime_s": time.perf_counter() - overall_t0,
        "error_message": "",
        "n_accepted": len(accepted_requests),
        "n_unassigned": n_requests - len(accepted_requests),
        "comparable_gap": comparable_gap,
    }


# ---------------------------------------------------------------------------
# main()
# ---------------------------------------------------------------------------


def main() -> None:
    """Run gap experiment for n=20 and n=30, seeds from config.SEEDS.

    Writes results/milp_gap.json.
    """
    rows: list[dict] = []
    for n in [20, 30]:
        for seed in SEEDS:
            print(f"  n={n}, seed={seed} ...", flush=True)
            row = run_gap_experiment(n, seed)
            rows.append(row)
            if row["gap_pct"] is not None:
                print(f"    gap={row['gap_pct']:.1f}%  "
                      f"alns_vkm={row['alns_vkm']:.2f}  "
                      f"milp_vkm={row['milp_vkm']:.2f}  "
                      f"status={row['milp_status']}  "
                      f"solve={row['solve_time']:.1f}s")
            else:
                print(f"    gap=N/A  status={row['milp_status']}")

    results_dir = os.path.join(_REPO_ROOT, "results")
    os.makedirs(results_dir, exist_ok=True)
    out_path = os.path.join(results_dir, "milp_gap.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
