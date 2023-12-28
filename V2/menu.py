from tkinter import *

menu = Tk()
jeu_commence = False

def commencer_jeu():
    menu.destroy()
    global jeu_commence
    jeu_commence = True

def quitter_jeu():
    menu.destroy()
    
def jeu_est_commence():
    return jeu_commence