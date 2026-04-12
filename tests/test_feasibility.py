"""
tests/test_feasibility.py — pytest suite for HEUR-03 feasibility checker.

Covers all 6 constraint classes from constraints.tex:
  con:capacity, con:tw-early, con:tw-late, con:ridetime,
  con:precedence-pos, con:route-duration
"""
import pytest
from drt.types import MeetingPoint, Request, Route, Vehicle
from drt.feasibility import check_feasibility


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def mp(id_, x, y):
    return MeetingPoint(id=id_, coords=(x, y))


def make_vehicle(capacity=4, max_route_duration=120.0,
                 pos=(0.0, 0.0), current_time=0.0):
    return Vehicle(
        id="v1",
        capacity=capacity,
        max_route_duration=max_route_duration,
        current_position=pos,
        current_time=current_time,
    )


def make_request(earliest=0.0, latest=60.0, max_ride_time=30.0):
    return Request(
        id="r1",
        origin=(0.0, 0.0),
        destination=(10.0, 0.0),
        earliest=earliest,
        latest=latest,
        max_ride_time=max_ride_time,
    )


# ---------------------------------------------------------------------------
# Test 1: Valid insertion
# ---------------------------------------------------------------------------

def test_valid_insertion():
    """A feasible insertion returns (True, '')."""
    vehicle = make_vehicle(capacity=4, max_route_duration=120.0,
                           pos=(0.0, 0.0), current_time=0.0)
    request = make_request(earliest=0.0, latest=60.0, max_ride_time=30.0)
    route = Route(vehicle_id="v1", stops=[])

    pickup  = mp("P", 2.0, 0.0)   # 2 units from vehicle, travel time = 2
    dropoff = mp("D", 5.0, 0.0)   # 3 units further, travel time = 3

    ok, reason = check_feasibility(
        route, request, pickup, dropoff,
        pos_p=0, pos_d=1, vehicle=vehicle, travel_speed=1.0,
    )
    assert ok is True
    assert reason == ""


# ---------------------------------------------------------------------------
# Test 2: Capacity violation
# ---------------------------------------------------------------------------

def test_capacity_violation():
    """Inserting into a full vehicle returns (False, 'capacity')."""
    vehicle = make_vehicle(capacity=1, max_route_duration=120.0,
                           pos=(0.0, 0.0), current_time=0.0)
    request = make_request(earliest=0.0, latest=60.0, max_ride_time=30.0)

    # Existing route: one pickup already on board (occupancy = 1 = capacity)
    existing_pickup = mp("EP", 1.0, 0.0)
    route = Route(vehicle_id="v1", stops=[(existing_pickup, 1.0)])

    pickup  = mp("P", 2.0, 0.0)
    dropoff = mp("D", 5.0, 0.0)

    # Insert new pickup at pos 0 (before existing stop) → occupancy hits 2 > 1
    ok, reason = check_feasibility(
        route, request, pickup, dropoff,
        pos_p=0, pos_d=2, vehicle=vehicle, travel_speed=1.0,
    )
    assert ok is False
    assert reason == "capacity"


# ---------------------------------------------------------------------------
# Test 3: Time window (late) violation
# ---------------------------------------------------------------------------

def test_tw_late_violation():
    """Pickup scheduled after request.latest returns (False, 'tw_late')."""
    # Vehicle starts at (0,0) at t=0; pickup is at (100, 0) → arrives at t=100
    vehicle = make_vehicle(capacity=4, max_route_duration=300.0,
                           pos=(0.0, 0.0), current_time=0.0)
    request = make_request(earliest=0.0, latest=50.0, max_ride_time=60.0)
    route = Route(vehicle_id="v1", stops=[])

    pickup  = mp("P", 100.0, 0.0)   # travel time = 100 > latest=50
    dropoff = mp("D", 110.0, 0.0)

    ok, reason = check_feasibility(
        route, request, pickup, dropoff,
        pos_p=0, pos_d=1, vehicle=vehicle, travel_speed=1.0,
    )
    assert ok is False
    assert reason == "tw_late"


# ---------------------------------------------------------------------------
# Test 4: Ride time violation
# ---------------------------------------------------------------------------

def test_ride_time_violation():
    """Ride time exceeding max_ride_time returns (False, 'ride_time')."""
    vehicle = make_vehicle(capacity=4, max_route_duration=300.0,
                           pos=(0.0, 0.0), current_time=0.0)
    # max_ride_time = 5; pickup at t=2, dropoff at t=52 → ride = 50 > 5
    request = make_request(earliest=0.0, latest=60.0, max_ride_time=5.0)
    route = Route(vehicle_id="v1", stops=[])

    pickup  = mp("P", 2.0, 0.0)    # arrives at t=2
    dropoff = mp("D", 52.0, 0.0)   # arrives at t=52; ride = 50

    ok, reason = check_feasibility(
        route, request, pickup, dropoff,
        pos_p=0, pos_d=1, vehicle=vehicle, travel_speed=1.0,
    )
    assert ok is False
    assert reason == "ride_time"


# ---------------------------------------------------------------------------
# Test 5: Precedence violation
# ---------------------------------------------------------------------------

def test_precedence_violation():
    """pos_d <= pos_p returns (False, 'precedence')."""
    vehicle = make_vehicle()
    request = make_request()
    route = Route(vehicle_id="v1", stops=[])

    pickup  = mp("P", 2.0, 0.0)
    dropoff = mp("D", 5.0, 0.0)

    # pos_d == pos_p → violation
    ok, reason = check_feasibility(
        route, request, pickup, dropoff,
        pos_p=1, pos_d=1, vehicle=vehicle, travel_speed=1.0,
    )
    assert ok is False
    assert reason == "precedence"

    # pos_d < pos_p → violation
    ok2, reason2 = check_feasibility(
        route, request, pickup, dropoff,
        pos_p=2, pos_d=1, vehicle=vehicle, travel_speed=1.0,
    )
    assert ok2 is False
    assert reason2 == "precedence"


# ---------------------------------------------------------------------------
# Test 6: Route duration violation
# ---------------------------------------------------------------------------

def test_route_duration_violation():
    """Total route time exceeding max_route_duration returns (False, 'route_duration')."""
    # max_route_duration = 10; dropoff is 100 units away → route time = 100 > 10
    vehicle = make_vehicle(capacity=4, max_route_duration=10.0,
                           pos=(0.0, 0.0), current_time=0.0)
    request = make_request(earliest=0.0, latest=200.0, max_ride_time=200.0)
    route = Route(vehicle_id="v1", stops=[])

    pickup  = mp("P", 50.0, 0.0)
    dropoff = mp("D", 100.0, 0.0)

    ok, reason = check_feasibility(
        route, request, pickup, dropoff,
        pos_p=0, pos_d=1, vehicle=vehicle, travel_speed=1.0,
    )
    assert ok is False
    assert reason == "route_duration"


# ---------------------------------------------------------------------------
# Test 7: Time window early violation
# ---------------------------------------------------------------------------

def test_tw_early_violation():
    """Pickup scheduled before request.earliest returns (False, 'tw_early')."""
    # Vehicle is already at pickup location at t=0; earliest=10
    vehicle = make_vehicle(capacity=4, max_route_duration=120.0,
                           pos=(2.0, 0.0), current_time=0.0)
    request = make_request(earliest=10.0, latest=60.0, max_ride_time=30.0)
    route = Route(vehicle_id="v1", stops=[])

    # pickup at (2,0) — vehicle is already there, arrives at t=0 < earliest=10
    pickup  = mp("P", 2.0, 0.0)
    dropoff = mp("D", 5.0, 0.0)

    ok, reason = check_feasibility(
        route, request, pickup, dropoff,
        pos_p=0, pos_d=1, vehicle=vehicle, travel_speed=1.0,
    )
    assert ok is False
    assert reason == "tw_early"
