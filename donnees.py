""" Ce fichier definit quelques donnees, sous la forme de variables, utiles au programme pendu"""
from random import randint
score = 0
count = 0
motInconnu = ""

liste_mots = ["pyromane", "lucioles", "turbines",
              "la", "monstre", "softwares",
              "angle", "peluche", "poulin",
              "plombier", "mobilier", "detracte",
              "ordinateurs", "porte", "tonnelle",
              "tabourets", "serviettes", "sommeil"]

motRecherche = liste_mots[randint(0, len(liste_mots)-1)]

while (len(motRecherche) > count):
    motInconnu += "-"
    count += 1

nb_coups = count
