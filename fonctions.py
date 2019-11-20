from donnees import *


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
    j = 0
    code = 1
    result = []

    print("Debug10: {}".format(motRecherche))
    for lettreMot in motRecherche:
        i += 1
        # Sequence1 = motRecherche[:i]
        # Sequence2 = motRecherche[i:]
        # motRecherche = Sequence1 + Sequence2
        # print("Debug6 {}".format(Sequence1))
        # print("Debug7 {}".format(Sequence2))
        # print("Debug8 {} + {}".format(Sequence1, Sequence2))
        print("Debug11: + lettre mot: {} lettre recherche {} mot inconnu {}".format(
            lettreMot, lettreRecherche, motInconnu[i-1]))
        if (lettreMot == lettreRecherche):
            code = 0
            print("Debug12: i: {} et j:{}".format(i, j))
            result.append(i)
            print("Debug13: motRecherche {} lettreRecherche {}".format(
                motRecherche, lettreRecherche))
            #print("Debug14: {}".format(motRecherche.replace(lettreRecherche, "")))
            j += 1

        # else:
        #    result += "-"
    return {'code': code, 'indice': result}
