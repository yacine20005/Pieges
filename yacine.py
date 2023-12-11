import random
import doctest
import sys

def creation_grille_B():
    lst = []
    for _ in range(7):
        lst2 = []
        for _ in range(7):
            chance = random.randint(1, 4)
            if chance == 1:
                lst2.append(True)
            else:
                lst2.append(False)
        lst.append(lst2)
    return lst

def creation_grille_H():
    lst = []
    for _ in range(7):
        lst2 = []
        for _ in range(7):
            chance = random.randint(1, 2)
            if chance == 1:
                lst2.append(0)
            else:
                lst2.append(1)
        lst.append(lst2)
    return lst

def creation_grille_V():
    lst = []
    for _ in range(7):
        lst2 = []
        for _ in range(7):
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

def bille_en_vie(grille_B, grille_H, grille_V):
    for y in range(len(grille_B) - 1):
        for x in range(len(grille_B[0]) - 1):
            if grille_H[y][x] + grille_V[y][x] == 3:
                grille_B[y][x] = False

def victoire(grille_B):
    for y in range(len(grille_B) - 1):
        for x in range(len(grille_B[0]) - 1):
            if grille_B[y][x] == True:
                return False
    return True



V = creation_grille_V()
H = creation_grille_H()
B = creation_grille_B()

for x in V:
    print(x)

print("")

for x in H:
    print(x)

print("")

for x in B:
    print(x)

print("")
print("Modif")
print("")
bille_en_vie(B, H, V)

for x in B:
    print(x)