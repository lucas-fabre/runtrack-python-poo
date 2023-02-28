class Personne():
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def SePresenter(self):
        print(self.prenom, self.nom)

personne1 = Personne( "Jhon", "Doe")
personne2 = Personne( "Jeanne", "Dupont")

SePresenter = Personne("Lucas", "Fabre")
SePresenter.SePresenter()

personne1.SePresenter()
personne2.SePresenter()