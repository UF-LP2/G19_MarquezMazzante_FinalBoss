import unittest
import pytest
from src.cShip import cShip
from src.cCargo import cCargo
from src.cCruise import cCruise
class Test1 (unittest.TestCase):
    def test_Pruebo(self):
        Ship = cShip(2000, 300)
        assert Ship.is_worth_it() == 1550
class Test2 (unittest.TestCase):
    def test_pruebodos(self):
        Cargo = cCargo(2000, 0.5, 1200, 300)
        assert Cargo.is_worth_it() == ##en otro momento hago la cuenta

class Test3 (unittest.TestCase):
    def test_pruebatres(self):
        Cruise= cCruise(2500, 3000, 1200)
        assert Cruise.is_worth_it() == ##en otro momento


if __name__ == '__main__':
    unittest.main()

