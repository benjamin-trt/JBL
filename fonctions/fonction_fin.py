import pygame

def fin(ecran_du_jeu, police_titre, police_retour, police_sortie, police_rejouer, GRIS1, ORANGE, BLANC):    
    """Cette fonction revoie l'écran affiché à la fin de la partie."""
    image_fin = pygame.image.load("images/image_fin.png")
    image_fin = pygame.transform.scale(image_fin, ecran_du_jeu.get_size())
    ecran_du_jeu.blit(image_fin, (0, 0))
    police_titre = pygame.font.SysFont("showcardgothic", 60)
    texte_fin = police_titre.render("COURSE TERMINÉE", True, ORANGE)
    police_retour = pygame.font.SysFont("impact", 25, italic=True)
    police_sortie = pygame.font.SysFont("impact", 25, italic=True)
    police_rejouer = pygame.font.SysFont("impact", 25, italic=True)
    texte_retour = police_retour.render("Z : menu", True, GRIS1)
    texte_sortie = police_sortie.render("A : quitter", True, GRIS1)
    texte_rejouer = police_rejouer.render("ENTREE : rejouer", True, GRIS1)
    ecran_du_jeu.blit(texte_fin, (765, 10))
    ecran_du_jeu.blit(texte_retour, (400, 700))
    ecran_du_jeu.blit(texte_sortie, (400, 650))
    ecran_du_jeu.blit(texte_rejouer, (400, 750))


    #image_accueil = pygame.image.load("images/villevoiture.png")
   #image_accueil = pygame.transform.scale(image_accueil, ecran_du_jeu.get_size())
    #ecran_du_jeu.blit(image_accueil, (0, 0))
    #police_titre = pygame.font.SysFont("showcardgothic", 90)
    #titre1 = police_titre.render("CRAZY", True, ROUGE)
    ##titre2 = police_titre.render("RACER", True, ROUGE)
    #police_texte = pygame.font.SysFont("impact", 20, italic=True)
    #police_texte1 = pygame.font.SysFont("showcardgothic", 35, bold=False)
    #sous_titre = police_texte.render("Test   your   skills   at   high   speed", True, DORE)
    #sous_titre = pygame.transform.rotate(sous_titre, -0.5)
