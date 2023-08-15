from src.Ship import Ship
class Cruise(Ship):
    def __init__(self, passengers, draft, crew):
        self.passengers = float(passengers)
        Ship.__init__(self, draft, crew)
    def is_worth_it(self):
        aux = self.passengers*2.25+self.crew*1.5
        loot = self.draft-aux
        if(loot > 20.0):
            return loot                     #barco merece ser robado
        else:
            raise ValueError("Error")

