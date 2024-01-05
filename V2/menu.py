from tkinter import *

menu = Tk()
JEU_COMMENCE = False

def commencer_jeu():
    menu.destroy()
    global JEU_COMMENCE
    JEU_COMMENCE = True

def quitter_jeu():
    menu.destroy()

def jeu_est_commence():
    return JEU_COMMENCE

def initialiser_menu():
    menu.title("Pièges !")
    menu.geometry("1200x800")

    image_fond = PhotoImage(file = "fond_jeu_menu.ppm")
    image_fond_redimensionnee = image_fond.zoom(2)

    fond_label = Label(menu, image = image_fond_redimensionnee)
    fond_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    commencer_bouton = Button(menu, text = "Démarrer le jeu", command = commencer_jeu)
    commencer_bouton.place(x = 550, y = 400)

    quitter_bouton = Button(menu, text = "Quitter le jeu", command = quitter_jeu)
    quitter_bouton.place(x = 550, y = 500)
