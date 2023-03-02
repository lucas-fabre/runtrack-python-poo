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
    

forme = Forme()
print(forme.aire())

forme1 = Rectangle(25, 10)
print(forme1.aire())