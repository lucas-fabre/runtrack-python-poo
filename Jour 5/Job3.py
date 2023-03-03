def longueur(l):
    if l == "":
        return 0
    
    else:
        return 1 + longueur(l[1:])
    
print(longueur("bonjour"))

#Dans " if l == "": " il faut definir un espace vide (donc l == "") ET PAS UN 0 ! étant donné qu'il s'agit d'une suite de caractère et non d'un entier/int.
#Dans "return 1 + longueur(l[1:])", "[1:]" permet de définir avec "1", d'omettre le premier caractère de la chaine et ":" la fin. Enfin je rajoute "1 +" au début pour compter la lettre omise.