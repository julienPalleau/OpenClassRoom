import pickle
import os


""" Example d'import d'un fichier ic multipli contenant des informations necessair à l'execution du programme"""
"""
import os
from multipli import *

# test de la fonction table
table(3, 20)
os.system("pause")
"""

""" Creation de listes """
ma_liste = list()  # On cree une liste vide
print(type(ma_liste))
print(ma_liste)

# Vous pouvez faire des listes de toute longeur.
# Les listes peuvent contenir n'importe quel type d'objet
# Les objets dans une liste peuvent etre mis dans un ordre quelconque. Toutefois
# la structure d'une liste fairt que chaque objet a sa place et que l'ordre compte.

ma_liste = [1, 2, 3, 4, 5]  # Une liste avec cinq objets
print(ma_liste)

# nous avons ici une liste contenant quatre
ma_liste = [1, 3.5, "une chaine", []]
# objets de types differents: un entier, un flottant, une chaine de caracteres et... une autre liste.


""" Voyons à present comment acceder aux elements d'une liste """
ma_liste = ['c', 'f', 'm']
print(ma_liste)
ma_liste[0]  # On accede au premier element de la liste 'c'
ma_liste[2]  # Troisieme element 'm'
ma_liste[1] = 'Z'  # On remplace 'f' par 'z'
print(ma_liste)
# contrairement à la classe str, la classe list vous permet de remplacer un element par un autre. les listes sont mutable


""" Inserer des objets dans une liste """
# ajouter un element à la fin de la liste
ma_liste = [1, 2, 3]
ma_liste.append(56)  # On ajoute 56 à la fin de la liste
print(ma_liste)

# Inserer un element dans la liste
ma_liste = ['a', 'b', 'd', 'e']
ma_liste.insert(2, 'c')  # On insere 'c' à l'indice 2
print(ma_liste)

# Concatenation des listes
ma_liste1 = [3, 4, 5]
ma_liste2 = [8, 9, 10]
ma_liste1.extend(ma_liste2)  # On insere ma_liste2 à la fin de ma_liste1
print(ma_liste1)

# il faut re-initialiser ma_liste1 car elle a ete modifier dans l'exemple ci-dessus
ma_liste1 = [3, 4, 5]
ma_liste1 += ma_liste2  # Identique à extend
print(ma_liste1)


""" Suppression d'elements d'une liste """
# Le mot clef del
variable = 34
print(variable)
del variable
# print(variable)

# Del prend en parametre l'indice de l'element à supprimer
ma_liste = [-5, -2, 1, 4, 7, 10]
del ma_liste[0]  # On supprime le premier element de la liste
print(ma_liste)
del ma_liste[2]  # On supprime le troisieme element de la liste
print(ma_liste)

# La methode remove
# Remove prend en parametre l'element à supprimer
ma_liste = [31, 32, 33, 34, 35]
ma_liste.remove(32)
print(ma_liste)


""" Le Parcours de listes """
ma_liste = ['a', 'b', 'd', 'e', 'f', 'g', 'h']
i = 0  # Notre indice pour la boucle while
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1  # On incremente i, ne pas oublier !

# cette methode est cependant preferable
for elt in ma_liste:  # elt va prendre les valeurs successives des elements de ma_liste
    print(elt)

# La fonction enumerate

# Les deux methodes ci-dessus ont chacune leur inconvenient:
#
# La methode utilisant while est plus longue à ecrire,
# moins intuitive et elle est permeable aux boucles infinies,
# si l'on oublie d'incrementer la variable compteur
#
# La methode par for se contente de parcourir la liste en capturant les elemants dans une variable
# sans qu'on puisse savoir ou ils sont dans la liste

for elt in enumerate(ma_liste):
    print(elt)


""" Un petit coup d'oeil aux tuples """
tuple_vide = ()
tuple_non_vide = (1,)  # est equivalent à ci-dessous
tuple_non_vide = 1,
tuple_avec_plusieurs_valeurs = (1, 2, 5)


def decomposer(entier, divise_par):
    """ Cette fonction retourne la partie entiere et le reste de 
    entier / divise_par"""

    p_e = entier // divise_par
    reste = entier % divise_par
    return p_e, reste


partie_entiere, reste = decomposer(20, 3)
print("partie_entiere :{} et reste :{}".format(partie_entiere, reste))


""" Entre chaines et listes """
""" Des chaines aux listes """
ma_chaine = "Bonjour à tous"
# note que dans le cas ou l'on veut spliter sur un espace comme ici, il est possible
print(ma_chaine.split(" "))
# de simmplifier l'ecriture comme suit machaine.split()


""" Des listes aux chaines """
ma_liste = ['Bonjour', 'à', 'tous']
print(" ".join(ma_liste))


""" Une application pratique """


def afficher_flottant(flottant):
    """Fonction prenant en parametre un flottant et renvoyant une chaine de caractere
    representant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum
    de 3 caracters.
    De plus, on va remplacer le point decimal par la virgule """

    if type(flottant) is not float:
        raise TypeError("Le parametre attendu doit etre un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entiere n'est pas à modifier
    # Seule la partie flottante doit etre tronquee
    return ",".join([partie_entiere, partie_flottante[:3]])


print(afficher_flottant(3.9999999999998))


""" Les listes et parametres de fonctions """


def fonction_inconnue(*parametres):
    """Test d'une fonction pouvant etre appelee avec un nombre variable de parametres"""
    print("J'ai recu {}.".format(parametres))


fonction_inconnue()  # On appelle la fonction sans parametre
fonction_inconnue(33)
fonction_inconnue('a', 'e', 'f')
var = 3.5
fonction_inconnue(var, [4], "...")


def afficher(*parametres, sep=' ', fin='\n'):
    """ Fonction chargee de reproduire le comportement de print.
    Elle doit finir par faire appel à print pour afficher le resultat.
    Mais les parametres devront deja avoir ete formates.
    On doit passe à print une unique chaine, en luis specifiant de ne rien mettre à la fin :
     print(chaine,end='')"""

    # Les parametres sont sous la forme d'u tuple
    # Or on a besoin de les convertir
    # Mais on ne peut pas modifier un tuple
    # On a plusieurs possibilites, ici je choisis de convertir le tuple en liste
    parametres = list(parametres)
    # On va commencer par convertir toutes les valeurs en chaine
    # Sinon on va avoir quelques problemes lors du join
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    # La liste des parametres ne contient plus des chaines de caracteres
    # A present on va constituer la chaine finale
    chaine = sep.join(parametres)
    # On ajoute le parametre fin à la fin de la chaine
    chaine += fin
    # On affiche l'ensemble
    print(chaine, end='')


afficher('un', 'deux', 'trois', 'quatre')


""" Les comprehensions de liste """
""" Parcours simple """
liste_origine = [0, 1, 2, 3, 4, 5]
print([nb**2 for nb in liste_origine])


""" Filtrage avec un branchement conditionnel """
liste_origine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([nb for nb in liste_origine if nb % 2 == 0])


""" Melangeons un peu tout cela """
qtt_a_retirer = 7  # On retire chaque semain 7 fruits de chaque sorte
fruits_stockes = [15, 3, 18, 21]  # Par exemple 15 pommes, 3 melons etc...
print([nb_fruits-qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits > qtt_a_retirer])


""" Nouvelle application concrete """
inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]

# On change le sens de l'inventaire, la quantite avant le nom
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit, qtt in inventaire]

# On n'a plus qu'à trier dans l'ordre decroissant l'invantaire inverse
# On reconstitue l'inventaire trie
inventaire = [(nom_fruit, qtt)
              for qtt, nom_fruit in sorted(inventaire_inverse, reverse=True)]
print(inventaire)


""" Exercices """
presences = [
    ("Julien", "present"),
    ("Lucie", "presente"),
    ("Tom", "present"),
    ("Eliott", "present"),
]

for nom, presence in sorted(presences):
    print(nom, presence)

presences = [(nom, presence) for nom, presence in sorted(presences)]
print(presences)

# Creer un Dictionnaire
mon_dictionnaire = {}  # initialisation du dictionnaire
mon_dictionnaire["pseudo"] = "Prolixe"
mon_dictionnaire["mot de passe"] = "*"
mon_dictionnaire["pseudo"] = "6april"  # ecrase la valeur Prolixe
print(mon_dictionnaire)

# Parcourir un dictionnaire
# Parcours des cles
fruits = {"pomme": 21, "melon": 3, "poires": 31}
for cle in fruits.keys():  # methode officiel on utilise la methode keys
    print(cle)

print("\n")

for mot in mon_dictionnaire:  # il est possible aussi de parcourir un dico
                             # via une boucle for classique mais preferer la methode officiel
                             # car on est sure en lisant l'instruction, que c'est la liste des
                             # cles que l'on parcourt
    print(mot)

print("\n")

# Parcours des valeurs
for valeur in fruits.values():
    print(valeur)

if 21 in fruits.values():
    print("Un des fruits se trouve dans la quantite 21.")

# Parcours des cles et des valeurs simultanement
for cle, valeur in fruits.items():
    print("La cle {} contient la valeur {}.".format(cle, valeur))

print("\n")
""" Exercices """
inventaire2 = dict()
inventaire2["isolation sols"] = 50
inventaire2["isolations combles perdus"] = 70
inventaire2["isolation integre"] = 125
inventaire2["isolation murs"] = 120
inventaire2["isolation combles amenages"] = 120
inventaire2["isolation par l'exterieur"] = 120


for cle, valeur in inventaire2.items():
    print("la cle {} contient la valeur {}".format(cle, valeur))


""" Les dictionnaires et parametres de fonction """


def fonction_inconnue2(**parametres_nommes):
    """ Fonction permettant de voir comment recuperer les parametres nommes
    dans un dictionnaire """

    print("J'ai recu en parametre nommes : {}.".format(parametres_nommes))


fonction_inconnue2()  # Aucun parametre
fonction_inconnue2(p=4, j=8)


""" Utilisez des fichiers """
print(os.getcwd())
os.chdir("C:/Users/MOTTIER LUCIE/Documents/GitHub/OpenClassroom")
print(os.getcwd())

""" Lecture d'un fichier """
with open("fichier.txt", "r") as nom_fichier:
    contenu = nom_fichier.read()
    print(contenu)


""" Ecriture dans un fichier """
with open("fichier.txt", "w") as nom_fichier:  # Argh j'ai tout ecrase !
    nom_fichier.write("Second test d'ecriture dans un fichier via Python")

""" Enregistrer des objets dans des fichiers """
score = {
    "Joueur 1": 5,
    "Joueur 2": 35,
    "Joueur 3": 20,
    "Joueur 4": 2,
}

# enregistrement ...
with open('donnees', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)

""" Recuperer nos objets enregistres """
with open('donnees', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()
    print(score_recupere)

# this is a git test
