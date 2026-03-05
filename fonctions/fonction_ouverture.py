import pygame

def accueil(image_accueil, ecran_du_jeu, police_titre, police_texte, BLANC, GRIS, bouton_jouer, son_menu):
    """Cette fonction renvoie l'écran d'accueil du jeu, et permet au joueur de lancer sa partie."""
    image_accueil = pygame.image.load("images/coucher_de_soleil.png")
    image_accueil = pygame.transform.scale(image_accueil, ecran_du_jeu.get_size())
    ecran_du_jeu.blit(image_accueil, (0, 0))
    titre = police_titre.render("CRAZY RACER", True, BLANC)
    sous_titre = police_texte.render("Test your skills at high speed", True, BLANC)
    ecran_du_jeu.blit(titre, (380, 260))
    ecran_du_jeu.blit(sous_titre, (420, 360))
    pygame.draw.rect(ecran_du_jeu, GRIS, bouton_jouer, border_radius=12)
    texte_jouer = police_texte.render("JOUER", True, BLANC)
    ecran_du_jeu.blit(texte_jouer, (bouton_jouer.x + 75, bouton_jouer.y + 25))
    if not son_menu.get_num_channels():
        son_menu.play(-1)
