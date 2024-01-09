"""
Module pour les boucles du jeu.

Ce module contient les fonctions liées à la boucle principale du jeu, 
à la gestion des événements dans la boucle principale.
"""

import grilles
import affichage
import fltk
import regles


def initialiser_plateau():
    """
    Initialise le plateau de jeu en créant les grilles verticales, horizontales
    et la fusion de celles-ci, ainsi qu'une grille vide pour les billes.

    Returns:
    - b (list): Grille pour les billes.
    - v (list): Grille verticale.
    - h (list): Grille horizontale.
    - plateau (list): Fusion des grilles verticales et horizontales.
    """
    v = grilles.creation_grille_v()
    h = grilles.creation_grille_h()
    plateau = grilles.fusion(v, h)
    b = grilles.creation_grille_b_vide()
    return b, v, h, plateau


def main_game_loop(b, v, h, plateau, phase_preliminaire, taille_plateau,
                   taille_case, taille_bouton, taille_bille, nb_joueur,
                   nb_de_billes_par_joueur, nb_de_billes_poser, lst_joueur,
                   hitbox_bouton, coord_min_x, coord_min_y, coord_max_x,
                   coord_max_y, coeff_bouton, coeff_bille, coeff_hitbox_bouton,):
    """
    Boucle principale du jeu. Affiche le jeu, attend les événements,
    et gère les événements en conséquence.

    Args:
    - b (list): Grille pour les billes.
    - v (list): Grille verticale.
    - h (list): Grille horizontale.
    - plateau (list): Fusion des grilles verticales et horizontales.
    - phase_preliminaire (bool): Phase préliminaire du jeu.
    - taille_plateau (int): Taille du plateau.
    - taille_case (float): Taille d'une case du plateau.
    - taille_bouton (float): Taille des boutons.
    - taille_bille (float): Taille des billes.
    - nb_joueur (int): Nombre de joueurs.
    - nb_de_billes_par_joueur (int): Nombre de billes par joueur.
    - nb_de_billes_poser (int): Nombre de billes à poser.
    - lst_joueur (list): Liste des joueurs.
    - hitbox_bouton (float): Hitbox des boutons.
    - coord_min_x (float): Coordonnée minimale en x.
    - coord_min_y (float): Coordonnée minimale en y.
    - coord_max_x (float): Coordonnée maximale en x.
    - coord_max_y (float): Coordonnée maximale en y.
    - coeff_bouton (float): Coefficient de redimensionnement des boutons.
    - coeff_bille (float): Coefficient de redimensionnement des billes.
    - coeff_hitbox_bouton (float): Coefficient de redimensionnement de la hitbox des boutons.
    """
    pose = False
    joueur = lst_joueur[0][0]
    affichage.affiche_jeu(b, phase_preliminaire, joueur, plateau, taille_plateau,
                taille_case, taille_bouton, taille_bille)
    ev = fltk.attend_ev()
    gerer_evenement_boucle(ev, pose, nb_joueur, nb_de_billes_par_joueur,
                           nb_de_billes_poser, lst_joueur, b, v, h, plateau,
                           taille_case, taille_bouton, taille_plateau, hitbox_bouton,
                           coord_min_x, coord_min_y, coord_max_x, coord_max_y,
                           coeff_bouton, coeff_bille, coeff_hitbox_bouton)


def gerer_evenement_boucle(ev, pose, nb_joueur, nb_de_billes_par_joueur,
                           nb_de_billes_poser, lst_joueur, b, v, h,
                           plateau, taille_case, taille_bouton, taille_plateau,
                           hitbox_bouton, coord_min_x, coord_min_y, coord_max_x,
                           coord_max_y, coeff_bouton, coeff_bille, coeff_hitbox_bouton):
    """
    Gère les événements de la boucle principale du jeu.

    Args:
    - ev: Événement.
    - pose (bool): Indique si une bille est posé ou non.
    - nb_joueur (int): Nombre de joueurs.
    - nb_de_billes_par_joueur (int): Nombre de billes par joueur.
    - nb_de_billes_poser (int): Nombre de billes à poser.
    - lst_joueur (list): Liste des joueurs.
    - b (list): Grille pour les billes.
    - v (list): Grille verticale.
    - h (list): Grille horizontale.
    - plateau (list): Fusion des grilles verticales et horizontales.
    - taille_case (float): Taille d'une case du plateau.
    - taille_bouton (float): Taille des boutons.
    - taille_plateau (int): Taille du plateau.
    - hitbox_bouton (float): Hitbox des boutons.
    - coord_min_x (float): Coordonnée minimale en x.
    - coord_min_y (float): Coordonnée minimale en y.
    - coord_max_x (float): Coordonnée maximale en x.
    - coord_max_y (float): Coordonnée maximale en y.
    - coeff_bouton (float): Coefficient de redimensionnement des boutons.
    - coeff_bille (float): Coefficient de redimensionnement des billes.
    - coeff_hitbox_bouton (float): Coefficient de redimensionnement de la hitbox des boutons.
    """
    if ev is not None:
        tev = fltk.type_ev(ev)
        if tev == "ClicGauche":
            gerer_clic(ev, pose, nb_joueur, nb_de_billes_par_joueur, nb_de_billes_poser, lst_joueur,
                       b, v, h, taille_case, taille_bouton, hitbox_bouton, coord_min_x, coord_min_y,
                       coord_max_x, coord_max_y)
        elif tev == "Redimension":
            gerer_redimension(coeff_bouton, coeff_bille, coeff_hitbox_bouton, b, plateau,
                              taille_plateau)
        elif tev == "Quitte":
            pass


def gerer_clic(ev, pose, phase_preliminaire, joueur, nb_joueur,
               nb_de_billes_par_joueur, nb_de_billes_poser,
               lst_joueur, b, v, h, taille_case, taille_bouton,
               hitbox_bouton, coord_min_x, coord_min_y, coord_max_x, coord_max_y):
    """
    Gère le clic de la souris.

    Args:
    - ev: Événement de clic.
    - pose (bool): Indique si une bille est posé.
    - phase_preliminaire (bool): Phase préliminaire du jeu.
    - joueur (int): Numéro du joueur en cours.
    - nb_joueur (int): Nombre de joueurs.
    - nb_de_billes_par_joueur (int): Nombre de billes par joueur.
    - nb_de_billes_poser (int): Nombre de billes à poser.
    - lst_joueur (list): Liste des joueurs.
    - b (list): Grille pour les billes.
    - v (list): Grille verticale.
    - h (list): Grille horizontale.
    - taille_case (float): Taille d'une case du plateau.
    - taille_bouton (float): Taille des boutons.
    - hitbox_bouton (float): Hitbox des boutons.
    - coord_min_x (float): Coordonnée minimale en x.
    - coord_min_y (float): Coordonnée minimale en y.
    - coord_max_x (float): Coordonnée maximale en x.
    - coord_max_y (float): Coordonnée maximale en y.

    Returns:
    - pose (bool): Indique si une bille est pose.
    - nb_de_billes_poser (int): Nombre de billes à poser.
    - phase_preliminaire (bool): Phase préliminaire du jeu.
    """

    if nb_de_billes_poser != nb_joueur * nb_de_billes_par_joueur:
        fltk.texte(100, 100, f"au joueur {joueur} de joueur", "white", "nw", tag="tour")
        clic_x, clic_y = fltk.abscisse(ev), fltk.ordonnee(ev)
        if grilles.verifier_bille_presente(b, clic_x, clic_y, coord_min_x, coord_min_y,
                                           taille_case):
            grilles.gerer_pose_bille(joueur, b, clic_x, clic_y, coord_min_x, coord_min_y,
                             coord_max_x, coord_max_y, taille_case)
            pose = True
            nb_de_billes_poser += 1
            grilles.deplacer_gauche(lst_joueur, 0)
            fltk.efface("tour")
        while not pose or regles.bille_en_vie(b, h, v) != 0:
            ev = fltk.attend_ev()
            tev = fltk.type_ev(ev)
            if tev == "ClicGauche":
                clic_x, clic_y = fltk.abscisse(ev), fltk.ordonnee(ev)
                if grilles.verifier_bille_presente(b, clic_x, clic_y, coord_min_x, coord_min_y,
                                           taille_case):
                    grilles.gerer_pose_bille(joueur, b, clic_x, clic_y, coord_min_x, coord_min_y,
                                     coord_max_x, coord_max_y, taille_case)
                    pose = True
                    nb_de_billes_poser += 1
                    grilles.deplacer_gauche(lst_joueur, 0)
                    fltk.efface("tour")
                else:
                    break
    else:
        phase_preliminaire = False
        clic_x, clic_y = fltk.abscisse(ev), fltk.ordonnee(ev)
        grilles.gerer_evenement_tirette(b, v, h, clic_x, clic_y, coord_min_x, coord_min_y,
                                coord_max_x, coord_max_y,
                                taille_case, taille_bouton, hitbox_bouton)
        regles.bille_en_vie(b, h, v)
        grilles.deplacer_gauche(lst_joueur, 0)
    return pose, nb_de_billes_poser, phase_preliminaire


def gerer_redimension(b, phase_preliminaire, joueur, coeff_bouton,
                      coeff_bille, coeff_hitbox_bouton, plateau, taille_plateau):
    """
    Gère le redimensionnement de la fenêtre.

    Args:
    - b (list): Grille pour les billes.
    - phase_preliminaire (bool): Phase préliminaire du jeu.
    - joueur (int): Numéro du joueur en cours.
    - coeff_bouton (float): Coefficient de redimensionnement des boutons.
    - coeff_bille (float): Coefficient de redimensionnement des billes.
    - coeff_hitbox_bouton (float): Coefficient de redimensionnement de la hitbox des boutons.
    - plateau (list): Fusion des grilles verticales et horizontales.
    - taille_plateau (int): Taille du plateau.

    Returns:
    - taille_case (float): Taille d'une case du plateau.
    - taille_bouton (float): Taille des boutons.
    - taille_bille (float): Taille des billes.
    - hitbox_bouton (float): Hitbox des boutons.
    - coord_min_x (float): Coordonnée minimale en x.
    - coord_max_x (float): Coordonnée maximale en x.
    - coord_min_y (float): Coordonnée minimale en y.
    - coord_max_y (float): Coordonnée maximale en y.
    """
    fltk.efface_tout()
    fltk.rectangle(0, 0, fltk.largeur_fenetre() , fltk.hauteur_fenetre() , "black", "black")
    taille_case = min(fltk.largeur_fenetre() , fltk.hauteur_fenetre()) / 10
    taille_bouton, taille_bille, hitbox_bouton = grilles.calcul_redimension(taille_case,
                                                                            coeff_bouton,
                                                                            coeff_bille,
                                                                            coeff_hitbox_bouton)
    affichage.affiche_jeu(b, phase_preliminaire, joueur, plateau,
                taille_plateau, taille_case, taille_bouton, taille_bille)
    coord_min_x, coord_max_x, coord_min_y, coord_max_y = grilles.calcul_coord(taille_case,
                                                                              taille_plateau)
    return (taille_case, taille_bouton, taille_bille, hitbox_bouton,
            coord_min_x, coord_max_x, coord_min_y, coord_max_y)
