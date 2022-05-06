
from Cristal import Cristal
from Creature import Creature
from Mage import Mage
from Blast import Blast

cristal1 = Cristal("Cristal nul", "Un vieux cristal", 5, 5)
creature1 = Creature("Dragon", "Un dragon trop stylé", 15, 20, 10)
blast1 = Blast("Boule de feu", "Une boule de feu (ça brûle)", 12, 8)

nomjoueur1 = input("Entrez le nom du 1er joueur: ")
nomjoueur2 = input("Entrez le nom du 2ème joueur: ")

joueur1 = Mage(nomjoueur1, 50, 10, [cristal1, creature1])
joueur2 = Mage(nomjoueur2, 50, 10, [cristal1, creature1, blast1])

joueurActif = joueur1
joueurNonActif = joueur2

gameover = False

while not gameover:
    hasPlayedCard = False
    print("Vous avez ", joueurActif.getManaActuelle(), "mana sur", joueurActif.getManaActuelle())
    print("Vous avez ", joueurActif.getPv(), " points de vie")
    print("Voici votre main : ")
    for i in range(len(joueurActif.getMain())):
        print(i, " - ",joueurActif.getMain()[i].getName(),": ", joueurActif.getMain()[i].getDescription(), ", Coût en mana: ", joueurActif.getMain()[i].getCost())
    choix = int(input("Que voulez-vous faire? 1 - Jouer une carte \n 2 - Passer à la phase d'attaque des créatures "))

    if choix == 1:
        hasPlayedCard = True
        choixCarte = (int(input("Entrez le numéro de la carte que vous désirez jouer: ")))
        carteJouee = joueurActif.getMain()[choixCarte]
        joueurActif.playCard(carteJouee, choixCarte)
        if carteJouee.getType() == "cristal":
            joueurActif.addManaTotale(carteJouee.getValue())

        elif carteJouee.getType() == "blast":
            print("Voici les cibles disponibles: \n 0 - ", joueurNonActif.getName())
            for i in range(len(joueurNonActif.getJeu())):
                if joueurNonActif.getJeu()[i].getType() == "creature":
                    print(i, " - ", joueurNonActif.getJeu()[i].getNom())
            choixCible = (int(input("Entrez le numéro de la cible a attaquer: ")))
            if choixCible == 0:
                target = joueurNonActif
                carteJouee.blast(target)
                if joueurActif.checkMort(target):
                    gameover = True
            else:
                target = joueurNonActif.getJeu()[choix]
                carteJouee.blast(target)
                if joueurActif.checkMort(target):
                    joueurNonActif.trashCard(target)
            joueurActif.trashCard(carteJouee)

    compteur = 0
    for i in range(len(joueurActif.getJeu())):
        if joueurActif.getJeu()[i].getType == "creature":
            compteur+=1
    if (compteur == 0 and not hasPlayedCard):
        print("Vous n'avez aucune carte pouvant attaquer sur votre zone de jeu, vous passez votre tour")
        joueurNonActif.getManaBack()
    elif (compteur == 0 and hasPlayedCard):
        print("Vous n'avez aucune carte pouvant attaquer sur votre zone de jeu, fin du tour")
    else: 
        print("Voici les cartes de votre zone de jeu qui peuvent attaquer: ")
        for i in range(len(joueurActif.getJeu())):
            if joueurActif.getJeu()[i].getType == "creature":
                print(i, " - ", joueurActif.getJeu()[i].getName())
        
        print("Voici les cibles disponibles: \n 0 - ", joueurNonActif.getName())
        for i in range(len(joueurNonActif.getJeu())):
            if joueurNonActif.getJeu()[i].getType() == "creature":
                print(i, " - ", joueurNonActif.getJeu()[i].getNom())
        choixCible = (int(input("Entrez le numéro de la cible a attaquer: ")))
        if choixCible == 0:
            target = joueurNonActif
            carteJouee.attaque(target)
            if joueurActif.checkMort(target):
                gameover = True
        else:
            target = joueurNonActif.getJeu()[choix]
            carteJouee.attaque(target)
            print(target.getName," riposte !")
            target.attaque(carteJouee)
            if joueurActif.checkMort(target):
                joueurNonActif.trashCard(target)
    
    if joueurActif == joueur1:
        joueurActif == joueur2
        joueurNonActif == joueur1
    else: 
        joueurActif == joueur1
        joueurNonActif == joueur2






        

    

