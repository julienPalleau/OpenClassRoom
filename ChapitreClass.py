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


bernard = Personne("Micado", "Bernard")
print(bernard.nom)
print(bernard.prenom)
print(bernard.age)


class Compteur:
    """Cette classe possede un attribut de classe qui s'incremente à chaque fois que l'on cree un objet de ce type"""
    print("Class Compteur")

    objets_crees = 0  # Le compteur vaut 0 au depart

    def __init__(self):
        """A chaque fois qu'on cree un objet, on incremente le compteur"""
        Compteur.objets_crees += 1


print(Compteur.objets_crees)
a = Compteur()  # On cree un premier objet
print(Compteur.objets_crees)
b = Compteur()  # On cree un second objet
print(Compteur.objets_crees)


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
