"""
Module that read a file and execute the module Ruler 
on the first two sequence it founds
it prints the result with a visual comparison if the two sequences
"""

from ruler import Ruler
import sys


def iter_rule(datfile: '.txt'):
    """
    itérateur qui parcoure le fichier texte et 
    effectue la comparaison de chaine sur les deux premières lignes qu'il trouve
    """
    with open(datfile, 'r') as f:
        string1 = ""
        string2 = ""
        for line in f:
            if line == '' or line == ' ' or line == '\n':  # on passe si la liste est vide
                pass
            elif string1 == '':  # on stocke la première ligne
                string1 = line
            elif string2 == '':  # on stocke la seconde ligne
                string2 = line

                ruler = Ruler(string1, string2)
                string1, string2 = '', ''  # on vide le stockage
                ruler.compute()
                top, bottom = ruler.report()

                yield ruler.distance, top, bottom


def affichage(datfile: '.txt'):
    """
    Fonction de rendu des chaines
    """
    for number, tuples in enumerate(iter_rule(datfile), 1):
        dist, top, bottom = tuples
        print(f"====== example # {number} - distance = {dist}")
        print(top)
        print(bottom)


def main():

    if len(sys.argv) == 2:
        datafile = sys.argv[1]
        affichage(datafile)
    return 0


if __name__ == '__main__':
    sys.exit(main())
