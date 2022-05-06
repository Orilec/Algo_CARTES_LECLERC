from Carte import Carte
class Creature(Carte):
    def __init__(self, name, description, cost, hp, attack):
        Carte.__init__(self, name, description, cost)
        self._type = "creature"
        self._pv = hp
        self._damages = attack

    def getPv(self):
        return self._pv

    def setPv(self, value):
        self._pv = value

    def perdsPv(self, value):
        self._pv -= value

    def attaque(self, target):
        print(self.getName(), "attaque ", target.getName(), "et lui inflige", self._damages, "dégats.")
        target.perdsPv(self._damages)
        if target.getPv() < 0:
            target.setPv(0)
        
    