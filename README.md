# JBL
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

Nous avons choisi de faire un jeu de voiture.
Il s'agirait d'un jeu où l'on doit conduire une voiture. On voit cette même voiture (qu'on va appeller ici voiture 1) d'un point de vue aérien (en 2D donc). Il y aurait 4 voies (il s'agit d'une autoroute). Des véhicules de différentes sortes (à la fois des camions, des voitures ou des scooters) apparaissent aléatoirement sur la route, et le but de l'utilisateur est de tous les éviter. Tous les véhicules vont dans le même sens (celui de la voiture 1) et celle-ci (allant plus vite qu'eux) doit les dépasser sans pour autant les heurter. Si la "zone de contact" de la voituere 1 rentre en contact avec la "zone de contact" d'un autre véhicule, la voiture 1 s'arrête, avec une animation d'accident. L'utilisateur doit recommencer sa partie. Il n'y a pas de niveaux, chaque partie s'arrête uniquement lorsqu'un accident est provoqué. Il y a de plus en plus de véhicules, rendant la manoeuvre de la voiture 1 de plus en plus compliquée. La voiture ne peut pas sortir des 4 voies, ni les autres véhicules. La voiture 1 a une vitesse minimale par défaut (qui doit être supérieure à la vitesse constante des véhicules) et qui croît progressivement. Cependant, malgré cette valeur minimale de vitesse, l'utilisateur peut décider ou non d'accélérer. Un compteur de vitesse peut apparaître (en haut à droite de l'écran par exemple), pour indiquer la vitesse. Il faudrait aussi afficher la vitesse maximale atteinte pour chaque partie
