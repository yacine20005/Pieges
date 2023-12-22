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
            if grille_H[y][x] + grille_V[y][x] == 0:
                grille_B[y][x] = False

def victoire(grille_B):
    """
    Parcourt l'ensemble de la grille bille pour vérifier la victoire du joueur ou non

    Args:
        grille_B (list): Tableau en 2 dimensions représentant la couche des billes

    Returns:
        bool: True si il n'y plus de billes et False si il en reste qu'un
    """
    for y in range(len(grille_B) - 1):
        for x in range(len(grille_B[0]) - 1):
            if grille_B[y][x] == True:
                return False
    print("Victoire !!!")
    return True

def placement_bille(n):
    for n in range:
        pass