import sys
import pygame
from fonction_ouverture import accueil    # Fonction qui affiche l'écran d'accueil
from fonction_fin import fin              # Fonction qui affiche l'écran de fin
from fonction_initial import init         # Fonction qui initialise la partie

pygame.init()               # Initialisation de pygame
pygame.mixer.init()         # Initialisation du module audio

# Chargement des sons
son_perdu = pygame.mixer.Sound("bruit_fin.wav") 
son_perdu.set_volume(0.5)   # Réglage du volume du son de défaite

son_moteur = pygame.mixer.Sound("bruit_moteur.wav") 
son_moteur.set_volume(0.7)  # Réglage du volume du moteur

son_menu = pygame.mixer.Sound("son_menu.wav") 
son_menu.set_volume(0.7)    # Réglage du volume du menu

# Taille de la fenêtre du jeu
taille_fenetre = (1300, 800)
ecran_du_jeu = pygame.display.set_mode(taille_fenetre)   # Création de la fenêtre
pygame.display.set_caption("Crazy Racer")                # Titre de la fenêtre

# Définition des couleurs
BLEU_CIEL = pygame.Color("deepskyblue2")
BLANC = pygame.Color("white")
NOIR = pygame.Color("black")
GRIS = pygame.Color("gray25")
ROUGE = pygame.Color("red")

# Différentes polices d'écriture
police_titre = pygame.font.SysFont(None, 110)
police_texte = pygame.font.SysFont(None, 50)

# Bouton "Jouer" sur l'écran d'accueil
bouton_jouer = pygame.Rect(525, 460, 250, 90)

# Différents états du jeu
ACCUEIL = 0
JEU = 1
FIN = 2
etat = ACCUEIL                  # État initial du jeu

# Création de la voiture
voiture = pygame.Rect(635, 350, 30, 60)
vitesse = 6                     # Vitesse de déplacement de la voiture par défaut

# Création de la route
route = pygame.Rect(350, 0, 600, 800)

clock = pygame.time.Clock()     # Horloge pour limiter les FPS
en_cours = True                 # Boucle principale
son_perdu_joue = True           # Variable pour gérer le son de défaite

# Définiton des voies de la route
nb_voies = 4
largeur_voie = route.width // nb_voies
route_offset = 0        

while en_cours:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            en_cours = False            # Fermeture de la fenêtre

        if e.type == pygame.MOUSEBUTTONDOWN:
            if etat == ACCUEIL and bouton_jouer.collidepoint(e.pos):
                etat = JEU
                voiture = init(son_menu)     # Lancement du jeu

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_z:
                etat = ACCUEIL          # Retour à l'accueil
            if etat == FIN and e.key == pygame.K_a:
                en_cours = False        # Quitter le jeu
            if etat == FIN and e.key == pygame.K_RETURN:
                etat = JEU
                voiture = init(son_menu)     # Redémarrage après la fin
                    
    touches = pygame.key.get_pressed()

    if etat == JEU:
        
        ecran_du_jeu.fill(BLEU_CIEL)                      # Dessin de la mer
        pygame.draw.rect(ecran_du_jeu, GRIS, route)       # Dessin de la route
        
        # Dessin des lignes de séparation des voies de la route
        for i in range(1, nb_voies):
            x = route.left + i * largeur_voie
            for y in range(-40, 800, 40):
                pygame.draw.rect(ecran_du_jeu, BLANC, (x - 2, y + route_offset, 4, 20))

        # Déplacements de la voiture
        if touches[pygame.K_LEFT]: 
            voiture.x -= vitesse
        if touches[pygame.K_RIGHT]:
            voiture.x += vitesse
        if touches[pygame.K_UP]:
            voiture.y -= vitesse
            son_moteur.play()         # Son du moteur quand accélération
        if touches[pygame.K_DOWN]:
            voiture.y += vitesse

        # Gestion des collisions de la voiture avec les bords de la route
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

        pygame.draw.rect(ecran_du_jeu, ROUGE, voiture)    # Dessin de la voiture       
    
    if etat == ACCUEIL:
        accueil(ecran_du_jeu, police_titre, police_texte,
            NOIR, BLANC, GRIS, bouton_jouer, son_menu)

    elif etat == FIN:
        fin(ecran_du_jeu, police_titre, police_texte, NOIR, BLANC)

    pygame.display.update()  # Mise à jour de l'écran
    clock.tick(60)           # Limitation du jeu à 60 FPS

pygame.quit()   # Fermeture de pygame
sys.exit()      # Fermeture du programme
