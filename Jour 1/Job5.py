class Point():
    def __init__(self):
        x = 1
        y = 1
        self.x = x
        self.y = y

    def affpoints(self):
        print(self.x, self.y )

    def affX(self):
        print(self.x)

    def affY(self):
        print(self.y)

    def changerX(self, nouveauX):
        self.x = nouveauX
        print(nouveauX)

    def changerY(self, nouveauY):
        self.y = nouveauY
        print(nouveauY)


Afficherpoints = Point()
Afficherpoints.affpoints()

AfficherX = Point()
AfficherX.affX()

AfficherY = Point()
AfficherY.affY()

ChX = Point()
ChX.changerX(5)

ChY = Point()
ChY.changerY(4)