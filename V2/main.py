from grilles import *
from regles import *
from affichage import *
from fltk import *
from tkinter import *
from menu import *
from boucle import *
#import fltk
#open() with wx,
#os()
#.sav, .txt
#chercher comment ouvrir l'explorateur de fichier pour choisir la sauvegarde
#write()

initialiser_menu()

while not jeu_est_commence():
    menu.update()
    
B, V, H, plateau = initialiser_plateau()

cree_fenetre(1200, 800, redimension = True)
rectangle(0,0, largeur_fenetre() , hauteur_fenetre() ,"black", "black")

nb_joueur = 2
taille_case = min(largeur_fenetre() ,hauteur_fenetre()) / 10
taille_plateau, taille_bouton, taille_bille, hitbox_bouton = 7, 25, 20, 3
coeff_bouton, coeff_bille, coeff_hitbox_bouton = 0.25, 0.2, 0.3
coord_min_x, coord_max_x, coord_min_y, coord_max_y = calcul_coord(taille_case, taille_plateau)
phase_preliminaire = True
nb_de_billes_par_joueur = 2
nb_de_billes_poser = 0
lst_joueur = creer_liste_joueurs(nb_joueur)
pose = False

"""
while bille_en_vie(B,V,H)!=0:
    B = creation_grille_B(plateau)
"""

while victoire(B, phase_preliminaire) is False :
    pose = False
    plateau = fusion(V, H)
    joueur = lst_joueur[0][0]
    affiche_jeu(B, plateau, taille_plateau, taille_case, taille_bouton, taille_bille)
    ev = attend_ev()
    if ev is not None:
        tev = type_ev(ev)
        
        if tev == "ClicGauche":
            pose, nb_de_billes_poser, phase_preliminaire = gerer_clic(ev, pose, phase_preliminaire, joueur, nb_joueur, nb_de_billes_par_joueur, nb_de_billes_poser, lst_joueur, B, V, H, taille_case, taille_bouton, hitbox_bouton, coord_min_x, coord_min_y, coord_max_x, coord_max_y)
            
        if tev == "Redimension":
            taille_case, taille_bouton, taille_bille, hitbox_bouton, coord_min_x, coord_max_x, coord_min_y, coord_max_y = gerer_redimension(coeff_bouton, coeff_bille, coeff_hitbox_bouton, B, plateau, taille_plateau)
            
        if tev =="Quitte":
            break