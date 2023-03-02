class Forme:
    def aire(self):
        return(0)
    
class Rectangle(Forme):
    def __init__(self, long, larg):
        super().__init__()
        self.longueur = long
        self.largeur = larg

    def aire(self):
        r = self.longueur * self.largeur
        return(r)

class Cercle(Forme):
    def __init__(self, rad):
        super().__init__()
        self.radius = rad

    def aire(self):
        r = (self.radius * self.radius) * 3.14
        return(r)
    
forme = Forme()
print(forme.aire())

forme1 = Rectangle(25, 10)
print(forme1.aire())

forme2 = Cercle(15)
print(forme2.aire())