class cShip(object):
    cantBarcos=0
    def __init__(self, draft, crew):
        self.draft = float(draft)
        self.crew = float(crew)
        cShip.cantBarcos = cShip.cantBarcos+1

    def is_worth_it(self):
        loot = self.draft - self.crew*1.5
        if(loot > 20.0):
            return loot                     #barco merece ser robado
        else:
            raise Exception("Error")
