from random import randint, choice
from math import cos, sin, radians
import sys
from fltk import *

# argparse
class Balle:
    """
    Classe permettant de gérer la balle
    """
    def vitesse_par_angle(self, angle):
        """Permet de calculer la vitesse horizontale et verticale de la balle à partir de son angle

        Args:
            angle (int(en degré)): angle en degré qui doit être convertie en radiant
        """

        self.vx = self.vitesse * cos(radians(angle))
        self.vy = -self.vitesse * sin(radians(angle))

    def __init__(self, difficulte):
        """
        Initialisateur de la classe Balle

        Args:
            difficulte (string): permet de chosisir la difficulté de partie
        """
        global NIVEAU_DIFFICULTE
        if difficulte == "sleep":
            NIVEAU_DIFFICULTE = 1
            self.nb_balle = 5
            self.vitesse = 5
        elif difficulte == "normal":
            NIVEAU_DIFFICULTE = 2
            self.nb_balle = 3
            self.vitesse = 9
        elif difficulte == "hero":
            NIVEAU_DIFFICULTE = 3
            self.nb_balle = 2
            self.vitesse = 16
        elif difficulte == "legend":
            NIVEAU_DIFFICULTE = 4
            self.nb_balle = 1
            self.vitesse = 23
        elif difficulte == "grandmaster":
            NIVEAU_DIFFICULTE = 5
            self.nb_balle = 1
            self.vitesse = 30
        self.x, self.y = 0, 0
        self.vx, self.vy = 0, 0
        self.vitesse_par_angle(60)
        self.sur_raquette = True
        self.vitesse_initiale = self.vitesse

    def reset_vitesse(self):
        """Permet de réinitialiser la vitesse de la balle
        """
        self.vitesse = self.vitesse_initiale

    def afficher(self):
        """Permet l'affichage de la balle 
        """
        cercle(self.x, self.y, RAYON_BALLE, COULEUR, COULEUR, tag = 'balle' )

    def rebond_raquette(self, raquette):
        """Permet de gérer le rebond avec la raquette et l'angle que la balle 
        va prendre par rapport à l'endroit de contact avec celle-ci

        Args:
            raquette (object): Objet de la classe Raquette
        """
        delta_x = raquette.x - self.x
        longueur_totale = raquette.longueur/2
        angle = 90 + 80*delta_x/longueur_totale
        self.vitesse_par_angle(angle)

    def deplacer(self, raquette):
        """Permet de gérer le déplacement simultané de la balle et raquette en début de jeu 
        ainsi que ses collisions avec les bords de la fenêtre de jeu

        Args:
            raquette (object): Objet de la classe Raquette
        """
        if self.sur_raquette:
            self.y = raquette.y - 2 * RAYON_BALLE
            self.x = raquette.x
        else:
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            if raquette.collision_balle(self) and self.vy > 0:
                self.rebond_raquette(raquette)
            if self.x + RAYON_BALLE > XMAX:
                self.vx = -self.vx
                jeu.CC
            if self.x - RAYON_BALLE < XMIN:
                self.vx = -self.vx
                jeu.CC
            if self.y + RAYON_BALLE > YMAX:
                self.sur_raquette = True
                self.nb_balle -= 1
            if self.y - RAYON_BALLE < YMIN:
                self.vy = -self.vy
                jeu.CC

class Raquette:
    """Classe permettant de gérer la raquette
    """
    def __init__(self):
        """Initialisateur de la classe Raquette
        """
        self.x = (XMIN + XMAX) / 2
        self.y = YMAX - RAYON_BALLE
        self.longueur = 10*RAYON_BALLE

    def afficher(self):
        """Permet l'affichage de la raquette
        """
        rectangle(int(self.x-self.longueur/2), int(self.y-RAYON_BALLE),
                  self.x+self.longueur/2, self.y+RAYON_BALLE, BLANC, BLANC, tag = 'raquette')

    def deplacer(self, x):
        """Permet de gérer le déplacement de la raquette

        Args:
            x (int): Position en x de la souris
        """
        if x - self.longueur/2 < XMIN:
            self.x = XMIN + self.longueur/2
        elif x + self.longueur/2 > XMAX:
            self.x = XMAX - self.longueur/2
        else:
            self.x = x

    def collision_balle(self, balle):
        """Permet de gérer la hitbox de la raquette

        Args:
            balle (object):

        Returns:
            bool: Si la collision à bien lieu ou non
        """
        vertical = abs(self.y - balle.y) < 2 * RAYON_BALLE
        horizontal = abs(self.x - balle.x) < self.longueur / 2 + RAYON_BALLE
        return vertical and horizontal

class Brique:
    """Classe permettant de gérer les briques
    """
    def __init__(self, position):
        """Initialisateur de la classe Raquette

        Args:
            position (int): coordonnées de la brique
        """
        global NIVEAU_DIFFICULTE
        self.x, self.y = position
        self.niveau = randint(0, NIVEAU_DIFFICULTE)
        self.vie = self.niveau
        self.largeur = LARGEUR_BRIQUE
        self.hauteur = HAUTEUR_BRIQUE

    def est_en_vie(self):
        """Permet de savoir si la brique à encore des points de vies

        Returns:
            bool: Si la brique est en vie ou non
        """
        return self.vie > 0

    def afficher(self):
        """Permet de gérer l'affichage ainsi que la couleur des différentes briques
        """
        if self.vie == 5:
            couleur = "#FFE100"
        elif self.vie == 4:
            couleur = "#FF00FF"
        elif self.vie == 3:
            couleur = "#FF0000"
        elif self.vie == 2:
            couleur = "#FF8000"
        elif self.vie == 1:
            couleur = "#00FF00"
        else:
            couleur = "#FFFFFF"
        rectangle(self.x, self.y, self.x + LARGEUR_BRIQUE, self.y + HAUTEUR_BRIQUE,
                  NOIR, couleur, tag = 'brique')


    def collision_balle(self, balle):
        """Collision entre la balle et les briques (l'enfer sur Python)

        Args:
            balle (object):

        Returns:
            bool: Si la balle a touché la brique ou non
        """
        marge = self.hauteur/2 + 2 * RAYON_BALLE
        #Calcul de la marge autour de la brique pour détecter la collision
        delta_y = balle.y - self.y
        #Calcul de la différence verticale entre la balle et la brique
        touche = False
        #Variable pour indiquer si la balle a touché la brique
        if balle.x >= self.x:
            #Vérification si la balle est à droite de la brique
            delta_x = balle.x - 2 * RAYON_BALLE - (self.x + self.largeur/2 - self.hauteur/2)
            #Calcul de la différence horizontale entre la balle et le bord droit de la brique
            if abs(delta_y) <= marge and delta_x <= marge:
                #Vérification de la collision en fonction de la position horizontale
                touche = True
                self.afficher()
                #Afficher la modification de la couleur
                if delta_x <= abs(delta_y):
                    #Collision sur le bord haut ou le bord bas
                    balle.vy = -balle.vy
                else:
                    #Collision sur le bord droit
                    balle.vx = -balle.vx
        else:
            #Sinon la balle est à gauche de la brique
            delta_x = balle.x - 3 * RAYON_BALLE - (self.x - self.largeur/2 + self.hauteur/2)
            #Calcul de la différence horizontale entre la balle et le bord gauche de la brique
            if abs(delta_y) <= marge and -delta_x <= marge:
                #Vérification de la collision en fonction de la position horizontale
                touche = True
                if -delta_x <= abs(delta_y):
                    # Collision sur le bord haut ou le bord bas
                    balle.vy = -balle.vy
                else:
                    #Collision sur le bord gauche
                    balle.vx = -balle.vx
        if touche:
            #Si la balle a touché la brique
            self.vie -= 1
        return touche
        #Renvoie True si la balle a touché la brique, sinon False

class Jeu:
    """Classe permettant de gérer le déroulement du JeuF
    """
    def __init__(self, difficulte):
        """Initialisateur de la classe Jeu

        Args:
            difficulte (str): la difficulte choisie
        """
        self.difficulte = difficulte
        self.balle = Balle(difficulte)
        self.raquette = Raquette()
        self.briques = []
        self.score = 0
        self.continuer = True
        self.game_over = 0
        self.T_BONUS_VITESSE = 0
        self.T_MALUS_VITESSE = 0
        self.bonus_actif = None

    def CC(self):
        """Permet le choix de couleur aléatoire pour la balle ?
        """
        global COULEUR
        COULEUR = "#"
        for _ in range(6):
            COULEUR = COULEUR + (choice(LC2))

    def gerer_evenements(self):
        """Permet le lancement de la balle au début du jeu ou après la réapparition d'une balle
        """
        if self.balle.sur_raquette:
            self.balle.sur_raquette = False
            self.balle.vitesse_par_angle(randint(-180, 180))

    def generer_brique(self, ligne, colonne):
        """Permet la génération et affichages des briques

        Args:
            ligne (int):
            colonne (int):
        """
        for y in range(colonne):
            for x in range(ligne):
                self.briques.append(Brique((80*x, 40 + 30*y)))


    def mettre_a_jour(self, t):
        """Permet l'apparition du game over,
        la récupération de la position de la souris,
        déplacement de la raquette,
        collision de la balle avec les briques
        et l'activation potentielle de bonus 

        Args:
            t (_type_): _description_
        """
        if self.balle.nb_balle < 1:
            self.game_over = True
        else:
            x = abscisse_souris()
            self.balle.deplacer(self.raquette)
            collision_frame = False
            for brique in self.briques:
                if brique.est_en_vie() and not collision_frame:
                    if brique.collision_balle(self.balle):
                        self.CC()
                        activation_bonus = randint(1, 100)
                        if activation_bonus == 1:
                            self.bonus(t)
                        self.score += 1
                        collision_frame = not collision_frame
                        if self.score % 20 == 0:
                            self.balle.nb_balle += 1
            self.raquette.deplacer(x)

    def ajouter_texte(self, ecrit, position, couleur):
        """Permet l'affichage de texte en utilisant fltk

        Args:
            ecrit (str): le texte affiché
            position (tuples): coordonnées
            couleur (str(hexadécimal)):
        """
        texte(int(position[0]), int(position[1]),
              ecrit, couleur, "center", "Helvetica", 18, tag = 'texte')

    def afficher(self):
        """Permet l'affichage du game over ainsi que la mise a jour de la fenêtre de jeu
        """
        finish = True
        if self.game_over:
            efface("texte")
            efface("balle")
            efface("raquette")
            efface("brique")
            efface("background")
            image(400, 300, 'images/game_over.png', ancrage = 'center', tag = 'game_over')
            mise_a_jour()
        else:
            efface("background")
            image(400, 300, f"images/{background}.png", ancrage = 'center', tag = 'background')
            efface("texte")
            xcoeur = 20
            ycoeur = 20
            efface("pv")
            for _ in range(self.balle.nb_balle):
                image(xcoeur, ycoeur, 'images/logocoeur.png', ancrage = 'center', tag = 'pv')
                xcoeur = xcoeur + 35
            self.ajouter_texte(f'Score: {self.score}', (740, 20), BLANC)
            efface("balle")
            self.balle.afficher()
            efface("raquette")
            self.raquette.afficher()
            efface("brique")
            for brique in self.briques:
                if brique.est_en_vie():
                    finish = False
                    brique.afficher()
                    self.ajouter_texte(str(brique.vie),
                                       (brique.x + LARGEUR_BRIQUE / 1.9 ,
                                        brique.y + HAUTEUR_BRIQUE / 1.6), NOIR)
                if finish:
                    efface("texte")
                    efface("balle")
                    efface("raquette")
                    efface("brique")
                    image(400, 300, 'images/victory.png', ancrage = 'center', tag = 'victory')

    def bonus(self, t):
        """Permet le choix et l'éxécution de bonus (non fini)

        Args:
            t (int): frame actuelle
        """
        bonus = randint(1, 5)
        if bonus == 1:
            print('bonus score')
            self.score += 20
        if bonus == 2 and difficulte != 'Sleep':
            print('destruction')
            for brique in self.briques:
                if brique.est_en_vie():
                    brique.vie -= 1
        if bonus == 3:
            print('vie bonus')
            self.balle.nb_balle += 1
        if bonus == 4:
            if self.bonus_actif != "vitesse":
                self.bonus_actif = "vitesse"
                self.balle.vitesse = self.balle.vitesse * 1.3
                self.T_MALUS_VITESSE = t
                print('boost de vitesse')
        if bonus == 5:
            if self.bonus_actif != "vitesse":
                self.bonus_actif = "vitesse"
                self.balle.vitesse = self.balle.vitesse * 0.7
                self.T_BONUS_VITESSE = t
                print('ralenti')

    def del_bonus(self, t):
        """Permet la désactivation du bonus (non fini)

        Args:
            t (int): frame actuelle
        """
        if t - self.T_BONUS_VITESSE >= 300 or self.T_MALUS_VITESSE >= 300 or self.balle.sur_raquette is True and self.bonus_actif == "vitesse":
            self.balle.reset_vitesse()
            self.bonus_actif = None

largeur, hauteur = 800, 600
XMIN, XMAX = 0, largeur
YMIN, YMAX = 0, hauteur
RAYON_BALLE = 10
LARGEUR_BRIQUE = (XMAX - XMIN) / 10
HAUTEUR_BRIQUE = (YMAX - YMIN) / 20

T_BONUS_VITESSE = 0
T_MALUS_VITESSE = 0

COULEUR = "#FFFFFF"
LC2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]


BLANC = "#FFFFFF"
NOIR = "#000000"
ROUGE = "#FF0000"
VERT = "#00FF00"
BLEU = "#0000FF"
CYAN = "#00FFFF"
MAGENTA = "#FF00FF"
JAUNE = "#FFFF00"

NIVEAU_DIFFICULTE = -1

# Programme principal

if len(sys.argv) != 3:
    print("Erreur : le jeu doit être lancé comme ceci : python3 jeu.py <difficulte> <background>")
    sys.exit(1)
difficulte = sys.argv[1].lower()
if difficulte not in ["sleep", "normal", "hero", "legend", "grandmaster"]:
    print("Difficulté invalide. Choisissez parmi : Sleep, Normal, Hero, Legend, Grandmaster.")
    sys.exit(1)

background = sys.argv[2].lower()
if difficulte not in ["brick", "earth", "mars", "mercury", "moon", "reef", "venus"]:
    print("Background invalide. Choisissez parmi : Brick, Earth, Mars, Mercury, Moon, Venus, Reef.")

jeu = Jeu(difficulte)
jeu.generer_brique(10, 5)
cree_fenetre(largeur,hauteur, frequence = 60)
rectangle(0, 0, largeur, hauteur, NOIR, NOIR, tag = 'fond')
T = 0

while jeu.continuer:
    T += 1
    mise_a_jour()
    jeu.mettre_a_jour(T)
    jeu.afficher()
    jeu.del_bonus(T)
    ev = donne_ev()
    if ev is not None:
        tev = type_ev(ev)
        if tev =="Quitte":
            ferme_fenetre()
        elif tev == "ClicGauche":
            jeu.gerer_evenements()
