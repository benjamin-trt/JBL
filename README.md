
SEANCE 1 :

Groupe de NSI de Benjamin, Luca et Jules

Idée de projet:
On aimerait bien faire un jeu de voiture dans le style de mario kart, avec un circuit à finir en évitant certains obstacles lors des tours

Autre idée de projet:
Potentiellement un jeu du style Donkey Kong, avec des obstacles et un parcours pour arriver jusqu'à un objectif final

Ou alors encore une autre idée:
Un jeu de logique du style Block Blast par exemple ou Tetris, avec des assemblages, des systèmes de point

Globalement, ce seraient des jeux en 2D, sauf peut-être le jeu de voiture (et encore)
Les deux premières idées seraient sûrement sous la forme de niveaux, de parcours, alors que le "Tetris" serait plûtot un jeu auquel on joue jusqu'à perdre


<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/289e7281-f396-4028-940a-fcb252264a8f" />
<img width="450" height="250" alt="image" src="https://github.com/user-attachments/assets/5699c408-a0c9-41b7-bb43-45789054b450" />
<img width="320" height="380" alt="image" src="https://github.com/user-attachments/assets/c8663b1e-8e11-45b0-a5c2-5031b55eee93" />
https://www.youtube.com/watch?v=6BE9dqqVZ2I


SEANCE 2 :

Nous avons choisi de faire un jeu de voiture (avec un seul joueur).

Il s'agirait d'un jeu où l'on doit conduire une voiture. Il faudrait importer une bibliothèque Pygames, pour avoir des fonctions précises nécessaires au bon fonctionnement du jeu. On voit cette même voiture (qu'on va appeller ici voiture 1) d'un point de vue aérien (en 2D donc). Il y aurait 4 voies (il s'agit d'une autoroute) avec un paysage de campagne qui défile, avec des graphismes classiques et assez simples. Des véhicules de différentes sortes (à la fois des camions, des voitures ou des scooters) apparaissent aléatoirement sur la route, et le but de l'utilisateur est de tous les éviter. La voiture peut se déplacer uniquement latéralement, avec les flèches droite et gauche du clavier. Tous les véhicules vont dans le même sens (celui de la voiture 1) et celle-ci (allant plus vite qu'eux) doit les dépasser sans pour autant les heurter. Si la "zone de contact" de la voiture 1 rentre en contact avec la "zone de contact" d'un autre véhicule, la voiture 1 s'arrête, avec une animation d'accident. L'utilisateur doit recommencer sa partie. Il n'y a pas de niveaux, chaque partie s'arrête uniquement lorsqu'un accident est provoqué. Il y a de plus en plus de véhicules, rendant la manoeuvre de la voiture 1 de plus en plus compliquée. La voiture ne peut pas sortir des 4 voies, ni les autres véhicules. La voiture 1 a une vitesse minimale par défaut (qui doit être supérieure à la vitesse constante des véhicules) et qui croît progressivement. Cependant, malgré cette valeur minimale de vitesse, l'utilisateur peut décider ou non d'accélérer, avec la flèche du haut du clavier. Un compteur de vitesse peut apparaître (en haut à droite de l'écran par exemple), pour indiquer la vitesse. Il faudrait aussi afficher la vitesse maximale atteinte pour chaque partie, et il faudrait afficher un compteur de points qui augmente progressivement au fur et à mesure que nous avançons dans la partie (mais qui se réinitialise à chaque début de partie). Il faudrait un compteur de distance aussi idéalement et un compteur de temps, pour indiquer le temps pendant lequel l'utilisateur manoeuvre sans causer d'accidents. Naturellement, tous les compteurs mentionnés précédemment se réinitialisent à chaque début de partie. Il pourrait y avoir un système de sélection de sa voiture 1, avec des skins disponibles (avec différents modèles de voitures, différentes couleurs, etc...). Il faudrait aussi que de temps en temps sur la route apparaissent des sortes de boîtes mystère (comme dans Mario Kart par exemple) qui feraient débloquer aléatoirement un pouvoir ou une capacité spéciale. Par exemple, nous avons pensé à un pouvoir de ralentissement des autres véhicules, un pouvoir de protection (sous la forme d'un bouclier temporaire qui nous protège quelques secondes contre un éventuel choc avec un véhicule), ou aussi par exemple un pouvoir de bazooka (qui pourrait être activé avec une touche comme "a" par exemple) et qui permettrait de détruire un véhicule et libérer la voie devant soi. Ces différents pouvoirs seraient temporaires (ils dureront quelques sencondes au maximum), et pourront s'accumuler (se superposer en quelque sorte). Il faudrait pouvoir se connecter à son profil pour retrouver ses données personnelles comme le meilleur temps, meilleurs score personnel, etc... Si nous avons le temps et les capacités pour, nous comptons pouvoir mettre un paramètre permettant de passer de la nuit à la jounée, et inversement. Il faudrait aussi mettre une petite musique de fond, qui idéalement irait bien dans le thème, et idéalement une musique qui peut être répétée en boucle, jusqu'à la fin de la partie. Pour tout ce qui concerne la sélection des skins, du jour ou de la nuit, etc il faudra aller dans le menu.

Voici ci-dessous un exemple de jeu existant et qui se rapproche grandement selon nous du jeu que nous voulons créer (bien que le jeu soit en 3D).

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/fd9e6338-5450-4e6e-8c13-c5658a759ce1" />


SEANCE 3 :

Planning pour les 15 semaines:

1ere séance:

- Création d'un groupe de 3 (Benjamin, Jules, Luca)
- Tous les membres du groupe se sont créés un compte sur Github
- Création d'un dépôt public au nom du groupe sur Github
- Invitation de tous les membres du groupe comme collaborateurs sur le projet
- Invitation de M.Barthelemy à collaborer lui aussi
- Ajout de quelques idées de projet, images et vidéos à l'appui, dans le fichier README du dépôt
- Toutes ces étapes ont été réalisées en groupe

2eme séance:

- Création d'un cahier des charges pour le projet :
- Choix une idée de projet
- Définition des caractéristiques détaillées de ce projet
- Toutes ces étapes ont été réalisées en groupe

3eme séance:

- Création d'un planning pour le projet :
- Grâce au cahier des charges, prévision du déroulement du projet sur 15 semaines et attribution des tâches aux différents membres du groupe
- Penser à prévoir du temps à la fin pour les tests et le débugage ainsi que pour la préparation de la présentation orale prévue à la rentrée des vacances de Pâques
- Rédaction du planning dans le fichier README du dépôt
- Toutes ces étapes ont été réalisées en groupe

4eme séance:

- Mise en place de l’environnement de travail (Python, Pygame, éditeur de code)
- Création du fichier principal du jeu et structure générale du programme
- Création de la fenêtre Pygame et de la boucle principale
- Benjamin : installation et vérification de l’environnement sur les postes
- Luca : création de la fenêtre Pygame et de la boucle principale
- Jules : organisation des fichiers et structure du code

5eme séance:

- Création de la route (4 voies) et du fond de jeu simple
- Définition des limites de la route
- Affichage de la voiture du joueur à l’écran
- Benjamin : dessin de la route et des voies
- Luca : affichage de la voiture du joueur
- Jules : gestion des limites de déplacement de la voiture

6eme séance:

- Implémentation du déplacement latéral progressif de la voiture
- Gestion des touches gauche et droite du clavier
- Tests pour garantir un déplacement fluide et contrôlable
- Benjamin : gestion des événements clavier
- Luca : calcul et ajustement de la vitesse latérale
- Jules : tests et corrections du déplacement

7eme séance:

- Mise en place du déplacement vertical simulé (route qui défile)
- Création des premiers véhicules adverses simples
- Apparition des véhicules sur les différentes voies
- Benjamin : défilement de la route et du décor
- Luca : création de la classe des véhicules adverses
- Jules : apparition aléatoire et gestion des voies

8eme séance:

- Déplacement des véhicules adverses
- Gestion de leur suppression lorsqu’ils sortent de l’écran
- Tests de stabilité (pas de ralentissement du jeu)
- Benjamin : gestion du déplacement des véhicules
- Luca : suppression des véhicules hors écran
- Jules : tests de performance et corrections

9eme séance:

- Mise en place des collisions entre la voiture du joueur et les véhicules adverses
- Définition de la zone de collision
- Gestion de la fin de partie lors d’un accident
- Benjamin : détection des collisions
- Luca : arrêt du jeu lors d’une collision
- Jules : tests des collisions dans différentes situations

10eme séance:

- Mise en place d’une animation simple lors d’un accident
- Possibilité de relancer une partie après un accident
- Vérification que le jeu est entièrement jouable du début à la fin
- Benjamin : animation d’accident
- Luca : réinitialisation des variables et redémarrage du jeu
- Jules : tests complets du cycle de jeu

11eme séance:

- Ajout du score de la partie
- Ajout du compteur de temps et du compteur de distance
- Réinitialisation des compteurs à chaque nouvelle partie
- Benjamin : compteur de score
- Luca : compteur de temps
- Jules : compteur de distance et affichage à l’écran

12eme séance:

- Gestion de la vitesse du joueur (vitesse minimale et accélération)
- Affichage de la vitesse actuelle et de la vitesse maximale atteinte
- Ajustement de la difficulté en fonction du temps ou du score
- Benjamin : gestion de la vitesse minimale
- Luca : gestion de l’accélération et de la vitesse maximale
- Jules : réglage progressif de la difficulté

13eme séance:

- Ajout des boîtes mystère sur la route
- Implémentation des premiers pouvoirs (bouclier)
- Gestion de la durée des pouvoirs
- Benjamin : apparition des boîtes mystère
- Luca : implémentation du bouclier
- Jules : tests et équilibrage du pouvoir

14eme séance:

- Ajout d’éléments de design simples (couleur du paysage, formes supplémentaires...)
- Ajout d’une musique de fond et gestion du son
- Sauvegarde des données du joueur (meilleur score, meilleur temps)
- Benjamin : amélioration visuelle du jeu
- Luca : gestion du son et de la musique
- Jules : sauvegarde et chargement du profil joueur

15eme séance:

- Phase finale de tests et de débogage
- Vérification du respect du cahier des charges
- Préparation et entraînement à la présentation orale
- Cette fois-ci tous en groupe


Voici le planning idéal que nous avons en tête. Cependant, nous nous doutons que ce sera plus compliqué que ça, et que nous devrons parfois inverser les rôles, nous entraider, ou passer plus de temps sur une tâche.




SEANCE 4 :

Voici notre début de code :
Il crée une fenêtre de jeu avec un fond de couleur que nous avons choisie (vert foncé) et avec le titre de notre jeu, "Crazy Racer". Cette fenêtre se ferme lorsque l'utilisateur appuie sur la croix en haut à droite de l'écran. La fenêtre reste ouverte tant que l'utilisateur n'appuie pas sur cette croix.


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

    ecran_du_jeu.fill(couleur_fond)
    pygame.display.update()

pygame.quit()
sys.exit()
