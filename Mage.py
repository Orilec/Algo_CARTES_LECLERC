class Mage:
    def __init__(self, name, hp, totalMana, hand):
        self._nom = name
        self._pv = hp
        self._manaTotale = totalMana
        self._manaActuelle = totalMana
        self._main = hand
        self._defausse = []
        self._jeu = []

    def getName(self):
        return self._nom

    def getPv(self):
        return self._pv

    def setPv(self, value):
        self._pv = value

    def perdsPv(self, value):
        self._pv -= value

    def getManaTotale(self):
        return self._manaTotale

    
    def addManaTotale(self, value):
        self._manaTotale += value

    def getManaActuelle(self):
        return self._manaActuelle

    def getMain(self):
        return self._main

    def getDefausse(self):
        return self._defausse

    def getJeu(self):
        return self._jeu

    def playCard(self, carte, index):
        if self._main[index].getName() == carte.getName():
            if carte.getCost() <= self._manaActuelle:
                print("Vous jouez ", carte.getName())
                self._manaActuelle -= carte.getCost()
                self._main.pop(index)
                self._jeu.append(carte)
            else: 
                print("pas assez de mana")


    def getManaBack(self):
        self._manaActuelle = self._manaTotale

    def trashCard(self, carte): 
        for i in range (len(self._jeu)):
            if self._jeu[i].getName() == carte.getName():
                self._jeu.pop(i)
                self._defausse.append(carte)

    def checkMort(self, target):
        if target.getPv() <= 0:
            return True
        else: 
            return False

    # def attaque(self, target, damages):
    #     target.perdsPv(damages)
    #     if target.getPv() < 0:
    #         target.setPv(0)


    


