from fonctions import *
from donnees import *

print("Vore prenom est : {}".format(nomJoueur()))
print("\n")
print(bienvenue())
print("\n")
print(liste_mots)
print("\n")
print("Trouvez le mot suivant {}".format(affichageInitial()))
lettreChoisi = input("Choisissez votre premiere lettre: ")

while(nb_coups > 0):
    print("Debug1 {}".format(lettreChoisi))
    laLettreChoisi = trouveLesLetrres(lettreChoisi)
    print("Debug2 {}".format(laLettreChoisi))
    if (lettreChoisi not in 'a-z'):
        print("la lettre n'appartient pas au mot")
        nb_coups -= 1
    else:
        print("vous avez trouve la lettre {}".format(lettreChoisi))
        if (nb_coups < 8):
            nb_coups += 1
        print("PENDU : {}".format(laLettreChoisi))

    print("Nombre de coups restants: {}".format(nb_coups))
    if (nb_coups > 0):
        lettreChoisi = input("Choisissez une autre lettre: ")
