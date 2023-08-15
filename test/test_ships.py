import pytest
from src.ships import Ship

def test_Ship1():
    Ship1 = Ship(2000, 300)
    assert (Ship1.is_worth_it()>= 20) == True
def test_Ship2():
    Ship2 = Ship(-1000, 202)
    with pytest.raises(ValueError):
        Ship2.is_worth_it()
def test_Ship3():
    with pytest.raises(ValueError):
        Ship3 = Ship("hola", 123)
        Ship3.is_worth_it()
def test_Ship4():
    with pytest.raises(ValueError):
        Ship4 = Ship(0, -800)
        Ship4.is_worth_it()