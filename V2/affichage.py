from fltk import *
from variable import *


""" Fonction d'affichage"""
    
def etat_tirette(lst, x, y):
    x,y = x-1,y-1
    n = lst[y][x]
    if n == 0:
        return "black"
    elif n == 1:
        return "blue"
    elif n == 2:
        return "yellow"
    elif n == 3:
        return "blue"

def affiche_plateau():
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

def affiche_tirette(plateau):
    MFL = largeur_fenetre() // 2
    MFH = hauteur_fenetre() // 2
    CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
    CDBY = MFH - (taille_plateau/2*taille_case) -taille_case
    for y in range(1, taille_plateau + 1):
        CDBY = CDBY + taille_case
        CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
        for x in range(1, taille_plateau + 1):
            CDBX = CDBX + taille_case
            cercle(CDBX+taille_case/2,CDBY+taille_case/2, taille_bouton, remplissage = etat_tirette(plateau,x,y), tag = "tirette")

def affiche_bouton_tirette():
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

def affiche_bille(PB):
    MFL = largeur_fenetre() // 2
    MFH = hauteur_fenetre() // 2
    CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
    CDBY = MFH - (taille_plateau/2*taille_case) - taille_case
    for y in range(len(PB)):
        for x in range(len(PB)):
            if PB[y][x] == True:
                X = CDBX + ((x+1) * taille_case) + taille_case/2
                Y = CDBY + ((y+1) * taille_case) + taille_case/2
                cercle(X,Y,taille_bille, "purple", "purple", tag="bille")