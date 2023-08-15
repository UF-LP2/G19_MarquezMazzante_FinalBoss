import pytest
from src.cShip import cShip

def test_Ship1():
    Ship1 = cShip(2000, 300)
    assert Ship1.is_worth_it() == 1550
def test_Ship2():
    Ship2 = cShip(-1000, 202)
    with pytest.raises(ValueError):
        Ship2.is_worth_it()
def test_Ship3():
    with pytest.raises(ValueError):
        Ship3 = cShip("hola", 123)
        Ship3.is_worth_it()
def test_Ship4():
    Ship4 = cShip(0,-800)
    with pytest.raises(ValueError):
        Ship4.is_worth_it()