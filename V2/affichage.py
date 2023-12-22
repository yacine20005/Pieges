from fltk import *


""" Fonction d'affichage"""
    
def etat_tirette(lst, x, y):
    x, y = x, y
    n = lst[y][x]
    if n == 0:
        return "black"
    elif n == 1:
        return "blue"
    elif n == 2:
        return "yellow"
    elif n == 3:
        return "blue"

def affiche_plateau(taille_plateau, taille_case):
    MFL = largeur_fenetre() // 2
    MFH = hauteur_fenetre() // 2
    CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
    CDBY = MFH - (taille_plateau/2*taille_case) -taille_case
    for y in range(taille_plateau):
        CDBY = CDBY + taille_case
        CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
        for x in range(taille_plateau):
            CDBX = CDBX + taille_case
            rectangle(CDBX,CDBY,CDBX+taille_case,CDBY+taille_case, "black", "white")

def affiche_tirette(plateau, taille_plateau, taille_case, taille_bouton):
    MFL = largeur_fenetre() // 2
    MFH = hauteur_fenetre() // 2
    CDBX = MFL - (taille_plateau / 2 * taille_case) - taille_case
    CDBY = MFH - (taille_plateau / 2 * taille_case) - taille_case
    for y in range(0, taille_plateau):
        CDBY = CDBY + taille_case
        CDBX = MFL - (taille_plateau / 2 * taille_case) - taille_case
        for x in range(0, taille_plateau):
            CDBX = CDBX + taille_case
            cercle(CDBX + taille_case / 2, CDBY + taille_case / 2, taille_bouton, remplissage = etat_tirette(plateau, x, y), tag = "tirette")

def affiche_bouton_tirette(taille_plateau, taille_case, taille_bouton):
    MFL = largeur_fenetre() // 2
    MFH = hauteur_fenetre() // 2
    CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
    CDBY = MFH - (taille_plateau/2*taille_case) - taille_case
    for i in range(taille_plateau):
        CDBX = CDBX + taille_case
        cercle(CDBX+taille_case/2,CDBY+taille_case/2,taille_bouton, "white", "yellow")
    CDBX = CDBX + taille_case
    for i in range(taille_plateau):
        CDBY = CDBY + taille_case
        cercle(CDBX+taille_case/2,CDBY+taille_case/2,taille_bouton, "white", "blue")  
    CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
    CDBY = MFH - (taille_plateau/2*taille_case) - taille_case
    for i in range(taille_plateau):
        CDBY = CDBY + taille_case
        cercle(CDBX+taille_case/2,CDBY+taille_case/2,taille_bouton, "white", "blue")
    CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
    CDBY = MFH + (taille_plateau/2*taille_case) 
    for i in range(taille_plateau):
        CDBX = CDBX + taille_case
        cercle(CDBX+taille_case/2,CDBY+taille_case/2,taille_bouton, "white", "yellow")

def affiche_bille(B, taille_plateau, taille_case, taille_bille):
    MFL = largeur_fenetre() // 2
    MFH = hauteur_fenetre() // 2
    CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
    CDBY = MFH - (taille_plateau/2*taille_case) - taille_case
    for y in range(len(B)):
        for x in range(len(B)):
            if B[y][x] == True:
                X = CDBX + ((x+1) * taille_case) + taille_case/2
                Y = CDBY + ((y+1) * taille_case) + taille_case/2
                cercle(X,Y,taille_bille, "purple", "purple", tag="bille")