import random
import doctest
import sys

def creation_grille():
    lst = []
    for k in range(7):
        lst2 = []
        for x in range(7):
            lst2.append(False)
        lst.append(lst2)
    return lst

def creation_tirette():
    lst = []
    for i in range():
        x = random.randint(0,1)
        lst2.append([x])
        lst2 = [True,False,False,True,False,False,True]
        for k in range (7):
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