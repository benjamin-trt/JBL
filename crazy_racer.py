import sys
import pygame
import random
from fonctions.fonction_ouverture import accueil    # Fonction qui affiche l'écran d'accueil
from fonctions.fonction_fin import fin              # Fonction qui affiche l'écran de fin
from fonctions.fonction_initial import init         # Fonction qui initialise la partie

pygame.init()               # Initialisation de pygame
pygame.mixer.init()         # Initialisation du module audio

# Chargement des sons
son_perdu = pygame.mixer.Sound("sons/crash_voiture.wav") 
son_perdu.set_volume(0.5)   # Réglage du volume du son de défaite

son_moteur = pygame.mixer.Sound("sons/son_voiture.wav") 
son_moteur.set_volume(0.7)  # Réglage du volume du moteur

son_menu = pygame.mixer.Sound("sons/son_menu2.wav") 
son_menu.set_volume(0.7)    # Réglage du volume du menu

son_fin = pygame.mixer.Sound("sons/bruit_fin1.wav")
son_fin.set_volume(0.7)     # Réglage du volume du son de fin

moteur_en_cours = False     
son_defaite = False
channel_perdu = pygame.mixer.Channel(1)

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
VIOLET = pygame.Color("violet")
DORE = pygame.Color("gold") 
INDIGO = pygame.Color("indigo")
GRIS1 = pygame.Color("lavenderblush4")
BLANC1 = pygame.Color("grey70")
ORANGE = pygame.Color("orange2")

# Différentes polices d'écriture
police_titre = pygame.font.SysFont(None, 110)
police_texte = pygame.font.SysFont(None, 50)
police_texte1 = pygame.font.SysFont(None, 40)
police_retour = pygame.font.SysFont(None, 150)
police_sortie = pygame.font.SysFont(None, 25)
police_rejouer = pygame.font.SysFont(None, 25)
police_texte_score = pygame.font.SysFont(None, 25)

# Bouton "Jouer" sur l'écran d'accueil
bouton_jouer = pygame.Rect(400, 700, 150, 75)


# Différents états du jeu
ACCUEIL = 0
JEU = 1
FIN = 2
etat = ACCUEIL                  # État initial du jeu

# Création de la voiture et de la mer
image_mer = pygame.image.load("images/mer_nsi.png")
image_voiture_originale = pygame.image.load("images/voiture_nsi.png").convert_alpha()
image_adverse_originale = pygame.image.load("images/voiture_adverse_nsi.png").convert_alpha()
image_voiture = pygame.transform.smoothscale(
    image_voiture_originale, (int(image_voiture_originale.get_width() * 0.30), int(image_voiture_originale.get_height() * 0.30))
)
mask_voiture = pygame.mask.from_surface(image_voiture)
image_voiture_adverse = pygame.transform.smoothscale(
    image_adverse_originale, (int(image_adverse_originale.get_width() * 0.30), int(image_adverse_originale.get_height() * 0.30))
)
mask_adverse = pygame.mask.from_surface(image_voiture_adverse)

voiture_init_x = 685
voiture_init_y = 500
voiture = image_voiture.get_rect()
hitbox_voiture = pygame.Rect(voiture_init_x + 20, voiture_init_y + 10, 60, 150)
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
mer_offset = 0

centres_voies = [
    route.left + largeur_voie // 2 + i*largeur_voie
    for i in range(nb_voies)
]

voitures_adverses = []
largeur_voiture = 40
hauteur_voiture = 70
compteur_spawn = 0
delai_spawn = random.randint(50, 80)
vitesse_adversaires = 5
vitesse_cible = 2
vitesse_max = 15
acceleration = 0.05

# Création du bouclier
image_bouclier_original = pygame.image.load("images/bouclier_nsi.png").convert_alpha()
largeur_bouclier = int(largeur_voie * 0.5)
hauteur_bouclier = int(largeur_bouclier * 1)
image_bouclier = pygame.transform.smoothscale(image_bouclier_original, (largeur_bouclier, hauteur_bouclier))
 
powerups = []
compteur_powerup = 0
delai_powerup = 300

bouclier_actif = False
temps_bouclier = 0
DUREE_BOUCLIER = 3000


# Compteurs
temps_debut = pygame.time.get_ticks()
distance = 0
score = 0

while en_cours:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            en_cours = False            # Fermeture de la fenêtre

        if e.type == pygame.MOUSEBUTTONDOWN:
            if etat == ACCUEIL and bouton_jouer.collidepoint(e.pos):
                etat = JEU
                voiture = init(voiture_init_x, voiture_init_y, son_menu)     # Lancement du jeu

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_z:
                etat = ACCUEIL          # Retour à l'accueil
            if etat == FIN and e.key == pygame.K_a:
                en_cours = False        # Quitter le jeu
            if etat == FIN and e.key == pygame.K_RETURN:
                etat = JEU
                voiture = init(voiture_init_x, voiture_init_y, son_menu)
                voitures_adverses.clear()
                compteur_spawn = 0
                vitesse_adversaires = 5
                vitesse_cible = 2
                son_perdu.stop()
                son_defaite = False
                temps_debut = pygame.time.get_ticks()
                distance = 0 
                score = 0  
                    
    touches = pygame.key.get_pressed()

    if etat == JEU:
        
        largeur_mer_gauche = route.left
        largeur_mer_droite = 1300 - route.right

        image_mer_gauche = pygame.transform.scale(image_mer, (largeur_mer_gauche, 800))
        image_mer_droite = pygame.transform.scale(image_mer, (largeur_mer_droite, 800))
        mer_offset += vitesse_adversaires
        ecran_du_jeu.blit(image_mer_gauche, (0, mer_offset % 800 - 800))
        ecran_du_jeu.blit(image_mer_gauche, (0, mer_offset % 800))

        ecran_du_jeu.blit(image_mer_droite, (route.right, mer_offset % 800 - 800))
        ecran_du_jeu.blit(image_mer_droite, (route.right, mer_offset % 800))
        pygame.draw.rect(ecran_du_jeu, GRIS, route)       # Dessin de la route
        
        compteur_spawn += 1
        compteur_powerup += 1

        temps = (pygame.time.get_ticks() - temps_debut) // 1000
        distance += vitesse_cible / 15

        son_menu.stop() 

        if vitesse_cible >8:
            score += vitesse_cible*distance / 1000

        if compteur_spawn >= delai_spawn:
            # Nombre de voitures à créer
            nb_voitures_spawn = random.randint(1, 2)

            for _ in range(nb_voitures_spawn):
                voie = random.randint(0, nb_voies - 1)
                x = centres_voies[voie] - image_voiture_adverse.get_width() // 2

                rect = image_voiture_adverse.get_rect()
                rect.x = x
                rect.y = -rect.height 
                voitures_adverses.append(rect)
            # Nouveau délai aléatoire à chaque spawn
            delai_spawn = random.randint(50, 80)
            compteur_spawn = 0

        # Spawn des boucliers
        if compteur_powerup >= delai_powerup:
            voies_libres = []
            for i in range(nb_voies):
                libre = True
                for v in voitures_adverses:
                    voie_v = (v.centerx - route.left) // largeur_voie
                    if voie_v == i and v.y < 200:
                        libre = False
                if libre:
                    voies_libres.append(i)

            if voies_libres:
                voie = random.choice(voies_libres)
                rect = image_bouclier.get_rect()
                rect.centerx = centres_voies[voie]
                rect.y = -rect.height
                powerups.append(rect)

            compteur_powerup = 0

        # Dessin des lignes de séparation des voies de la route
        route_offset += vitesse_adversaires
        route_offset %= 40
        for i in range(1, nb_voies):
            x = route.left + i * largeur_voie
            for y in range(-40, 800, 40):
                pygame.draw.rect(ecran_du_jeu, BLANC, (x - 2, y + route_offset, 4, 20))

        if touches[pygame.K_UP]:
            vitesse_cible = min(vitesse_cible + 0.3, vitesse_max)
            if not moteur_en_cours:
                son_moteur.play(-1)  
                moteur_en_cours = True
        else:
            vitesse_cible = max(vitesse_cible - 0.1, 6)
            if moteur_en_cours:
                son_moteur.stop()
                moteur_en_cours = False

        vitesse_adversaires += (vitesse_cible - vitesse_adversaires) * acceleration

        # Déplacement et affichage des voitures adverses
        for rect in voitures_adverses[:]:
            rect.y += vitesse_adversaires   # vitesse des adversaires
            offset = (rect.x - voiture.x, rect.y - voiture.y) 

            if rect.bottom < 0:
                voitures_adverses.remove(rect)

            if mask_voiture.overlap(mask_adverse, offset):
                if bouclier_actif:
                    voitures_adverses.remove(rect)
                    bouclier_actif = False
                    
                else:
                    if not son_defaite:
                        channel_perdu.play(son_perdu)
                        son_defaite = True
                        son_moteur.stop()
                    etat = FIN

            ecran_du_jeu.blit(image_voiture_adverse, rect)

        for p in powerups[:]:
            p.y += vitesse_adversaires
            if p.top > 800:
                powerups.remove(p)
            if hitbox_voiture.colliderect(p):
                    bouclier_actif = True
                    temps_bouclier = pygame.time.get_ticks()
                    powerups.remove(p)

            ecran_du_jeu.blit(image_bouclier, p)

        if bouclier_actif and pygame.time.get_ticks() - temps_bouclier > DUREE_BOUCLIER:
            bouclier_actif = False

        # Affichage des compteurs 
        police_texte_temps = pygame.font.SysFont("impact", 30)
        police_texte_distance = pygame.font.SysFont("impact", 30)
        police_texte_vitesse = pygame.font.SysFont("impact", 30)
        police_texte_score = pygame.font.SysFont("impact", 30)
        texte_temps = police_texte_temps.render(f"Temps : {temps}s", True, BLANC)
        texte_distance = police_texte_distance.render(f"Distance : {int(distance)} m", True, BLANC)
        texte_vitesse = police_texte_vitesse.render(f"Vitesse : {int(vitesse_cible)*10} km/h", True, BLANC)
        texte_score = police_texte_score.render(f"Score : {int(score)}", True, BLANC)
        if bouclier_actif:
            police_texte_bouclier = pygame.font.SysFont("impact", 30)
            texte_bouclier = police_texte_bouclier.render("Bouclier actif", True, DORE)
            ecran_du_jeu.blit(texte_bouclier, (1000, 180))
        ecran_du_jeu.blit(texte_temps, (1000, 20))
        ecran_du_jeu.blit(texte_distance, (1000, 60))
        ecran_du_jeu.blit(texte_vitesse, (1000, 100))
        ecran_du_jeu.blit(texte_score, (1000, 140))

        # Déplacement de la voiture
        if touches[pygame.K_LEFT]:
            voiture.x -= vitesse
        if touches[pygame.K_RIGHT]:
            voiture.x += vitesse

        #Rester dans la route
        voiture.x = max(route.left, min(voiture.x, route.right - image_voiture.get_width()))
        

        hitbox_voiture.x = max(route.left, min(hitbox_voiture.x, route.right - image_voiture.get_width()))
# Mettre à jour la hitbox
        hitbox_voiture.x = voiture.x + 14
        hitbox_voiture.y = voiture.y + 10
        # Dessin
        ecran_du_jeu.blit(image_voiture, voiture)

    
    if etat == ACCUEIL:
        if not pygame.mixer.get_busy():
            son_menu.play(-1)
        accueil(ecran_du_jeu, police_titre, police_texte, police_texte1, BLANC, BLANC1, GRIS1, INDIGO, ROUGE, GRIS, DORE, bouton_jouer, son_menu)

    elif etat == FIN:
        if son_defaite and not channel_perdu.get_busy():
            channel_perdu.play(son_fin)
            son_defaite = False
        fin(ecran_du_jeu, police_titre, police_retour, police_sortie, police_rejouer, score, GRIS1, ORANGE, BLANC)
    
    pygame.display.update()  # Mise à jour de l'écran
    clock.tick(60)           # Limitation du jeu à 60 FPS

pygame.quit()   # Fermeture de pygame
sys.exit()      # Fermeture du programme
