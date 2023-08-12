from src.cShip import cShip
class cCruise(cShip):
    def __init__(self, passengers, draft, crew):
        self.passengers = passengers
        cShip.__init__(self, draft, crew)
    def is_worth_it(self):
        pesoTotal = self.passengers*2.25+self.crew*1.5
        worthIt = self.draft-pesoTotal
        return worthIt

