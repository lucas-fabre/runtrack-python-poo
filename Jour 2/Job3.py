class Livre:
    def __init__(self):
        self.__auteur = "J.K Rowling"
        self.__titre = "Le Seigneur des Boules de cristal"
        self.__nbrpages = 171
        self.__disponible = True

    def setAttributs(self):
        print(self.__auteur, self.__titre, self.__nbrpages)

    def verification(self):
        if self.__disponible == True:
            return("True")
        
        if self.__disponible == False:
            return("False")
        
    def emprunter(self):
        if self.verification() == "True":
            self.__disponible = False
            print("Vous avez emprunté le livre")
        
        elif self.verification() == "False":
            print("Le livre n'est pas disponible")

    def rendre(self):
        if self.verification() == "False":
            print("Le livre a bien été emprunté, vous pouvez le rendre")
            self.__disponible = True

        else:
            print("Le livre est déjà rendu")

    def getAttributs(self, nAuteur, nTitre, nNbrpages):
        self.__auteur = nAuteur
        self.__titre = nTitre
        if nNbrpages > 0:
            print(nAuteur, nTitre, nNbrpages)
        if nNbrpages < 0:
            print("Le nombre de pages doit être un nombre positif !")

livre1 = Livre()
livre1.setAttributs()
print(livre1.verification())
livre1.emprunter()
livre1.rendre()
livre1.getAttributs("Son Goku", "Harry Potter des Anneaux", -40)