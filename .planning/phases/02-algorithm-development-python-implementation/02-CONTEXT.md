# Phase 2: Algorithm Development & Python Implementation - Context

**Gathered:** 2026-04-11
**Status:** Ready for planning

<domain>
## Phase Boundary

Phase 2 delivers a working Python implementation of both the exact MILP benchmark and the large-scale rolling horizon + ALNS heuristic. The package `src/drt/` is the primary artifact. All modules are tested with pytest. The heuristic must meet the response-time requirement (< 1 second average decision time per request on large-scale instances).

</domain>

<decisions>
## Implementation Decisions

### Solver
- **Gurobi (gurobipy)** — user decision (D-01). Do not use PuLP, OR-Tools, or CPLEX.
- Gurobi Python API: `import gurobipy as gp; from gurobipy import GRB`
- Model object: `gp.Model("drt_milp")`

### Python Package Structure
- **Single package `src/drt/`** — user decision (D-02)
- Module layout (fixed, do not reorganize):
  - `types.py` — dataclasses: Request, Vehicle, Route, MeetingPoint, Bundle
  - `choice.py` — MNL utility and choice probability
  - `candidate.py` — HEUR-01: top-k candidate generation
  - `feasibility.py` — HEUR-03: fast feasibility checker (reused by MILP and ALNS)
  - `insertion.py` — HEUR-02: online insertion evaluator
  - `milp.py` — EXACT-01/02/03: Gurobi MILP formulation
  - `alns.py` — HEUR-04/05: rolling horizon + ALNS operators

### Testing
- **pytest** — user decision (D-03)
- Test files in `tests/` directory at project root
- At minimum: `test_feasibility.py`, `test_insertion.py`, `test_candidate.py`, `test_milp.py`

### Key Design Choices
- `feasibility.py` is a shared dependency — both `milp.py` (constraint validation) and `alns.py` (insertion feasibility during repair) import from it
- All dataclasses use `@dataclass` from Python stdlib; no Pydantic or attrs
- MNL choice in `choice.py` is stateless (pure functions); no class needed
- Euclidean distance model (from Phase 1 decision) — no road network data required
- Continuous time as float (seconds or minutes from simulation start)

</decisions>

<notation_mapping>
## Notation Mapping: Python Variables → Phase 1 Math Symbols

| Python name | Math symbol | Source file | Description |
|---|---|---|---|
| `Request.id` | r | types.py | Request index |
| `Request.origin` | o_r | types.py | Origin coordinates (x, y) |
| `Request.destination` | d_r | types.py | Destination coordinates (x, y) |
| `Request.earliest` | e_r | types.py | Earliest pickup time |
| `Request.latest` | l_r | types.py | Latest pickup time |
| `Request.max_ride_time` | T_r^max | types.py | Maximum in-vehicle time |
| `Vehicle.id` | v | types.py | Vehicle index |
| `Vehicle.capacity` | Q_v | types.py | Seat capacity |
| `Vehicle.max_route_duration` | T_v^max | types.py | Max total route duration |
| `MeetingPoint.id` | m | types.py | Meeting point index |
| `MeetingPoint.coords` | (x_m, y_m) | types.py | Coordinates |
| `Bundle.pickup_mp` | m_r^P | types.py | Assigned pickup meeting point |
| `Bundle.dropoff_mp` | m_r^D | types.py | Assigned dropoff meeting point |
| `Bundle.departure_time` | τ_r | types.py | Scheduled departure time |
| `Bundle.price` | p_r | types.py | Fare |
| `rho_p` | ρ^P | candidate.py | Max walking radius for pickup |
| `rho_d` | ρ^D | candidate.py | Max walking radius for dropoff |
| `k_top` | k^top | candidate.py | Number of top candidates returned |
| `H` | H | alns.py | Rolling horizon window length |
| `delta` | Δ | alns.py | Re-optimization interval |
| `z_r` | z_r | milp.py | Binary accept variable |
| `s_vi` | s_{v,i} | milp.py | Schedule time at position i in route v |
| `beta` | β = (β1,β2,β3,β4) | choice.py | MNL utility coefficients |
| `U_rb` | U_rb^k | choice.py | Utility of bundle b for type-k passenger |
| `P_rb` | P_rb^k | choice.py | Choice probability |
| `P_r0` | P_r0^k | choice.py | Outside option probability |

</notation_mapping>

<dependency_notes>
## Module Dependency Graph

```
types.py        (no internal deps)
choice.py       → types.py
candidate.py    → types.py
feasibility.py  → types.py
insertion.py    → types.py, feasibility.py, candidate.py
milp.py         → types.py, feasibility.py
alns.py         → types.py, feasibility.py, insertion.py
```

`feasibility.py` is the critical shared module. Both `milp.py` (for constraint validation in post-processing) and `alns.py` (for repair operator feasibility checks) depend on it. It must be implemented before Plans 02-03 and 02-04.

</dependency_notes>

<phase1_artifacts>
## Phase 1 Artifacts to Reference

- `model/notation.tex` — all symbols (Q_v, L^max, T_v^max, ρ^P, ρ^D, k^top, H, Δ, etc.)
- `model/constraints.tex` — constraint labels: con:capacity, con:tw-early, con:tw-late, con:ridetime, con:walk-pickup, con:walk-dropoff, con:precedence-pos, con:precedence-time, con:time-consistency, con:route-duration
- `model/choice-model.tex` — MNL utility, β parameters, choice probability
- `model/problem-definition.tex` — objective, decision vector

</phase1_artifacts>

<deferred>
## Deferred

- Anticipatory/lookahead extensions (EXT-01)
- Electric vehicle constraints (EXT-03)
- Real data validation (EXT-04)
- Parallel ALNS (multi-threaded destroy/repair) — post-Phase 2 optimization if needed

</deferred>
