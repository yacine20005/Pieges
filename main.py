import random
import doctest
import sys

""" Variable global """
nb_coup = 0


def creation_grille_B():
    """
    Retourne un tableau en 2 dimensions pour les billes

    Returns:
        list
    """
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
    """
    Retourne un tableau en 2 dimensions pour les tirettes horizontaux

    Returns:
        list
    """
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
    """
    Retourne un tableau en 2 dimensions pour les tirettes verticaux

    Returns:
        list
    """
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
    """
    Décale toutes les valeurs de la liste vers la droite de facon circulaire

    Args:
        grille (lst): La grille contenant la tirette qui va avoir ses valeurs décalé
        ligne (int): La tirette qui va avoir ses valeurs décalé
    """
    last_val = grille[ligne].pop()
    grille[ligne].insert(0, last_val)
    print(f"Déplacement à droite de la ligne {ligne}")

def deplacer_gauche(grille, ligne):
    """
    Décale toutes les valeurs de la liste vers la gauche de facon circulaire

    Args:
        grille (lst): La grille contenant la tirette qui va avoir ses valeurs décalé
        ligne (int): La tirette qui va avoir ses valeurs décalé
    """
    first_val = grille[ligne][0]
    del grille[ligne][0]
    grille[ligne].insert(len(grille[ligne]) - 1, first_val)
    print(f"Déplacement à gauche de la ligne {ligne}")

def deplacer_bas(grille, colonne):
    """
    Décale toutes les valeurs de la grille vers le bas de facon circulaire

    Args:
        grille (lst): La grille contenant la tirette qui va avoir ses valeurs décalé
        ligne (int): La tirette qui va avoir ses valeurs décalé
    """
    last_val = grille[len(grille) - 1][colonne]
    for x in range(len(grille) - 1, 0, -1):
        grille[x][colonne] = grille[x - 1][colonne]
    grille[0][colonne] = last_val
    print(f"Déplacement vers le bas de la colonne {colonne}")

def deplacer_haut(grille, colonne):
    """
    Décale toutes les valeurs de la grille vers le haut de facon circulaire

    Args:
        grille (lst): La grille contenant la tirette qui va avoir ses valeurs décalé
        ligne (int): La tirette qui va avoir ses valeurs décalé
    """
    first_val = grille[0][colonne]
    for x in range(len(grille) - 1):
        grille[x][colonne] = grille[x + 1][colonne]
    grille[len(grille)- 1][colonne] = first_val
    print(f"Déplacement vers le haut de la colonne {colonne}")


def bille_en_vie(grille_B, grille_H, grille_V):
    """
    Parcourt l'ensemble de la grille pour faire tomber et donc disparaître les billes du plateau ayant un trou en dessous d'eux

    Args:
        grille_B (list): Tableau en 2 dimensions représentant la couche des billes
        grille_H (list): Tableau en 2 dimensions représentant les tirettes horizontaux
        grille_V (list): Tableau en 2 dimensions représentant les tirettes verticaux
    """
    for y in range(len(grille_B)):
        for x in range(len(grille_B[0])):
            if grille_H[y][x] + grille_V[y][x] == 3:
                grille_B[y][x] = False

def victoire(grille_B):
    """
    Parcourt l'ensemble de la 

    Args:
        grille_B (_type_): _description_

    Returns:
        _type_: _description_
    """
    for y in range(len(grille_B) - 1):
        for x in range(len(grille_B[0]) - 1):
            if grille_B[y][x] == True:
                return False
    return True

def comparaison(PL,TV,TH):
    "
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
victoire(B)

print("Bienvenue dans le jeu Pieges !")
print("Les tirettes horizontaux sont composes de 0 et de 1")
print("Tandis que les tirettes verticaux sont composes de 0 et de 2")


while victoire(B) is False:
    X = 99
    Mouv = ""
    choix = ""
    plateau = fusion(V, H)
    affichage_grille(plateau)
    affichage_grille(B)
    while choix != "H" and choix != "V" and choix != "STOP":
        choix = input("Quelles tirettes voulez-vous deplacer ? H ou V : ")
    if choix == "V":
        while X not in range(len(B)) :
            X = int(input("Quelle Tirette voulez vous deplacez ?"))
        while Mouv != "Haut" and Mouv != "Bas":
            Mouv = input("Comment voulez vous la deplacer, Haut ou Bas ")
        if Mouv == "Bas":
            deplacer_bas(plateau, X)
        elif Mouv == "Haut":
            deplacer_haut(plateau, X)
        bille_en_vie(B, H, V)
        compteur_de_coup(True, nb_coup)
        print(nb_coup)
        print("Vous avez deplacer la tirette verticale numéro", X ,"vers le", Mouv)
        affichage_grille(plateau)
        affichage_grille(B)
    elif choix == "H":
        while X not in range(len(B)) :
            X = int(input("Quelle Tirette voulez vous deplacez ?"))
        while Mouv != "Gauche" and Mouv != "Droite":
            Mouv = input("Comment voulez vous la deplacer, Gauche ou Droite ")
        if Mouv == "Gauche":
            deplacer_droite(plateau, X)
        elif Mouv == "Droite":
            deplacer_gauche(plateau, X)
        bille_en_vie(B, H, V)
        compteur_de_coup(True, nb_coup)
        print(nb_coup)
        print("Vous avez deplacer la tirette horizontale numéro", X ,"vers le", Mouv)
        affichage_grille(plateau)
        affichage_grille(B)
    elif choix == "STOP":
        break