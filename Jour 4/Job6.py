class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("\nmarque du vehicule", self.marque,
              "\nmodele du vehicule", self.modele,
              "\nannee du vehicule", self.annee,
              "\nprix du vehicule", self.prix)
        
    def demarrer(self):
        print("Attention, je roule")
        
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        Vehicule.informationsVehicule(self),
        print("nombre de portes du vehicule", self.portes)

    def demarrer(self):
        print("Attention, j'ai 2500 chevaux sous le capot")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues = 2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        Vehicule.informationsVehicule(self),
        print("nombre de roues sur le vehicule", self.roues)

    def demarrer(self):
        print("Attention, j'ai pas autant de chevaux mais j'ai la classe")

multipla = Voiture("Fiat", "Multipla", 2000, 50, 5)
multipla.informationsVehicule()
multipla.demarrer()

harley = Moto("Harley Davidson", "Super Dinka", 2007, 5000)
harley.informationsVehicule()
harley.demarrer()