"""
Module pour la gestion des grilles.

Ce module contient des fonctions liées à la création des grilles, au déplacement des billes,
à la fusion des tirettes, à la pose des billes par les joueurs, à la gestion des événements
de tirettes, au calcul des coordonnées du plateau, et au redimensionnement des éléments graphiques.
"""

import random
import fltk

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
    """
    Crée une grille de billes aléatoires à partir du plateau donné.

    Args:
    - plateau (list): Grille représentant l'emplacement des trous.

    Returns:
    - lst: Grille de billes.
    """
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
    Affiche une grille ligne par ligne.

    Args:
        grille (list): Grille à afficher.
    """
    for x in grille:
        print(x)
    print("")

def deplacer_droite(grille, tirette):
    """
    Déplace les valeurs de la tirette vers la droite de manière circulaire.

    Args:
        grille (list): Grille contenant la tirette.
        tirette (int): Index de la tirette.
    """
    last_val = grille[tirette].pop()
    grille[tirette].insert(0, last_val)

def deplacer_gauche(grille, tirette):
    """
    Déplace les valeurs de la tirette vers la gauche de manière circulaire.

    Args:
        grille (list): Grille contenant la tirette.
        tirette (int): Index de la tirette.
    """
    first_val = grille[tirette].pop(0)
    grille[tirette].insert(len(grille[tirette]), first_val)

def deplacer_bas(grille, colonne):
    """
    Déplace les valeurs de la grille vers le bas de manière circulaire.

    Args:
        grille (list): Grille contenant la colonne.
        colonne (int): Index de la colonne.
    """
    last_val = grille[len(grille) - 1][colonne]
    for x in range(len(grille) - 1, 0, -1):
        grille[x][colonne] = grille[x - 1][colonne]
    grille[0][colonne] = last_val

def deplacer_haut(grille, colonne):
    """
    Déplace les valeurs de la grille vers le haut de manière circulaire.

    Args:
        grille (list): Grille contenant la colonne.
        colonne (int): Index de la colonne.
    """
    first_val = grille[0][colonne]
    for x in range(len(grille) - 1):
        grille[x][colonne] = grille[x + 1][colonne]
    grille[len(grille)- 1][colonne] = first_val

def fusion(tirette_v, tirette_h):
    """
    Fusionne les tirettes verticales et horizontales pour former une grille unique.

    Args:
        tirette_v (list): Grille des tirettes verticales.
        tirette_h (list): Grille des tirettes horizontales.

    Returns:
        list: Grille fusionnée.
    """
    lst_vide = []
    for y in range(len(tirette_v)):
        lst_vide2 = []
        for x in range(len(tirette_v)):
            lst_vide2.append(tirette_v[y][x] + tirette_h[y][x])
        lst_vide.append(lst_vide2)
    return lst_vide

def poser_bille(plateau_bille, x, y, joueur):
    """
    Place une bille sur le plateau à la position donnée.

    Args:
        plateau_bille (list): Grille des billes.
        x (int): Coordonnée x de la position.
        y (int): Coordonnée y de la position.
        joueur (int): Numéro du joueur.
    """
    plateau_bille[y][x] = int(joueur)

def verifier_bille_presente(b, x, y, coord_min_x, coord_min_y, taille_case):
    """
    Vérifie si une bille est présente à la position donnée.

    Args:
        b (list): Grille des billes.
        x (float): Coordonnée x du clic.
        y (float): Coordonnée y du clic.
        coord_min_x (float): Coordonnée minimale en x.
        coord_min_y (float): Coordonnée minimale en y.
        taille_case (float): Taille d'une case.

    Returns:
        bool: True si une bille est présente, False sinon.
    """
    case_x = int((x - coord_min_x) // taille_case) - 1
    case_y = int((y - coord_min_y) // taille_case) - 1
    if case_x in range(len(b)) and case_y in range(len(b)):
        if b[case_y][case_x] == 0:
            return True
    return False

def gerer_pose_bille(joueur, b, x, y, coord_min_x, coord_min_y,
                     coord_max_x, coord_max_y, taille_case):
    """
    Gère la pose d'une bille sur le plateau.

    Args:
        joueur (int): Numéro du joueur.
        b (list): Grille des billes.
        x (float): Coordonnée x du clic.
        y (float): Coordonnée y du clic.
        coord_min_x (float): Coordonnée minimale en x.
        coord_min_y (float): Coordonnée minimale en y.
        coord_max_x (float): Coordonnée maximale en x.
        coord_max_y (float): Coordonnée maximale en y.
        taille_case (float): Taille d'une case.
    """
    if (coord_min_x + taille_case < x < coord_max_x and
            coord_min_y + taille_case < y < coord_max_y):
        case_x = int((x - coord_min_x) // taille_case) - 1
        case_y = int((y - coord_min_y) // taille_case) - 1
        if verifier_bille_presente(b, x, y, coord_min_x, coord_min_y, taille_case):
            poser_bille(b, case_x, case_y, joueur)


def gerer_evenement_tirette(b, v, h, x, y, coord_min_x, coord_min_y,
                            coord_max_x, coord_max_y, taille_case, taille_bouton, hit_box_bouton):
    """
    Gère les événements liés aux tirettes.

    Args:
        b (list): Grille des billes.
        v (list): Grille verticale.
        h (list): Grille horizontale.
        x (float): Coordonnée x du clic.
        y (float): Coordonnée y du clic.
        coord_min_x (float): Coordonnée minimale en x.
        coord_min_y (float): Coordonnée minimale en y.
        coord_max_x (float): Coordonnée maximale en x.
        coord_max_y (float): Coordonnée maximale en y.
        taille_case (float): Taille d'une case.
        taille_bouton (float): Taille des boutons.
        hit_box_bouton (float): Hitbox des boutons.
    """
    if (coord_min_x < x < coord_min_x + taille_case and
            coord_min_y < y < coord_max_y):
        case_y = int((y - coord_min_y) // taille_case) - 1
        if case_y in range(len(b[0])):
            deplacer_droite(h, case_y)

    elif (coord_max_x < x < coord_max_x + taille_bouton * hit_box_bouton and
          coord_min_y < y < coord_max_y):
        case_y = int((y - coord_min_y) // taille_case) - 1
        if case_y in range(len(b[0])):
            deplacer_gauche(h, case_y)

    elif (coord_min_x + taille_case < x < coord_max_x and
          coord_min_y - taille_bouton * hit_box_bouton < y < coord_min_y + taille_case):
        case_x = int((x - coord_min_x) // taille_case) - 1
        if case_x in range(len(b)):
            deplacer_bas(v, case_x)

    elif (coord_min_x + taille_case < x < coord_max_x and
          coord_max_y < y < coord_max_y + taille_bouton * hit_box_bouton):
        case_x = int((x - coord_min_x) // taille_case) - 1
        if case_x in range(len(b)):
            deplacer_haut(v, case_x)


def calcul_coord(taille_case, taille_plateau):
    """
    Calcule les coordonnées minimales et maximales du plateau.

    Args:
        taille_case (float): Taille d'une case.
        taille_plateau (int): Taille du plateau.

    Returns:
        tuple: Coordonnées minimales et maximales en x et y.
    """
    coord_min_x = fltk.largeur_fenetre() / 2 - (taille_plateau /2 * taille_case) - taille_case
    coord_max_x = (coord_min_x + taille_case) + (taille_case * taille_plateau)
    coord_min_y = fltk.hauteur_fenetre() / 2 - (taille_plateau/2 * taille_case) - taille_case
    coord_max_y = (coord_min_y + taille_case) + (taille_case * taille_plateau)
    return coord_min_x, coord_max_x, coord_min_y, coord_max_y

def calcul_redimension(taille_case, coeff_bouton, coeff_bille, coeff_hitbox_bouton):
    """
    Calcule les tailles des boutons, des billes et la hitbox des boutons après redimensionnement.

    Args:
        taille_case (float): Taille d'une case.
        coeff_bouton (float): Coefficient de redimensionnement des boutons.
        coeff_bille (float): Coefficient de redimensionnement des billes.
        coeff_hitbox_bouton (float): Coefficient de redimensionnement de la hitbox des boutons.

    Returns:
        tuple: Tailles des boutons, des billes et la hitbox des boutons.
    """
    taille_bouton = coeff_bouton * taille_case
    taille_bille = coeff_bille * taille_case
    hitbox_bouton = coeff_hitbox_bouton * taille_case
    return taille_bouton, taille_bille, hitbox_bouton
