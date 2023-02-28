class Animal():
    def __init__(self):
        age = 0
        prenom = ""
        self.age = age
        self.prenom = prenom

    def defage(self):
        print(self.age)

    def vieillir(self):
        self.age += 1
        print(self.age)

    def nommer(self, prenom2):
        self.prenom = prenom2
        print("L'animal se nomme", self.prenom)

age1 = Animal()
age1.defage()
age1.vieillir()
age1.nommer("Bertha")