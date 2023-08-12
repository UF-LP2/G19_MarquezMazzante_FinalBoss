from src.cShip import Ship
class Cruise(Ship):
    def __init__(self, passengers, draft, crew):
        self.passengers = passengers
        Ship.__init__(self, draft, crew)
