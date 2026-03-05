import pygame

def init(x_init, y_init, son_menu):
    """Cette fonction renvoie tout les éléments du jeu qui ne changent pas et qui ont besoin d'être réinitialisés au début de chaque partie."""
    voiture = pygame.Rect(x_init, y_init, 30, 60)
    son_menu.play()
    return voiture
