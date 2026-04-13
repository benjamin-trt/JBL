import pygame
def accueil(ecran_du_jeu, police_titre, police_texte, police_texte1, BLANC, BLANC1, GRIS1, INDIGO, ROUGE, GRIS, DORE, bouton_jouer, son_menu, skins, index_skin):
    """Cette fonction renvoie l'écran d'accueil du jeu, et permet au joueur de lancer sa partie."""
    image_accueil = pygame.image.load("images/villevoiture.png")
    image_accueil = pygame.transform.scale(image_accueil, ecran_du_jeu.get_size())
    ecran_du_jeu.blit(image_accueil, (0, 0))
    police_titre = pygame.font.SysFont("showcardgothic", 90)
    titre1 = police_titre.render("CRAZY", True, ROUGE)
    titre2 = police_titre.render("RACER", True, ROUGE)
    police_texte = pygame.font.SysFont("impact", 20, italic=True)
    police_texte1 = pygame.font.SysFont("showcardgothic", 35, bold=False)
    sous_titre = police_texte.render("Test   your   skills   at   high   speed", True, DORE)
    sous_titre = pygame.transform.rotate(sous_titre, -0.5)
    ecran_du_jeu.blit(titre1, (950, 30))
    ecran_du_jeu.blit(titre2, (950, 100))
    ecran_du_jeu.blit(sous_titre, (300, 368))
    pygame.draw.rect(ecran_du_jeu, BLANC1, bouton_jouer, border_radius=10)
    texte_jouer = police_texte1.render("JOUER", True, GRIS)
    ecran_du_jeu.blit(texte_jouer, (bouton_jouer.x + 25, bouton_jouer.y + 25))
    image_preview = pygame.image.load(skins[index_skin]).convert_alpha()
    image_preview = pygame.transform.scale(image_preview, (120, 240))
    ecran_du_jeu.blit(image_preview, (150, 475))
    
    if not son_menu.get_num_channels():
        son_menu.play(-1)
