from grilles import *
from affichage import *
from fltk import *


def initialiser_plateau():
    v = creation_grille_v()
    h = creation_grille_h()
    plateau = fusion(v, h)
    b = creation_grille_b_vide()
    return b, v, h, plateau


def main_game_loop(b, v, h, plateau, phase_preliminaire, taille_plateau,
                   taille_case, taille_bouton, taille_bille, nb_joueur,
                   nb_de_billes_par_joueur, nb_de_billes_poser, lst_joueur,
                   hitbox_bouton, coord_min_x, coord_min_y, coord_max_x,
                   coord_max_y, coeff_bouton, coeff_bille, coeff_hitbox_bouton,):
    pose = False
    joueur = lst_joueur[0][0]
    affiche_jeu(b, phase_preliminaire, joueur, plateau, taille_plateau,
                taille_case, taille_bouton, taille_bille)
    ev = attend_ev()
    gerer_evenement_boucle(ev, pose, nb_joueur, nb_de_billes_par_joueur,
                           nb_de_billes_poser, lst_joueur, b, v, h, plateau,
                           taille_case, taille_bouton, taille_plateau, hitbox_bouton,
                           coord_min_x, coord_min_y, coord_max_x, coord_max_y,
                           coeff_bouton, coeff_bille, coeff_hitbox_bouton)


def gerer_evenement_boucle(ev, pose, nb_joueur, nb_de_billes_par_joueur,
                           nb_de_billes_poser, lst_joueur, b, v, h,
                           plateau, taille_case, taille_bouton, taille_plateau,
                           hitbox_bouton, coord_min_x, coord_min_y, coord_max_x,
                           coord_max_y, coeff_bouton, coeff_bille, coeff_hitbox_bouton):
    if ev is not None:
        tev = type_ev(ev)
        if tev == "ClicGauche":
            gerer_clic(ev, pose, nb_joueur, nb_de_billes_par_joueur, nb_de_billes_poser, lst_joueur, b, v, h, taille_case, taille_bouton, hitbox_bouton, coord_min_x, coord_min_y, coord_max_x, coord_max_y)
        elif tev == "Redimension":
            gerer_redimension(coeff_bouton, coeff_bille, coeff_hitbox_bouton, b, plateau, taille_plateau)
        elif tev == "Quitte":
            pass


def gerer_clic(ev, pose, phase_preliminaire, joueur, nb_joueur,
               nb_de_billes_par_joueur, nb_de_billes_poser,
               lst_joueur, b, v, h, taille_case, taille_bouton,
               hitbox_bouton, coord_min_x, coord_min_y, coord_max_x, coord_max_y):
    if nb_de_billes_poser != nb_joueur * nb_de_billes_par_joueur:
        texte(100, 100, f"au joueur {joueur} de joueur", "white", "nw", tag="tour")
        clic_x, clic_y = abscisse(ev), ordonnee(ev)
        if verifier_bille_presente(b, clic_x, clic_y, coord_min_x, coord_min_y, taille_case):
            gerer_pose_bille(joueur, b, clic_x, clic_y, coord_min_x, coord_min_y,
                             coord_max_x, coord_max_y, taille_case)
            pose = True
            nb_de_billes_poser += 1
            deplacer_gauche(lst_joueur, 0)
            efface("tour")
        while not pose or bille_en_vie(b, h, v) != 0:
            ev = attend_ev()
            tev = type_ev(ev)
            if tev == "ClicGauche":
                clic_x, clic_y = abscisse(ev), ordonnee(ev)
                if verifier_bille_presente(b, clic_x, clic_y, coord_min_x, coord_min_y,
                                           taille_case):
                    gerer_pose_bille(joueur, b, clic_x, clic_y, coord_min_x, coord_min_y,
                                     coord_max_x, coord_max_y, taille_case)
                    pose = True
                    nb_de_billes_poser += 1
                    deplacer_gauche(lst_joueur, 0)
                    efface("tour")
                else:
                    break
    else:
        phase_preliminaire = False
        clic_x, clic_y = abscisse(ev), ordonnee(ev)
        gerer_evenement_tirette(b, v, h, clic_x, clic_y, coord_min_x, coord_min_y,
                                coord_max_x, coord_max_y,
                                taille_case, taille_bouton, hitbox_bouton)
        bille_en_vie(b, h, v)
        deplacer_gauche(lst_joueur, 0)
    return pose, nb_de_billes_poser, phase_preliminaire


def gerer_redimension(b, phase_preliminaire, joueur, coeff_bouton,
                      coeff_bille, coeff_hitbox_bouton, plateau, taille_plateau):
    efface_tout()
    rectangle(0, 0, largeur_fenetre() , hauteur_fenetre() , "black", "black")
    taille_case = min(largeur_fenetre() , hauteur_fenetre()) / 10
    taille_bouton, taille_bille, hitbox_bouton = calcul_redimension(taille_case, coeff_bouton,
                                                                    coeff_bille,
                                                                    coeff_hitbox_bouton)
    affiche_jeu(b, phase_preliminaire, joueur, plateau,
                taille_plateau, taille_case, taille_bouton, taille_bille)
    coord_min_x, coord_max_x, coord_min_y, coord_max_y = calcul_coord(taille_case, taille_plateau)
    return taille_case, taille_bouton, taille_bille, hitbox_bouton, coord_min_x, coord_max_x, coord_min_y, coord_max_y
