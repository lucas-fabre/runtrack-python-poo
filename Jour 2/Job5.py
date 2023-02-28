class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.en_marche = False
        self.__reservoir = 50


    def demarrer(self):
        print("Le reservoir est à", self.__verifier_plein(), "litres")
        if self.__verifier_plein() >= 5:
            self.en_marche = True
            print("La voiture peut demarrer")
        else:
            print("La voiture n'a pas assez d'essence")

    def arret(self):
        self.en_marche = False
        print("La voiture est arretée")

    def __verifier_plein(self):
        return(self.__reservoir)

    # def setMarque(self):
    
    # def setModele(self):

    # def setAnnee(self):

    # def setKilometrage(self):
    

    # def getMarque(self):

    # def getModele(self):

    # def getAnnee(self):

    # def getKilometrage(self):

route = Voiture("audi", "shelby", 1989, 2)
route.demarrer()
route.arret()