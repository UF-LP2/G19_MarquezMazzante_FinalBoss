import pytest
from src.Cargo import Cargo

def test_Cargo1():
    Cargo1 = Cargo(2000, 0.5, 1200, 300)
    with pytest.raises(ValueError):
        Cargo1.is_worth_it()
def test_Cargo2():
    Cargo2=Cargo(51, 0.25, 2827, 117)
    assert (Cargo2.is_worth_it() >= 20)== True
def test_Cargo3():
    Cargo3=Cargo(34, 0.5, 4231, 1290)
    assert (Cargo3.is_worth_it() >= 20)== True

def test_Cargo4():
    with pytest.raises(ValueError):
        Cargo4 = Cargo("jaimito", "*93", 000, 0000)
        Cargo4.is_worth_it()