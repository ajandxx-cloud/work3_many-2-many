"""
milp.py — EXACT-01/02/03: Static snapshot MILP for many-to-many DRT.

Formulates and solves a batch assignment problem:
  - Accepts/rejects requests
  - Assigns each accepted request to a vehicle
  - Selects pickup and dropoff meeting points
  - Schedules pickup and dropoff times

Requires Gurobi (gurobipy). Import is deferred to build()/solve() so the
module can be imported without a Gurobi installation.
"""
from __future__ import annotations

import json
import math
import os
from typing import Optional

from drt.types import MeetingPoint, Request, Vehicle
from drt.candidate import euclidean, generate_candidates


class DRTModel:
    """
    EXACT-01: Static snapshot MILP for many-to-many DRT with bidirectional
    meeting points.

    Solves a batch of requests assigned to vehicles in a single optimisation
    window.  The model is a *static snapshot* — it takes a fixed set of
    requests and vehicles and finds the optimal assignment.

    Parameters
    ----------
    requests        : list of Request objects
    vehicles        : list of Vehicle objects
    meeting_points  : list of MeetingPoint objects (full candidate set)
    rho_p           : maximum pickup walking radius (ρ^P)
    rho_d           : maximum dropoff walking radius (ρ^D)
    cost_weights    : (α1, α2, α3, α4, α5) for C^op, C^wait, C^walk,
                      C^IVT, C^rej
    travel_speed    : speed used to convert distance to travel time
    time_limit      : Gurobi time limit in seconds (T-02-07 DoS mitigation)
    mip_gap         : Gurobi relative MIP gap tolerance
    """

    def __init__(
        self,
        requests: list[Request],
        vehicles: list[Vehicle],
        meeting_points: list[MeetingPoint],
        rho_p: float,
        rho_d: float,
        cost_weights: tuple = (1, 1, 1, 1, 5),
        travel_speed: float = 1.0,
        time_limit: float = 300.0,
        mip_gap: float = 0.05,
    ) -> None:
        self.requests = requests
        self.vehicles = vehicles
        self.meeting_points = meeting_points
        self.rho_p = rho_p
        self.rho_d = rho_d
        self.alpha = cost_weights
        self.speed = travel_speed
        self.time_limit = time_limit
        self.mip_gap = mip_gap
        self.model = None
        self.result: Optional[dict] = None
        # internal variable references set by build()
        self._z = None
        self._x = None
        self._s = None
        self._cand_p: Optional[dict] = None
        self._cand_d: Optional[dict] = None

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _travel_time(self, a: tuple, b: tuple) -> float:
        return euclidean(a, b) / self.speed

    # ------------------------------------------------------------------
    # Model construction
    # ------------------------------------------------------------------

    def build(self) -> None:
        """
        EXACT-01: Build the Gurobi model.

        Must be called before solve().  Raises ImportError if gurobipy is
        not installed.
        """
        try:
            import gurobipy as gp
            from gurobipy import GRB
        except ImportError:
            raise ImportError(
                "gurobipy not found. Install with: pip install gurobipy "
                "(requires Gurobi license)"
            )

        R = self.requests
        V = self.vehicles
        MP = self.meeting_points
        speed = self.speed
        BIG_M = 1e6

        # Candidate meeting points per request (filtered by walking radius)
        cand_p = {
            r.id: generate_candidates(r, MP, self.rho_p, len(MP), "pickup")
            for r in R
        }
        cand_d = {
            r.id: generate_candidates(r, MP, self.rho_d, len(MP), "dropoff")
            for r in R
        }
        self._cand_p = cand_p
        self._cand_d = cand_d

        m = gp.Model("drt_milp")
        m.setParam("TimeLimit", self.time_limit)
        m.setParam("MIPGap", self.mip_gap)
        m.setParam("OutputFlag", 0)  # suppress Gurobi console output

        # ------------------------------------------------------------------
        # Decision variables
        # ------------------------------------------------------------------

        # z[r] ∈ {0,1}: accept request r  (EXACT-01)
        z = m.addVars([r.id for r in R], vtype=GRB.BINARY, name="z")

        # x[r,v,mp_p,mp_d] ∈ {0,1}: assign request r to vehicle v with
        # pickup meeting point mp_p and dropoff meeting point mp_d
        x = {}
        for r in R:
            for v in V:
                for mp_p in cand_p[r.id]:
                    for mp_d in cand_d[r.id]:
                        x[r.id, v.id, mp_p.id, mp_d.id] = m.addVar(
                            vtype=GRB.BINARY,
                            name=f"x_{r.id}_{v.id}_{mp_p.id}_{mp_d.id}",
                        )

        # s[r,v,'p'] ≥ 0: scheduled pickup time for request r on vehicle v
        # s[r,v,'d'] ≥ 0: scheduled dropoff time for request r on vehicle v
        s = {}
        for r in R:
            for v in V:
                s[r.id, v.id, "p"] = m.addVar(
                    lb=0, ub=BIG_M, name=f"s_p_{r.id}_{v.id}"
                )
                s[r.id, v.id, "d"] = m.addVar(
                    lb=0, ub=BIG_M, name=f"s_d_{r.id}_{v.id}"
                )

        m.update()

        # ------------------------------------------------------------------
        # Constraints (11 classes from constraints.tex)
        # ------------------------------------------------------------------

        # con:assignment — each accepted request assigned to exactly one
        # (vehicle, pickup mp, dropoff mp) combination
        for r in R:
            m.addConstr(
                gp.quicksum(
                    x[r.id, v.id, mp_p.id, mp_d.id]
                    for v in V
                    for mp_p in cand_p[r.id]
                    for mp_d in cand_d[r.id]
                )
                == z[r.id],
                name=f"con_assign_{r.id}",
            )

        # con:capacity — total requests assigned to vehicle v ≤ Q_v
        # (simplified simultaneous capacity bound)
        for v in V:
            m.addConstr(
                gp.quicksum(
                    x[r.id, v.id, mp_p.id, mp_d.id]
                    for r in R
                    for mp_p in cand_p[r.id]
                    for mp_d in cand_d[r.id]
                )
                <= v.capacity,
                name=f"con_capacity_{v.id}",
            )

        # con:tw-early — pickup time ≥ earliest (binding only when assigned)
        for r in R:
            for v in V:
                assigned_rv = gp.quicksum(
                    x[r.id, v.id, mp_p.id, mp_d.id]
                    for mp_p in cand_p[r.id]
                    for mp_d in cand_d[r.id]
                )
                m.addConstr(
                    s[r.id, v.id, "p"] >= r.earliest * assigned_rv,
                    name=f"con_tw_early_{r.id}_{v.id}",
                )

        # con:tw-late — pickup time ≤ latest (big-M when not assigned)
        for r in R:
            for v in V:
                assigned_rv = gp.quicksum(
                    x[r.id, v.id, mp_p.id, mp_d.id]
                    for mp_p in cand_p[r.id]
                    for mp_d in cand_d[r.id]
                )
                m.addConstr(
                    s[r.id, v.id, "p"] <= r.latest + BIG_M * (1 - assigned_rv),
                    name=f"con_tw_late_{r.id}_{v.id}",
                )

        # con:ridetime — dropoff − pickup ≤ max_ride_time
        for r in R:
            for v in V:
                m.addConstr(
                    s[r.id, v.id, "d"] - s[r.id, v.id, "p"] <= r.max_ride_time,
                    name=f"con_ridetime_{r.id}_{v.id}",
                )

        # con:precedence-time — pickup before dropoff
        for r in R:
            for v in V:
                m.addConstr(
                    s[r.id, v.id, "d"] >= s[r.id, v.id, "p"],
                    name=f"con_prec_time_{r.id}_{v.id}",
                )

        # con:precedence-pos — travel time from pickup mp to dropoff mp must
        # fit between scheduled times (big-M when not assigned)
        for r in R:
            for v in V:
                for mp_p in cand_p[r.id]:
                    for mp_d in cand_d[r.id]:
                        tt = self._travel_time(mp_p.coords, mp_d.coords)
                        m.addConstr(
                            s[r.id, v.id, "d"]
                            >= s[r.id, v.id, "p"]
                            + tt * x[r.id, v.id, mp_p.id, mp_d.id],
                            name=(
                                f"con_prec_pos_{r.id}_{v.id}"
                                f"_{mp_p.id}_{mp_d.id}"
                            ),
                        )

        # con:walk-pickup — walking distance origin → pickup mp ≤ rho_p
        # (already enforced by candidate filtering; explicit for completeness)
        for r in R:
            for v in V:
                for mp_p in cand_p[r.id]:
                    for mp_d in cand_d[r.id]:
                        walk_p = euclidean(r.origin, mp_p.coords)
                        m.addConstr(
                            walk_p * x[r.id, v.id, mp_p.id, mp_d.id]
                            <= self.rho_p,
                            name=(
                                f"con_walk_p_{r.id}_{v.id}"
                                f"_{mp_p.id}_{mp_d.id}"
                            ),
                        )

        # con:walk-dropoff — walking distance dropoff mp → destination ≤ rho_d
        for r in R:
            for v in V:
                for mp_p in cand_p[r.id]:
                    for mp_d in cand_d[r.id]:
                        walk_d = euclidean(mp_d.coords, r.destination)
                        m.addConstr(
                            walk_d * x[r.id, v.id, mp_p.id, mp_d.id]
                            <= self.rho_d,
                            name=(
                                f"con_walk_d_{r.id}_{v.id}"
                                f"_{mp_p.id}_{mp_d.id}"
                            ),
                        )

        # con:time-consistency — schedule time ≥ vehicle start time
        for r in R:
            for v in V:
                m.addConstr(
                    s[r.id, v.id, "p"] >= v.current_time,
                    name=f"con_time_consist_{r.id}_{v.id}",
                )

        # con:route-duration — dropoff time ≤ vehicle start + max_route_duration
        for r in R:
            for v in V:
                m.addConstr(
                    s[r.id, v.id, "d"] - v.current_time
                    <= v.max_route_duration,
                    name=f"con_route_dur_{r.id}_{v.id}",
                )

        # ------------------------------------------------------------------
        # Objective: min α1·C^op + α2·C^wait + α3·C^walk + α4·C^IVT + α5·C^rej
        # ------------------------------------------------------------------
        a1, a2, a3, a4, a5 = self.alpha

        # C^op: operational cost ∝ in-vehicle travel distance
        c_op = gp.quicksum(
            euclidean(mp_p.coords, mp_d.coords)
            / speed
            * x[r.id, v.id, mp_p.id, mp_d.id]
            for r in R
            for v in V
            for mp_p in cand_p[r.id]
            for mp_d in cand_d[r.id]
        )

        # C^wait: waiting cost ∝ scheduled pickup time
        c_wait = gp.quicksum(
            s[r.id, v.id, "p"] for r in R for v in V
        )

        # C^walk: walking cost ∝ total walk distance (pickup + dropoff)
        c_walk = gp.quicksum(
            (
                euclidean(r.origin, mp_p.coords)
                + euclidean(mp_d.coords, r.destination)
            )
            * x[r.id, v.id, mp_p.id, mp_d.id]
            for r in R
            for v in V
            for mp_p in cand_p[r.id]
            for mp_d in cand_d[r.id]
        )

        # C^IVT: in-vehicle time cost
        c_ivt = gp.quicksum(
            s[r.id, v.id, "d"] - s[r.id, v.id, "p"]
            for r in R
            for v in V
        )

        # C^rej: rejection penalty
        c_rej = gp.quicksum(1 - z[r.id] for r in R)

        m.setObjective(
            a1 * c_op + a2 * c_wait + a3 * c_walk + a4 * c_ivt + a5 * c_rej,
            GRB.MINIMIZE,
        )

        self.model = m
        self._z = z
        self._x = x
        self._s = s

    # ------------------------------------------------------------------
    # Solve
    # ------------------------------------------------------------------

    def solve(self) -> dict:
        """
        EXACT-02/03: Solve the model.

        Builds the model if not already built.  Returns a result dict with:
          status          : 'optimal' | 'feasible' | 'infeasible' | 'timeout'
          objective_value : float or None
          mip_gap         : float or None
          solve_time      : float (seconds)
          accepted        : list of accepted request ids
        """
        try:
            import gurobipy as gp
            from gurobipy import GRB
        except ImportError:
            raise ImportError(
                "gurobipy not found. Install with: pip install gurobipy "
                "(requires Gurobi license)"
            )

        if self.model is None:
            self.build()

        self.model.optimize()
        m = self.model

        status_map = {
            GRB.OPTIMAL: "optimal",
            GRB.SUBOPTIMAL: "feasible",
            GRB.INFEASIBLE: "infeasible",
            GRB.TIME_LIMIT: "timeout",
        }
        status = status_map.get(m.Status, "unknown")

        result: dict = {
            "status": status,
            "objective_value": m.ObjVal if m.SolCount > 0 else None,
            "mip_gap": m.MIPGap if m.SolCount > 0 else None,
            "solve_time": m.Runtime,
            "accepted": [],
        }
        if m.SolCount > 0:
            result["accepted"] = [
                r.id for r in self.requests if self._z[r.id].X > 0.5
            ]

        self.result = result
        return result

    # ------------------------------------------------------------------
    # Benchmark output  (EXACT-04)
    # ------------------------------------------------------------------

    def write_benchmark(
        self, instance_id: str, output_path: str = "results/milp_benchmark.json"
    ) -> None:
        """
        EXACT-04: Write solve result to a JSON benchmark file.

        The file is consumed by Phase 3 heuristic comparison.

        Parameters
        ----------
        instance_id : human-readable label for this instance
        output_path : destination file path (created if missing)
        """
        if self.result is None:
            raise RuntimeError("Call solve() before write_benchmark().")

        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

        payload = {
            "instance_id": instance_id,
            "n_requests": len(self.requests),
            "n_vehicles": len(self.vehicles),
            "objective_value": self.result["objective_value"],
            "mip_gap": self.result["mip_gap"],
            "solve_time": self.result["solve_time"],
            "accepted_requests": self.result["accepted"],
        }

        with open(output_path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2)
