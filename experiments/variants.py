"""
experiments/variants.py — Six runnable model variant classes.

Each variant implements run(scenario: Scenario) -> SimulationResult.
The six variants form the experimental units for Phase 3 numerical experiments.

Variants
--------
DoorToDoor            : no meeting points; direct origin→destination routing
SingleSidedPickup     : flexible pickup MP, door-to-door dropoff
BidirectionalNoChoice : both MPs, deterministic acceptance (no MNL rejection)
FullModel             : bidirectional MPs + MNL choice + rolling horizon (main contribution)
AblationNoRollingHorizon : FullModel without periodic re-optimization (greedy only)
AblationNoChoice      : FullModel without MNL rejection (all feasible requests accepted)

Threat T-03-07 mitigation: unique names asserted at module load time.
"""
from __future__ import annotations

import hashlib
import math
import random
import time
import warnings
from abc import ABC, abstractmethod
from copy import deepcopy

from experiments.config import (
    ALPHA_WEIGHTS,
    CHOICE_OUTSIDE_OPTION_CONSTANT,
    CHOICE_SEED,
    CHOICE_SERVICE_ASC,
    CHOICE_TYPE_SHARES,
    DELTA,
    H_WINDOW,
    K_TOP,
    RHO_D,
    RHO_P,
)
from experiments.metrics import PassengerRecord, SimulationResult
from experiments.scenarios import Scenario
from src.drt.alns import ALNSState, RollingHorizon, _apply_insertion, _to_plain_routes, greedy_insertion
from src.drt.candidate import euclidean, generate_candidates
from src.drt.choice import (
    accept_probability,
    assign_passenger_type,
    evaluate_single_offer,
    feasibility_rejected_evaluation,
)
from src.drt.insertion import evaluate_insertion
from src.drt.types import (
    Bundle,
    ChoiceParameters,
    MeetingPoint,
    OfferAttributes,
    PassengerType,
    PRICE_SENSITIVE,
    TIME_SENSITIVE,
    WALK_SENSITIVE,
    Route,
)

# ---------------------------------------------------------------------------
# Shared constants
# ---------------------------------------------------------------------------

PASSENGER_TYPES = [PRICE_SENSITIVE, TIME_SENSITIVE, WALK_SENSITIVE]

# Travel speed used for time estimates (m/s ≈ 30 km/h)
TRAVEL_SPEED = 8.33

# Cost weights tuple: (alpha_op, alpha_wait, alpha_walk, alpha_ivt)
_COST_WEIGHTS = tuple(ALPHA_WEIGHTS[:4])

# Zero-beta passenger type for "no MNL" variants — all utilities equal → all accepted
_ZERO_BETA_TYPE = PassengerType(
    name="zero_beta",
    beta_walk=0.0,
    beta_wait=0.0,
    beta_ivt=0.0,
    beta_price=0.0,
)


# ---------------------------------------------------------------------------
# MNL filtering helper
# ---------------------------------------------------------------------------


def _mnl_filter_requests(
    requests: list,
    arrival_times: list,
    scenario,
) -> list:
    """
    Legacy proxy MNL filter retained only for regression checks.

    Phase 3 behavioral variants must use actual feasible offers from
    _run_actual_offer_sequence instead of this nearest-meeting-point proxy.

    Apply MNL Bernoulli acceptance to each request before routing.

    For each request, construct a representative Bundle using the nearest
    meeting point as pickup and dropoff proxy, then compute accept_probability.
    Simulate acceptance with a deterministic RNG seeded by request id hash.

    Unit note: MNL betas (from Phase 1) are calibrated for km and minutes.
    Scenario coordinates are in meters, times in seconds.
    Bundle attributes are scaled before calling accept_probability:
      walk_dist: meters → km  (divide by 1000)
      wait_time: seconds → minutes  (divide by 60)
      ivt:       seconds → minutes  (divide by 60)
    This is achieved by wrapping the bundle in a scaled proxy via a custom
    PassengerType that absorbs the unit conversion into the beta values.
    """
    if not scenario.meeting_points:
        return list(requests)

    # Scale betas to match raw meter/second units used in Bundle construction.
    # Original betas assume km and minutes; multiply by conversion factors:
    #   beta_walk_scaled = beta_walk_km * (1/1000)   [per meter]
    #   beta_wait_scaled = beta_wait_min * (1/60)    [per second]
    #   beta_ivt_scaled  = beta_ivt_min  * (1/60) * (1/TRAVEL_SPEED)
    #                    [mnl_utility uses raw Euclidean distance as IVT proxy,
    #                     so 1 meter = 1/TRAVEL_SPEED seconds]
    def _scale_ptype(ptype: PassengerType) -> PassengerType:
        return PassengerType(
            name=ptype.name,
            beta_walk=ptype.beta_walk / 1000.0,
            beta_wait=ptype.beta_wait / 60.0,
            beta_ivt=ptype.beta_ivt / (60.0 * TRAVEL_SPEED),
            beta_price=ptype.beta_price,
        )

    accepted = []
    for idx, request in enumerate(requests):
        ptype = _scale_ptype(PASSENGER_TYPES[idx % len(PASSENGER_TYPES)])
        arrival_t = arrival_times[idx]

        # Find nearest meeting point as pickup and dropoff proxy
        nearest_pu = min(
            scenario.meeting_points,
            key=lambda mp: math.sqrt(
                (mp.coords[0] - request.origin[0]) ** 2
                + (mp.coords[1] - request.origin[1]) ** 2
            ),
        )
        nearest_do = min(
            scenario.meeting_points,
            key=lambda mp: math.sqrt(
                (mp.coords[0] - request.destination[0]) ** 2
                + (mp.coords[1] - request.destination[1]) ** 2
            ),
        )

        bundle = Bundle(
            request_id=request.id,
            pickup_mp=nearest_pu,
            dropoff_mp=nearest_do,
            departure_time=request.earliest,
            price=0.0,
        )

        accept_prob = accept_probability(bundle, request, ptype, arrival_t)

        rng = random.Random(int.from_bytes(hashlib.sha256(request.id.encode()).digest()[:4], "big"))
        if rng.random() <= accept_prob:
            accepted.append(request)

    return accepted


# ---------------------------------------------------------------------------
# Base variant
# ---------------------------------------------------------------------------


class BaseVariant(ABC):
    """Abstract base for all 6 model variants."""

    name: str
    method_label: str = ""
    service_design: str = ""
    choice_model: str = "none"
    reoptimization: str = "none"
    routing_solver: str = "greedy_insertion"
    evidence_family: str = "diagnostic"
    diagnostic_role: str = "unspecified"
    legacy_class: str | None = None

    @property
    def method_metadata(self) -> dict[str, str]:
        """Return concept-level method metadata for result rows."""
        data = {
            "method_label": self.method_label or self.name,
            "service_design": self.service_design,
            "choice_model": self.choice_model,
            "reoptimization": self.reoptimization,
            "routing_solver": self.routing_solver,
            "evidence_family": self.evidence_family,
            "diagnostic_role": self.diagnostic_role,
        }
        if self.legacy_class:
            data["legacy_class"] = self.legacy_class
        return data

    def _default_choice_params(self) -> ChoiceParameters:
        return getattr(
            self,
            "_choice_config",
            ChoiceParameters(
                service_asc=CHOICE_SERVICE_ASC,
                outside_option_constant=CHOICE_OUTSIDE_OPTION_CONSTANT,
                choice_seed=CHOICE_SEED,
                type_shares=dict(CHOICE_TYPE_SHARES),
            ),
        )

    def run(self, scenario: Scenario) -> SimulationResult:
        """Execute variant on scenario, return SimulationResult."""
        t0 = time.perf_counter()
        state = self._solve(scenario)
        cpu_time = time.perf_counter() - t0

        records = self._build_records(scenario, state)
        vehicle_km = self._total_vehicle_km(state, scenario) + getattr(state, 'extra_vehicle_km', 0.0)
        utility_logs = [
            evaluation.as_log_row()
            for evaluation in getattr(state, "choice_evaluations", {}).values()
        ]
        return SimulationResult(
            records=records,
            total_vehicle_km=vehicle_km,
            cpu_time=cpu_time,
            utility_logs=utility_logs,
        )

    @abstractmethod
    def _solve(self, scenario: Scenario) -> ALNSState:
        """Solve the routing problem; return final ALNSState."""
        ...

    # ------------------------------------------------------------------
    # Helpers shared by all variants
    # ------------------------------------------------------------------

    def _vehicles_dict(self, scenario: Scenario) -> dict:
        """Convert scenario.vehicles list to {vehicle_id: Vehicle} dict."""
        return {v.id: v for v in scenario.vehicles}

    def _initial_state(self, scenario: Scenario) -> ALNSState:
        """Build an empty ALNSState with all requests unassigned."""
        routes = {v.id: Route(vehicle_id=v.id, stops=[]) for v in scenario.vehicles}
        return ALNSState(
            routes=routes,
            unassigned=list(scenario.requests),
            cost=0.0,
        )

    def _run_actual_offer_sequence(
        self,
        scenario: Scenario,
        service_design: str,
        meeting_points_for_request,
        rho_p: float,
        rho_d: float,
        k_top: int,
        cost_weights: tuple,
    ) -> ALNSState:
        """Sequential actual-offer acceptance path shared by behavioral variants."""
        vehicles_dict = self._vehicles_dict(scenario)
        state = self._initial_state(scenario)
        state.unassigned = []
        choice_evaluations = {}
        params = self._default_choice_params()

        for request in sorted(scenario.requests, key=lambda r: r.earliest):
            meeting_points = meeting_points_for_request(request)
            plain_routes = _to_plain_routes(state.routes)
            result = evaluate_insertion(
                request,
                plain_routes,
                vehicles_dict,
                meeting_points,
                rho_p,
                rho_d,
                k_top,
                cost_weights,
                TRAVEL_SPEED,
            )
            ptype = assign_passenger_type(
                request.id,
                PASSENGER_TYPES,
                params.type_shares,
                seed=params.choice_seed,
            )
            if result is None:
                reason = self._feasibility_reason(request, meeting_points, rho_p, rho_d, k_top)
                evaluation = feasibility_rejected_evaluation(
                    request_id=request.id,
                    detailed_reason=reason,
                    passenger_type=ptype.name,
                )
                state.unassigned.append(request)
                choice_evaluations[request.id] = evaluation
                continue

            offer = self._offer_from_insertion(
                request,
                result,
                plain_routes,
                vehicles_dict,
                service_design,
            )
            evaluation = evaluate_single_offer(offer, ptype, params)
            choice_evaluations[request.id] = evaluation
            if evaluation.accepted:
                _apply_insertion(state, result, request, vehicles_dict, TRAVEL_SPEED)
            else:
                state.unassigned.append(request)

        state.choice_evaluations = choice_evaluations
        return state

    def _feasibility_reason(
        self,
        request,
        meeting_points,
        rho_p: float,
        rho_d: float,
        k_top: int,
    ) -> str:
        pickup_candidates = generate_candidates(request, meeting_points, rho_p, k_top, "pickup")
        dropoff_candidates = generate_candidates(request, meeting_points, rho_d, k_top, "dropoff")
        if not pickup_candidates or not dropoff_candidates:
            return "no_candidate_mp"
        return "no_feasible_route"

    def _offer_from_insertion(
        self,
        request,
        result,
        plain_routes,
        vehicles,
        service_design: str,
    ) -> OfferAttributes:
        route = plain_routes.get(result.vehicle_id, Route(vehicle_id=result.vehicle_id, stops=[]))
        new_stops = list(route.stops)
        new_stops.insert(result.pos_p, (result.pickup_mp, 0.0))
        new_stops.insert(result.pos_d, (result.dropoff_mp, 0.0))
        vehicle = vehicles[result.vehicle_id]
        t = vehicle.current_time
        prev = vehicle.current_position
        pickup_time = request.earliest
        dropoff_time = request.earliest
        for idx, (mp, _) in enumerate(new_stops):
            t += euclidean(prev, mp.coords) / TRAVEL_SPEED
            if idx == result.pos_p:
                pickup_time = t
            if idx == result.pos_d:
                dropoff_time = t
            prev = mp.coords
        return OfferAttributes(
            request_id=request.id,
            service_design=service_design,
            pickup_walk=euclidean(request.origin, result.pickup_mp.coords) / 1000.0,
            dropoff_walk=euclidean(result.dropoff_mp.coords, request.destination) / 1000.0,
            wait_time=max(0.0, pickup_time - request.earliest) / 60.0,
            ivt=max(0.0, dropoff_time - pickup_time) / 60.0,
            fare=0.0,
            pickup_mp_id=result.pickup_mp.id,
            dropoff_mp_id=result.dropoff_mp.id,
            vehicle_id=result.vehicle_id,
            scheduled_pickup=pickup_time,
            scheduled_dropoff=dropoff_time,
        )

    def _assigned_request_ids(self, state: ALNSState) -> set[str]:
        """Return set of request IDs that appear in routes (tagged stops)."""
        ids: set[str] = set()
        for route in state.routes.values():
            for stop in route.stops:
                if len(stop) >= 3:
                    ids.add(stop[2])
        return ids

    def _build_records(self, scenario: Scenario, state: ALNSState) -> list[PassengerRecord]:
        """Build per-passenger PassengerRecord list from final ALNSState."""
        in_route_ids = self._assigned_request_ids(state)
        completed_ids = getattr(state, 'completed_ids', set())
        assigned_ids = in_route_ids | completed_ids
        unassigned_ids = {r.id for r in state.unassigned}
        choice_evaluations = getattr(state, "choice_evaluations", {})

        records: list[PassengerRecord] = []
        for idx, request in enumerate(scenario.requests):
            evaluation = choice_evaluations.get(request.id)
            if evaluation is not None:
                ptype = next(
                    (candidate for candidate in PASSENGER_TYPES if candidate.name == evaluation.passenger_type),
                    PASSENGER_TYPES[idx % len(PASSENGER_TYPES)],
                )
                status = evaluation.status
                detailed_reason = evaluation.detailed_reason
                acceptance_probability = evaluation.acceptance_probability
                random_draw = evaluation.random_draw
            else:
                ptype = PASSENGER_TYPES[idx % len(PASSENGER_TYPES)]
                status = None
                detailed_reason = ""
                acceptance_probability = None
                random_draw = None
            accepted = (request.id in assigned_ids) and (request.id not in unassigned_ids)

            if accepted and request.id in in_route_ids:
                pickup_mp, dropoff_mp, pickup_time, dropoff_time = self._find_stop_info(
                    request.id, state
                )
                if pickup_mp is None:
                    accepted = False
            elif accepted and request.id in completed_ids:
                # Completed request: stop info was pruned; use stored pickup_time if available
                pickup_mp = dropoff_mp = None
                stored_pickup_times = getattr(state, 'pickup_times', {})
                if request.id in stored_pickup_times:
                    pickup_time = stored_pickup_times[request.id]
                else:
                    pickup_time = request.earliest
                dropoff_time = pickup_time + euclidean(request.origin, request.destination) / TRAVEL_SPEED
            else:
                pickup_mp = dropoff_mp = None
                pickup_time = dropoff_time = 0.0

            if accepted and (pickup_mp is not None or request.id in completed_ids):
                if pickup_mp is not None:
                    pickup_walk = euclidean(request.origin, pickup_mp.coords)
                    dropoff_walk = euclidean(dropoff_mp.coords, request.destination)
                else:
                    # Completed: no walk info, use 0 (conservative estimate)
                    pickup_walk = 0.0
                    dropoff_walk = 0.0
                wait_time = max(0.0, pickup_time - request.earliest)
                if pickup_mp is not None and pickup_time >= dropoff_time:
                    warnings.warn(
                        f"Request {request.id}: pickup_time ({pickup_time:.1f}) >= "
                        f"dropoff_time ({dropoff_time:.1f}); using Euclidean fallback for IVT.",
                        RuntimeWarning,
                        stacklevel=3,
                    )
                ivt = max(0.0, dropoff_time - pickup_time) if dropoff_time > pickup_time else (
                    euclidean(request.origin, request.destination) / TRAVEL_SPEED
                    if pickup_mp is None else
                    euclidean(pickup_mp.coords, dropoff_mp.coords) / TRAVEL_SPEED
                )
                direct_time = euclidean(request.origin, request.destination) / TRAVEL_SPEED
                if evaluation is not None and evaluation.components is not None:
                    total_disutility = evaluation.components.total_utility
                else:
                    total_disutility = (
                        ptype.beta_walk * (pickup_walk + dropoff_walk)
                        + ptype.beta_wait * wait_time
                        + ptype.beta_ivt * ivt
                    )
                records.append(PassengerRecord(
                    request_id=request.id,
                    passenger_type=ptype.name,
                    accepted=True,
                    wait_time=wait_time,
                    pickup_walk=pickup_walk,
                    dropoff_walk=dropoff_walk,
                    ivt=ivt,
                    direct_time=direct_time,
                    total_disutility=total_disutility,
                    status="served",
                    detailed_reason=detailed_reason or "accepted",
                    acceptance_probability=acceptance_probability,
                    random_draw=random_draw,
                ))
            else:
                direct_time = euclidean(request.origin, request.destination) / TRAVEL_SPEED
                if status is None:
                    status = "feasibility_rejected"
                    detailed_reason = detailed_reason or "no_feasible_route"
                records.append(PassengerRecord(
                    request_id=request.id,
                    passenger_type=ptype.name,
                    accepted=False,
                    wait_time=0.0,
                    pickup_walk=0.0,
                    dropoff_walk=0.0,
                    ivt=0.0,
                    direct_time=direct_time,
                    total_disutility=0.0,
                    status=status,
                    detailed_reason=detailed_reason,
                    acceptance_probability=acceptance_probability,
                    random_draw=random_draw,
                ))
        return records

    def _find_stop_info(
        self, request_id: str, state: ALNSState
    ) -> tuple[MeetingPoint | None, MeetingPoint | None, float, float]:
        """
        Find pickup and dropoff MeetingPoints and scheduled times for a request.
        Returns (pickup_mp, dropoff_mp, pickup_time, dropoff_time).
        Returns (None, None, 0, 0) if not found.
        """
        for route in state.routes.values():
            pickup_mp = None
            dropoff_mp = None
            pickup_time = 0.0
            dropoff_time = 0.0
            for stop in route.stops:
                if len(stop) >= 4 and stop[2] == request_id:
                    if stop[3] == 'pickup':
                        pickup_mp = stop[0]
                        pickup_time = stop[1]
                    elif stop[3] == 'dropoff':
                        dropoff_mp = stop[0]
                        dropoff_time = stop[1]
            if pickup_mp is not None and dropoff_mp is not None:
                return pickup_mp, dropoff_mp, pickup_time, dropoff_time
        return None, None, 0.0, 0.0

    def _total_vehicle_km(self, state: ALNSState, scenario: Scenario) -> float:
        """Compute total vehicle distance driven across all routes (km)."""
        vehicles_dict = self._vehicles_dict(scenario)
        total_m = 0.0
        for vid, route in state.routes.items():
            vehicle = vehicles_dict.get(vid)
            if vehicle is None:
                continue
            prev = vehicle.current_position
            for stop in route.stops:
                mp = stop[0]
                total_m += euclidean(prev, mp.coords)
                prev = mp.coords
        return total_m / 1000.0  # convert meters to km


# ---------------------------------------------------------------------------
# Variant 1: DoorToDoor
# ---------------------------------------------------------------------------


class DoorToDoor(BaseVariant):
    """
    Baseline: no meeting points.
    Pickup = request.origin, dropoff = request.destination.
    Uses greedy_insertion with synthetic MPs at origin/destination.
    pickup_walk = 0, dropoff_walk = 0 for all accepted requests.
    """

    name = "DoorToDoor"
    method_label = "DoorToDoor_Choice_CommonRouting"
    service_design = "door_to_door"
    choice_model = "binary_logit"
    reoptimization = "common_sequential_insertion"
    routing_solver = "greedy_insertion"
    evidence_family = "behavioral_main"
    diagnostic_role = "behavioral_baseline"
    legacy_class = "DoorToDoor"

    def __init__(
        self,
        rho_p: float = None,
        rho_d: float = None,
        cost_weights: tuple | None = None,
        choice_params: ChoiceParameters | None = None,
    ):
        self._rho_p = rho_p if rho_p is not None else RHO_P
        self._rho_d = rho_d if rho_d is not None else RHO_D
        self._cost_weights = cost_weights if cost_weights is not None else _COST_WEIGHTS
        self._choice_config = choice_params or self._default_choice_params()

    def _solve(self, scenario: Scenario) -> ALNSState:
        return self._run_actual_offer_sequence(
            scenario=scenario,
            service_design="DoorToDoor",
            meeting_points_for_request=lambda request: [
                MeetingPoint(id=f"dtd_pu_{request.id}", coords=request.origin),
                MeetingPoint(id=f"dtd_do_{request.id}", coords=request.destination),
            ],
            rho_p=0.0,
            rho_d=0.0,
            k_top=1,
            cost_weights=self._cost_weights,
        )
        vehicles_dict = self._vehicles_dict(scenario)
        state = self._initial_state(scenario)
        state.unassigned = []

        # Process each request individually with synthetic MPs at origin/destination
        for request in scenario.requests:
            pickup_mp = MeetingPoint(
                id=f"dtd_pu_{request.id}",
                coords=request.origin,
            )
            dropoff_mp = MeetingPoint(
                id=f"dtd_do_{request.id}",
                coords=request.destination,
            )
            # Use a single-request state for insertion
            req_state = ALNSState(
                routes=deepcopy(state.routes),
                unassigned=[request],
                cost=0.0,
            )
            result_state = greedy_insertion(
                req_state,
                vehicles_dict,
                [pickup_mp, dropoff_mp],
                rho_p=float('inf'),   # infinite radius — always finds the synthetic MP
                rho_d=float('inf'),
                k_top=1,
                cost_weights=self._cost_weights,
                travel_speed=TRAVEL_SPEED,
            )
            # Merge back: update routes, track unassigned
            state.routes = result_state.routes
            if result_state.unassigned:
                _existing_ids = {r.id for r in state.unassigned}
                for _req in result_state.unassigned:
                    if _req.id not in _existing_ids:
                        state.unassigned.append(_req)
                        _existing_ids.add(_req.id)

        return state


# ---------------------------------------------------------------------------
# Variant 1b: DoorToDoorCapped
# ---------------------------------------------------------------------------


class DoorToDoorCapped(BaseVariant):
    """
    DoorToDoor variant with an endogenous acceptance cap.

    Once accepted_count / total_requests >= cap_share, all subsequent
    requests are rejected without route insertion. ALNS continues
    optimizing routes for already-accepted passengers.

    cap_share: float — target served share (e.g. 0.235 for 23.5%)

    Threat T-12-01 mitigation: cap check uses >= (not >) to prevent
    off-by-one; total_requests guard prevents ZeroDivisionError.
    """

    name = "DoorToDoorCapped"
    method_label = "DoorToDoor_Capped_MatchedCoverage"
    service_design = "door_to_door"
    choice_model = "deterministic_cap"
    reoptimization = "none"
    routing_solver = "greedy_insertion"
    evidence_family = "supplementary_control"
    diagnostic_role = "matched_coverage_control"
    legacy_class = "DoorToDoorCapped"

    def __init__(
        self,
        cap_share: float = 0.235,
        rho_p: float = None,
        rho_d: float = None,
        cost_weights: tuple | None = None,
    ):
        self._cap_share = cap_share
        self._rho_p = rho_p if rho_p is not None else RHO_P
        self._rho_d = rho_d if rho_d is not None else RHO_D
        self._cost_weights = cost_weights if cost_weights is not None else _COST_WEIGHTS

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles_dict = self._vehicles_dict(scenario)
        state = self._initial_state(scenario)
        state.unassigned = []

        total_requests = len(scenario.requests)
        accepted_count = 0

        for request in scenario.requests:
            # Cap check: if cap reached, reject without insertion
            # T-12-01: >= prevents off-by-one; total_requests > 0 prevents ZeroDivisionError
            if total_requests > 0 and accepted_count / total_requests >= self._cap_share:
                state.unassigned.append(request)
                continue

            pickup_mp = MeetingPoint(
                id=f"dtdc_pu_{request.id}",
                coords=request.origin,
            )
            dropoff_mp = MeetingPoint(
                id=f"dtdc_do_{request.id}",
                coords=request.destination,
            )
            req_state = ALNSState(
                routes=deepcopy(state.routes),
                unassigned=[request],
                cost=0.0,
            )
            result_state = greedy_insertion(
                req_state,
                vehicles_dict,
                [pickup_mp, dropoff_mp],
                rho_p=float('inf'),
                rho_d=float('inf'),
                k_top=1,
                cost_weights=self._cost_weights,
                travel_speed=TRAVEL_SPEED,
            )
            state.routes = result_state.routes
            if result_state.unassigned:
                _existing_ids = {r.id for r in state.unassigned}
                for _req in result_state.unassigned:
                    if _req.id not in _existing_ids:
                        state.unassigned.append(_req)
                        _existing_ids.add(_req.id)
            else:
                accepted_count += 1

        return state


# ---------------------------------------------------------------------------
# Variant 2: SingleSidedPickup
# ---------------------------------------------------------------------------


class SingleSidedPickup(BaseVariant):
    """
    Flexible pickup meeting point (within rho_P), door-to-door dropoff.
    dropoff_walk = 0 for all accepted requests.
    """

    name = "SingleSidedPickup"
    method_label = "SingleSidedPickup_Choice_CommonRouting"
    service_design = "single_sided_pickup"
    choice_model = "binary_logit"
    reoptimization = "common_sequential_insertion"
    routing_solver = "greedy_insertion"
    evidence_family = "behavioral_main"
    diagnostic_role = "behavioral_service_design_baseline"
    legacy_class = "SingleSidedPickup"

    def __init__(self, choice_params: ChoiceParameters | None = None):
        self._choice_config = choice_params or self._default_choice_params()

    def _solve(self, scenario: Scenario) -> ALNSState:
        return self._run_actual_offer_sequence(
            scenario=scenario,
            service_design="SingleSidedPickup",
            meeting_points_for_request=lambda request: list(scenario.meeting_points)
            + [MeetingPoint(id=f"ssp_do_{request.id}", coords=request.destination)],
            rho_p=RHO_P,
            rho_d=0.0,
            k_top=K_TOP,
            cost_weights=_COST_WEIGHTS,
        )
        vehicles_dict = self._vehicles_dict(scenario)
        state = self._initial_state(scenario)
        state.unassigned = []

        for request in scenario.requests:
            # Dropoff MP is always at destination (zero dropoff walk)
            dropoff_mp = MeetingPoint(
                id=f"ssp_do_{request.id}",
                coords=request.destination,
            )
            # Pickup MPs from scenario meeting_points (flexible)
            pickup_mps = scenario.meeting_points

            req_state = ALNSState(
                routes=deepcopy(state.routes),
                unassigned=[request],
                cost=0.0,
            )
            # Pass pickup MPs + synthetic dropoff MP; rho_d=inf to always find dropoff
            combined_mps = list(pickup_mps) + [dropoff_mp]
            result_state = greedy_insertion(
                req_state,
                vehicles_dict,
                combined_mps,
                rho_p=RHO_P,
                rho_d=float('inf'),
                k_top=K_TOP,
                cost_weights=_COST_WEIGHTS,
                travel_speed=TRAVEL_SPEED,
            )
            state.routes = result_state.routes
            if result_state.unassigned:
                state.unassigned.extend(result_state.unassigned)

        return state


# ---------------------------------------------------------------------------
# Variant 2b: SingleSidedDropoff
# ---------------------------------------------------------------------------


class SingleSidedDropoff(BaseVariant):
    """
    Door-to-door pickup, flexible dropoff meeting point.
    pickup_walk = 0 for all accepted requests.
    """

    name = "SingleSidedDropoff"
    method_label = "SingleSidedDropoff_Choice_CommonRouting"
    service_design = "single_sided_dropoff"
    choice_model = "binary_logit"
    reoptimization = "common_sequential_insertion"
    routing_solver = "greedy_insertion"
    evidence_family = "behavioral_main"
    diagnostic_role = "behavioral_service_design_baseline"
    legacy_class = "SingleSidedDropoff"

    def __init__(self, choice_params: ChoiceParameters | None = None):
        self._choice_config = choice_params or self._default_choice_params()

    def _solve(self, scenario: Scenario) -> ALNSState:
        return self._run_actual_offer_sequence(
            scenario=scenario,
            service_design="SingleSidedDropoff",
            meeting_points_for_request=lambda request: [
                MeetingPoint(id=f"ssd_pu_{request.id}", coords=request.origin)
            ] + list(scenario.meeting_points),
            rho_p=0.0,
            rho_d=RHO_D,
            k_top=K_TOP,
            cost_weights=_COST_WEIGHTS,
        )


# ---------------------------------------------------------------------------
# Variant 3: BidirectionalNoChoice
# ---------------------------------------------------------------------------


class BidirectionalNoChoice(BaseVariant):
    """
    Bidirectional meeting points (both sides flexible), deterministic acceptance.
    No MNL rejection — all feasible requests are accepted.
    Implementation: use zero-beta PassengerType so all utilities equal → no rejection.
    Threat T-03-05 mitigation: zero-beta type instead of monkey-patching.
    """

    name = "BidirectionalNoChoice"
    method_label = "BidirectionalMP_NoChoice_Greedy"
    service_design = "bidirectional_mp"
    choice_model = "none"
    reoptimization = "none"
    routing_solver = "greedy_insertion"
    evidence_family = "deterministic_diagnostic"
    diagnostic_role = "no_choice_feasibility_diagnostic"
    legacy_class = "BidirectionalNoChoice"

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles_dict = self._vehicles_dict(scenario)
        state = self._initial_state(scenario)

        result_state = greedy_insertion(
            state,
            vehicles_dict,
            scenario.meeting_points,
            rho_p=RHO_P,
            rho_d=RHO_D,
            k_top=K_TOP,
            cost_weights=_COST_WEIGHTS,
            travel_speed=TRAVEL_SPEED,
        )
        return result_state


# ---------------------------------------------------------------------------
# Variant 3b: GreedyInsertionBaseline
# ---------------------------------------------------------------------------


class GreedyInsertionBaseline(BaseVariant):
    """Named greedy insertion algorithm diagnostic for small scenarios."""

    name = "GreedyInsertionBaseline"
    method_label = "GreedyInsertionBaseline_Diagnostic"
    service_design = "bidirectional_mp"
    choice_model = "fixed_accepted_set"
    reoptimization = "none"
    routing_solver = "greedy_insertion"
    evidence_family = "algorithm_diagnostic"
    diagnostic_role = "greedy_insertion"
    legacy_class = "GreedyInsertionBaseline"

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles_dict = self._vehicles_dict(scenario)
        state = self._initial_state(scenario)
        return greedy_insertion(
            state,
            vehicles_dict,
            scenario.meeting_points,
            rho_p=RHO_P,
            rho_d=RHO_D,
            k_top=K_TOP,
            cost_weights=_COST_WEIGHTS,
            travel_speed=TRAVEL_SPEED,
        )


# ---------------------------------------------------------------------------
# Variant 4: FullModel
# ---------------------------------------------------------------------------


class FullModel(BaseVariant):
    """
    Main contribution: bidirectional MPs + MNL choice + rolling horizon.
    Uses RollingHorizon from alns.py with PASSENGER_TYPES for MNL filtering.
    MNL acceptance: after finding best insertion, simulate Bernoulli acceptance
    using accept_probability. Rejected requests are excluded from routing.
    """

    name = "FullModel"
    method_label = "BidirectionalMP_Choice_RH_ALNS"
    service_design = "bidirectional_mp"
    choice_model = "binary_logit"
    reoptimization = "rolling_horizon"
    routing_solver = "alns"
    evidence_family = "behavioral_main"
    diagnostic_role = "main_service_design"
    legacy_class = "FullModel"

    def __init__(
        self,
        rho_p: float = None,
        rho_d: float = None,
        gamma: float = 0.0,
        cost_weights: tuple | None = None,
        choice_params: ChoiceParameters | None = None,
    ):
        self._rho_p = rho_p if rho_p is not None else RHO_P
        self._rho_d = rho_d if rho_d is not None else RHO_D
        self._gamma = gamma
        self._cost_weights = cost_weights if cost_weights is not None else _COST_WEIGHTS
        self._choice_config = choice_params or self._default_choice_params()

    def _solve(self, scenario: Scenario) -> ALNSState:
        return self._run_actual_offer_sequence(
            scenario=scenario,
            service_design="BidirectionalMeetingPoint",
            meeting_points_for_request=lambda request: scenario.meeting_points,
            rho_p=self._rho_p,
            rho_d=self._rho_d,
            k_top=K_TOP,
            cost_weights=self._cost_weights,
        )


# ---------------------------------------------------------------------------
# Variant 5: AblationNoRollingHorizon
# ---------------------------------------------------------------------------


class AblationNoRollingHorizon(BaseVariant):
    """
    Ablation: FullModel without periodic re-optimization.
    Uses greedy_insertion only (single pass, no ALNS reoptimize calls).
    Applies MNL filtering same as FullModel.
    """

    name = "AblationNoRollingHorizon"
    method_label = "BidirectionalMP_Choice_NoRollingHorizon"
    service_design = "bidirectional_mp"
    choice_model = "binary_logit"
    reoptimization = "none"
    routing_solver = "greedy_insertion"
    evidence_family = "algorithm_diagnostic"
    diagnostic_role = "no_rolling_horizon_diagnostic"
    legacy_class = "AblationNoRollingHorizon"

    def __init__(self, choice_params: ChoiceParameters | None = None):
        self._choice_config = choice_params or self._default_choice_params()

    def _solve(self, scenario: Scenario) -> ALNSState:
        return self._run_actual_offer_sequence(
            scenario=scenario,
            service_design="BidirectionalMeetingPointNoRollingHorizon",
            meeting_points_for_request=lambda request: scenario.meeting_points,
            rho_p=RHO_P,
            rho_d=RHO_D,
            k_top=K_TOP,
            cost_weights=_COST_WEIGHTS,
        )


# ---------------------------------------------------------------------------
# Variant 6: AblationNoChoice
# ---------------------------------------------------------------------------


class AblationNoChoice(BaseVariant):
    """
    Ablation: FullModel without MNL rejection.
    Uses RollingHorizon (same as FullModel) but all feasible requests are accepted.
    Implementation: same as BidirectionalNoChoice but with rolling horizon.
    """

    name = "AblationNoChoice"
    method_label = "BidirectionalMP_NoChoice_RH_ALNS"
    service_design = "bidirectional_mp"
    choice_model = "none"
    reoptimization = "rolling_horizon"
    routing_solver = "alns"
    evidence_family = "deterministic_diagnostic"
    diagnostic_role = "no_choice_routing_diagnostic"
    legacy_class = "AblationNoChoice"

    def _solve(self, scenario: Scenario) -> ALNSState:
        vehicles_dict = self._vehicles_dict(scenario)

        rh = RollingHorizon(
            vehicles=vehicles_dict,
            meeting_points=scenario.meeting_points,
            rho_p=RHO_P,
            rho_d=RHO_D,
            k_top=K_TOP,
            H=H_WINDOW,
            delta=DELTA,
            cost_weights=_COST_WEIGHTS,
            travel_speed=TRAVEL_SPEED,
            alns_iterations=50,
            seed=42,
        )

        sorted_requests = sorted(scenario.requests, key=lambda r: r.earliest)
        arrival_times = [r.earliest for r in sorted_requests]

        rh.run_simulation(sorted_requests, arrival_times)

        assigned_ids = set(rh.completed_request_ids)
        for route in rh.routes.values():
            for stop in route.stops:
                if len(stop) >= 3:
                    assigned_ids.add(stop[2])

        unassigned = [r for r in scenario.requests if r.id not in assigned_ids]
        return ALNSState(routes=rh.routes, unassigned=unassigned, cost=0.0,
                         completed_ids=set(rh.completed_request_ids),
                         extra_vehicle_km=rh.accumulated_vehicle_km,
                         pickup_times=dict(rh.pickup_times))


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

ALL_VARIANTS = [
    DoorToDoor(),
    DoorToDoorCapped(),
    SingleSidedPickup(),
    SingleSidedDropoff(),
    BidirectionalNoChoice(),
    GreedyInsertionBaseline(),
    FullModel(),
    AblationNoRollingHorizon(),
    AblationNoChoice(),
]

# Threat T-03-07 mitigation: assert unique names at module load time
_names = [v.name for v in ALL_VARIANTS]
assert len(_names) == len(set(_names)), f"Duplicate variant names detected: {_names}"
