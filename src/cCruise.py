from src.cShip import cShip
class cCruise(cShip):
    def __init__(self, passengers, draft, crew):
        self.passengers = passengers
        cShip.__init__(self, draft, crew)
