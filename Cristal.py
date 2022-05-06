from Carte import Carte
class Cristal(Carte):
    def __init__(self, name, description, cost, value):
        Carte.__init__(self, name, description, cost)
        self._type = "cristal"
        self._value = value

    def getValue(self):
        return self._value

