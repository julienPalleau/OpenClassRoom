from fonctions import *
from donnees import *
test = 1

print("Vore prenom est : {}".format(nomJoueur()))
print("\n")
print(bienvenue())
print("\n")
print(liste_mots)
print("\n")
print("Trouvez le mot suivant {}".format(affichageInitial()))
print("Debug0: le mot recherche est {}".format(motRecherche))


while(nb_coups > 0 and "-" in motInconnu):
    lettreChoisieParLeJoueur = input("Choisissez votre premiere lettre: ")
    print("Debug1 Lettre choise par le joueur: {}".format(lettreChoisieParLeJoueur))
    codeRetour = trouveLesLetrres(lettreChoisieParLeJoueur)['code']
    indice = trouveLesLetrres(lettreChoisieParLeJoueur)['indice']

    # print("Debug2 codeRetour: {}, longueur de la liste indice: {} et valeur de l'indice {}".format(
    #    codeRetour, len(indice), indice))
    print("Debug3 Lettre choise par le joueur: {}".format(lettreChoisieParLeJoueur))
    if (codeRetour == 1):
        print("Debug4 la lettre {} n'appartient pas au mot. Il vous reste {} coups".format(
            lettreChoisieParLeJoueur, nb_coups))

        nb_coups -= 1
    else:
        i = 0

        for i in indice:
            print("Debug5 La valeur de i est: {}, la lettre du mot recherche est: {}, la lettre choisie par le joueur est: {}".format(
                i, motRecherche[i-1], lettreChoisieParLeJoueur))
            if (motRecherche[i-1] == lettreChoisieParLeJoueur):
                print("Debug6 vous avez trouve la lettre {} longueur du mot recherche {}".format(
                    lettreChoisieParLeJoueur, len(motRecherche)))
                Sequence1 = motInconnu[:i-1]
                Sequence2 = motInconnu[i:]
                print("Debug7: Sequence1: {} + lettreChoisiParLeJoueur: {} + Sequence2: {}".format(Sequence1,
                                                                                                   lettreChoisieParLeJoueur, Sequence2))
                motInconnu = Sequence1 + lettreChoisieParLeJoueur + Sequence2
            i += 1

        print("Debug8: PENDU : {}".format(motInconnu))

"""
        if (nb_coups < 8):
            nb_coups += 1

        print("\n\n\n\n\n")

    
    if (nb_coups > 0):
        lettreChoisieParLeJoueur = input("Choisissez une autre lettre: ")
"""
