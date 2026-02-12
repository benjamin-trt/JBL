import pygame

def fin(ecran_du_jeu, police_titre, police_texte, NOIR, BLANC):    
    """Cette fonction revoie l'écran affiché à la fin de la partie."""
    ecran_du_jeu.fill(NOIR)
    texte_fin = police_titre.render("COURSE TERMINÉE", True, BLANC)
    texte_retour = police_texte.render("Appuie sur Z pour retourner au menu", True, BLANC)
    texte_sortie = police_texte.render("Appuie sur A pour sortir du jeu", True, BLANC)
    texte_rejouer = police_texte.render("Appuie sur ENTREE pour relancer une partie", True, BLANC)
    ecran_du_jeu.blit(texte_fin, (330, 300))
    ecran_du_jeu.blit(texte_retour, (390, 430))
    ecran_du_jeu.blit(texte_sortie, (390, 470))
    ecran_du_jeu.blit(texte_rejouer, (390, 510))
