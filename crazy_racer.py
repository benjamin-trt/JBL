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
son_menu.set_volume(0.99)    # Réglage du volume du menu

son_fin = pygame.mixer.Sound("sons/bruit_fin1.wav")
son_fin.set_volume(0.3)     # Réglage du volume du son de fin

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

skins = [
    "images/voiture_nsi.png",
    "images/voiture_nsi_vert.png",
    "images/voiture_nsi_violet.png",
    "images/voiture_nsi_jaune.png",
    "images/voiture_nsi_turquoise.png"
]

index_skin = 0

image_mer = pygame.image.load("images/mer_nsi.png")
image_adverse_originale = pygame.image.load("images/voiture_adverse_nsi.png").convert_alpha()
image_voiture_originale = pygame.image.load(skins[index_skin]).convert_alpha()
image_voiture = pygame.transform.smoothscale(
    image_voiture_originale,
    (int(image_voiture_originale.get_width() * 0.30),
     int(image_voiture_originale.get_height() * 0.30))
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
largeur_powerup = int(largeur_voie * 0.5)
hauteur_powerup = int(largeur_powerup * 1)
image_bouclier = pygame.transform.smoothscale(image_bouclier_original, (largeur_powerup, hauteur_powerup))
 
powerups = []
compteur_powerup = 0
delai_powerup = 300

bouclier_actif = False
temps_bouclier = 0
DUREE_BOUCLIER = 3000

# Autres power-ups
image_multi_original = pygame.image.load("images/multi_nsi.png").convert_alpha()
image_multi = pygame.transform.smoothscale(image_multi_original, (largeur_powerup, hauteur_powerup))
image_slow_original = pygame.image.load("images/slow_nsi.png").convert_alpha()
image_slow = pygame.transform.smoothscale(image_slow_original, (largeur_powerup, hauteur_powerup))
image_destruction_original = pygame.image.load("images/destruction_nsi.png").convert_alpha()
image_destruction = pygame.transform.smoothscale(image_destruction_original, (largeur_powerup, hauteur_powerup))
image_multi_original_1 = pygame.image.load("images/multi_nsi.png").convert_alpha()
image_multi_1 = pygame.transform.smoothscale(image_multi_original_1, (30, 30))
image_slow_original_1 = pygame.image.load("images/slow_nsi.png").convert_alpha()
image_slow_1 = pygame.transform.smoothscale(image_slow_original_1, (30, 30))
image_destruction_original_1 = pygame.image.load("images/destruction_nsi.png").convert_alpha()
image_destruction_1 = pygame.transform.smoothscale(image_destruction_original_1, (30, 30))
image_bouclier_original_1 = pygame.image.load("images/bouclier_nsi.png").convert_alpha()
image_bouclier_1 = pygame.transform.smoothscale(image_bouclier_original_1, (30, 30))
images_powerups = {
    "bouclier": image_bouclier,
    "multi": image_multi,
    "slow": image_slow,
    "destruction": image_destruction
}


slow_actif = False
temps_slow = 0
DUREE_SLOW = 4000

multiplicateur = 1
temps_multi = 0
DUREE_MULTI = 5000

DUREE_DESTRUCTION = 2000


# Compteurs
temps_debut = pygame.time.get_ticks()
distance = 0
score = 0
meilleur_score = 0
nouveau_record = False
temps_record = 0

while en_cours:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            en_cours = False            # Fermeture de la fenêtre

        if e.type == pygame.MOUSEBUTTONDOWN:
            if etat == ACCUEIL and bouton_jouer.collidepoint(e.pos):
                image_voiture_originale = pygame.image.load(skins[index_skin]).convert_alpha()

                image_voiture = pygame.transform.smoothscale(
                    image_voiture_originale,
                    (int(image_voiture_originale.get_width() * 0.30),
                    int(image_voiture_originale.get_height() * 0.30))
                )

                mask_voiture = pygame.mask.from_surface(image_voiture)
                
                etat = JEU
                voiture = init(voiture_init_x, voiture_init_y, son_menu)     # Lancement du jeu
                temps_debut = pygame.time.get_ticks()

        if e.type == pygame.KEYDOWN:
            if etat == ACCUEIL:
                if e.key == pygame.K_RIGHT:
                    index_skin = (index_skin + 1) % len(skins)

                if e.key == pygame.K_LEFT:
                    index_skin = (index_skin - 1) % len(skins)
            
            if e.key == pygame.K_z:
                etat = ACCUEIL          # Retour à l'accueil
                # Reset du jeu
                voitures_adverses.clear()
                powerups.clear()
                compteur_spawn = 0
                compteur_powerup = 0

                vitesse_adversaires = 5
                vitesse_cible = 2
                son_moteur.stop()
                son_perdu.stop()
                son_defaite = False

                distance = 0
                score = 0
                nouveau_record = False
            if etat == FIN and e.key == pygame.K_a:
                en_cours = False        # Quitter le jeu
            if etat == FIN and e.key == pygame.K_RETURN:
                etat = JEU
                voiture = init(voiture_init_x, voiture_init_y, son_menu)
                voitures_adverses.clear()
                powerups.clear()
                bouclier_actif = False
                slow_actif = False
                multiplicateur = 1
                temps_multi = 0
                temps_bouclier = 0
                compteur_powerup = 0
                compteur_spawn = 0
                vitesse_adversaires = 5
                vitesse_cible = 2
                son_perdu.stop()
                son_defaite = False
                temps_debut = pygame.time.get_ticks()
                distance = 0 
                score = 0 
                nouveau_record = False 

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

        temps = float((pygame.time.get_ticks() - temps_debut) // 1000)
        distance += vitesse_cible / 20

        if score > meilleur_score:
            meilleur_score = score
            nouveau_record = True
            temps_record = pygame.time.get_ticks()

        if etat == JEU:
            if nouveau_record:
                if pygame.time.get_ticks() - temps_record < 3000:
                    police_texte_record = pygame.font.SysFont("impact", 30)
                    texte_record = police_texte_record.render("Nouveau record !", True, DORE)
                    ecran_du_jeu.blit(texte_record, (1000, 220))
        else:
            nouveau_record = False
        # fin slow
        if slow_actif and pygame.time.get_ticks() - temps_slow > DUREE_SLOW:
            slow_actif = False

        # fin multiplicateur
        if multiplicateur == 2 and pygame.time.get_ticks() - temps_multi > DUREE_MULTI:
            multiplicateur = 1          
              

        son_menu.stop() 

        if vitesse_cible >8:
            score += multiplicateur * vitesse_cible * distance / 3000

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

        # Spawn des pouvoirs aléatoire
        if compteur_powerup >= delai_powerup:
            essais = 0
            spawn_reussi = False

            while essais < 10 and not spawn_reussi:
                voie = random.randint(0, nb_voies - 1)

                rect = image_bouclier.get_rect()
                rect.centerx = centres_voies[voie]
                rect.y = -rect.height

                voie_libre = True

                for v in voitures_adverses:
                    if abs(v.centerx - centres_voies[voie]) < largeur_voie // 2:
                        if v.y < 200:
                            voie_libre = False
                            break

                if voie_libre:
                    type_powerup = random.choice(["bouclier", "slow", "multi", "destruction"])
                    powerups.append({
                        "rect": rect,
                        "type": type_powerup
                    })
                    spawn_reussi = True

                essais += 1

            compteur_powerup = 0

        # Dessin des lignes de séparation des voies de la route
        vitesse_lignes = vitesse_cible * 2
        route_offset += vitesse_lignes
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
            vitesse_effective = vitesse_adversaires
            if slow_actif:
                vitesse_effective *= 0.5

            rect.y += vitesse_effective   # vitesse des adversaires
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
                    if e.key == pygame.K_z:
                        son_perdu.stop()
                        son_defaite = False

            ecran_du_jeu.blit(image_voiture_adverse, rect)

        for p in powerups[:]:
            rect = p["rect"]

            for v in voitures_adverses:
                if p["rect"].colliderect(v):
                    powerups.remove(p)
                    break

            vitesse_effective = vitesse_adversaires
            if slow_actif:
                vitesse_effective *= 0.5

            rect.y += vitesse_effective

            if rect.top > 800:
                powerups.remove(p)

            if hitbox_voiture.colliderect(rect):
                if p["type"] == "bouclier":
                    bouclier_actif = True
                    temps_bouclier = pygame.time.get_ticks()

                elif p["type"] == "slow":
                    slow_actif = True
                    temps_slow = pygame.time.get_ticks()

                elif p["type"] == "multi":
                    multiplicateur = 2
                    temps_multi = pygame.time.get_ticks()

                elif p["type"] == "destruction":
                    voitures_adverses.clear()
                    if pygame.time.get_ticks() - temps_multi > DUREE_DESTRUCTION:
                        police_texte_destruction = pygame.font.SysFont("impact", 150)
                        texte_destruction = police_texte_destruction.render("BOOM !", True, DORE)
                        ecran_du_jeu.blit(texte_destruction, (450, 100))

                powerups.remove(p)

            image_a_afficher = images_powerups.get(p["type"], image_bouclier)
            ecran_du_jeu.blit(image_a_afficher, rect)

            

        if bouclier_actif and pygame.time.get_ticks() - temps_bouclier > DUREE_BOUCLIER:
            bouclier_actif = False

        # Affichage des compteurs 
        police_texte_temps = pygame.font.SysFont("impact", 30)
        police_texte_distance = pygame.font.SysFont("impact", 30)
        police_texte_vitesse = pygame.font.SysFont("impact", 30)
        police_texte_score = pygame.font.SysFont("impact", 30)
        police_texte_highest_score = pygame.font.SysFont("impact", 30)
        police_texte_powerup = pygame.font.SysFont("impact", 30)
        texte_temps = police_texte_temps.render(f"Temps : {temps}s", True, BLANC)
        texte_distance = police_texte_distance.render(f"Distance : {int(distance)} m", True, BLANC)
        texte_vitesse = police_texte_vitesse.render(f"Vitesse : {int(vitesse_cible)*10} km/h", True, BLANC)
        texte_score = police_texte_score.render(f"Score : {int(score)}", True, BLANC)
        texte_highest_score = police_texte_highest_score.render(f"Record : {int(meilleur_score)}", True, BLANC)
        texte_powerup1 = police_texte_powerup.render(f"Pouvoirs :", True, BLANC)
        texte_bouclier1 = police_texte_powerup.render(f"Bouclier", True, BLANC)
        texte_slow1 = police_texte_powerup.render(f"Slow", True, BLANC)
        texte_destruction1 = police_texte_powerup.render(f"Destruction", True, BLANC)
        texte_multi1 = police_texte_powerup.render(f"Multiplicateur", True, BLANC)
        if bouclier_actif:
            police_texte_bouclier = pygame.font.SysFont("impact", 30)
            texte_bouclier = police_texte_bouclier.render("Bouclier actif", True, DORE)
            ecran_du_jeu.blit(texte_bouclier, (1000, 260))
        if slow_actif:
            police_texte_slow = pygame.font.SysFont("impact", 30)
            texte_slow = police_texte_slow.render("Slow actif", True, DORE)
            ecran_du_jeu.blit(texte_slow, (1000, 300))
        if multiplicateur == 2:
            police_texte_multi = pygame.font.SysFont("impact", 30)
            texte_multi = police_texte_multi.render("Multiplicateur actif", True, DORE)
            ecran_du_jeu.blit(texte_multi, (1000, 340))    
        ecran_du_jeu.blit(texte_temps, (1000, 20))
        ecran_du_jeu.blit(texte_distance, (1000, 60))
        ecran_du_jeu.blit(texte_vitesse, (1000, 100))
        ecran_du_jeu.blit(texte_score, (1000, 140))
        ecran_du_jeu.blit(texte_highest_score, (1000, 180))
        ecran_du_jeu.blit(texte_powerup1, (40, 20))
        ecran_du_jeu.blit(texte_bouclier1, (40, 60))
        ecran_du_jeu.blit(texte_slow1, (40, 100))
        ecran_du_jeu.blit(texte_destruction1, (40, 140))
        ecran_du_jeu.blit(texte_multi1, (40, 180))

        ecran_du_jeu.blit(image_bouclier_1, (250, 65))
        ecran_du_jeu.blit(image_slow_1, (250, 105))
        ecran_du_jeu.blit(image_destruction_1, (250, 145))
        ecran_du_jeu.blit(image_multi_1, (250, 185))
        


        # Déplacement de la voiture
        if touches[pygame.K_LEFT]:
            voiture.x -= vitesse
        if touches[pygame.K_RIGHT]:
            voiture.x += vitesse

        #Rester dans la route
        voiture.x = max(route.left, min(voiture.x, route.right - image_voiture.get_width()))
        

        hitbox_voiture.x = max(route.left, min(hitbox_voiture.x, route.right - image_voiture.get_width()))
        
        hitbox_voiture.x = voiture.x + 14
        hitbox_voiture.y = voiture.y + 10
        
        ecran_du_jeu.blit(image_voiture, voiture)

    
    if etat == ACCUEIL:
        if not pygame.mixer.get_busy():
            son_menu.play(-1)
        accueil(ecran_du_jeu, police_titre, police_texte, police_texte1, BLANC, BLANC1, GRIS1, INDIGO, ROUGE, GRIS, DORE, bouton_jouer, son_menu, skins, index_skin)

    elif etat == FIN:
        if son_defaite and not channel_perdu.get_busy():
            channel_perdu.play(son_fin)
            son_defaite = False
        if score > meilleur_score:
            meilleur_score = score
        
        fin(ecran_du_jeu, police_titre, police_retour, police_sortie, police_rejouer, score, GRIS1, ORANGE, BLANC)
    
        police_texte_meilleur_score = pygame.font.SysFont("showcardgothic", 40, italic=True)
        texte_meilleur_score = police_texte_meilleur_score.render(f"Meilleur score : {int(meilleur_score)}", True, GRIS1)
        ecran_du_jeu.blit(texte_meilleur_score, (345, 650))
    
    pygame.display.update()  # Mise à jour de l'écran
    clock.tick(60)           # Limitation du jeu à 60 FPS

pygame.quit()   # Fermeture de pygame
sys.exit()      # Fermeture du programme
