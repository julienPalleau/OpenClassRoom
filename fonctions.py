from donnees import *
import os
import pickle


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
    code = 1
    result = []

    print("Debug9 {}".format(motRecherche))
    for lettreMot in motRecherche:
        i += 1
        # Sequence1 = motRecherche[:i]
        # Sequence2 = motRecherche[i:]
        # motRecherche = Sequence1 + Sequence2
        # print("Debug6 {}".format(Sequence1))
        # print("Debug7 {}".format(Sequence2))
        # print("Debug8 {} + {}".format(Sequence1, Sequence2))
        print("Debug10 + lettre mot: {} lettre recherche {} mot inconnu {}".format(
            lettreMot, lettreRecherche, motInconnu[i-1]))
        if (lettreMot == lettreRecherche):
            code = 0
            result.append(i)
            print("motRecherche {} lettreMot {}".format(motRecherche, lettreMot))
            print("Debug11 {}".format(motRecherche.replace(lettreMot, "")))

        # else:
        #    result += "-"
    return {'code': code, 'indice': result}


def calculScores(nbdash, scoreSauvegarde):
    score = (nb_coups - nbdash) + scoreSauvegarde
    # Le score du joueur sera simple à calculer :
    # on prend le score courant (0 si le joueur
    # n'a aucun score déjà enregistré) et, à chaque
    # partie, on lui ajoute le nombre de coups restants
    # comme points de partie. Si, par exemple, il me
    # reste trois coups au moment où je trouve le mot,
    # je gagne trois points.
    return(score)


def sauvegarde(scores):
    os.chdir("C:/Users/MOTTIER LUCIE/Documents/GitHub/OpenClassroom")
    with open('scores', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(scores)
