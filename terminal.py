import random
import doctest


def init_plateau(taille):
    '''Initialise un plateau en lui renseignant la taille.

    ParamÃ¨tre:
        taille: int

    Renvoie un plateau (list)

    >>> init_plateau(2)
    [[None, None], [None, None]]
    '''
    plateau = []
    for i in range(taille):
        plateau2 = []
        for j in range(taille):
            plateau2.append(None)
        plateau.append(plateau2)
    return plateau


def n(a):
    '''
    >>> n(5)
    8
    >>> n(7)
    10
    '''
    return a + 3


def deplacer_droite(tirette):
    """
    >>> deplacer_droite([False, False, False, True, True, False, True])
    [True, False, False, False, True, True, False]
    """
    # new_tirette = [tirette[:-1]].insert(0, tirette[-1])
    res = tirette.pop()
    tirette.insert(0, res)
    # remove + append pour gauche


# Billes ->
# Billes -> random.randint(start, end) [start, end] pour les placer
tirettes_horizontales = [[False, False, False, True, True, False, True],
                         ...,
                         ...]

tirettes_verticales = [[False, False, True, False, True, False, True],
                       ...,
                       ...]

plateau = init_plateau(7)
print(plateau)

# help(init_plateau)

random.seed(1)
print(random.randint(1, 10))

doctest.testmod()