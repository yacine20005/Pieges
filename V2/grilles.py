import random
from fltk import *

def old_creation_grille_B(plateau):
    """
    Retourne un tableau en 2 dimensions contenant l'emplacement des billes choisis aléatoirement

    Returns:
        lst: liste contenant les emplacements des billes choisis aléatoirement
    """
    cpt_j1 = 0
    cpt_j2 = 0
    lst = []
    for y in range(7):
        lst2 = []
        for x in range(7):
            if x == 6 and y == 6:
                if cpt_j1 > cpt_j2:
                    lst2.append(2)
            else:
                if plateau[y][x] == 0:
                    lst2.append(0)
                else:
                    chance = random.randint(1, 8)
                    if chance == 1:
                        if cpt_j1 <= cpt_j2:
                            lst2.append(1)
                            cpt_j1 += 1
                        else:
                            lst2.append(2)
                            cpt_j2 += 1
                    else:
                        lst2.append(0)
                    print(chance, cpt_j1, cpt_j2)
        lst.append(lst2)
    return lst

def creation_grille_B(plateau):
    valeur = [1] * 7 + [2] * 7
    manquant = len(plateau) ** 2 - len(valeur)
    valeur = valeur + [0] * manquant
    random.shuffle(valeur)
    lst = []
    for y in range(7):
        lst_ligne = []
        for x in range(7):
            if plateau[y][x] == 0:
                pass
            lst_ligne.append(random.choice(valeur))
        lst.append(lst_ligne)
    return lst
    
def creation_grille_H():
    """
    Retourne un tableau en 2 dimensions contenant l'emplacement des trous choisis aléatoirement des tirettes horizontaux

    Returns:
        lst: liste contenant les emplacements des trous choisis aléatoirement
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
    Retourne un tableau en 2 dimensions contenant l'emplacement des trous choisis aléatoirement des tirettes verticaux

    Returns:
        lst: liste contenant les emplacements des trous choisis aléatoirement
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

def affichage_grille(grille):
    """
    Affiche un tableau en 2 dimensions ligne par ligne

    Args:
        grille (list): tableaux en 2 dimensions représentant la grille de la couche de jeu
    """
    for x in grille:
        print(x)
    print("")

def deplacer_droite(grille, ligne):
    """
    Décale toutes les valeurs de la liste vers la droite de facon circulaire

    Args:
        grille (lst): La grille contenant la tirette qui va avoir ses valeurs décalé
        ligne (int): La tirette qui va avoir ses valeurs décalé
    """
    last_val = grille[ligne].pop()
    grille[ligne].insert(0, last_val)

def deplacer_gauche(grille, ligne):
    """
    Décale toutes les valeurs de la liste vers la gauche de facon circulaire

    Args:
        grille (lst): La grille contenant la tirette qui va avoir ses valeurs décalé
        ligne (int): La tirette qui va avoir ses valeurs décalé
    """
    first_val = grille[ligne].pop(0)
    grille[ligne].insert(len(grille[ligne]), first_val)

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
    PB[y][x] = 1

def gerer_evenement(B, V, H, x, y, coord_min_x, coord_min_y, coord_max_x, coord_max_y, taille_case, taille_bouton, hitbox_b):
    if x > coord_min_x + taille_case and x < coord_max_x and y > coord_min_y + taille_case and y < coord_max_y:
        X = int((x - coord_min_x) // taille_case) - 1
        Y = int((y - coord_min_y) // taille_case) - 1
        poser_bille(B, X, Y)
        
    elif x > coord_min_x and x < coord_min_x + taille_case and y > coord_min_y and y < coord_max_y:
        Y = int((y - coord_min_y) // taille_case) - 1
        if Y in range(len((B)[0])):
            deplacer_droite(H, Y)
            
    elif x > coord_max_x and x < coord_max_x + taille_bouton * hitbox_b  and y > coord_min_y and y < coord_max_y:
        Y = int((y - coord_min_y) // taille_case) - 1
        if Y in range(len((B)[0])):
            deplacer_gauche(H, Y)
            
    elif x > coord_min_x + taille_case and x < coord_max_x and y < coord_min_y + taille_case and y > coord_min_y - taille_bouton * hitbox_b:
        X = int((x - coord_min_x) // taille_case) - 1
        if X in range(len(B)):
            deplacer_bas(V, X)
            
    elif x > coord_min_x + taille_case and x < coord_max_x and y > coord_max_y and y < coord_max_y + taille_bouton * hitbox_b:
        X = int((x - coord_min_x) // taille_case) - 1
        if X in range(len(B)):
            deplacer_haut(V, X)

def calcul_coord(taille_case, taille_plateau):
    coord_min_x = largeur_fenetre() / 2 - (taille_plateau /2 * taille_case) - taille_case
    coord_max_x = (coord_min_x + taille_case) + (taille_case * taille_plateau)
    coord_min_y = hauteur_fenetre() / 2 - (taille_plateau/2 * taille_case) - taille_case
    coord_max_y = (coord_min_y + taille_case) + (taille_case * taille_plateau)
    return coord_min_x, coord_max_x, coord_min_y, coord_max_y