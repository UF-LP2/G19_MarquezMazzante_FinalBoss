import pytest
from src.cShip import cShip
from src.cCargo import cCargo
from src.cCruise import cCruise


def test_Ship():
    Ship = cShip(2000, 300)
    assert Ship.is_worth_it() == 1550


def test_Cargo():
    Cargo = cCargo(2000, 0.5, 1200, 300)
    with pytest.raises(Exception):
        Cargo.is_worth_it()


def test_Cruise():
    Cruise = cCruise(2500, 3000, 1200)
    with pytest.raises(Exception):
        Cruise.is_worth_it()
