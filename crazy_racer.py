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
            if e.key == pygame.K_r :
                couleur_fond = ('red')
            if e.key == pygame.K_b :
                couleur_fond = ('bleu')
            if e.key == pygame.K.backspace :
                couleur_fond = ('aquamarine4')
    ecran_du_jeu.fill(couleur_fond)
    pygame.display.update()


pygame.quit()

sys.exit()





# bonjour, voici une version du code avec plusieurs interactions normalement:
# -si vous cliquez sur la touche r du clavier, le fond deviendra rouge
# -si vous cliquez sur la touche bleu du clavier, le fond deviendra bleu
# -si vous cliquez sur la touche retour arriere du clavier, le fond redeviendra comme avant (vert foncé)
# en classe, la fenêtre s'ouvrait et se fermait sans erreur lorsque l'on appuyait sur la croix en haut à droite
# bon week end
