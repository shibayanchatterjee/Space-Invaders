import math
import os
import random

import pygame
import pygame as pyg
from pygame import mixer

global bullet_state

BACKGROUND_IMAGE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'background.png'))
BACKGROUND_MUSIC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'background.wav'))


def fire_bullet(screen, x, y, bullet_img):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False


def show_score(screen, x, y, score_value, font):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text(screen, x, y, over_font):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (x, y))


def player(screen, x, y, player_img):
    screen.blit(player_img, (x, y))


def enemy(screen, x, y, enemy_img):
    screen.blit(enemy_img, (x, y))


def space_invader():
    # Initialize Pygame
    pyg.init()

    # Set up the screen
    screen = pyg.display.set_mode((800, 600))

    # Background image
    background = pyg.image.load(BACKGROUND_IMAGE_PATH)

    # Sound
    mixer.music.load(BACKGROUND_MUSIC_PATH)
    mixer.music.play(-1)

    # Caption and icon
    pyg.display.set_caption("Space Invaders")
    icon = pyg.image.load(
        os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'space-invaders.png')))
    pyg.display.set_icon(icon)

    # Player
    player_img = pyg.image.load(
        os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'rocket.png')))
    scaled_img = pygame.transform.scale(player_img, (100, 100))

    player_x = 370
    player_y = 480
    player_x_change = 0
    player_y_change = 0

    # Enemy
    enemy_images = []
    enemy_x = []
    enemy_y = []
    enemy_x_change = []
    enemy_y_change = []
    num_of_enemies = 3
    for i in range(num_of_enemies):
        enemy_images.append(
            pyg.image.load(
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'ghost-red.png'))))
        enemy_x.append(i * 100)
        enemy_y.append(50)
        enemy_x_change.append(4)
        enemy_y_change.append(40)

    # Bullet
    # Ready - no bullets on the screen
    # Fire - bullet is moving
    bullet_img = pyg.image.load(
        os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'bullet.png')))
    bullet_x = 0
    bullet_y = 480
    bullet_x_change = 0
    bullet_y_change = 10
    bullet_state = "ready"  # Ready - you can't see the bullet on the screen

    # Score
    score_value = 0
    font = pyg.font.Font('freesansbold.ttf', 32)
    text_x = 10
    text_y = 10

    # Game over
    over_font = pyg.font.Font('freesansbold.ttf', 64)

    running = True
    while running:

        # Fill the screen with the background color
        screen.fill((0, 0, 0))
        # Background image
        screen.blit(background, (0, 0))

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -5
                if event.key == pygame.K_RIGHT:
                    player_x_change = 5
                if event.key == pygame.K_UP:
                    player_y_change = -5
                if event.key == pygame.K_DOWN:
                    player_y_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound(
                            os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'laser.wav')))
                        bullet_sound.play()
                        bullet_x = player_x
                        fire_bullet(screen, bullet_x, bullet_y, bullet_img)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0

        player_x += player_x_change
        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:
            player_x = 736
        player_y += player_y_change
        if player_y <= 0:
            player_y = 0
        elif player_y >= 536:
            player_y = 536

        # Enemy movement
        for i in range(num_of_enemies):
            # Game Over
            if enemy_y[i] > 440:
                for j in range(num_of_enemies):
                    enemy_y[j] = 2000
                game_over_text(screen, 200, 250, over_font)
                break

            enemy_x[i] += enemy_x_change[i]
            if enemy_x[i] <= 0:
                enemy_x_change[i] = 4
                enemy_y[i] += enemy_y_change[i]
            elif enemy_x[i] >= 736:
                enemy_x_change[i] = -4
                enemy_y[i] += enemy_y_change[i]

            # Collision
            collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
            if collision:
                explosion_sound = mixer.Sound(
                    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'explosion.wav')))
                explosion_sound.play()
                bullet_y = 480
                bullet_state = "ready"
                score_value += 1
                enemy_x[i] = random.randint(0, 735)
                enemy_y[i] = random.randint(50, 150)

        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = "ready"
        if bullet_state == "fire":
            fire_bullet(screen, bullet_x, bullet_y, bullet_img)
            bullet_y -= bullet_y_change

        player(screen, player_x, player_y, scaled_img)
        show_score(screen, text_x, text_y, score_value, font)
        pyg.display.update()
