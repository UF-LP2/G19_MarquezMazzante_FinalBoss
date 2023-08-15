import pytest
from src.Cargo import cCargo

def test_Cargo1():
    Cargo1 = cCargo(2000, 0.5, 1200, 300)
    with pytest.raises(ValueError):
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