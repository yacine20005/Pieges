def creation_grille():
    lst = []
    for k in range(13):
        lst2 = []
        for x in range(13):
            lst2.append(0)
        lst.append(lst2)
    return lst

def deplacer_tirets_horizontal(grille, tiret, direction):
    for x in range(len(grille[tiret])):
        if direction < 0:
            if grille[tiret][x] == 1:
                grille[tiret][x] = 0
                grille[tiret][x - direction] = 1
        if direction > 0:
            x = len(grille[tiret]) - x
            if grille[tiret][x] == 1:
                grille[tiret][x] = 0
                grille[tiret][x + direction] = 1

def deplacer_tirets_horizontal_merde(grille, tiret, direction):
    for x in range(7):
        if x - direction > 0:
                if direction < 0:
                    grille[tiret][x-direction] = grille[tiret][x]
                elif direction > 0:
                    grille[tiret][x+direction] = grille[tiret][x]

plateau = creation_grille()
tirette_verticale = creation_grille()
tirette_horizontale = creation_grille()
print(plateau)