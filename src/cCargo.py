from src.cShip import cShip
class cCargo(cShip):
    def __init__(self, cargo, quality, draft, crew):
        self.cargo = cargo
        self.quality = float(quality)
        cShip.__init__(self, draft, crew)

    def is_worth_it(self):
        aux = (self.crew)* 1.5
        if(self.quality == 1 and self.cargo != ""):
            aux += float(self.cargo)*3.5
        elif(self.quality == 0.5 and self.cargo != ""):
            aux += float(self.cargo)*2
        elif(self.quality == 0.25 and self.cargo != ""):
            aux += float(self.cargo)*0.5

        loot = self.draft - aux
        if(loot > 20.0):
            return loot                     #barco merece ser robado
        else:
            raise Exception("Error")