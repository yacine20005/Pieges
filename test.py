import sys

import random
import doctest

def creation_grille():
    lst = []
    for k in range(7):
        lst2 = []
        for x in range(7):
            lst2.append(False)
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


def creation_tirette():
    lst = []
    lst2 = [True,False,False,True,False,False,True]
    for k in range (5):
        lst.append(lst2)
    return lst

plateau = creation_grille()
TiretteV = creation_grille()
TiretteH = creation_grille()



def comparaison(PL,TV,TH):
    for y in range(len(PL)-1):
        for x in range(len(PL)-1):
            if TV[y][x] == TH[y][x]:
                PL[y][x] = True

            


comparaison(plateau,TiretteV,TiretteH)
 
for x in plateau:
    print(x)









    