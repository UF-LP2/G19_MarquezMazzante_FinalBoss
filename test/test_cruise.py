import pytest
from src.cCruise import cCruise

def test_Cruise1():
    Cruise1 = cCruise(2500, 3000, 1200)
    with pytest.raises(ValueError):
        Cruise1.is_worth_it()

def test_Cruise2():
    Cruise2= cCruise(29,2823,51)
    assert Cruise2.is_worth_it()== 2681.25
