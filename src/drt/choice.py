"""
choice.py — MNL utility and binary logit acceptance probability.

Implements the binary logit passenger acceptance model for the single-offer
mechanism (Layer 1), where exactly one bundle b* is presented to the passenger:

  U_rb^k = β1^k · Walk_rb + β2^k · Wait_rb + β3^k · IVT_rb + β4^k · p_r

  P_accept(b*) = exp(U_{b*}) / (exp(U_0) + exp(U_{b*}))

Outside option utility U_0 = 0.0 (normalized baseline).
"""

from __future__ import annotations

import hashlib
import math
import random

from .types import (
    Bundle,
    ChoiceEvaluation,
    ChoiceParameters,
    MeetingPoint,
    OfferAttributes,
    PassengerType,
    Request,
    UtilityComponents,
)


def euclidean(a: tuple[float, float], b: tuple[float, float]) -> float:
    """Euclidean distance between two (x, y) coordinate tuples."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def mnl_utility(
    bundle: Bundle,
    request: Request,
    ptype: PassengerType,
    current_time: float,
) -> float:
    """
    Compute MNL utility U_rb^k for a passenger of type k evaluating bundle b.

    Parameters
    ----------
    bundle       : service bundle (pickup mp, dropoff mp, departure time, price)
    request      : the passenger's trip request
    ptype        : passenger type with β coefficients
    current_time : clock time at which the request is evaluated (t_r^req)

    Returns
    -------
    float : U_rb^k  (negative — all attributes are disutilities)

    Attribute proxies
    -----------------
    walk_dist = dist(origin → pickup_mp) + dist(dropoff_mp → destination)
    wait_time = departure_time − current_time
    ivt       = dist(pickup_mp → dropoff_mp)  [Euclidean proxy for in-vehicle time]
    """
    walk_dist = (
        euclidean(request.origin, bundle.pickup_mp.coords)
        + euclidean(bundle.dropoff_mp.coords, request.destination)
    )
    wait_time = bundle.departure_time - current_time
    ivt = euclidean(bundle.pickup_mp.coords, bundle.dropoff_mp.coords)

    return (
        ptype.beta_walk * walk_dist
        + ptype.beta_wait * wait_time
        + ptype.beta_ivt * ivt
        + ptype.beta_price * bundle.price
    )


def accept_probability(
    bundle: Bundle,
    request: Request,
    ptype: PassengerType,
    current_time: float,
) -> float:
    """
    Binary logit acceptance probability for a single offered bundle b*.

    The system presents exactly one bundle b* to the passenger (single-offer
    mechanism, Layer 1). The passenger accepts with probability:

        P_accept(b*) = exp(U_{b*}) / (exp(U_0) + exp(U_{b*}))

    where U_0 = 0.0 is the normalized outside-option utility.

    Parameters
    ----------
    bundle       : the single offered service bundle b*
    request      : the passenger's trip request
    ptype        : passenger type with beta coefficients
    current_time : clock time at which the request is evaluated (t_r^req)

    Returns
    -------
    float : acceptance probability in (0, 1)
    """
    u_bundle = mnl_utility(bundle, request, ptype, current_time)
    exp_bundle = math.exp(u_bundle)
    # U_0 = 0.0 (normalized outside option) → exp(U_0) = 1.0
    exp_outside = 1.0
    return exp_bundle / (exp_outside + exp_bundle)


def _binary_logit_probability(offer_utility: float, outside_utility: float) -> float:
    """Stable P(offer) for a binary logit between offer and outside option."""
    delta = outside_utility - offer_utility
    if delta >= 0:
        exp_neg_delta = math.exp(-delta) if delta < 745 else 0.0
        return exp_neg_delta / (1.0 + exp_neg_delta)
    exp_delta = math.exp(delta) if delta > -745 else 0.0
    return 1.0 / (1.0 + exp_delta)


def evaluate_offer_utility(
    offer: OfferAttributes,
    ptype: PassengerType,
    params: ChoiceParameters | None = None,
) -> UtilityComponents:
    """Compute the utility decomposition for one actual feasible offer."""
    params = params or ChoiceParameters()
    total_walk = offer.pickup_walk + offer.dropoff_walk
    walk_utility = ptype.beta_walk * total_walk
    wait_utility = ptype.beta_wait * offer.wait_time
    ivt_utility = ptype.beta_ivt * offer.ivt
    fare_utility = ptype.beta_price * offer.fare
    total_utility = (
        params.service_asc
        + walk_utility
        + wait_utility
        + ivt_utility
        + fare_utility
    )
    outside_utility = params.outside_option_constant
    return UtilityComponents(
        walk_utility=walk_utility,
        wait_utility=wait_utility,
        ivt_utility=ivt_utility,
        fare_utility=fare_utility,
        service_asc=params.service_asc,
        outside_option_constant=params.outside_option_constant,
        total_utility=total_utility,
        outside_utility=outside_utility,
    )


def evaluate_single_offer(
    offer: OfferAttributes,
    ptype: PassengerType,
    params: ChoiceParameters | None = None,
    random_draw: float | None = None,
) -> ChoiceEvaluation:
    """Evaluate a Phase 3 single-offer acceptance decision."""
    params = params or ChoiceParameters()
    components = evaluate_offer_utility(offer, ptype, params)
    probability = _binary_logit_probability(
        components.total_utility,
        components.outside_utility,
    )
    draw = random_draw
    if draw is None:
        rng = random.Random(_stable_int(f"{params.choice_seed}:{offer.request_id}:draw"))
        draw = rng.random()
    accepted = draw <= probability
    return ChoiceEvaluation(
        request_id=offer.request_id,
        status="served" if accepted else "choice_rejected",
        detailed_reason="accepted" if accepted else "passenger_declined",
        passenger_type=ptype.name,
        offer=offer,
        components=components,
        acceptance_probability=probability,
        random_draw=draw,
        accepted=accepted,
    )


def feasibility_rejected_evaluation(
    request_id: str,
    detailed_reason: str,
    passenger_type: str = "",
) -> ChoiceEvaluation:
    """Build a no-offer rejection row without fabricating proxy utility."""
    return ChoiceEvaluation(
        request_id=request_id,
        status="feasibility_rejected",
        detailed_reason=detailed_reason,
        passenger_type=passenger_type,
        offer=None,
        components=None,
        acceptance_probability=None,
        random_draw=None,
        accepted=False,
    )


def assign_passenger_type(
    request_id: str,
    passenger_types: list[PassengerType],
    type_shares: dict[str, float],
    seed: int = 42,
) -> PassengerType:
    """Assign a passenger type deterministically from seed and request id."""
    if not passenger_types:
        raise ValueError("passenger_types must not be empty")
    total_share = 0.0
    for ptype in passenger_types:
        share = type_shares.get(ptype.name, 0.0)
        if share < 0.0:
            raise ValueError("type shares must be non-negative")
        total_share += share
    if total_share <= 0.0:
        raise ValueError("type shares must sum to a positive value")

    rng = random.Random(_stable_int(f"{seed}:{request_id}:ptype"))
    draw = rng.random() * total_share
    cumulative = 0.0
    for ptype in passenger_types:
        cumulative += type_shares.get(ptype.name, 0.0)
        if draw <= cumulative:
            return ptype
    return passenger_types[-1]


def _stable_int(text: str) -> int:
    return int.from_bytes(hashlib.sha256(text.encode("utf-8")).digest()[:8], "big")
