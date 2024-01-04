def bille_en_vie(grille_B, grille_H, grille_V):
    """
    Parcourt l'ensemble de la grille pour faire tomber et donc disparaître les billes du plateau ayant un trou en dessous d'eux

    Args:
        grille_B (list): Tableau en 2 dimensions représentant la couche des billes
        grille_H (list): Tableau en 2 dimensions représentant les tirettes horizontaux
        grille_V (list): Tableau en 2 dimensions représentant les tirettes verticaux
    """
    nb_billes_tombe = 0
    for y in range(len(grille_B)):
        for x in range(len(grille_B[0])):
            if grille_H[y][x] + grille_V[y][x] == 0 and grille_B[y][x] != 0:
                grille_B[y][x] = 0
                nb_billes_tombe = nb_billes_tombe + 1
    return nb_billes_tombe


def victoire(grille_B, X):
    """
    Parcourt l'ensemble de la grille bille pour vérifier la victoire du joueur ou non

    Args:
        grille_B (list): Tableau en 2 dimensions représentant la couche des billes

    Returns:
        bool: True si il n'y plus de billes et False si il en reste qu'un
    """
    if X == True:
        return False
    else:
        for y in range(len(grille_B)):
            for x in range(len(grille_B[0])):
                if grille_B[y][x] != 0:
                    return False
        print("Victoire !!!")
        return True

def creer_liste_joueurs(nombre_joueurs):
    if nombre_joueurs < 1:
        raise ValueError("Le nombre de joueurs doit être supérieur ou égal à 1")
    
    liste_joueur = [f"{i}" for i in range(1, nombre_joueurs + 1)]
    liste_joueurs = []
    liste_joueurs.append(liste_joueur)
    return liste_joueurs
