import random

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
    for x in grille:
        print(x)
    print("")

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