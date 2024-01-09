"""
Module pour la gestion du déroulement du jeu.

Ce module contient le code principal qui initialise le menu, le plateau, et gère le déroulement du 
jeu à travers la boucle principale, la gestion des événements, la pose des billes, 
la vérification de la victoire, et la gestion de la redimension de la fenêtre.
"""
import regles
import grilles
import affichage
import fltk
import menu
import boucle

menu.initialiser_menu()

while not menu.jeu_est_commence():
    menu.menu.update()

B, V, H, plateau = boucle.initialiser_plateau()

fltk.cree_fenetre(1200, 800, redimension=True)
fltk.rectangle(0, 0, fltk.largeur_fenetre() , fltk.hauteur_fenetre() , "black", "black")

NB_JOUEUR = 2
taille_case = min(fltk.largeur_fenetre() , fltk.hauteur_fenetre()) / 10
taille_plateau, taille_bouton, taille_bille, hitbox_bouton = 7, 25, 20, 3
coeff_bouton, coeff_bille, coeff_hitbox_bouton = 0.25, 0.2, 0.3
(coord_min_x, coord_max_x, coord_min_y,
 coord_max_y) = grilles.calcul_coord(taille_case, taille_plateau)
PHASE_PRELIMINAIRE = True
NB_BILLE_JOUEUR = 2
NB_BILLES_POSE = 0
lst_joueur = regles.creer_liste_joueurs(NB_JOUEUR)
POSE = False

while regles.victoire(B, PHASE_PRELIMINAIRE) is False:
    POSE = False
    plateau = grilles.fusion(V, H)
    joueur = lst_joueur[0][0]
    affichage.affiche_jeu(B, PHASE_PRELIMINAIRE, joueur, plateau, taille_plateau,
                taille_case, taille_bouton, taille_bille)
    ev = fltk.attend_ev()
    if ev is not None:
        tev = fltk.type_ev(ev)

        if tev == "ClicGauche":
            POSE, NB_BILLES_POSE, PHASE_PRELIMINAIRE = boucle.gerer_clic(ev, POSE,
                                                                  PHASE_PRELIMINAIRE, joueur,
                                                                  NB_JOUEUR, NB_BILLE_JOUEUR,
                                                                  NB_BILLES_POSE, lst_joueur,
                                                                  B, V, H, taille_case,
                                                                  taille_bouton,
                                                                  hitbox_bouton, coord_min_x,
                                                                  coord_min_y, coord_max_x,
                                                                  coord_max_y)

        if tev == "Redimension":
            (taille_case, taille_bouton, taille_bille, hitbox_bouton, coord_min_x,
             coord_max_x, coord_min_y,
             coord_max_y) = boucle.gerer_redimension(B, PHASE_PRELIMINAIRE,
                                                     joueur, coeff_bouton,
                                                    coeff_bille, coeff_hitbox_bouton,
                                                    plateau, taille_plateau)

        if tev == "Quitte":
            break
