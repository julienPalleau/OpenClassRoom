from operator import itemgetter, attrgetter


class Personne:
    """Classe definissant une personne caracterisee par :
    - son nom
    - son prenom
    - son age
    - son lieu de residence"""
    print("Class Personne")

    def __init__(self, nom, prenom):  # Notre methode constructeur
        """Constructeur de notre classe. Chaque attribut va etre instancie
                avec une valeur par defaut... original"""

        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self.lieu_residence = "Nice"

    def _get_lieu_residence(self):
        """Methode qui sera appelee quand on souhaitera acceder en lecture a l'attribut 'lieu_residence'"""
        print("On accede à l'attribut lieu_residence !")
        return self._lieu_residence

    def _set_lieu_residence(self, nouvelle_residence):
        """Methode appelee quand on souhaite modifier le lieu de residence"""
        # print("Attention, il semble que {} demenage à {}.".format(
        #    self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence

    # On va dire à Python que notre attribut lieu_residence pointe vers une propriete
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)


jean = Personne("Micado", "Jean")
# print(jean.nom)
# print(jean.prenom)
# print(jean.age)
# print(jean.lieu_residence)
jean.lieu_residence = "Berlin"
print(jean.lieu_residence)
print("\n")


class Compteur:
    """Cette classe possede un attribut de classe qui s'incremente à chaque fois que l'on cree un objet de ce type"""
    print("Class Compteur")

    objets_crees = 0  # Le compteur vaut 0 au depart

    # methode d'instance
    def __init__(self):
        """A chaque fois qu'on cree un objet, on incremente le compteur"""
        Compteur.objets_crees += 1

    # methode de classe
    def combien(cls):
        """ Methode de classe affichant combien d'objet ont ette crees"""
        print("Jusqua'à present, {} objets ont ete crees".format(cls.objets_crees))
    combien = classmethod(combien)

# methode statique


class Test:
    """Une classe de test tout simplement """
    def afficher():
        """Fonction chargee d'afficher quelque chose"""
        print("On affiche la meme chose.")
        print("peu importe les donnees de l'objet ou de la classe.")
    afficher = staticmethod(afficher)


print(Compteur.objets_crees)
a = Compteur()  # On cree un premier objet
print(Compteur.objets_crees)
b = Compteur()  # On cree un second objet
print(Compteur.objets_crees)
print("\n")

Compteur.combien()
a = Compteur()
Compteur.combien()
b = Compteur()
Compteur.combien()
print("\n")

Test.afficher()
print("\n")


class TableauNoir:
    """Classe definissant une surface sur laquelle on peut ecrire,
    que l'on peut lire et effacer, par jeu de methodes. L'attribut modifie
    est 'surface'"""
    print("Classe TableauNoir")

    def __init__(self):
        """Par defaut, notre surface est vide"""
        self.surface = ""

    def ecrire(self, message_a_ecrire):
        """Methode permettant d'ecrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à ecrire"""

        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

    def lire(self):
        """Cette methode se charge d'afficher, grace à print,
        la surface du tableau"""
        print(self.surface)

    def effacer(self):
        """Cette methode permet d'effacer la surface du tableau"""
        self.surface = ""


tab = TableauNoir()
tab.lire()
tab.ecrire("Salut tout le monde")
tab.ecrire("La forme ?")
tab.lire()
tab.effacer()
tab.lire()

# Les methodes mathematiques


class Duree:
    """Classe contenant des durees sous la forme d'un nombre de minutes et de secondes"""

    def __init__(self, min=0, sec=0):
        """Constructeur de la classe"""
        self.min = min  # Nombre de minutes
        self.sec = sec  # Nombre de secondes

    def __str__(self):
        """Affichage un peu plus joli de nos objets"""
        return "{0:02}:{1:02}".format(self.min, self.sec)

    def __add__(self, objet_a_ajouter):
        """L'objet à ajouter est un entier, le nombre de secondes"""
        nouvelle_duree = Duree()
        # On va copier self dans l'objet créé pour avoir la même durée
        nouvelle_duree.min = self.min
        nouvelle_duree.sec = self.sec
        # On ajoute la durée
        nouvelle_duree.sec += objet_a_ajouter

        # Si le nombre de secondes >= 60
        if nouvelle_duree.sec >= 60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60

        # On renvoie la nouvelle durée
        return nouvelle_duree


d1 = Duree(12, 8)
print(d1)
d2 = d1 + 54
print(d2)

d1 = Duree(3, 5)
print(d1)

""" Appliquez deux methodes de tri en Python """
""" Premiere approche du tri """
prenom = ["Jacques", "Laure", "Andre", "Victoire", "Albert", "Sophie"]
print("on trie aver sorted")
print(sorted(prenom))  # sorted renvoir la liste trie
print(prenom)  # prenom n'a pas ete modifie

print("\n")

print("On trie avec sort")
print(prenom.sort())  # prenom.sort ne renvoie rien contrairement a sorted(prenom)
prenom.sort()  # trie la liste
print(prenom)  # la liste triee est re-affecte dans prenom donc prenom est modifie !

print("\n")

""" Trier avec des cles precises, cela se fait avec une fonction lambda """
etudiants = [
    ("Clement", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15)
]
print("On trie sur sur les moyennes (dernier colonnes) avec une fonction lambda")
print(sorted(etudiants, key=lambda colonnes: colonnes[2]))
print("\n")


""" Trier une liste d'objets """


class Etudiant:
    """ Classe representant un etudiant.

    On represente un etudiant par son prenom (attribut prenom), son age (attribut age)
    et sa note moyenne (attribut moyenne, entre 0 et 20)

    Parametres du constructeur :
        Prenom -- le prenom de l'etudiant
        age -- l'age de l'etudiant
        moyenne -- la moyenne de l'etudiant
    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Etudiant {} (age={}, moyenne={})>".format(self.prenom, self.age, self.moyenne)


etudiants = [
    Etudiant("Clements", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]

print("On trie sur une liste d'objets sur la moyenne (dernier colonne)")
print(sorted(etudiants, key=lambda etudiant: etudiant.moyenne))
print("\n")

""" Trier dans l'ordre inverse """
print("On trie sur une liste d'objets sur l'age en ordre decroissant")
print(sorted(etudiants, key=lambda etudiant: etudiant.age, reverse=True))

print("\n")

""" Plus rapide et plus efficace """
""" Trier une liste d'objets """
print("Trie la moyenne avec une liste d'objets avec attrgetter:")
print(sorted(etudiants, key=attrgetter("moyenne")))

print("\n")

""" Trier selon plusieurs criteres """
print("trier selon plusieurs criteres ici age et moyenne :")
print(sorted(etudiants, key=attrgetter("age", "moyenne")))

print("\n")

""" Trier une liste de tuples """
etudiants = [
    ("Clements", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]
# Si on veut trier par moyenne ascendante, nous avons vu qu'il suffisait de faire:
# sorted(etudiants, key=lambda etudiant: etudiant[2])
# pour faire la meme chose sans fonction lambda, avec la fonction itemgetter du
# module operator:
print("Trie la moyenne via une liste de tuples avec itemgetter :")
print(sorted(etudiants, key=itemgetter(2)))

print("\n")

""" Chainage de tris """


class LigneInventaire:

    """ Classe representant une ligne d'un inventaire de vente.

    Attributs attendus par le constructeur :
        produit -- le nom du produit
        prix -- le prix unitaire du produit
        quantite -- la quantite vendue du produit

    """

    def __init__(self, produit, prix, quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        return "<ligne d'inventaire {} ({}X{})>".format(self.produit, self.prix, self.quantite)


# Creation de l'inventaire
inventaire = [
    LigneInventaire("pomme rouge", 1.2, 19),
    LigneInventaire("orange", 1.4, 24),
    LigneInventaire("banane", 0.9, 21),
    LigneInventaire("poire", 1.2, 24),
]

# On veut trier cette liste par prix et par quantite
print("Trie de la liste par prix et par quantite:")
print(sorted(inventaire, key=attrgetter("prix", "quantite")))
