"""
drt — Many-to-many DRT co-optimization package.

Public API re-exported from sub-modules so callers can do:
    from drt import Request, accept_probability
"""

from .types import (
    Bundle,
    ChoiceEvaluation,
    ChoiceParameters,
    MeetingPoint,
    OfferAttributes,
    PassengerType,
    Request,
    Route,
    UtilityComponents,
    Vehicle,
)
from .choice import (
    accept_probability,
    assign_passenger_type,
    evaluate_offer_utility,
    evaluate_single_offer,
    feasibility_rejected_evaluation,
    mnl_utility,
)

__all__ = [
    "Request",
    "Vehicle",
    "Route",
    "MeetingPoint",
    "Bundle",
    "OfferAttributes",
    "ChoiceParameters",
    "UtilityComponents",
    "ChoiceEvaluation",
    "PassengerType",
    "mnl_utility",
    "accept_probability",
    "evaluate_offer_utility",
    "evaluate_single_offer",
    "feasibility_rejected_evaluation",
    "assign_passenger_type",
]
