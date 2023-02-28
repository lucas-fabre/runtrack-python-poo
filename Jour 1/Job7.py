class Personnage():
	def __init__(self, X, Y):
		self.matrix = [[1,2,3],[4,5,6],[7,8,9]]

		##--Définition de la position de base du joueur--##
		self.X = X
		self.Y = Y

		self.debut = self.matrix[self.X][self.Y]
		##--Fin Définition--##

	 ##--Définition changement de positions--##
	def gauche(self):
		self.Y -= 1
		self.debut = self.matrix[self.X][self.Y]
		
	def droite(self):
		self.Y += 1
		self.debut = self.matrix[self.X][self.Y]

	def haut(self):
		self.X -= 1
		self.debut = self.matrix[self.X][self.Y]

	def bas(self):
		self.X += 1
		self.debut = self.matrix[self.X][self.Y]
	##--Fin définition--##

	def Position(self):
		position = (self.X, self.Y)
		print(position)

debut = Personnage(1,1)
debut.Position()
debut.bas()
debut.Position()
debut.gauche()
debut.Position()
