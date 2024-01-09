"""
Module pour la gestion du menu du jeu Pièges.

Ce module utilise la bibliothèque Tkinter pour créer une interface graphique
permettant de démarrer ou quitter le jeu.
"""
import tkinter

menu = tkinter.Tk()
JEU_COMMENCE = False

def commencer_jeu():
    """
    Détruit la fenêtre du menu et déclare que le jeu a commencé.
    """
    menu.destroy()
    global JEU_COMMENCE
    JEU_COMMENCE = True

def quitter_jeu():
    """
    Détruit la fenêtre du menu pour quitter le jeu.
    """
    menu.destroy()

def jeu_est_commence():
    """
    Indique si le jeu a commencé.

    Returns:
        bool: True si le jeu a commencé, False sinon.
    """
    return JEU_COMMENCE

def initialiser_menu():
    """
    Initialise la fenêtre du menu avec un titre, un fond et deux boutons.
    """
    menu.title("Pièges !")
    menu.geometry("1200x800")

    image_fond = tkinter.PhotoImage(file = "fond_jeu_menu.ppm")
    image_fond_redimensionnee = image_fond.zoom(2)

    fond_label = tkinter.Label(menu, image = image_fond_redimensionnee)
    fond_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    commencer_bouton = tkinter.Button(menu, text = "Démarrer le jeu", command = commencer_jeu)
    commencer_bouton.place(x = 550, y = 400)

    quitter_bouton = tkinter.Button(menu, text = "Quitter le jeu", command = quitter_jeu)
    quitter_bouton.place(x = 550, y = 500)
