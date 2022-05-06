class Carte:
    def __init__(self, name, description, cost):
        self._nom = name
        self._description = description
        self._coutMana = cost
        self._type = "null"

    def getName(self):
        return self._nom

    def getDescription(self):
        return self._description

    def getCost(self):
        return self._coutMana

    def getType(self):
        return self._type