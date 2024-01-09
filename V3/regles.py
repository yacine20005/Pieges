"""
Module pour la gestion des règles du jeu Pièges.

Ce module contient des fonctions liées aux règles du jeu, telles que la vérification
de la disparition de billes, la détection de victoire, etc.
"""

def bille_en_vie(grille_b, grille_h, grille_v):
    """
    Parcourt l'ensemble de la grille pour faire tomber et donc disparaître les billes du plateau
    ayant un trou en dessous d'eux

    Args:
        grille_B (list): Tableau en 2 dimensions représentant la couche des billes
        grille_H (list): Tableau en 2 dimensions représentant les tirettes horizontaux
        grille_V (list): Tableau en 2 dimensions représentant les tirettes verticaux
    """
    nb_billes_tombe = 0
    for y in range(len(grille_b)):
        for x in range(len(grille_b[0])):
            if grille_h[y][x] + grille_v[y][x] == 0 and grille_b[y][x] != 0:
                grille_b[y][x] = 0
                nb_billes_tombe = nb_billes_tombe + 1
    return nb_billes_tombe


def victoire(grille_b, phase):
    """
    Parcourt l'ensemble de la grille bille pour vérifier la victoire du joueur ou non

    Args:
        grille_B (list): Tableau en 2 dimensions représentant la couche des billes

    Returns:
        bool: True si il n'y plus de billes et False si il en reste qu'un
    """
    if phase is True:
        return False
    victorieux = 0
    for y in range(len(grille_b)):
        for x in range(len(grille_b[0])):
            if grille_b[y][x] != victorieux and grille_b[y][x] != 0:
                if victorieux == 0:
                    victorieux = grille_b[y][x]
                else:
                    return False
    print(f"Victoire du joueur {victorieux}")
    return True

def creer_liste_joueurs(nombre_joueurs):
    """
    Crée une liste de joueurs avec des noms numérotés.

    Args:
        nombre_joueurs (int): Nombre de joueurs.

    Returns:
        list: Liste de joueurs.
    """
    if nombre_joueurs < 1:
        raise ValueError("Le nombre de joueurs doit être supérieur ou égal à 1")

    liste_joueur = [f"{i}" for i in range(1, nombre_joueurs + 1)]
    liste_joueurs = []
    liste_joueurs.append(liste_joueur)
    return liste_joueurs
