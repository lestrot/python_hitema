class compteBancaire:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde

    def ajoutsolde(self, somme):
        self.solde = self.solde + somme

    def retrait(self, somme):
        self.solde = self.solde - somme

    def affichersolde(self):
        print(self.solde)


compte1 = compteBancaire('jean', 2000)
compte2 = compteBancaire('dupont2', 1000)
compte3 = compteBancaire('dupont3', 1000)


# compte1.ajoutsolde(200)
# compte1.retrait(724)
# print(compte1.nom, compte1.solde)
# compte1.affichersolde()

# jupiter est un IDE serveur, et les fichiers sotn des calepins

# mot = "lac"
# print(mot)
# # le point dans le 1 représente un slice
# # [1:] => coupe le contenu avant le caratère 1 donc mot = ac
# # b + ac = bac
# mot = "b" + mot[1:]
# print(mot)

# self = this

# init = construct

###########################
################ Exercice 2
###########################

class point:
    def __init__(self, x, y, *z):
        self.x = x
        self.y = y
        self.z = z

    def toString(self, num):
        print('P = ',self.x, self.y, self.z)


p1 = point(2,3.1)
p1.toString(3)

p2 = point(5, 7, 23)
# p2.toString(3)

###########################
################ Exercice 3
###########################

class DateNaissance:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def toString(self):
        print('la date est: '+ str(self.jour)+'/'+str(self.mois)+'/'+str(self.annee))

date1 = DateNaissance(27, 4, 2020)
date1.toString()