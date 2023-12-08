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
    x = len(tirette)-1
    prem_val = tirette[0] 
    del tirette[0]
    tirette.insert(x, prem_val)



#Programme principal 

plateau = creation_grille()
TiretteH = creation_tirette()
TiretteV = creation_tirette()

def comparaison(PL,TV,TH):
    for y in range(len(PL)):
        for x in range(len(PL)):
            if TV[y][x] == 2 and TH[y][x] == 1:
                PL[y][x] = True


comparaison(plateau,TiretteV,TiretteH)
 
for x in plateau:
    print(x)