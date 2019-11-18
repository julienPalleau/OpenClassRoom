from fonctions import *
from donnees import *

print("Vore prenom est : {}".format(nomJoueur()))
print("\n")
print(bienvenue())
print("\n")
print(liste_mots)
print("\n")
print("Trouvez le mot suivant {}".format(affichageInitial()))
lettreChoisieParLeJoueur = input("Choisissez votre premiere lettre: ")

while(nb_coups > 0):
    print("Debug1 {}".format(lettreChoisieParLeJoueur))
    codeRetour = trouveLesLetrres(lettreChoisieParLeJoueur)['code']
    indice = trouveLesLetrres(lettreChoisieParLeJoueur)['indice']

    print("Debug2 codeRetour {} et indice {}".format(codeRetour, indice))
    print("Debug3 {}".format(lettreChoisieParLeJoueur))
    if (codeRetour == 1):
        print("la lettre n'appartient pas au mot")
        nb_coups -= 1
    else:
        i = 1
        print("vous avez trouve la lettre {}".format(lettreChoisieParLeJoueur))
        for lettremot in motRecherche:
            print("Debug valeur de i: {} valeur de indice: {} lettremot {}".format(
                i, indice, lettremot))
            if ((i) == indice):
                Sequence1 = motInconnu[:i-1]
                Sequence2 = motInconnu[i:]
                print("Debug8 {} + {} + {}".format(Sequence1, lettremot, Sequence2))
                motInconnu = Sequence1 + lettremot + Sequence2
            i += 1

        if (nb_coups < 8):
            nb_coups += 1
        print("PENDU : {}".format(motInconnu))

    print("Nombre de coups restants: {}".format(nb_coups))
    if (nb_coups > 0):
        lettreChoisieParLeJoueur = input("Choisissez une autre lettre: ")
