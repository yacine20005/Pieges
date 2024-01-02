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

# Chargez l'image de fond

image_fond = PhotoImage(file="fond_jeu_menu.ppm")

# Redimensionnez l'image en utilisant subsample
image_fond_redimensionnee = image_fond.zoom(2)

# Créez un label pour afficher l'image redimensionnée en tant que fond
fond_label = Label(menu, image=image_fond_redimensionnee)
fond_label.place(x=0, y=0, relwidth=1, relheight=1)

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


nb_joueur = 2
taille_case = min(largeur_fenetre() ,hauteur_fenetre()) / 10
taille_plateau, taille_bouton, taille_bille, hitbox_b = 7, 25, 20, 3
coeff_bouton, coeff_bille, coeff_hitbox_b = 0.25, 0.2, 0.3
coord_min_x, coord_max_x, coord_min_y, coord_max_y = calcul_coord(taille_case, taille_plateau)
phase_1 = True
nb_de_billes_par_joueur= 2
nb_de_billes_poser = 0
lstjoueur = creer_liste_joueurs(nb_joueur)
Banane = False

"""
while bille_en_vie(B,V,H)!=0:
    B = creation_grille_B(plateau)
"""

while victoire(B, phase_1) is False :

    Banane = False
    plateau = fusion(V, H)
    joueur = lstjoueur[0][0]
    affiche_jeu(B, plateau, taille_plateau, taille_case, taille_bouton, taille_bille)
    ev = attend_ev()
    if ev is not None:
        tev = type_ev(ev)
        if tev == "ClicGauche":
            if nb_de_billes_poser != nb_joueur * nb_de_billes_par_joueur:
                x,y = abscisse(ev), ordonnee(ev)
                if verifier_bille(B, x, y, coord_min_x, coord_min_y, taille_case):
                    gerer_evenement_bille(joueur,B,x, y, coord_min_x, coord_min_y, 
                                            coord_max_x, coord_max_y, taille_case)
                else:
                    while not Banane:
                        print("banana")
                        ev = attend_ev()
                        tev = type_ev(ev)
                        if tev == "ClicGauche":
                            x,y = abscisse(ev), ordonnee(ev)
                            if verifier_bille(B, x, y, coord_min_x, coord_min_y, taille_case):
                                gerer_evenement_bille(joueur,B,x, y, coord_min_x, coord_min_y, 
                                                coord_max_x, coord_max_y, taille_case)
                                Banane = True
                while bille_en_vie(B, H, V)!= 0 :
                    ev = attend_ev()
                    tev = type_ev(ev)
                    if tev == "ClicGauche":
                        x,y = abscisse(ev), ordonnee(ev)
                        gerer_evenement_bille(joueur,B,x, y, coord_min_x, coord_min_y, 
                                        coord_max_x, coord_max_y, taille_case)
                nb_de_billes_poser = nb_de_billes_poser + 1
                print(nb_de_billes_poser)
            else:
                phase_1 = False
                x,y = abscisse(ev), ordonnee(ev)
                gerer_evenement_tirette(B, V, H, x, y, coord_min_x, coord_min_y,
                                        coord_max_x, coord_max_y, taille_case, taille_bouton, hitbox_b)
                bille_en_vie(B, H, V)
            deplacer_gauche(lstjoueur,0)
            affichage_grille(B)
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
