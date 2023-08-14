import pytest
from src.cShip import cShip
from src.cCargo import cCargo
from src.cCruise import cCruise


def test_Pruebo():
    Ship = cShip(2000, 300)
    assert Ship.is_worth_it() == 1550


def test_pruebodos():
    Cargo = cCargo(2000, 0.5, 1200, 300)
    assert Cargo.is_worth_it() == -2800


def test_pruebatres():
    Cruise = cCruise(2500, 3000, 1200)
    assert Cruise.is_worth_it() == -4425
