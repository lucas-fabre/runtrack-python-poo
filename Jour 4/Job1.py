class Personne:
    def __init__(self):
        self.age = 14


    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nAge):
        self.age = nAge
        print(nAge)
    
class Eleve(Personne):
    def __init__(self):
        super().__init__()
    
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("j'ai", self.age, "ans")

class Professeur():
    def __init__(self, matEn) -> None:
        self.__matiereEnseignee = matEn

    def enseigner(self):
        print("Le cours va commencer")

personne1 = Personne()
personne1.afficherAge()
personne1.bonjour()
personne1.modifierAge(25)

theo = Eleve()
theo.allerEnCours()
theo.affichageAge()

celine = Professeur("Devweb")
celine.enseigner()