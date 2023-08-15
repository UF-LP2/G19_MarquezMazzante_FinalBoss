import pytest
from src.ships import Cruise

def test_Cruise1():
    Cruise1 = Cruise(2500, 3000, 1200)
    with pytest.raises(ValueError):
        Cruise1.is_worth_it()

def test_Cruise2():
    Cruise2= Cruise(29,2823,51)
    assert (Cruise2.is_worth_it() >= 20)== True
