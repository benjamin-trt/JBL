import sys
import pygame
from fonction_ouverture import accueil

pygame.init()
pygame.mixer.init()
son_perdu = pygame.mixer.Sound("bruit_fin.wav") 
son_perdu.set_volume(0.5)
son_moteur = pygame.mixer.Sound("bruit_moteur.wav") 
son_moteur.set_volume(0.7)
son_menu = pygame.mixer.Sound("son_menu.wav") 
son_moteur.set_volume(0.7)

taille_fenetre = (1300, 800)
ecran_du_jeu = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Crazy Racer")

BLEU_CIEL = pygame.Color("deepskyblue2")
BLANC = pygame.Color("white")
NOIR = pygame.Color("black")
GRIS = pygame.Color("gray25")
ROUGE = pygame.Color("red")

police_titre = pygame.font.SysFont(None, 110)
police_texte = pygame.font.SysFont(None, 50)

bouton_jouer = pygame.Rect(525, 460, 250, 90)

ACCUEIL = 0
JEU = 1
FIN = 2
etat = ACCUEIL

voiture = pygame.Rect(635, 350, 30, 60)
vitesse = 6

route = pygame.Rect(350, 0, 600, 800)

clock = pygame.time.Clock()
en_cours = True
son_perdu_joue = True

while en_cours:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            en_cours = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            if etat == ACCUEIL and bouton_jouer.collidepoint(e.pos):
                etat = JEU
                voiture.x = 635
                voiture.y = 350
                son_menu.play()

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_z:
                etat = ACCUEIL
            if e.key == pygame.K_a:
                en_cours = FALSE
            if etat == JEU:
                if e.key == pygame.K_ESCAPE:
                    etat = FIN
                    

    touches = pygame.key.get_pressed()

    if etat == JEU:
        if touches[pygame.K_LEFT]:
            voiture.x -= vitesse
        if touches[pygame.K_RIGHT]:
            voiture.x += vitesse
        if touches[pygame.K_UP]:
            voiture.y -= vitesse
            son_moteur.play()
        if touches[pygame.K_DOWN]:
            voiture.y += vitesse

       
        if voiture.left < route.left:
            voiture.left = route.left
            son_perdu.play()
            etat = FIN
        if voiture.right > route.right:
            voiture.right = route.right
            son_perdu.play()
        if voiture.top < route.top:
            son_perdu.play()
            voiture.top = route.top
        if voiture.bottom > route.bottom:
            voiture.bottom = route.bottom
            son_perdu.play()

    if etat == ACCUEIL:
        accueil(ecran_du_jeu, police_titre, police_texte,
            NOIR, BLANC, GRIS, bouton_jouer, son_menu)

    elif etat == JEU:
        ecran_du_jeu.fill(BLEU_CIEL)
        pygame.draw.rect(ecran_du_jeu, GRIS, route)
        pygame.draw.rect(ecran_du_jeu, ROUGE, voiture)

    elif etat == FIN:
        ecran_du_jeu.fill(NOIR)
        texte_fin = police_titre.render("COURSE TERMINÉE", True, BLANC)
        texte_retour = police_texte.render("Appuie sur Z pour retourner au menu", True, BLANC)
        texte_sortie = police_texte.render("Appuie sur a pour sortir du jeu", True, BLANC)
        ecran_du_jeu.blit(texte_fin, (330, 300))
        ecran_du_jeu.blit(texte_retour, (390, 430))
        ecran_du_jeu.blit(texte_sortie, (390, 470))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()

