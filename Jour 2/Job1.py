class Rectangle:
    def __init__(self):
        self.__longeur = 10
        self.__largeur = 5

    def setAttributs(self):
        print(self.__longeur, self.__largeur)
    
    def getAttributs(self, nlongeur, nlargeur):
        self.__longeur = nlongeur
        self.__largeur = nlargeur
        print(nlongeur, nlargeur)

forme1 = Rectangle()
forme1.setAttributs()
forme1.getAttributs(15, 7)