import pygame
from pygame.locals import *

pygame.init()

# Ouverture de la fenetre Pygame
fenetre = pygame.display.set_mode((640, 480))


# Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0, 0))

# Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
perso_x = 0
perso_y = 0
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)
fenetre.blit(perso, (perso_x, perso_y))

# Rafraichissement de l'ecran
pygame.display.flip()

# Boucle infinie
continuer = 1

# Repetition quand on maintient la touche enfoncee
pygame.key.set_repeat(400, 30)

while continuer:
    # On parcours la liste de tous les evenements recus
    for event in pygame.event.get():
        if event.type == QUIT:  # Si un de ces evenenements est de type QUIT
            continuer = 0

        if event.type == KEYDOWN:
            if event.key == K_DOWN:  # Si "fleche bas"
                # On descend le perso
                position_perso = position_perso.move(0, 13)
        if event.type == KEYDOWN:
            if event.key == K_UP:  # Si "fleche bas"
                # On monte le perso
                position_perso = position_perso.move(0, -13)
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:  # Si "fleche bas"
                # On fait aller le perso à droite
                position_perso = position_perso.move(13, 0)
        if event.type == KEYDOWN:
            if event.key == K_LEFT:  # Si "fleche bas"
                # On fait aller le perso à gauche
                position_perso = position_perso.move(-13, 0)

        # Si bouton gauche
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Si clic gauche on change les coordonnees du perso
                perso_x = event.pos[0]
                perso_y = event.pos[1]

        # Si mouvement de la souris
        if event.type == MOUSEMOTION:  # Si mouvement de souris
            # On change les coordonnees du perso
            perso_x = event.pos[0]
            perso_y = event.pos[1]

    # Re-collage clavier
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, position_perso)

    # Re-collage souris
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, (perso_x, perso_y))
    # Rafraichissement
    pygame.display.flip()
