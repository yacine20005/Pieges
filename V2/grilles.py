import random
from fltk import *
from regles import *

def creation_grille_b_vide():
    """
    Retourne un tableau qui contiendra prochainement l'emplacement des billes placés

    Returns:
        lst: liste contenant les emplacements des billes (vide pour le moment)
    """
    lst = []
    for _ in range(7):
        lst2 = []
        for _ in range(7):
            lst2.append(0)
        lst.append(lst2)
    return lst

def creation_grille_b(plateau):
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
            choix = random.choice(valeur)
            lst_ligne.append(choix)
            valeur.remove(choix)
        lst.append(lst_ligne)
    return lst

def creation_grille_h():
    """
    Retourne un tableau en 2 dimensions contenant l'emplacement des trous
    choisis aléatoirement des tirettes horizontaux

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

def creation_grille_v():
    """
    Retourne un tableau en 2 dimensions contenant l'emplacement des trous
    choisis aléatoirement des tirettes verticaux

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

def deplacer_droite(grille, tirette):
    """
    Décale toutes les valeurs de la liste vers la droite de facon circulaire

    Args:
        grille (lst): La grille contenant la tirette qui va avoir ses valeurs décalé
        tirette (int): La tirette qui va avoir ses valeurs décalé
    """
    last_val = grille[tirette].pop()
    grille[tirette].insert(0, last_val)

def deplacer_gauche(grille, tirette):
    """
    Décale toutes les valeurs de la liste vers la gauche de facon circulaire

    Args:
        grille (lst): La grille contenant la tirette qui va avoir ses valeurs décalé
        tirette (int): La tirette qui va avoir ses valeurs décalé
    """
    first_val = grille[tirette].pop(0)
    grille[tirette].insert(len(grille[tirette]), first_val)

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

def fusion(tirette_v, tirette_h):
    """
    Fusionne la couche des tirettes verticales et horizontales
    pour ne former qu'un tableau en 2 dimensions qui sera affiché au joueur

    Args:
        TV (list): tableaux en 2 dimensions représentant les tirettes verticaux
        TH (list): tableaux en 2 dimensions représentant les tirettes horizontaux

    Returns:
        list: Tableau en 2 dimensions représentant les 2 couches de jeu
    """
    lst_vide = []
    for y in range(len(tirette_v)):
        lst_vide2 = []
        for x in range(len(tirette_v)):
            lst_vide2.append(tirette_v[y][x] + tirette_h[y][x])
        lst_vide.append(lst_vide2)
    return lst_vide

def poser_bille(plateau_bille, x, y, joueur):
    plateau_bille[y][x] = int(joueur)

def verifier_bille_presente(b, x, y, coord_min_x, coord_min_y, taille_case):
    case_x = int((x - coord_min_x) // taille_case) - 1
    case_y = int((y - coord_min_y) // taille_case) - 1
    if case_x in range(len(b)) and case_y in range(len(b)):
        if b[case_y][case_x] == 0:
            return True
    return False

def gerer_pose_bille(joueur, b, x, y, coord_min_x, coord_min_y, coord_max_x, coord_max_y, taille_case):
    if x > coord_min_x + taille_case and x < coord_max_x and y > coord_min_y + taille_case and y < coord_max_y:
        case_x = int((x - coord_min_x) // taille_case) - 1
        case_y = int((y - coord_min_y) // taille_case) - 1
        if verifier_bille_presente(b, x, y, coord_min_x, coord_min_y, taille_case):
            poser_bille(b, case_x, case_y ,joueur)

def gerer_evenement_tirette(b, v, h, x, y, coord_min_x, coord_min_y,
                            coord_max_x, coord_max_y, taille_case, taille_bouton, hit_box_bouton):
    if x > coord_min_x and x < coord_min_x + taille_case and y > coord_min_y and y < coord_max_y:
        case_y = int((y - coord_min_y) // taille_case) - 1
        if case_y in range(len((b)[0])):
            deplacer_droite(h, case_y)

    elif x > coord_max_x and x < coord_max_x + taille_bouton * hit_box_bouton  and y > coord_min_y and y < coord_max_y:
        case_y = int((y - coord_min_y) // taille_case) - 1
        if case_y in range(len((b)[0])):
            deplacer_gauche(h, case_y)

    elif x > coord_min_x + taille_case and x < coord_max_x and y < coord_min_y + taille_case and y > coord_min_y - taille_bouton * hit_box_bouton:
        case_x = int((x - coord_min_x) // taille_case) - 1
        if case_x in range(len(b)):
            deplacer_bas(v, case_x)

    elif x > coord_min_x + taille_case and x < coord_max_x and y > coord_max_y and y < coord_max_y + taille_bouton * hit_box_bouton:
        case_x = int((x - coord_min_x) // taille_case) - 1
        if case_x in range(len(b)):
            deplacer_haut(v, case_x)

def calcul_coord(taille_case, taille_plateau):
    coord_min_x = largeur_fenetre() / 2 - (taille_plateau /2 * taille_case) - taille_case
    coord_max_x = (coord_min_x + taille_case) + (taille_case * taille_plateau)
    coord_min_y = hauteur_fenetre() / 2 - (taille_plateau/2 * taille_case) - taille_case
    coord_max_y = (coord_min_y + taille_case) + (taille_case * taille_plateau)
    return coord_min_x, coord_max_x, coord_min_y, coord_max_y

def calcul_redimension(taille_case, coeff_bouton, coeff_bille, coeff_hitbox_bouton):
    taille_bouton = coeff_bouton * taille_case
    taille_bille = coeff_bille * taille_case
    hitbox_bouton = coeff_hitbox_bouton * taille_case
    return taille_bouton, taille_bille, hitbox_bouton
