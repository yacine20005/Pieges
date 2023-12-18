from grilles import *
from regles import *
from affichage import *
from fltk import *
from variable import *

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
taille_case = 80
taille_plateau = 7
taille_bouton = 25
taille_bille = 20
HitBoxBouton = 3
affiche_plateau()
affiche_bouton_tirette()
affiche_tirette(plateau)
CoMinX = largeur_fenetre() / 2 - (taille_plateau /2 * taille_case) - taille_case
CoMaxX = (CoMinX + taille_case) + (taille_case * taille_plateau)
CoMinY = hauteur_fenetre() / 2 - (taille_plateau/2*taille_case) - taille_case
CoMaxY = (CoMinY + taille_case) + (taille_case * taille_plateau)


#Nouvelle boucle de gameplay 

while victoire(B) is False:

    bille_en_vie(B, H, V)
    affiche_bille(B)
    plateau = fusion(V, H)
    affiche_tirette(plateau)
    affiche_bille(B)
    ev = attend_ev()
    if ev is not None:
        tev = type_ev(ev)
        if tev == "ClicGauche":
            x,y = abscisse(ev), ordonnee(ev)
            gerer_evenement(B,V,H,x,y, CoMinX, CoMinY, CoMaxX, CoMaxY)
            bille_en_vie(B, H, V)
            nb_coup += 1
        if tev == "Redimension":
            efface_tout()
            rectangle(0,0,largeur_fenetre() ,hauteur_fenetre() ,"black", "black")
            affiche_plateau()
            affiche_bouton_tirette()
            affiche_tirette(plateau)
            CoMinX = largeur_fenetre() / 2 - (taille_plateau /2 * taille_case) - taille_case
            CoMaxX = (CoMinX + taille_case) + (taille_case * taille_plateau)
            CoMinY = hauteur_fenetre() / 2 - (taille_plateau/2*taille_case) - taille_case
            CoMaxY = (CoMinY + taille_case) + (taille_case * taille_plateau)
        if tev =="Quitte":
            break
    efface("bille")
    efface("tirette")  

#Ancienne boucle de gameplay
"""
while victoire(B) is False:

    tirette = None
    mouv = ""
    direction = ""
    plateau = fusion(V, H)
    print("")
    affichage_grille(plateau)
    affichage_grille(B)
    while direction not in ("H", "V", "STOP"):
        direction = input("Voulez-vous deplacer les tirettes horizontaux ou verticaux ? (H ou V ou STOP) : ")

    if direction == "V":
        while tirette not in range(len(B)) :
            tirette = (input("Quelle tirette voulez-vous deplacer ? (0 - 6) : "))
            if tirette.isdigit():
                tirette = int(tirette)
        while mouv not in ("H", "B"):
            mouv = input("Dans quelle direction ? (H ou B) : ")
        if mouv == "B":
            deplacer_bas(V, tirette)
        elif mouv == "H":
            deplacer_haut(V, tirette)
        bille_en_vie(B, H, V)
        nb_coup += 1
        print("")
        print("Vous avez deplacer des tirettes", nb_coup, "fois")

    elif direction == "H":
        while tirette not in range(len((B)[0])):
            tirette = (input("Quelle tirette voulez-vous deplacer ? (0 - 6) : "))
            if tirette.isdigit():
                tirette = int(tirette)
        while mouv not in ("G", "D"):
            mouv = input("Dans quelle direction ? (D ou G) : ")
        if mouv == "G":
            deplacer_gauche(H, tirette)
        elif mouv == "D":
            deplacer_droite(H, tirette)
        bille_en_vie(B, H, V)
        nb_coup += 1
        print("")
        print("Vous avez deplacer des tirettes", nb_coup, "fois")

    elif direction == "STOP":
        break
"""