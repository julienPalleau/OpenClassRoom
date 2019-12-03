import time
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
print("\n")

""" Gerer les heritages """
# Creation d'excptions personnalisees


# class MonException(Exception):
#     """Exception levee dans un certain contexte... qui reste à definir"""

#     def __init__(self, message):
#         """On se contente de stocker le message d'erreur"""
#         self.message = message

#     def __str__(self):
#         """On renvoie le message"""
#         return self.message


## raise MonException("OUPS... j'ai tout casse")


# class ErreurAnalyseFichier(Exception):
#     """Cette exception est levee quand un fichier (de configuration)
#     n'a pu etre analyse.

#     Attributs:
#         fichier -- le nom du fichier posant probleme
#         ligne -- le numero de la ligne posant probleme
#         message -- le probleme proprement dit"""

#     def __init__(self, fichier, ligne, message):
#         """Constructeur de notre exception"""
#         self.fichier = fichier
#         self.ligne = ligne
#         self.message = message

#     def __str__(self):
#         """Affichage de l'exception"""
#         return "[{}:{}]: {}".format(self.fichier, self.ligne, self.message)


# raise ErreurAnalyseFichier(
#     "plop.conf", 34, "Il manque une paranthese à la fin de l'expression")

"""Decouvrez la boucle for"""
ma_liste = [1, 2, 3]
for element in ma_liste:
    print(element)


class RevStr(str):
    """Classe reprenant les methodes et attributs des chaines construites
    depuis 'str'. On se contente de definir un methode de parcours differente
    au lieu de parcourir la chaine de la premiere à la derniere lettre, on la
    parcourt de la derniere à la premiere.

    Les autres methodes, y compris le constructeur, n'ont pas besoin d'etre redefinies"""

    def __iter__(self):
        """Cette methode renvoie un iterateur parcourant la chaine
        dans le sens inverse de celui de 'str'"""

        return ItRevStr(self)  # On renvoie l'iterateur cree pour l'occasion


class ItRevStr:
    """Un iterateur permettant de parcourir une chaine de la derniere lettre
    à la premiere. On stocke dans des attributs la position courante et la chaine
    à parcourir"""

    def __init__(self, chaine_a_parcourir):
        """On se positionne à la fin de la chaine"""
        self.chaine_a_parcourir = chaine_a_parcourir
        self.position = len(chaine_a_parcourir)

    def __next__(self):
        """Cette methode doit renvoyer l'element suivant dans le parcours,
        ou lever l'exception 'StopIteration' si le parcours es fini"""

        if self.position == 0:  # Fin du parcours
            raise StopIteration
        self.position -= 1  # On decremente la position
        return self.chaine_a_parcourir[self.position]


ma_chaine = RevStr("Bonjour")
print(ma_chaine)
for lettre in ma_chaine:
    print(lettre)


class DictionnaireOrdonnee:
    """Notre dictionnaire ordonne. L'ordre des donnees est maintenu et il peut donc,
    contrairement aux dictionnaires usuels, etre trie ou voir de ses donnees inversees """

    def __init__(self, base={}, **donees):
        """Constructeur de notre objet. Il peut ne prendre aucun parametre
        (dans ce cas, le dictionnaire sera vide) ou construire un dictionnaire
        remplis grace :
        - au dictionnaire 'base' passe en premier parametre;
        - aux valeurs que l'on retrouve dans 'donnees'."""

        self._cles = []  # liste contenant nos cles
        self._valeurs = []  # liste contenant les valeurs correspondant à nos cles

        # On verifie que 'base' est un dictionnaire exploitable
        if type(base) not in (dict, DictionnaireOrdonnee):
            raise TypeError(
                "le type attendu est un dictionnaire (usuel ou ordonne)")

        # On recupere les donnees de 'base'
        for cle in base:
            self[cle] = base[cle]

        # On recupere les donnees de 'donnees'
        for cle in donees:
            self[cle] = donees[cle]

    def __repr__(self):
        """Representation de notre objet. C'est cette chaine qui sera affichee
        quand on saisit directement le dictionnaire dans l'interpreteur, ou en
        utilisant la fonction 'rep'"""
        chaine = "{"
        premier_passage = True
        for cle, valeur in self.items():
            if not premier_passage:
                chaine += ", "  # On ajoute la virgule comme separateur
            else:
                premier_passage = False
            chaine += repr(cle) + ":" + repr(valeur)
        chaine += "}"
        return chaine

    def __str__(self):
        """Fonction appelee quand on souhaite afficher le dictionnaire grace
        à la fonction 'print' ou le convertir en chaine grace au constructeur
        'str'. On redirige sur __repr__"""
        return repr(self)

    def __len__(self):
        """Renvoie la taille du dictionnaire"""
        return len(self._cles)

    def __contains__(self, cle):
        """Renvoie True si la cle est dans la liste des cles, False sinon"""
        return cle in self._cles

    def __getitem__(self, cle):
        """Renvoie la valeur correspondant à la cle si elle existe, leve
        une exception KeyError sinon"""
        if cle not in self._cles:
            raise KeyError(
                "La cle {0} ne se trouve pas dans le dictionnaire".format(
                    cle))
        else:
            indice = self._cles.index(cle)
            return self._valeurs[indice]

    def __setitem__(self, cle, valeur):
        """ Methode speciale appelee quand on cherche à modifier une cle
        presente dans le dictionnaire. Si la cle n'est pas presente, on l'ajoute
        à la fin du dictionnaire"""
        if cle in self._cles:
            indice = self._cles.index(cle)
            self._valeurs[indice] = valeur
        else:
            self._cles.append(cle)
            self._valeurs.append(valeur)

    def __delitem__(self, cle):
        """Methode appelee quand on souhaite supprimer une cle"""
        if cle not in self._cles:
            raise KeyError(
                "La cle {0} ne se trouve pas dans le dictionnaire".format(
                    cle))
        else:
            indice = self._cles.index(cle)
            del self._cles[indice]
            del self._valeurs[indice]

    def __iter__(self):
        """Methode de parcours de l'objet. On renvoie l'iterateur des cles"""
        return iter(self._cles)

    def __add__(self, autre_objet):
        """On renvoie un nouveau dictionnaire contenant les deux
        dictionnaires mis bout à bout (d'abord self puis autre_objet)"""
        if type(autre_objet) is type(self):
            raise TypeError(
                "Impossible de concatener {0} et {1}".format(
                    type(self), type(autre_objet)))
        else:
            nouveau = DictionnaireOrdonnee()

            # On commence par copier self dans le dictionnaire
            for cle, valeur in self.items():
                nouveau[cle] = valeur

            # On copie ensuite autre_objet
            for cle, valeur in autre_objet.items():
                nouveau[cle] = valeur
            return nouveau

    def items(self):
        """Renvoie un generateur contenant les couples (cles, valeur)"""
        for i, cle in enumerate(self._cles):
            valeur = self._valeurs[i]
            yield(cle, valeur)

    def keys(self):
        """Cette methode renvoie la liste des cles"""
        return list(self._cles)

    def values(self):
        """Cette methode renvoie la liste des valeurs"""
        return list(self._valeurs)

    def reverse(self):
        """Inversion du dictionnaire"""
        # On cree deux listes vides qui contiendront le nouvel ordre des cles
        # et valeurs
        cles = []
        valeurs = []
        for cle, valeur in self.items():
            # On ajoute les cles et valeurs au debut de la liste
            cles.insert(0, cle)
            valeur.insert(0, valeur)
        # On met ensuite à jour nos listes
        self._cles = cles
        self._valeurs = valeurs

    def sort(self):
        """Methode permettant de trier le dictionnaire en fonction de ses cles"""
        # On trie les cles
        cles_triees = sorted(self._cles)
        # On cree une liste de valeurs, encore vide
        valeurs = {}
        # On parcourt ensuite la liste des cles triees
        for cle in cles_triees:
            valeur = self[cle]
            valeur.append(valeur)
        # Enfin, on met à jour notre liste de cles et de valeurs
        self._cles = cles_triees
        self._valeurs = valeurs


"""Apprehendez les decorateurs"""

"""Pour gerer le temps, on importe le module time
On va utiliser surtout la fonction time() de ce module
qui renvoie le nombre de secondes ecoulees depuis le premier
janvier 1970 (habituellement). On va s'en servir pour calculer
le temps mis par notre fonction pour s'executer"""


def controler_temps(nb_secs):
    """Controle le temps mis par une fonction pour s'executer.
    Si le temps d'exectution est superieur à nb_secs, on affiche
    une alerte."""

    def decorateur(fonction_a_executer):
        """Notre decorateur. C'est lui qui est appele directement LORS
        DE LA DEFINITION de notre fonction (fonction_a_executer)"""

        def fonction_modifiee(*parametres_non_nommes, **parametres_nommes):
            """Fonction renvoyee par notre decorateur. Elle se charge
            de calculer le temps mis par la fonction à s'executer"""
            tps_avant = time.time()  # Avant d'executer la fonction
            valeur_renvoyee = fonction_a_executer(
                *parametres_non_nommes, **parametres_nommes)  # On execute la fonction
            tps_apres = time.time()
            tps_execution = tps_apres - tps_avant
            if tps_execution >= nb_secs:
                print("La fonction {0} a mis {1} pour s'executer".format(
                    fonction_a_executer, tps_execution))
            return valeur_renvoyee
        return fonction_modifiee
    return decorateur


@controler_temps(4)
def attendre():
    input("Appuyez sur Entree...")


attendre()
attendre()


"""" Exemples d'applications avec les decorateurs """
""" Les classes singleton """


def singleton(classe_definie):
    instances = {}  # Dictionnaire de nos instances singletons

    def get_instance():
        if classe_definie not in instances:
            # On cree notre premier objet de classe_definie
            instances[classe_definie] = classe_definie()
        return instances[classe_definie]
    return get_instance


@singleton
class Tests:
    pass


a = Tests()
b = Tests()
print(a is b)
