"""
types.py — Core dataclasses for the many-to-many DRT model.

Notation mapping (Python field → math symbol from Phase 1):
  Request.id                → r
  Request.origin            → o_r  (x, y)
  Request.destination       → d_r  (x, y)
  Request.earliest          → e_r  (earliest acceptable pickup time)
  Request.latest            → l_r  (latest acceptable pickup time)
  Request.max_ride_time     → T_r^ride (maximum in-vehicle time)

  Vehicle.id                → v
  Vehicle.capacity          → Q_v
  Vehicle.max_route_duration→ T_v^max
  Vehicle.current_position  → pos_v  (x, y)
  Vehicle.current_time      → t_v^now

  MeetingPoint.id           → m
  MeetingPoint.coords       → (x_m, y_m)

  Bundle.request_id         → r  (links bundle to request)
  Bundle.pickup_mp          → m_r^pu  (pickup meeting point)
  Bundle.dropoff_mp         → m_r^do  (dropoff meeting point)
  Bundle.departure_time     → τ_r  (scheduled pickup time)
  Bundle.price              → p_r  (fare offered to passenger)

  Route.vehicle_id          → v
  Route.stops               → sequence of (m, t) pairs

  PassengerType.name        → k  (passenger type label)
  PassengerType.beta_walk   → β1^k
  PassengerType.beta_wait   → β2^k
  PassengerType.beta_ivt    → β3^k
  PassengerType.beta_price  → β4^k
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Request:
    """A passenger trip request r."""

    id: str
    origin: tuple[float, float]          # o_r
    destination: tuple[float, float]     # d_r
    earliest: float                      # e_r — earliest acceptable pickup time
    latest: float                        # l_r — latest acceptable pickup time
    max_ride_time: float                 # T_r^ride — max in-vehicle time


@dataclass
class Vehicle:
    """A DRT vehicle v."""

    id: str
    capacity: int                        # Q_v
    max_route_duration: float            # T_v^max
    current_position: tuple[float, float]
    current_time: float                  # t_v^now


@dataclass(frozen=True)
class MeetingPoint:
    """A candidate meeting point m (pickup or dropoff).

    frozen=True makes MeetingPoint hashable, required because Bundle
    (also frozen) contains MeetingPoint fields.
    """

    id: str
    coords: tuple[float, float]          # (x_m, y_m)


@dataclass(frozen=True)
class Bundle:
    """
    A service bundle b offered to request r.

    Combines a pickup meeting point, a dropoff meeting point,
    a scheduled departure time, and a fare.

    frozen=True makes Bundle hashable so it can be used as a dict key
    in accept_probability call sites.
    """

    request_id: str                      # r
    pickup_mp: MeetingPoint              # m_r^pu
    dropoff_mp: MeetingPoint             # m_r^do
    departure_time: float                # τ_r
    price: float                         # p_r


@dataclass(frozen=True)
class OfferAttributes:
    """Actual feasible single-offer attributes used by the Phase 3 choice model."""

    request_id: str
    service_design: str
    pickup_walk: float
    dropoff_walk: float
    wait_time: float
    ivt: float
    fare: float
    pickup_mp_id: str | None
    dropoff_mp_id: str | None
    vehicle_id: str | None
    scheduled_pickup: float | None
    scheduled_dropoff: float | None


@dataclass(frozen=True)
class ChoiceParameters:
    """Choice-model parameters shared across behavioral service designs."""

    service_asc: float = 0.0
    outside_option_constant: float = 0.0
    choice_seed: int = 42
    type_shares: dict[str, float] = field(
        default_factory=lambda: {
            "price_sensitive": 0.34,
            "time_sensitive": 0.33,
            "walk_sensitive": 0.33,
        }
    )


@dataclass(frozen=True)
class UtilityComponents:
    """Utility decomposition for one actual offered bundle."""

    walk_utility: float
    wait_utility: float
    ivt_utility: float
    fare_utility: float
    service_asc: float
    outside_option_constant: float
    total_utility: float
    outside_utility: float


@dataclass(frozen=True)
class ChoiceEvaluation:
    """Logged result of evaluating one request under the single-offer model."""

    request_id: str
    status: str
    detailed_reason: str
    passenger_type: str
    offer: OfferAttributes | None
    components: UtilityComponents | None
    acceptance_probability: float | None
    random_draw: float | None
    accepted: bool

    def as_log_row(self) -> dict[str, object]:
        """Flatten the evaluation for utility-component CSV/JSONL outputs."""
        row: dict[str, object] = {
            "request_id": self.request_id,
            "status": self.status,
            "detailed_reason": self.detailed_reason,
            "passenger_type": self.passenger_type,
            "acceptance_probability": self.acceptance_probability,
            "random_draw": self.random_draw,
            "accepted": self.accepted,
        }
        if self.offer is not None:
            row.update(
                {
                    "pickup_walk": self.offer.pickup_walk,
                    "dropoff_walk": self.offer.dropoff_walk,
                    "wait_time": self.offer.wait_time,
                    "ivt": self.offer.ivt,
                    "fare": self.offer.fare,
                    "service_design": self.offer.service_design,
                    "pickup_mp_id": self.offer.pickup_mp_id,
                    "dropoff_mp_id": self.offer.dropoff_mp_id,
                    "vehicle_id": self.offer.vehicle_id,
                    "scheduled_pickup": self.offer.scheduled_pickup,
                    "scheduled_dropoff": self.offer.scheduled_dropoff,
                }
            )
        if self.components is not None:
            row.update(
                {
                    "walk_utility": self.components.walk_utility,
                    "wait_utility": self.components.wait_utility,
                    "ivt_utility": self.components.ivt_utility,
                    "fare_utility": self.components.fare_utility,
                    "service_asc": self.components.service_asc,
                    "outside_option_constant": self.components.outside_option_constant,
                    "total_utility": self.components.total_utility,
                    "outside_utility": self.components.outside_utility,
                }
            )
        return row


@dataclass
class Route:
    """
    A vehicle route: ordered sequence of (meeting_point, scheduled_arrival_time) stops.
    """

    vehicle_id: str
    stops: list = field(default_factory=list)
    # Each element: (MeetingPoint, float) — meeting point and scheduled arrival time


@dataclass
class PassengerType:
    """
    Passenger type k with MNL utility coefficients.

    Pre-defined types (from Phase 1 calibration):
      price_sensitive : β = [-0.005, -0.04, -0.02, -0.15]
      time_sensitive  : β = [-0.005, -0.10, -0.08, -0.03]
      walk_sensitive  : β = [-0.020, -0.04, -0.02, -0.05]

    All β values should be negative (disutility attributes).
    """

    name: str
    beta_walk: float    # β1^k — disutility per unit walk distance
    beta_wait: float    # β2^k — disutility per unit wait time
    beta_ivt: float     # β3^k — disutility per unit in-vehicle time
    beta_price: float   # β4^k — disutility per unit fare


# ---------------------------------------------------------------------------
# Pre-defined passenger types from Phase 1 notation
# ---------------------------------------------------------------------------

PRICE_SENSITIVE = PassengerType(
    name="price_sensitive",
    beta_walk=-0.005,
    beta_wait=-0.04,
    beta_ivt=-0.02,
    beta_price=-0.15,
)

TIME_SENSITIVE = PassengerType(
    name="time_sensitive",
    beta_walk=-0.005,
    beta_wait=-0.10,
    beta_ivt=-0.08,
    beta_price=-0.03,
)

WALK_SENSITIVE = PassengerType(
    name="walk_sensitive",
    beta_walk=-0.020,
    beta_wait=-0.04,
    beta_ivt=-0.02,
    beta_price=-0.05,
)
