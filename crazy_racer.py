import sys
import pygame

pygame.init()

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

while en_cours:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            en_cours = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            if etat == ACCUEIL and bouton_jouer.collidepoint(e.pos):
                etat = JEU
                voiture.x = 635
                voiture.y = 350

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_z:
                etat = ACCUEIL

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
        if touches[pygame.K_DOWN]:
            voiture.y += vitesse

       
        if voiture.left < route.left:
            voiture.left = route.left
        if voiture.right > route.right:
            voiture.right = route.right
        if voiture.top < route.top:
            voiture.top = route.top
        if voiture.bottom > route.bottom:
            voiture.bottom = route.bottom

    if etat == ACCUEIL:
        ecran_du_jeu.fill(NOIR)
        titre = police_titre.render("CRAZY RACER", True, BLANC)
        sous_titre = police_texte.render("Test your skills at high speed", True, BLANC)
        ecran_du_jeu.blit(titre, (380, 260))
        ecran_du_jeu.blit(sous_titre, (420, 360))
        pygame.draw.rect(ecran_du_jeu, GRIS, bouton_jouer, border_radius=12)
        texte_jouer = police_texte.render("JOUER", True, BLANC)
        ecran_du_jeu.blit(texte_jouer, (bouton_jouer.x + 75, bouton_jouer.y + 25))

    elif etat == JEU:
        ecran_du_jeu.fill(BLEU_CIEL)
        pygame.draw.rect(ecran_du_jeu, GRIS, route)
        pygame.draw.rect(ecran_du_jeu, ROUGE, voiture)

    elif etat == FIN:
        ecran_du_jeu.fill(NOIR)
        texte_fin = police_titre.render("COURSE TERMINÉE", True, BLANC)
        texte_retour = police_texte.render("Appuie sur Z pour retourner au menu", True, BLANC)
        ecran_du_jeu.blit(texte_fin, (330, 300))
        ecran_du_jeu.blit(texte_retour, (390, 430))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
