from src.cShip import cShip
class cCargo(cShip):
    def __init__(self, cargo, quality, draft, crew):
        self.cargo = cargo
        self.quality = quality
        cShip.__init__(draft, crew)
