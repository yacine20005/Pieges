def creation_grille():
    lst = []
    for k in range(7):
        lst2 = []
        for x in range(7):
            lst2.append(0)
        lst.append(lst2)
    return lst

def poser_bille(grille,x,y):
    grille[y][x] = 1
    return grille
    
def creation_tirette():
    lst = []
    lst2 = [1, 0, 0, 1, 0, 0, 1]
    for i in range(7):
        lst.append(lst2)
    return lst

def deplacer_tirets_horizontal(grille, tiret, direction):
    for x in range(len(grille[tiret])):
        if direction < 0:
            if grille[tiret][x] == 1:
                grille[tiret][x] = 0
                grille[tiret][x + direction] = 1
        if direction > 0:
            x = len(grille[tiret]) - x
            if grille[tiret][x] == 1:
                grille[tiret][x] = 0
                grille[tiret][x + direction] = 1

plateau = creation_grille()
tirette_verticale = creation_tirette()
tirette_horizontale = creation_tirette()
#print(plateau)
#print(tirette_verticale)
#tirette_horizontale = deplacer_tirets_horizontal(tirette_horizontale, 1, 1)
#print(tirette_horizontale)