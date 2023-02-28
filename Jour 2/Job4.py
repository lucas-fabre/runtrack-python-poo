class Student:
    def __init__(self):
        self.__prenom = "Jhon"
        self.__nom = "Dhoe"
        self.__numetud = "145"
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, ajout):
        if ajout < 0:
            print("impossible d'ajouter une valeur négative")
        
        if ajout >= 0:
            self.__credits += ajout
            self.__level = self.__studentEval()
            print("Le nombre de credits pour",self.__prenom, self.__nom, "est de", self.__credits,"points")

    def __studentEval(self):
        if self.__credits >= 90:
            #print("Excellent")
            return("Excellent")
        
        elif self.__credits >= 80 and 90 > self.__credits:
            #print("Tres bien")
            return("tres bien")
        
        elif self.__credits >= 70 and 80 > self.__credits:
            #print("Bien")
            return("Bien")
        
        elif self.__credits >= 60 and 70 > self.__credits:
            #print("Passable")
            return("Passable")

        elif self.__credits < 60:
            #print("Insufisant")
            return("Insufisant")

    def studentInfo(self):
        print("Nom =", self.__nom,"\n"
              "Prenom =", self.__prenom,"\n"
              "ID =", self.__numetud,"\n"
              "level =", self.__level,"\n")

etudiant = Student()
etudiant.add_credits(50)
etudiant.add_credits(10)
etudiant.add_credits(10)
etudiant.studentInfo()