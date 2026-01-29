import pygame

from random import randint

FPS = 30

pyx.init(180, 260, title= "Hallowen Game", fps= 30)
pyxel.load("pyxeldraw.pyxres")

#global variables
side_character = 28
side_ammunition = 16

x_player = 86
y_player = 230
#number of player image
image_nb_player = 0

xy_canon_1 = [56, 10]
xy_canon_2 = [86, 10]
xy_canon_3 = [118, 10]
xy_canon_4 = [148, 10]

list_pumpkins = []
list_ammunitions = []
list_candybowls = []

#to control ammunition time shift between shoots
sleep = 0

score = 0
level = 1

#veocity of pumpkins
v_pump = 7

game_state = "home"
    
def display_background():
    """display the background during the entire game"""
    pyxel.blt(35, 0, img=0, u=0, v=48, w=104, h=176, colkey=14, scale= 2)
    
def display_player():
    global x_player, y_player, image_nb_player
    if image_nb_player == 0:
        pyxel.blt(x_player, y_player, img=0, u=0, v=16, w=16, h=16, colkey= 14, scale=2)
    elif image_nb_player == 1:
        pyxel.blt(x_player, y_player, img=0, u=16, v=16, w=16, h=16, colkey= 14, scale=2)
    else:
        pyxel.blt(x_player, y_player, img=0, u=32, v=16, w=16, h=16, colkey= 14, scale=2)
    if pyxel.frame_count%(FPS/3) == 0:
        image_nb_player = image_nb_player + 1
        if image_nb_player > 2:
            image_nb_player = 0
            
    
    
    
    
    #pyxel.blt(x_player, y_player -22 , img=0, u=0, v=32, w=15, h=15, colkey= 14, scale=1)
def display_canons():
    pyxel.blt(56, 10, img=0, u=0, v=240, w=16, h=16, colkey=14, scale=2)
    pyxel.blt(86, 10, img=0, u=0, v=240, w=16, h=16, colkey=14, scale=2)
    pyxel.blt(118, 10, img=0, u=0, v=240, w=16, h=16, colkey=14, scale=2)
    pyxel.blt(148, 10, img=0, u=0, v=240, w=16, h=16, colkey=14, scale=2)
    
def move_player():
    global x_player, y_player
    if pyxel.btn(pyxel.KEY_RIGHT) and x_player < 147:
        x_player = x_player + 2
    if pyxel.btn(pyxel.KEY_LEFT) and x_player > 55:
        x_player = x_player - 2
    if pyxel.btn(pyxel.KEY_UP) and y_player > 43:
        y_player = y_player -2
    if pyxel.btn(pyxel.KEY_DOWN) and y_player < 235:
        y_player = y_player +2
        
def add_pumpkins():
    #canons shoot a pumpkin every second
    global list_pumpkins, xy_canon_1, xy_canon_2, xy_canon_3, xy_canon_4
    if pyxel.frame_count%(FPS*1.5) == 0:
        #take a random number between 1 and 4, to determined the canon where the pumpkin will appear
        canon_nb = randint(1, 4)
        if canon_nb == 1:
            #[x, y, image number]
            list_pumpkins.append([xy_canon_1[0], xy_canon_1[1] + 32, 0])
        if canon_nb == 2:
            list_pumpkins.append([xy_canon_2[0], xy_canon_2[1] + 32, 0])
        if canon_nb == 3:
            list_pumpkins.append([xy_canon_3[0], xy_canon_3[1] + 32, 0])
        if canon_nb == 4:
            list_pumpkins.append([xy_canon_4[0], xy_canon_4[1] + 32, 0])
        
def manage_pumpkins():
    """change the number of pumpkin image every 1/3 seconds to give a spinning effect, make move them and remove pumpkins out of the scene"""
    global list_pumpkins, score
    if pyxel.frame_count%(FPS/3) == 0:
        i = 0 #rank of element worked
        for element in list_pumpkins:
            element[1] = element[1] + v_pump
            if element[2] < 7:
                element[2] = element[2] + 1
            else:
                element[2] = 0
            if element[1] > 270:
                list_pumpkins.pop(i)
                score = score - 1
            i = i + 1
                

def display_pumpkins():
    global list_pumpkins
    for element in list_pumpkins:
        pyxel.blt(element[0], element[1], img=0, u=16*element[2], v=0, w=16, h=16, colkey=14, scale=2)
        #as each image take 16 pyxels, i have just to take number of image time 16 to have the width of the image that correspond of the numero (as images are placed in the order of numero) 
        
def manage_ammunitions():
    global list_ammunitions, sleep
    if pyxel.frame_count%(FPS*1.2) == 0:
        sleep = 0
    if pyxel.btn(pyxel.KEY_SPACE) and sleep == 0:
        rand = randint(0,2)
        list_ammunitions.append([x_player, y_player - side_character//2 - side_ammunition//2, rand])
        #add [x, y, image number]
        sleep = 1

def move_ammunitions():
    global list_ammunitions
    if pyxel.frame_count%(FPS/10) == 0:
        i = 0 #give the rank of the element treated
        for element in list_ammunitions:
            if element[1] > 43:
                element[1] = element[1] - 7
            else:
                list_ammunitions.pop(i)
            i = i + 1
            

def display_ammunitions():
    global list_ammunitions
    for element in list_ammunitions:
        pyxel.blt(element[0], element[1], img=0, u=16*element[2], v=32, w=16, h=16, colkey=14)
        
def shocks_pumpkins_ammunitions():
    """collision between ammunitions and pumpkins"""
    global list_ammunitions, list_pumpkins, score, list_candybowls
    a = 0
    for element_amu in list_ammunitions:
        p = 0
        for element_pum in list_pumpkins:
            if abs(element_amu[0] - element_pum[0]) < side_character//2 + side_ammunition//2 and abs(element_amu[1] - element_pum[1]) < side_character//2 + side_ammunition//2:
                list_pumpkins.pop(p)
                list_ammunitions.pop(a)
                list_candybowls.append([element_pum[0], element_pum[1], 0])
            p = p + 1
        a = a + 1
    
def shocks_character_candybowls():
    """collision between character and candy bowls"""
    global list_candybowls, score
    i = 0
    for element in list_candybowls:
        if abs(element[0] - x_player) < side_character//2 + side_ammunition//2 and abs(element[1] - y_player) < side_character//2 + side_ammunition//2:
            score = score + 1
            list_candybowls.pop(i)
        i = i + 1
        
def shocks_character_pumpkin():
    global list_pumpkins, game_state, side_character, score
    for element in list_pumpkins:
        if abs(element[0] - x_player) < side_character and abs(element[1] - y_player) < side_character:
            game_state = "game_over"
            
def manage_candybowls():
    """if the player don't take the bowl in 5 seconds, it disappear"""
    global list_candybowls
    if pyxel.frame_count%FPS == 0:
        i = 0
        for element in list_candybowls:
            element[2] = element[2] + 1
            if element[2] > 4:
                list_candybowls.pop(i)
            i = i + 1
                
def display_candybowls():
    global list_candybowls
    for element in list_candybowls:
        pyxel.blt(element[0], element[1], img=0, u=112, v=16, w=16, h=16, colkey=14)
    
def display_score():
    pyxel.text(10, 20, f"SCORE = {score}", 7)

def manage_level():
    global v_pump, score, level
    if score >= 10:
        score = 0
        level = level + 1
        v_pump = v_pump + 1
        
def display_level():
    pyxel.text(10, 30, f"LEVEL = {level}", 0)
        

    
    #for a in range(len(list_ammunitions) - 1):
        #for p in range(len(list_pumpkins) - 1):
            #if abs(list_ammunitions[a][0] - list_pumpkins[p][0]) < side_character//2 + side_ammunition + 16 and abs(list_ammunitions[a][1] - list_pumpkins[p][1]) < side_character//2 + 16:
                #list_candybowls.append(list_pumpkins[p])
                #list_pumpkins.pop(p)
                #list_ammunitions.pop(a)
    
####

def draw():
    global game_state
    if not pyxel.btn(pyxel.KEY_SPACE) and game_state == "home":
    #if pyxel.frame_count < FPS*10:
        pyxel.text(10, 80, "Shoot the pumpkins and collect", 9)
        pyxel.text(10, 90, "the bowls of candy inside", 9)
        pyxel.text(5, 110, "Don't let pumpkin go behind the scene", 8)
        pyxel.text(5, 120, "otherwise, you will lost point,", 8)
        pyxel.text(5, 130, "or touch you otherwise, it would sign", 8)
        pyxel.text(5, 140, "the end of the game", 8)
        pyxel.blt(75, 165, img=0, u=0, v=0, w=16, h=16, colkey=14, scale = 2)
        pyxel.text(40, 200, "press SPACE to start", 7)
    elif game_state != "game_over" and score >= 0:
        game_state = "play"
        display_background()
        display_player()
        display_canons()
        display_pumpkins()
        display_ammunitions()
        display_candybowls()
        display_score()
        display_level()
    else:
        display_background()
        display_canons()
        pyxel.text(71, 80, "game over !", 7)
        pyxel.blt(80, 120, img=0, u=16, v=240, w=16, h=16, colkey=14, scale = 4)
        pyxel.text(35, 170, 'Click "reload" to restart', 2)
        pyxel.blt(81, 190, img=0, u=32, v=240, w=16, h=16, colkey=14, scale = 1)
        

def update():
    global game_state
    if game_state == "play":
        move_player()
        add_pumpkins()
        manage_pumpkins()
        manage_ammunitions()
        move_ammunitions()
        shocks_pumpkins_ammunitions()
        manage_candybowls()
        shocks_character_candybowls()
        shocks_character_pumpkin()
        manage_level()

#if 0 == 0:
    #pyxel.music(msc=0)
    #pyxel.music(msc=1)

pyxel.run(update, draw)