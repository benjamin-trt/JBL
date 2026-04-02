import pygame

def fin(ecran_du_jeu, police_titre, police_retour, police_sortie, police_rejouer, score, GRIS1, ORANGE, BLANC):    
    """Cette fonction revoie l'écran affiché à la fin de la partie."""
    image_fin = pygame.image.load("images/image_fin.png")
    image_fin = pygame.transform.scale(image_fin, ecran_du_jeu.get_size())
    ecran_du_jeu.blit(image_fin, (0, 0))
    police_titre = pygame.font.SysFont("showcardgothic", 60)
    texte_fin = police_titre.render("COURSE TERMINÉE", True, ORANGE)
    police_retour = pygame.font.SysFont("impact", 25, italic=True)
    police_sortie = pygame.font.SysFont("impact", 25, italic=True)
    police_rejouer = pygame.font.SysFont("impact", 25, italic=True)
    police_texte_score = pygame.font.SysFont("showcardgothic", 70, italic=True)
    texte_retour = police_retour.render("Z : menu", True, BLANC)
    texte_sortie = police_sortie.render("A : quitter", True, BLANC)
    texte_rejouer = police_rejouer.render("ENTREE : rejouer", True, BLANC)
    texte_score = police_texte_score.render(f"Score : {int(score)}", True, GRIS1)
    ecran_du_jeu.blit(texte_fin, (765, 10))
    ecran_du_jeu.blit(texte_sortie, (25, 65))
    ecran_du_jeu.blit(texte_retour, (25, 105))
    ecran_du_jeu.blit(texte_rejouer, (25, 25))
    ecran_du_jeu.blit(texte_score, (350, 700))

