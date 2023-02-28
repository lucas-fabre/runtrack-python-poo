class Produit():
    def __init__(self):
        self.nom = "RTX 4090tkt"
        self.prixHT = 15
        self.TVA = 0.2

    def changerV(self, nN, nPHT, nTVA):
        self.nom = nN
        self.prixHT = nPHT
        self.TVA = nTVA

    def CalculerPrixTTC(self):
        self.prixTTC = self.prixHT + (self.prixHT * self.TVA)
        return("Prix TTC =", self.prixTTC, "euros")

    def afficher(self):
        return(self.nom, self.prixHT, "euros", self.TVA, "TVA", self.prixTTC, "euros")
    

resultat = Produit()
print(resultat.CalculerPrixTTC())
print(resultat.afficher())

resultat1 = Produit()
print(resultat1.changerV('Scotch', 25, 0.3))
print(resultat1.CalculerPrixTTC())
print(resultat1.afficher())
