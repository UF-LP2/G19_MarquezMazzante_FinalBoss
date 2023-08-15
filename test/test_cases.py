import pytest
from src.cShip import cShip
from src.cCargo import cCargo
from src.cCruise import cCruise


def test_Ship1():
    Ship1 = cShip(2000, 300)
    assert Ship1.is_worth_it() == 1550
def test_Ship2():
    Ship2 = cShip(-1000, 202)
    with pytest.raises(Exception):
        Ship2.is_worth_it()
def test_Ship3():
    with pytest.raises(ValueError):
        Ship3 = cShip("hola", 123)
        Ship3.is_worth_it()
def test_Ship4():
    Ship4 = cShip(0,0)
    with pytest.raises(Exception):
        Ship4.is_worth_it()


def test_Cargo1():
    Cargo1 = cCargo(2000, 0.5, 1200, 300)
    with pytest.raises(Exception):
        Cargo1.is_worth_it()
def test_Cargo2():
    Cargo2=cCargo(51, 0.25, 2827, 117)
    assert Cargo2.is_worth_it()== 2626
def test_Cargo3():
    Cargo3=cCargo(34, 0.5, 4231, 1290)
    assert Cargo3.is_worth_it()== 2228

def test_Cargo4():
    with pytest.raises(ValueError):
        Cargo4 = cCargo("jaimito", "*93", 000, 0000)
        Cargo4.is_worth_it()

def test_Cruise1():
    Cruise1 = cCruise(2500, 3000, 1200)
    with pytest.raises(Exception):
        Cruise1.is_worth_it()

def test_Cruise2():
    Cruise2= cCruise(29,2823,51)
    assert Cruise2.is_worth_it()== 2681.25
