from random import randint
from donnees import *

motRecherche = liste_mots[randint(0, 11)]
motInconnu = "--------"


def bienvenue():
    regles = ("Bienvenue au jeu du pendu, vous trouverez ci-dessous un petit rappel des regles: \n Rappel des regles du jeu du pendu: "
              " L\"ordinateur choisi un mot au hasard dans une liste, "
              "un mot de huit lettres maximum. Le joueur tente de trouver les lettres composant le mot. "
              "A chaque coup, il saisit une lettre. Si la lettre figure dans le mot, l\"ordinateur "
              "affiche le mot avec les lettres deja trouve. Celles qui ne le sont pas encore sont "
              "remplacees par des etoiles(*). Le joueur a 8 chances. Au dela, il a perdu.")
    return regles


def nomJoueur():
    prenom = input("Veuillez saisir votre prenom:")
    return prenom


def choisiUnMot():
    return(motRecherche)


def affichageInitial():
    return motInconnu


def trouveLesLetrres(lettreRecherche):
    i = 0
    result = ""
    print("Debug3 {}".format(motRecherche))
    for lettreMot in motRecherche:
        Sequence1 = motRecherche[:i]
        Sequence2 = motRecherche[i:]
        i += 1
        print("Debug4 {}".format(Sequence1))
        print("Debug5 {}".format(Sequence2))
        print("Debug6 {} + {}".format(Sequence1, Sequence2))
        if (lettreMot == lettreRecherche):
            result += lettreRecherche
        else:
            result += "-"

    return(result)
