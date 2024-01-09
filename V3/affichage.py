"""
Module pour l'affichage du jeu.

Ce module contient des fonctions liées à l'affichage du plateau, 
des tirettes, des boutons de tirettes,
des billes, et du texte indiquant le tour du joueur.
"""

import fltk

def etat_tirette(lst, x, y):
    """
    Choisit la couleur à affiché sur la case en fonction de la présence ou non des tirettes

    Args:
        lst (list): liste contenant les couches de tirettes verticales et horizontales
        x (int): coordonnées largeur
        y (int): coordonnées hauteur

    Returns:
        str: couleur à affiché
    """
    n = lst[y][x]
    if n == 0:
        return "black"
    elif n == 1:
        return "blue"
    elif n == 2:
        return "yellow"
    else:
        return "blue"

def affiche_plateau(taille_plateau, taille_case):
    """
    Affiche le plateau 

    Args:
        taille_plateau (int): taille du plateau
        taille_case (int): taille des cases
    """
    mileu_fenetre_largeur = fltk.largeur_fenetre() // 2
    milieu_fenetre_hauteur = fltk.hauteur_fenetre() // 2
    coord_bord_x = mileu_fenetre_largeur - (taille_plateau / 2 * taille_case) - taille_case
    coord_bord_y = milieu_fenetre_hauteur - (taille_plateau / 2 * taille_case) - taille_case
    for _ in range(taille_plateau):
        coord_bord_y = coord_bord_y + taille_case
        coord_bord_x = mileu_fenetre_largeur - (taille_plateau/2*taille_case) - taille_case
        for _ in range(taille_plateau):
            coord_bord_x = coord_bord_x + taille_case
            fltk.rectangle(coord_bord_x, coord_bord_y, coord_bord_x + taille_case,
                      coord_bord_y + taille_case, "black", "white")

def affiche_tirette(plateau, taille_plateau, taille_case, taille_bouton):
    """
    Affiche des tirettes horizontale et verticale

    Args:
        plateau (list): liste contenant l'emplacement des trous des tirettes horizontaux et verticau
        taille_plateau (int): taille du plateau
        taille_case (int): taille des cases
        taille_bouton (int): taille des boutons
    """
    mileu_fenetre_largeur = fltk.largeur_fenetre() // 2
    milieu_fenetre_hauteur = fltk.hauteur_fenetre() // 2
    coord_bord_x = mileu_fenetre_largeur - (taille_plateau / 2 * taille_case) - taille_case
    coord_bord_y = milieu_fenetre_hauteur - (taille_plateau / 2 * taille_case) - taille_case
    for y in range(0, taille_plateau):
        coord_bord_y = coord_bord_y + taille_case
        coord_bord_x = mileu_fenetre_largeur - (taille_plateau / 2 * taille_case) - taille_case
        for x in range(0, taille_plateau):
            coord_bord_x = coord_bord_x + taille_case
            fltk.cercle(coord_bord_x + taille_case / 2, coord_bord_y + taille_case / 2,
                        taille_bouton, remplissage = etat_tirette(plateau, x, y), tag = "tirette")


def affiche_bouton_tirette(taille_plateau, taille_case, taille_bouton):
    """
    Affiche les boutons des tirettes

    Args:
        taille_plateau (int): taille du plateau
        taille_case (int): taille des cases
        taille_bouton (int): taille des boutons
    """
    mileu_fenetre_largeur = fltk.largeur_fenetre() // 2
    milieu_fenetre_hauteur = fltk.hauteur_fenetre() // 2
    coord_bord_x = mileu_fenetre_largeur - (taille_plateau/2*taille_case) - taille_case
    coord_bord_y = milieu_fenetre_hauteur - (taille_plateau/2*taille_case) - taille_case
    for _ in range(taille_plateau):
        coord_bord_x = coord_bord_x + taille_case
        fltk.cercle(coord_bord_x + taille_case / 2, coord_bord_y + taille_case / 2,
               taille_bouton, "white", "yellow")
    coord_bord_x = coord_bord_x + taille_case
    for _ in range(taille_plateau):
        coord_bord_y = coord_bord_y + taille_case
        fltk.cercle(coord_bord_x + taille_case / 2, coord_bord_y + taille_case / 2,
                    taille_bouton, "white", "blue")
    coord_bord_x = mileu_fenetre_largeur - (taille_plateau/2*taille_case) - taille_case
    coord_bord_y = milieu_fenetre_hauteur - (taille_plateau/2*taille_case) - taille_case
    for _ in range(taille_plateau):
        coord_bord_y = coord_bord_y + taille_case
        fltk.cercle(coord_bord_x+taille_case/2,coord_bord_y + taille_case / 2,
               taille_bouton, "white", "blue")
    coord_bord_x = mileu_fenetre_largeur - (taille_plateau/2*taille_case) - taille_case
    coord_bord_y = milieu_fenetre_hauteur + (taille_plateau/2*taille_case)
    for _ in range(taille_plateau):
        coord_bord_x = coord_bord_x + taille_case
        fltk.cercle(coord_bord_x + taille_case / 2, coord_bord_y + taille_case / 2,
               taille_bouton, "white", "yellow")

def affiche_bille(b, taille_plateau, taille_case, taille_bille):
    """
    Affiche les billes

    Args:
        B (list): liste contenant l'emplacement des billes
        taille_plateau (int): taille du plateau
        taille_case (int): taille des cases
        taille_bille (int): taille des billes
    """
    mileu_fenetre_largeur = fltk.largeur_fenetre() // 2
    milieu_fenetre_hauteur = fltk.hauteur_fenetre() // 2
    coord_bord_x = mileu_fenetre_largeur - (taille_plateau / 2 * taille_case) - taille_case
    coord_bord_y = milieu_fenetre_hauteur - (taille_plateau / 2 * taille_case) - taille_case
    for y in range(len(b)):
        for x in range(len(b[0])):
            if b[y][x] != 0:
                case_x = coord_bord_x + ((x+1) * taille_case) + taille_case/2
                case_y = coord_bord_y + ((y+1) * taille_case) + taille_case/2
                if b[y][x] == 1:
                    fltk.cercle(case_x, case_y,taille_bille, "purple", "purple", tag = "bille_1")
                elif b[y][x] == 2:
                    fltk.cercle(case_x, case_y, taille_bille, "red", "red", tag = "bille_2")
                elif b[y][x] == 3:
                    fltk.cercle(case_x, case_y, taille_bille, "green", "green", tag = "bille_3")
                elif b[y][x] == 4:
                    fltk.cercle(case_x, case_y, taille_bille, "grey", "grey", tag = "bille_4")


def affichage_tour(joueur, phase_preliminaire, taille_plateau, taille_case):
    """
    Affiche le texte indiquant le tour du joueur pendant la phase préliminaire.

    Args:
        joueur (int): Numéro du joueur en cours.
        phase_preliminaire (bool): Indique si le jeu est en phase préliminaire.
        taille_plateau (int): Taille du plateau.
        taille_case (int): Taille des cases.
    """
    fltk.efface("tour")
    if phase_preliminaire is True:
        mileu_fenetre_largeur = fltk.largeur_fenetre() // 2
        milieu_fenetre_hauteur = fltk.hauteur_fenetre() // 2
        coord_bord_x = mileu_fenetre_largeur - (taille_plateau / 2 * taille_case) - taille_case
        coord_bord_y = milieu_fenetre_hauteur - (taille_plateau / 2 * taille_case) - taille_case
        fltk.texte(coord_bord_x, coord_bord_y - 30,
              f"au tour de joueur {joueur} de jouer", "white", "nw", tag = "tour", taille = 18)

def affiche_jeu(b, phase_preliminaire, joueur, plateau,
                taille_plateau, taille_case, taille_bouton, taille_bille):
    """
    Affiche l'intégralité des éléments du jeu sur la fenêtre

    Args:
        B (list): liste contenant l'emplacement des billes
        plateau (list): liste contenant l'emplacement des trous des tirettes
        taille_plateau (int): taille du plateau
        taille_case (int): taille des cases
        taille_bouton (int): taille des boutons 
        taille_bille (int): taille des billes
    """
    affiche_plateau(taille_plateau, taille_case)
    affiche_bouton_tirette(taille_plateau, taille_case, taille_bouton)
    affiche_tirette(plateau, taille_plateau, taille_case, taille_bouton)
    affiche_bille(b, taille_plateau, taille_case, taille_bille)
    affichage_tour(joueur, phase_preliminaire, taille_plateau, taille_case)
