from grilles import *
from regles import *
from affichage import *
from fltk import *
from tkinter import *
from menu import *
#import fltk
#open() with wx,
#os()
#.sav, .txt
#chercher comment ouvrir l'explorateur de fichier pour choisir la sauvegarde
#write()

menu.title("Pièges !")
menu.geometry("1200x800")

commencer_bouton = Button(menu, text= "Démarrer le jeu", command = commencer_jeu)
commencer_bouton.place(x = 550, y = 400)

quitter_bouton = Button(menu, text = "Quitter le jeu", command = quitter_jeu)
quitter_bouton.place(x = 550, y = 500)

while not jeu_est_commence():
    menu.update()

V = creation_grille_V()
H = creation_grille_H()
plateau = fusion(V, H)
B = creation_grille_B_vide()

"""while victoire(B):
    V = creation_grille_V()
    H = creation_grille_H()
    plateau = fusion(V, H)
    B = creation_grille_B_vide()"""

cree_fenetre(1200, 800, redimension = True)
rectangle(0,0, largeur_fenetre() , hauteur_fenetre() ,"black", "black")

nb_joueur = 4
taille_case = min(largeur_fenetre() ,hauteur_fenetre()) / 10
taille_plateau, taille_bouton, taille_bille, hitbox_b = 7, 25, 20, 3
coeff_bouton, coeff_bille, coeff_hitbox_b = 0.25, 0.2, 0.3
coord_min_x, coord_max_x, coord_min_y, coord_max_y = calcul_coord(taille_case, taille_plateau)
phase_1 = True
nb_de_billes_par_joueur= 2
nb_de_billes_poser = 0
lstjoueur = creer_liste_joueurs(nb_joueur)

"""C'est fait"""
#While bille des 2 joueur non égal à 7 ?
#Demander de poser des billes à chaque jouer

"""
while bille_en_vie(B,V,H)!=0:
    B = creation_grille_B(plateau)
"""

while victoire(B, phase_1) is False :

    plateau = fusion(V, H)
    affiche_jeu(B, plateau, taille_plateau, taille_case, taille_bouton, taille_bille)
    ev = attend_ev()
    if ev is not None:
        tev = type_ev(ev)
        if tev == "ClicGauche":
            if nb_de_billes_poser != nb_joueur * nb_de_billes_par_joueur:
                joueur = lstjoueur[0][0]
                x,y = abscisse(ev), ordonnee(ev)
                gerer_evenement_bille(joueur,B,x, y, coord_min_x, coord_min_y, 
                                        coord_max_x, coord_max_y, taille_case)
                while bille_en_vie(B, H, V)!= 0:
                    ev = attend_ev()
                    tev = type_ev(ev)
                    if tev == "ClicGauche":
                        x,y = abscisse(ev), ordonnee(ev)
                        gerer_evenement_bille(joueur,B,x, y, coord_min_x, coord_min_y, 
                                        coord_max_x, coord_max_y, taille_case)
                nb_de_billes_poser = nb_de_billes_poser + 1
                deplacer_gauche(lstjoueur,0)
            else:
                phase_1 = False
                x,y = abscisse(ev), ordonnee(ev)
                gerer_evenement_tirette(B, V, H, x, y, coord_min_x, coord_min_y,
                                        coord_max_x, coord_max_y, taille_case, taille_bouton, hitbox_b)
                bille_en_vie(B, H, V)
        if tev == "Redimension":
            efface_tout()
            rectangle(0,0,largeur_fenetre() ,hauteur_fenetre() ,"black", "black")
            taille_case = min(largeur_fenetre() ,hauteur_fenetre()) / 10
            taille_bouton = coeff_bouton * taille_case
            taille_bille = coeff_bille * taille_case
            hitbox_b = coeff_hitbox_b * taille_case
            affiche_jeu(B, plateau, taille_plateau, taille_case, taille_bouton, taille_bille)
            coord_min_x, coord_max_x, coord_min_y, coord_max_y = calcul_coord(taille_case,
                                                                              taille_plateau)
        if tev =="Quitte":
            break
    efface("bille")
    efface("tirette")
