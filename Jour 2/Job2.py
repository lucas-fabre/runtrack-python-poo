class Livre:
    def __init__(self):
        self.__auteur = "J.K Rowling"
        self.__titre = "Le Seigneur des Boules de cristal"
        self.__nbrpages = 171

    def setAttributs(self):
        print(self.__auteur, self.__titre, self.__nbrpages)

    def getAttributs(self, nAuteur, nTitre, nNbrpages):
        self.__auteur = nAuteur
        self.__titre = nTitre
        if nNbrpages > 0:
            print(nAuteur, nTitre, nNbrpages)
        if nNbrpages < 0:
            print("Le nombre de pages doit être un nombre positif !")

livre1 = Livre()
livre1.setAttributs()
livre1.getAttributs("Son Goku", "Harry Potter des Anneaux", -40)