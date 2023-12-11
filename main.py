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

def deplacer_droite(grille, ligne):
    last_val = grille[ligne].pop()
    grille[ligne].insert(0, last_val)
    print(f"Déplacement à droite de la ligne {ligne}")

def deplacer_gauche(grille, ligne):
    first_val = grille[ligne][0]
    del grille[ligne][0]
    grille[ligne].insert(len(grille[ligne]) - 1, first_val)
    print(f"Déplacement à gauche de la ligne {ligne}")

def deplacer_bas(grille, colonne):
    last_val = grille[len(grille) - 1][colonne]
    for x in range(len(grille) - 1, 0, -1):
        grille[x][colonne] = grille[x - 1][colonne]
    grille[0][colonne] = last_val
    print(f"Déplacement vers le bas de la colonne {colonne}")

def deplacer_haut(grille, colonne):
    first_val = grille[0][colonne]
    for x in range(len(grille) - 1):
        grille[x][colonne] = grille[x + 1][colonne]
    grille[len(grille)- 1][colonne] = first_val
    print(f"Déplacement vers le haut de la colonne {colonne}")


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

def comparaison(PL,TV,TH):
    for y in range(len(PL)):
        for x in range(len(PL)):
            if TV[y][x] == True and TH[y][x] == True:
                PL[y][x] = True

def fusion(TV, TH):
    LstVide = []
    for y in range(len(TV)):
        LstVide2 = []
        for x in range(len(TV)):
            LstVide2.append(TV[y][x] + TH[y][x])
        LstVide.append(LstVide2)
    return LstVide

def compteur_de_coup(etat, nb_coup):
    if etat == True:
        nb_coup += 1
    return nb_coup

def affichage_grille(grille):
    for x in grille:
        print(x)
    print("")

#Boucle de gameplay
V = creation_grille_V()
H = creation_grille_H()
B = creation_grille_B()

print("Bienvenue dans le jeu Pièges !")
print("Les tirettes horizontaux sont composés de 0 et de 1")
print("Tandis que les tirettes verticaux sont composés de 0 et de 2")
print("Utilisez les fonctions suivantes pour déplacer les différentes tirettes : ")
print("deplacer_droite(grille, ligne) \n deplacer_gauche(grille, ligne) \n deplacer_bas(grille, colonne) \n deplacer_haut(grille, colonne)")

affichage_grille(V)
affichage_grille(H)
Fusion = fusion(V, H)
affichage_grille(Fusion)