class Ville:
    def __init__(self, nom, nombre):
        self.__nom = nom
        self.__nbrhab = nombre
        print("La population de",self.__nom, "est de", self.__nbrhab, "habitants")

    def getnomville(self):
        return(self.__nom)
    
    def getnbrhab(self):
        #permet de récupérer la valeur privée du nombre d'habitant de la ville
        return(self.__nbrhab)
    
    def setnbrhab(self, nbrhab):
        
        self.__nbrhab = nbrhab

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        
    def ajouterPersonne(self, ville):
        #Récupére la ville à la quelle nous allons rajouter une personne
        self.Ville = ville
        #Créer une nouvelle valeur "nbrhab" qui va permettre de redéfinir le nombre d'habitant
        nbrhab = ville.getnbrhab()
        nbrhab += 1
        #Applique la valeur du nbrhab au .setnbrhab de la classe "Ville" pour le mettre à jour
        ville.setnbrhab(nbrhab)
        



Paris = Ville("Paris", 1000000)
Marseille = Ville("Marseille", 861635)

Jhon = Personne("Jhon", 45, "Paris")
Myrtille = Personne("Myrtille", 4, "Paris")
Chloe = Personne("Chloé", 18, "Marseille")

Jhon.ajouterPersonne(Paris)
Myrtille.ajouterPersonne(Paris)
Chloe.ajouterPersonne(Marseille)

print("Mise a jour de la population de la ville de", Paris.getnomville(), Paris.getnbrhab(), "habitants")
print("Mise a jour de la population de la ville de", Marseille.getnomville(), Marseille.getnbrhab(), "habitants")