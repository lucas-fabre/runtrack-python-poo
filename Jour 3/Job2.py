class CompteBancaire:
    def __init__(self, numcompte, nom , prenom, solde):
        self.__numcompte = numcompte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = True
            
    def getsolde(self):
        return(self.__solde)
    
    def setsolde(self, total):
        self.__solde = total

    def afficher(self):
        print("numéro de compte",self.__numcompte,"\n"
              "nom du propriétaire",self.__nom,"\n"
              "prénom du propriétaire",self.__prenom)
        
    def afficherSolde(self):
        print("Le solde du compte est de", self.__solde, "euros")

    def versement(self, ajout):
        self.__solde += ajout
        return(self.__solde)

    def retrait(self, deduit):
        if self.__decouvert == True:
            self.__solde -= deduit
            print("Le solde du compte est maintenant de", self.__solde, "euros")
        elif self.__decouvert == False:
            if self.__solde > deduit:
                self.__solde -= deduit
                print("Le solde du compte est maintenant de", self.__solde, "euros")
            else:
                print("Erreur, pas assez d'argent sur le compte")

    def agios(self):
        if self.__decouvert == True and self.__solde < 0:
            self.__solde = self.__solde + (self.__solde * 0.2)
            print("La solde du compte avec les agios s'élevent à", self.__solde, "euros")

    def virement(self, recepteur, montant):
        if self.__decouvert == True:
            self.__solde -= montant
            recepteur.versement(montant)
            print("Le transfert d'un montant de", montant, "euros", "a bien été effectué")
        
        elif self.__decouvert == False and self.__solde < montant:
            print("Erreur, pas assez d'argent sur le compte")




Personne1 = CompteBancaire(1707, "Fabre", "Lucas", 17000)
Personne2 = CompteBancaire(1800, "Cornet", "Chris", -5000)

Personne1.versement(500)
Personne1.afficher()
Personne1.afficherSolde()
#Personne1.retrait(450)
#Personne1.retrait(18000)
Personne1.agios()
Personne1.virement(Personne2, 18000)
Personne1.afficherSolde()
Personne2.afficherSolde()