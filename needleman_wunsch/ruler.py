import numpy as np
from colorama import Fore, Style
import time
import itertools


def red_text(text: str):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"


def simil(carac1: str, carac2: str):
    """
    détermine si les deux carctères sont identiques et renvoie le poids associé
    """
    if carac1 == carac2:
        return 0
    else:
        return -1   # Possibilité d'attribuer une variable à fixer plutôt que un entier dans
                    # Une optique de plus de modularité. ( Les rentrer en paramètres d'appels de la fonction)
                    # A plus de dimensions, on pourrait utiliser une table de de correspondance
                    # Entre un couple d'entrée et un un poids associé. Ex : Dictionnaire de dictionnaires

class Ruler:
    def __init__(self, string1: str, string2: str):
        self.string1 = string1
        self.string2 = string2
        self.d = -1 # On pourrait introduire la valeur de d en argument du constructeur pour plus de modularité
    
    def get_distance_too_soon(self):
        raise AttributeError( "Vous n'avez pas encore execute compute")

    distance = property(get_distance_too_soon)
    
    def Mat_F(self):
        """
        Construction de la matrice F
        """

        self.string1
        self.string2
        self.d 

        F = np.zeros((len(self.string1), len(self.string2)))
        m, n = F.shape

        for i in range(m):
            F[i, 0] = self.d*i
        for j in range(n):
            F[0, j] = self.d*j
        for i, j in itertools.product(range(1, m), range(1, n)):
            F[i, j] = max(F[i, j-1] + self.d, F[i-1, j] + self.d,
                          F[i-1, j-1] + simil(self.string1[i], self.string2[j]))

        self.mat_F = F

    def dist(self):
        """
        Algorithme de calcul de l'alignement optimal
        """
        string1 = self.string1
        string2 = self.string2
        d = self.d
        mat_F = self.mat_F

        distance = 0

        align1 = ""
        align2 = ""
        i = len(string1)-1
        j = len(string2)-1
        while j > 0 and i > 0:  # condition d'arret
            score = mat_F[i, j]
            # Extraction des poids pour les actions possibles pour ce nouveau caractère
            scorediag = mat_F[i-1, j-1]
            scoreUp = mat_F[i, j-1]
            scoreLeft = mat_F[i-1, j]
            # Calcul de la solution optimale
            if score == scorediag + simil(string1[i], string2[j]):
                if simil(string1[i], string2[j]) != 0:
                    distance += 1
                align1 = string1[i] + align1
                align2 = string2[j] + align2
                i = i-1
                j = j-1
            elif score == scoreLeft + d:
                distance += 1
                align1 = string1[i] + align1
                align2 = '=' + align2
                i = i-1
            elif score == scoreUp + d:
                distance += 1
                align1 = '=' + align1
                align2 = string2[j] + align2
                j = j-1
        # Finir l'alignement
        if i == j:  # il reste une lettre
            if simil(string1[i], string2[j]) != 0:
                distance += 1
            align1 = string1[i] + align1
            align2 = string2[j] + align2
        else:
            while i >= 0:  # Compléter l'alignement 2 avec des '='
                distance += 1
                align1 = string1[i] + align1
                align2 = '=' + align2
                i = i-1
            while j >= 0:  # Compléter l'alignement 1 avec des '='
                distance += 1
                align1 = '='+align1
                align2 = string2[j] + align2
                j = j-1

        # Création des nouveaux attributs
        setattr(Ruler, 'align1', align1)
        setattr(Ruler, 'align2', align2)
        setattr(Ruler, 'distance', distance)

    def compute(self):

        self.Mat_F()

        self.dist()

    def report(self):
        """
        Renvoie les chaines coloréees à interpréter par le terminal
        """
        top = ""
        bottom = ""
        for a, b in zip(self.align1, self.align2):
            if a == '=':
                top += red_text(a)
                bottom += b
            elif b == '=':
                top += a
                bottom += red_text(b)
            elif a != b:
                top += red_text(a)
                bottom += red_text(b)
            else:
                top += a
                bottom += b

        return top, bottom
