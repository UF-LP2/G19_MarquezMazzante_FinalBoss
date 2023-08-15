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

def test_Cuatro():
    Cruise= cCruise(29,2823,51)
    assert Cruise.is_worth_it()== 2681.25

def test_Cinco():
    Cargo=cCargo(51, 0.25, 2827, 117)
    assert Cargo.is_worth_it()== 2626

def test_Seis():
    Cargo=cCargo(34, 0.5, 4231, 1290)
    assert Cargo.is_worth_it()== 2228

def test_siete():
    with pytest.raises(Exception):
     Ship=cShip("holaa", 1200)

