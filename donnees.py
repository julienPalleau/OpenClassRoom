""" Ce fichier definit quelques donnees, sous la forme de variables, utiles au programme pendu"""
from random import randint
nb_coups = 8
liste_mots = ["pyromane", "lucioles", "turbines",
              "laiterie", "monstres", "software",
              "creneaux", "savoyard", "poulines",
              "plombier", "mobilier", "detracte"
              "receveur", "ultrason", "tonnelle"]
motRecherche = liste_mots[randint(0, 11)]
motInconnu = "--------"
