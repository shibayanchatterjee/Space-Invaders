import pygame as pyg
import random as rd

pyg.init()

# Screen
screen = pyg.display.set_mode((800, 600))

# Title and Icon
pyg.display.set_caption('Space Invaders')
icon = pyg.image.load('rocket.png')
pyg.display.set_icon(icon)

# Player
player_img = pyg.image.load('space-invaders.png')
player_img = pyg.transform.scale(player_img, (64, 64))

player_x = 370
player_y = 480

def player(x, y):
    screen.blit(player_img, (x, y))


#Enemy-1
enemy1 = pyg.image.load('ghost-blue.png')
enemy1 = pyg.transform.scale(enemy1, (64, 64))
enemy1_x = rd.randint(0, 736)
enemy1_y = rd.randint(50, 150)
def enemy1_draw(x, y):
    screen.blit(enemy1, (x, y))

#Enemy-2
enemy2 = pyg.image.load('ghost-red.png')
enemy2 = pyg.transform.scale(enemy2, (64, 64))
enemy2_x = rd.randint(0, 736)
enemy2_y = rd.randint(50, 150)
def enemy2_draw(x, y):
    screen.blit(enemy2, (x, y))

#Enemy-3
enemy3 = pyg.image.load('ghost-black.png')
enemy3 = pyg.transform.scale(enemy3, (64, 64))
enemy3_x = rd.randint(0, 736)
enemy3_y = rd.randint(150, 200)
def enemy3_draw(x, y):
    screen.blit(enemy3, (x, y))


# Game loop
running = True
while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
    screen.fill((200, 200, 200))
    # Player movement
    keys = pyg.key.get_pressed()
    if keys[pyg.K_LEFT] and player_x > 0:
        player_x -= 0.2
    if keys[pyg.K_RIGHT] and player_x < 736:
        player_x += 0.2
    if keys[pyg.K_UP] and player_y > 0:
        player_y -= 0.2
    if keys[pyg.K_DOWN] and player_y < 536:
        player_y += 0.2
    
    # Player boundary check
    if player_x < 0:
        player_x = 0
    elif player_x > 736:
        player_x = 736
    if player_y < 0:
        player_y = 0
    elif player_y > 536:
        player_y = 536      

    player(player_x, player_y)
    enemy1_draw(enemy1_x, enemy1_y)
    enemy2_draw(enemy2_x, enemy2_y)
    enemy3_draw(enemy3_x, enemy3_y)
    pyg.display.update()
