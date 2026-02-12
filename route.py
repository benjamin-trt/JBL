import pygame
import sys

# Initialisation de pygame
pygame.init()

# Taille de la fenêtre
LARGEUR = 1000
HAUTEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Route en pygame")

# Couleurs
VERT = (0, 150, 0)      # herbe
GRIS = (80, 80, 80)     # route
BLANC = (255, 255, 255) # lignes

# Route
largeur_route = 400
x_route = (LARGEUR - largeur_route) // 2
en_cours = True

# Boucle principale
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Fond (herbe)
    fenetre.fill("deepskyblue2")

    # Dessin de la route
    pygame.draw.rect(
        fenetre,
        GRIS,
        (x_route, 0, largeur_route, HAUTEUR)
    )

    # Lignes blanches (séparation des voies)
    largeur_ligne = 5
    espace = largeur_route // 3

    for i in range(1, 3):
        x_ligne = x_route + i * espace
        pygame.draw.line(
            fenetre,
            BLANC,
            (x_ligne, 0),
            (x_ligne, HAUTEUR),
            largeur_ligne
        )

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()