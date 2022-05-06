from Carte import Carte
class Blast(Carte):
    def __init__(self, name, description, cost, attack):
        Carte.__init__(self, name, description, cost)
        self._type = "blast"
        self._damages = attack

    def blast(self, target):
        print("Vous utilisez", self.getName()," sur", target.getName(), "et lui infligez", self._damages, "dégats.")
        target.perdsPv(self._damages)