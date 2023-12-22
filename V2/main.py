from grilles import *
from regles import *
from affichage import *
from fltk import *
from tkinter import * 

#Crée une fenêtre pour le menu
menu = Tk()
menu.title("Menu du Jeu")
#=======

# Définir la taille de la fenêtre du menu
menu.geometry("1000x660")

# Chargez l'image de fond
image_fond = PhotoImage(file="pieges.ppm")

# Redimensionnez l'image en utilisant subsample
image_fond_redimensionnee = image_fond.zoom(3,3)

# Créez un label pour afficher l'image redimensionnée en tant que fond
fond_label = Label(menu, image=image_fond_redimensionnee)
fond_label.place(x=0, y=0, relwidth=1, relheight=1)

def commencer_jeu():
    menu.destroy()  # Ferme la fenêtre du menu
    global jeu_commence
    jeu_commence = True

def quitter_jeu():
    menu.destroy()

# Crée un bouton pour démarrer le jeu
commencer_bouton = Button(menu, text="Démarrer le jeu", command=commencer_jeu)
commencer_bouton.place(x=450, y=300)  # Ajustez les coordonnées x et y selon vos besoins

# Crée un bouton pour quitter le jeu
quitter_bouton = Button(menu, text="Quitter le jeu", command=quitter_jeu)
quitter_bouton.place(x=450, y=350)  # Ajustez les coordonnées x et y selon vos besoins

jeu_commence = False  # Variable pour savoir si le jeu a commencé
while not jeu_commence:
    menu.update()  # Mise à jour de la fenêtre du menu


#Boucle de gameplay

V = creation_grille_V()
H = creation_grille_H()
B = creation_grille_B()
victoire(B)

print("Bienvenue dans le jeu Pieges !")
print("Les tirettes horizontaux sont composes de 0 et de 1")
print("Tandis que les tirettes verticaux sont composes de 0 et de 2")

cree_fenetre(1200, 800, redimension = True)
rectangle(0,0,largeur_fenetre() ,hauteur_fenetre() ,"black", "black")
plateau = fusion(V, H)

taille_case = min(largeur_fenetre() ,hauteur_fenetre()) / 10
taille_plateau = 7
taille_bouton = 25
taille_bille = 20
hitbox_b = 3

coeff_bouton = 0.25
coeff_bille = 0.2
coeff_Hitbox_B = 0.3

affiche_plateau(taille_plateau, taille_case)
affiche_bouton_tirette(taille_plateau, taille_case, taille_bouton)
affiche_tirette(plateau, taille_plateau, taille_case, taille_bouton)
CoMinX = largeur_fenetre() / 2 - (taille_plateau /2 * taille_case) - taille_case
CoMaxX = (CoMinX + taille_case) + (taille_case * taille_plateau)
CoMinY = hauteur_fenetre() / 2 - (taille_plateau/2*taille_case) - taille_case
CoMaxY = (CoMinY + taille_case) + (taille_case * taille_plateau)


#Nouvelle boucle de gameplay 

while victoire(B) is False:

    bille_en_vie(B, H, V)
    affiche_bille(B, taille_plateau, taille_case, taille_bille)
    plateau = fusion(V, H)
    affiche_tirette(plateau, taille_plateau, taille_case, taille_bouton)
    affiche_bille(B, taille_plateau, taille_case, taille_bille)
    ev = attend_ev()
    if ev is not None:
        tev = type_ev(ev)
        if tev == "ClicGauche":
            x,y = abscisse(ev), ordonnee(ev)
            gerer_evenement(B,V,H,x,y, CoMinX, CoMinY, CoMaxX, CoMaxY, taille_case, taille_bouton, hitbox_b)
            affichage_grille(H)
            bille_en_vie(B, H, V)
        if tev == "Redimension":
            efface_tout()
            rectangle(0,0,largeur_fenetre() ,hauteur_fenetre() ,"black", "black")
            taille_case = min(largeur_fenetre() ,hauteur_fenetre()) / 10
            taille_bouton = coeff_bouton * taille_case
            taille_bille = coeff_bille * taille_case
            Hitbox_B = coeff_Hitbox_B * taille_case
            affiche_plateau(taille_plateau, taille_case)
            affiche_bouton_tirette(taille_plateau, taille_case, taille_bouton)
            affiche_tirette(plateau, taille_plateau, taille_case, taille_bouton)
            CoMinX = largeur_fenetre() / 2 - (taille_plateau /2 * taille_case) - taille_case
            CoMaxX = (CoMinX + taille_case) + (taille_case * taille_plateau)
            CoMinY = hauteur_fenetre() / 2 - (taille_plateau/2*taille_case) - taille_case
            CoMaxY = (CoMinY + taille_case) + (taille_case * taille_plateau)
        if tev =="Quitte":
            break
    efface("bille")
    efface("tirette")  