class cShip(object):
    cantBarcos=0
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        cShip.cantBarcos = cShip.cantBarcos+1

    def is_worth_it(self):
        worthIt = self.draft-self.crew*1.5
        return worthIt


    #hola lolo