"""
choice.py — MNL utility and choice probability functions.

Implements the Multinomial Logit (MNL) passenger choice model from Phase 1:

  U_rb^k = β1^k · Walk_rb + β2^k · Wait_rb + β3^k · IVT_rb + β4^k · p_r

  P_rb^k = exp(U_rb^k) / (exp(U_r0^k) + Σ_{b'} exp(U_rb'^k))

Outside option utility U_r0 = 0.0 (normalized baseline).
"""

from __future__ import annotations

import math
from typing import Optional

from .types import Bundle, MeetingPoint, PassengerType, Request


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


def choice_probability(
    bundles: list[Bundle],
    request: Request,
    ptype: PassengerType,
    current_time: float,
) -> dict[Optional[Bundle], float]:
    """
    Compute MNL choice probabilities for all bundles plus the outside option.

    Parameters
    ----------
    bundles      : list of service bundles offered to the request
    request      : the passenger's trip request
    ptype        : passenger type with β coefficients
    current_time : clock time at which the request is evaluated

    Returns
    -------
    dict mapping Bundle → probability, with None → outside-option probability.
    All values are in [0, 1] and sum to 1.0 (within floating-point precision).

    Outside option
    --------------
    U_r0 = 0.0 (normalized baseline; represents not taking the DRT service).
    """
    # Outside option: U_r0 = 0.0 → exp(0) = 1.0
    exp_outside = 1.0

    # Compute exp(U_rb) for each bundle
    exp_utilities: list[tuple[Bundle, float]] = []
    for b in bundles:
        u = mnl_utility(b, request, ptype, current_time)
        exp_utilities.append((b, math.exp(u)))

    exp_sum = exp_outside + sum(e for _, e in exp_utilities)

    probs: dict[Optional[Bundle], float] = {}
    for b, exp_u in exp_utilities:
        probs[b] = exp_u / exp_sum
    probs[None] = exp_outside / exp_sum  # outside option

    return probs
