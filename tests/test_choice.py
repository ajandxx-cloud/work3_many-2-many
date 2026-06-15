"""Tests for Phase 3 passenger choice primitives."""

from __future__ import annotations

import math

import pytest

from drt import accept_probability
from drt.choice import (
    assign_passenger_type,
    evaluate_offer_utility,
    evaluate_single_offer,
    feasibility_rejected_evaluation,
)
from drt.types import (
    Bundle,
    ChoiceParameters,
    MeetingPoint,
    OfferAttributes,
    PassengerType,
    PRICE_SENSITIVE,
    TIME_SENSITIVE,
    WALK_SENSITIVE,
    Request,
)


def make_offer(**overrides) -> OfferAttributes:
    values = {
        "request_id": "req_1",
        "service_design": "BidirectionalMeetingPoint",
        "pickup_walk": 0.2,
        "dropoff_walk": 0.1,
        "wait_time": 5.0,
        "ivt": 12.0,
        "fare": 0.0,
        "pickup_mp_id": "mp_pu",
        "dropoff_mp_id": "mp_do",
        "vehicle_id": "veh_1",
        "scheduled_pickup": 15.0,
        "scheduled_dropoff": 27.0,
    }
    values.update(overrides)
    return OfferAttributes(**values)


def make_ptype() -> PassengerType:
    return PassengerType(
        name="test_type",
        beta_walk=-1.0,
        beta_wait=-0.1,
        beta_ivt=-0.05,
        beta_price=-0.2,
    )


def test_existing_accept_probability_import_still_works():
    request = Request(
        id="req_1",
        origin=(0.0, 0.0),
        destination=(10.0, 0.0),
        earliest=0.0,
        latest=100.0,
        max_ride_time=100.0,
    )
    pickup = MeetingPoint(id="p", coords=(0.0, 0.0))
    dropoff = MeetingPoint(id="d", coords=(10.0, 0.0))
    bundle = Bundle(request_id=request.id, pickup_mp=pickup, dropoff_mp=dropoff, departure_time=0.0, price=0.0)

    probability = accept_probability(bundle, request, make_ptype(), current_time=0.0)

    assert 0.0 < probability < 1.0


def test_service_asc_increases_acceptance_probability():
    offer = make_offer()
    ptype = make_ptype()
    low = evaluate_single_offer(
        offer,
        ptype,
        ChoiceParameters(service_asc=-1.0, outside_option_constant=0.0),
        random_draw=0.5,
    )
    high = evaluate_single_offer(
        offer,
        ptype,
        ChoiceParameters(service_asc=1.0, outside_option_constant=0.0),
        random_draw=0.5,
    )

    assert high.acceptance_probability > low.acceptance_probability


def test_outside_option_constant_lowers_acceptance_probability():
    offer = make_offer()
    ptype = make_ptype()
    weak_outside = evaluate_single_offer(
        offer,
        ptype,
        ChoiceParameters(service_asc=0.0, outside_option_constant=-1.0),
        random_draw=0.5,
    )
    strong_outside = evaluate_single_offer(
        offer,
        ptype,
        ChoiceParameters(service_asc=0.0, outside_option_constant=1.0),
        random_draw=0.5,
    )

    assert strong_outside.acceptance_probability < weak_outside.acceptance_probability


def test_worse_offer_attributes_lower_utility():
    ptype = make_ptype()
    good = evaluate_offer_utility(make_offer(pickup_walk=0.1, wait_time=2.0, ivt=8.0, fare=0.0), ptype)
    bad = evaluate_offer_utility(make_offer(pickup_walk=1.0, wait_time=20.0, ivt=30.0, fare=5.0), ptype)

    assert bad.total_utility < good.total_utility


def test_extreme_utility_does_not_overflow():
    ptype = PassengerType(
        name="extreme",
        beta_walk=-1000.0,
        beta_wait=-1000.0,
        beta_ivt=-1000.0,
        beta_price=-1000.0,
    )
    result = evaluate_single_offer(
        make_offer(pickup_walk=1000.0, dropoff_walk=1000.0, wait_time=1000.0, ivt=1000.0, fare=1000.0),
        ptype,
        ChoiceParameters(service_asc=-1000.0, outside_option_constant=1000.0),
        random_draw=0.5,
    )

    assert math.isfinite(result.acceptance_probability)
    assert 0.0 <= result.acceptance_probability <= 1.0


def test_utility_component_log_row_contains_required_fields():
    result = evaluate_single_offer(make_offer(), make_ptype(), random_draw=0.5)
    row = result.as_log_row()
    required = {
        "status",
        "detailed_reason",
        "passenger_type",
        "pickup_walk",
        "dropoff_walk",
        "wait_time",
        "ivt",
        "fare",
        "service_design",
        "pickup_mp_id",
        "dropoff_mp_id",
        "vehicle_id",
        "scheduled_pickup",
        "scheduled_dropoff",
        "walk_utility",
        "wait_utility",
        "ivt_utility",
        "fare_utility",
        "service_asc",
        "outside_option_constant",
        "total_utility",
        "outside_utility",
        "acceptance_probability",
        "random_draw",
    }

    assert required.issubset(row.keys())


def test_same_seed_and_request_return_same_passenger_type():
    types = [PRICE_SENSITIVE, TIME_SENSITIVE, WALK_SENSITIVE]
    shares = {"price_sensitive": 0.34, "time_sensitive": 0.33, "walk_sensitive": 0.33}

    first = assign_passenger_type("req_42", types, shares, seed=99)
    second = assign_passenger_type("req_42", types, shares, seed=99)

    assert first == second


def test_service_design_does_not_affect_passenger_type_assignment():
    types = [PRICE_SENSITIVE, TIME_SENSITIVE, WALK_SENSITIVE]
    shares = {"price_sensitive": 0.34, "time_sensitive": 0.33, "walk_sensitive": 0.33}

    # The helper intentionally has no service_design argument, so paired methods share type assignment.
    door_to_door_type = assign_passenger_type("req_42", types, shares, seed=99)
    bidirectional_type = assign_passenger_type("req_42", types, shares, seed=99)

    assert door_to_door_type == bidirectional_type


def test_invalid_type_shares_raise_clear_error():
    types = [PRICE_SENSITIVE, TIME_SENSITIVE, WALK_SENSITIVE]

    with pytest.raises(ValueError, match="non-negative"):
        assign_passenger_type("req_1", types, {"price_sensitive": -1.0}, seed=42)

    with pytest.raises(ValueError, match="positive"):
        assign_passenger_type("req_1", types, {}, seed=42)


def test_non_uniform_type_shares_are_respected():
    types = [PRICE_SENSITIVE, TIME_SENSITIVE, WALK_SENSITIVE]
    selected = {
        assign_passenger_type(
            f"req_{idx}",
            types,
            {"price_sensitive": 1.0, "time_sensitive": 0.0, "walk_sensitive": 0.0},
            seed=42,
        ).name
        for idx in range(10)
    }

    assert selected == {"price_sensitive"}


def test_feasibility_rejected_row_has_no_proxy_utility():
    result = feasibility_rejected_evaluation(
        request_id="req_no_offer",
        detailed_reason="no_feasible_route",
        passenger_type="walk_sensitive",
    )
    row = result.as_log_row()

    assert result.status == "feasibility_rejected"
    assert result.offer is None
    assert result.components is None
    assert row["acceptance_probability"] is None
    assert "total_utility" not in row
    assert "pickup_walk" not in row
