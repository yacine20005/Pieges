import random
import doctest
import sys

def creation_grille_B():
    lst = []
    for k in range(7):
        lst2 = []
        for x in range(7):
            chance = random.randint(1, 2)
            if chance == 1:
                lst2.append(False)
            else:
                lst2.append(True)
        lst.append(lst2)
    return lst

def creation_grille_H():
    lst = []
    for k in range(7):
        lst2 = []
        for x in range(7):
            chance = random.randint(1, 2)
            if chance == 1:
                lst2.append(0)
            else:
                lst2.append(1)
        lst.append(lst2)
    return lst

def creation_grille_V():
    lst = []
    for k in range(7):
        lst2 = []
        for x in range(7):
            chance = random.randint(1, 2)
            if chance == 1:
                lst2.append(0)
            else:
                lst2.append(2)
        lst.append(lst2)
    return lst

def deplacer_droite(tirette):
    last_val = tirette.pop()
    tirette.insert(0, last_val)

def deplacer_gauche(tirette):
    first_val = tirette[0] 
    del tirette[0]
    tirette.insert(len(tirette) - 1, first_val)

def deplacer_bas(grille, colonne):
    last_val = grille[len(grille) - 1][colonne]
    for x in range(len(grille) - 1, 0, -1):
        grille[x][colonne] = grille[x - 1][colonne]
    grille[0][colonne] = last_val

def deplacer_haut(grille, colonne):
    first_val = grille[0][colonne]
    for x in range(len(grille) - 1):
        grille[x][colonne] = grille[x + 1][colonne]
    grille[len(grille)- 1][colonne] = first_val

TiretteV = creation_grille_V()
TiretteH = creation_grille_H()
Bille = creation_grille_B()
PlateauTrou = creation_grille_B()
LstFusion = []

def comparaison(PL,TV,TH):
    for y in range(len(PL)):
        for x in range(len(PL)):
            if TV[y][x] == True and TH[y][x] == True:
                PL[y][x] = True

def fusion(LstVide, TV, TH):
    LstVide = []
    for y in range(len(TV)):
        LstVide2= []
        for x in range(len(TV)):
            LstVide2.append(TV[y][x] + TH[y][x])
        LstVide.append(LstVide2)

comparaison(PlateauTrou,TiretteV,TiretteH)
fusion(LstFusion,TiretteV,TiretteH)
 
for x in LstFusion:
    print(x)

fusion(LstFusion,TiretteV,TiretteH)

for x in LstFusion:
    print(x)








    