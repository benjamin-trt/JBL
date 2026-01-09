import sys
import pygame

pygame.init()
taille_fenetre = (1300,800)
ecran_du_jeu = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Crazy Racer")
couleur_fond = ('aquamarine4')
debut_jeu = True

while debut_jeu == True :
    evenement = pygame.event.get()
    for e in evenement :
        if e.type == pygame.QUIT :
            debut_jeu = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                couleur_fond = ('red')
            if e.key == pygame.K_b:
                couleur_fond = ('bleu')
            if e.key == pygame.K.backspace:
                couleur_fond = ('aquamarine4')
    ecran_du_jeu.fill(couleur_fond)
    pygame.display.update()



pygame.quit()
sys.exit()