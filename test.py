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
