from fltk import *

L_Fenetre = 1200
H_Fenetre = 800
taille_case = 80
taille_plateau = 7
taille_bouton = 25
taille_bille = 20

""" Fonction d'affichage"""

def etat_tirette(lst, x, y):
    x,y = x-1,y-1
    n = lst[y][x]
    if n == 0:
        return "white"
    elif n == 1:
        return "blue"
    elif n == 2:
        return "yellow"
    elif n == 3:
        return "green"

def affiche_plateau():
    MFL = L_Fenetre // 2
    MFH = H_Fenetre // 2
    CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
    CDBY = MFH - (taille_plateau/2*taille_case) -taille_case
    for y in range(taille_plateau):
        CDBY = CDBY + taille_case
        CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
        for x in range(taille_plateau):
            CDBX = CDBX + taille_case
            rectangle(CDBX,CDBY,CDBX+taille_case,CDBY+taille_case, "white")

def affiche_tirette(plateau):
    Y = 0
    MFL = L_Fenetre // 2
    MFH = H_Fenetre // 2
    CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
    CDBY = MFH - (taille_plateau/2*taille_case) -taille_case
    for y in range(taille_plateau):
        X = 0
        Y = Y+1
        CDBY = CDBY + taille_case
        CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
        for x in range(taille_plateau):
            X = X + 1
            CDBX = CDBX + taille_case
            rectangle(CDBX,CDBY,CDBX+taille_case,CDBY+taille_case, remplissage = etat_tirette(plateau,X,Y), tag = "tirette")

def affiche_bouton_tirette():
    MFL = L_Fenetre // 2
    MFH = H_Fenetre // 2
    CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
    CDBY = MFH - (taille_plateau/2*taille_case) - taille_case
    for i in range(taille_plateau):
        CDBX = CDBX + taille_case
        cercle(CDBX+taille_case/2,CDBY+taille_case/2,taille_bouton, "red", "red")
    CDBX = CDBX + taille_case
    for i in range(taille_plateau):
        CDBY = CDBY + taille_case
        cercle(CDBX+taille_case/2,CDBY+taille_case/2,taille_bouton, "red", "red")  
    CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
    CDBY = MFH - (taille_plateau/2*taille_case) - taille_case
    for i in range(taille_plateau):
        CDBY = CDBY + taille_case
        cercle(CDBX+taille_case/2,CDBY+taille_case/2,taille_bouton, "red", "red")
    CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
    CDBY = MFH + (taille_plateau/2*taille_case) 
    for i in range(taille_plateau):
        CDBX = CDBX + taille_case
        cercle(CDBX+taille_case/2,CDBY+taille_case/2,taille_bouton, "red", "red")

def affiche_bille(PB):
    MFL = L_Fenetre // 2
    MFH = H_Fenetre // 2
    CDBX = MFL - (taille_plateau/2*taille_case) - taille_case
    CDBY = MFH - (taille_plateau/2*taille_case) - taille_case
    for y in range(len(PB)):
        for x in range(len(PB)):
            if PB[y][x] == True:
                X = CDBX + ((x+1) * taille_case) + taille_case/2
                Y = CDBY + ((y+1) * taille_case) + taille_case/2
                cercle(X,Y,taille_bille, "purple", "purple", tag="bille")