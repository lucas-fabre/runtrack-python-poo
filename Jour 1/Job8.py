class Cercle():
    def __init__(self):
        self.r = 2

    def changerR(self, nouveauR):
        self.r = nouveauR
        print(nouveauR)

    def circonference(self):
        self.C = 2 * 3.14 * self.r
        print(self.C)
    
    def air(self):
        self.A = (self.r * self.r) * 3.14
        print(self.A)

    def diametre(self):
        self.D = self.r * 2
        print(self.D)

    def afficheInfos(self):
        print("Les informations générales du cercle sont:", "le rayon=",self.r,"la circonférence =", self.C,"l'air =", self.A,"le diamètre =", self.D)

geo = Cercle()
geo.circonference()
geo.air()
geo.diametre()
geo.afficheInfos()

geo1 = Cercle()
geo1.changerR(4)
geo1.circonference()
geo1.air()
geo1.diametre()
geo1.afficheInfos()

geo2 = Cercle()
geo2.changerR(7)
geo2.circonference()
geo2.air()
geo2.diametre()
geo2.afficheInfos()