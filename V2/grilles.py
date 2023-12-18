import random
from variable import *
from fltk import *

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
            chance = random.randint(1, 8)
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
    print("")
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
    print("")
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
    print("")
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
    print("")
    print(f"Déplacement vers le haut de la colonne {colonne}")


def affichage_grille(grille):
    """
    Affiche un tableau en 2 dimensions ligne par ligne

    Args:
        grille (list): tableaux en 2 dimensions représentant la grille de la couche de jeu
    """
    for x in grille:
        print(x)
    print("")

def comparaison(PL,TV,TH):
    """
    Fonction inutilisé ?
    """
    for y in range(len(PL)):
        for x in range(len(PL)):
            if TV[y][x] == True and TH[y][x] == True:
                PL[y][x] = True

def fusion(TV, TH):
    """
    Fusionne la couche des tirettes verticales et horizontales pour ne former qu'un tableau en 2 dimensions qui sera affiché au joueur

    Args:
        TV (list): tableaux en 2 dimensions représentant les tirettes verticaux
        TH (list): tableaux en 2 dimensions représentant les tirettes horizontaux

    Returns:
        list: Tableau en 2 dimensions représentant les 2 couches de jeu
    """
    LstVide = []
    for y in range(len(TV)):
        LstVide2 = []
        for x in range(len(TV)):
            LstVide2.append(TV[y][x] + TH[y][x])
        LstVide.append(LstVide2)
    return LstVide

def poser_bille(PB,x,y):
    x,y = x-1,y-1
    PB[y][x] = True

def gerer_evenement(B,V,H,x,y, CoMinX, CoMinY, CoMaxX, CoMaxY):
    if x > CoMinX + taille_case  and x < CoMaxX and y > CoMinY + taille_case and y < CoMaxY:
        X = int((x - CoMinX) // taille_case)
        Y = int((y - CoMinY) // taille_case)
        print(X,Y)
        poser_bille(B,X,Y)
    elif x > CoMinX and x < CoMinX + taille_case and y > CoMinY and y < CoMaxY:
        Y = int((y - CoMinY) // taille_case) - 1
        if Y in range(len((B)[0])):
            deplacer_droite(H, Y)
    elif x > CoMaxX and x < CoMaxX + taille_bouton * HitBoxBouton  and y > CoMinY and y < CoMaxY:
        Y = int((y - CoMinY) // taille_case) -1
        if Y in range(len((B)[0])):
            deplacer_gauche(H, Y)
    elif x > CoMinX + taille_case and x < CoMaxX  and y < CoMinY + taille_case and y > CoMinY - taille_bouton * HitBoxBouton :
        X = int((x - CoMinX) // taille_case) - 1
        if X in range(len(B)):
            deplacer_bas(V, X)
    elif x > CoMinX + taille_case and x < CoMaxX and y > CoMaxY and y < CoMaxY + taille_bouton * HitBoxBouton :
        X = int((x - CoMinX) // taille_case) - 1
        if X in range(len(B)):
            deplacer_haut(V, X)
