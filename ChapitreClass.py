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
