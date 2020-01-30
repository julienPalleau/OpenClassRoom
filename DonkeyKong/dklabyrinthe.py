"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit deplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""

import pygame
from pygame.locals import *
from classes import *
from constantes import *

pygame.init()


# Ouverture de la fenetre Pygame
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

# Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

# Titre
pygame.display.set_caption(titre_fenetre)


# Boucle principale
continuer = 1
while continuer:
    # Chargement et affichage de l'ecran d'acceuil
    acceuil = pygame.image.load(image_acceuil).convert()
    fenetre.blit(acceuil, (0, 0))

    # Rafraichissement de l'ecran
    pygame.display.flip()

    # On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1

    # Boucle d'accueil
    while continuer_accueil:
        # Limitation de vitesse de la boucle
        # 30 frames par secondes suffisent
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # Si l'utilisateur quitte, on met les variables
            # de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                # variable de choix du niveau
                choix = 0

            elif event.type == KEYDOWN:
                # Lancement du niveau 1
                if event.key == K_F1:
                    continuer_accueil = 0  # On quitte l'accueil
                    choix = 'n1'  # On definit le niveau à charger
                # lancement du niveau 2
                elif event.key == K_F2:
                    continuer_accueil = 0
                    choix = 'n2'

    # On verifie que le joueur a bien fait un choix de niveau
    # pour ne pas charger s'il quitte
    if choix != 0:
        # Chargement du fond
        fond = pygame.image.load(image_fond).convert()

        # Generation d'un niveau à partir d'un fichier
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(fenetre)

        # Creation de Donkey Kong
        dk = Perso("images/dk_droite.png", "images/dk_gauche.png",
                   "images/dk_haut.png", "images/dk_bas.png", niveau)

    # BOUCLE JEUX
    while continuer_jeu:

        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # Si l'utilisateur quitte, on met la variable qui continue le jeu
            # Et la variable generale à 0 pour fermer la fenetre
            if event.type == QUIT:
                continue_jeu = 0
                continuer = 0

            elif event.type == KEYDOWN:
                # Si l'utilisateur presse Echap ici, on revient seulement au menu
                if event.key == K_ESCAPE:
                    continuer_jeu = 0

            # Touches de deplacement de Donkey Kong
            elif event.key == K_RIGHT:
                dk.deplacer('droite')
            elif event.key == K_LEFT:
                dk.deplacer('gauche')
            elif event.key == K_UP:
                dk.deplacer('haut')
            elif event.key == K_DOWN:
                dk.deplacer('bas')

        # Affichages aux nouvelles positions
        fenetre.blit(fond, (0, 0))
        niveau.afficher(fenetre)
        # dk.direction = l'image dans la bonne direction
        fenetre.blit(dk.direction, (dk.x, dk.y))
        pygame.display.flip()

        # Victoire -> Retour à l'acceuil
        if niveau.structure[dk.case_y][dk.case_x] == 'a':
            continuer_jeu = 0
