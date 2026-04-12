"""
drt — Many-to-many DRT co-optimization package.

Public API re-exported from sub-modules so callers can do:
    from drt import Request, choice_probability
"""

from .types import Request, Vehicle, Route, MeetingPoint, Bundle, PassengerType
from .choice import mnl_utility, choice_probability

__all__ = [
    "Request",
    "Vehicle",
    "Route",
    "MeetingPoint",
    "Bundle",
    "PassengerType",
    "mnl_utility",
    "choice_probability",
]
