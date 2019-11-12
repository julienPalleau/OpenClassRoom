numerateur = int(input("saisir un numerateur : "))
denominateur = int(input("saisir un denominateur : "))
try:
    resultat = int(numerateur / denominateur)
except NameError:
    print("Erreur lors de la conversion de l'annee.")
except TypeError:
    print("La variable numerateur ou denominateur possede un type incompatible avec la division")
except ZeroDivisionError:
    print("La variable denominateur est egale a 0.")
else:
    print("numerateur : ", numerateur)
    print("denominateur : ", denominateur)
    print("Le resultat obtenu est", resultat)
