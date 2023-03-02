class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        peri = (self.__longueur + self.__largeur) * 2
        print(peri)
    
    def surface(self):
        self._surf = self.__longueur * self.__largeur
        print(self._surf)

    def getlongueur(self):
        return(self.__longueur)
    
    def getlargeur(self):
        return(self.__largeur)
    
    def setlongueur(self, nlong):
        self.__longueur = nlong
    
    def setlargeur(self, nlarg):
        self.__largeur = nlarg

class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        vol = self._surf * self.hauteur
        print(vol)

forme = Rectangle(25, 10)
forme = Parallélépipède(25, 10, 15)
forme.perimetre()
forme.surface()
forme.volume()