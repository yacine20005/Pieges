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

def deplacer_bas(grille, colonne):
    longueur = len(grille)
    for ligne in grille:



plateau = creation_grille()
print(plateau)
test = [False, True, True, False, False, False, True],
[False, False, True, False, False, False, True],
[False, False, True, False, False, False, True],
[False, False, True, False, False, False, True],
[False, False, True, False, False, False, True],
[False, False, True, False, False, False, True],
[False, True, True, False, False, False, True]
print(test)
deplacer_gauche(test)
print(test)