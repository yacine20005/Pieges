import random
import doctest

def creation_grille():
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

test = creation_grille()
for x in test:
    print(x)