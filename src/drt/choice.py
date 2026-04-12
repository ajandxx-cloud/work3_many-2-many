"""
choice.py — MNL utility and binary logit acceptance probability.

Implements the binary logit passenger acceptance model for the single-offer
mechanism (Layer 1), where exactly one bundle b* is presented to the passenger:

  U_rb^k = β1^k · Walk_rb + β2^k · Wait_rb + β3^k · IVT_rb + β4^k · p_r

  P_accept(b*) = exp(U_{b*}) / (exp(U_0) + exp(U_{b*}))

Outside option utility U_0 = 0.0 (normalized baseline).
"""

from __future__ import annotations

import math

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
