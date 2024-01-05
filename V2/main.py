from tkinter import *
from grilles import *
from regles import *
from affichage import *
from fltk import *
from menu import *
from boucle import *

initialiser_menu()

while not jeu_est_commence():
    menu.update()

B, V, H, plateau = initialiser_plateau()

cree_fenetre(1200, 800, redimension = True)
rectangle(0,0, largeur_fenetre() , hauteur_fenetre() ,"black", "black")

NB_JOUEUR = 2
taille_case = min(largeur_fenetre() ,hauteur_fenetre()) / 10
taille_plateau, taille_bouton, taille_bille, hitbox_bouton = 7, 25, 20, 3
coeff_bouton, coeff_bille, coeff_hitbox_bouton = 0.25, 0.2, 0.3
coord_min_x, coord_max_x, coord_min_y, coord_max_y = calcul_coord(taille_case, taille_plateau)
PHASE_PRELIMINAIRE = True
NB_BILLE_JOUEUR = 2
NB_BILLES_POSE = 0
lst_joueur = creer_liste_joueurs(NB_JOUEUR)
POSE = False

while victoire(B, PHASE_PRELIMINAIRE) is False :
    POSE = False
    plateau = fusion(V, H)
    joueur = lst_joueur[0][0]
    affiche_jeu(B, PHASE_PRELIMINAIRE, joueur, plateau, taille_plateau,
                taille_case, taille_bouton, taille_bille)
    ev = attend_ev()
    if ev is not None:
        tev = type_ev(ev)

        if tev == "ClicGauche":
            POSE, NB_BILLES_POSE, PHASE_PRELIMINAIRE = gerer_clic(ev, POSE, PHASE_PRELIMINAIRE, joueur, NB_JOUEUR, NB_BILLE_JOUEUR, NB_BILLES_POSE, lst_joueur, B, V, H, taille_case, taille_bouton, hitbox_bouton, coord_min_x, coord_min_y, coord_max_x, coord_max_y)

        if tev == "Redimension":
            taille_case, taille_bouton, taille_bille, hitbox_bouton, coord_min_x, coord_max_x, coord_min_y, coord_max_y = gerer_redimension(B, PHASE_PRELIMINAIRE,  joueur, coeff_bouton, coeff_bille, coeff_hitbox_bouton, B, plateau, taille_plateau)

        if tev =="Quitte":
            break
