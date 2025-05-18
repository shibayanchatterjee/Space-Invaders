import math

import pygame as pyg

from .constants import *


def fire_bullet(screen, x, y, bullet_img):
    global bullet_state
    bullet_state = BULLET_FIRE
    screen.blit(bullet_img, (x + 15, y - 50))


def setup_bullet():
    bullet_img = pyg.image.load(BULLET_IMAGE_PATH)
    scaled_img = pyg.transform.scale(bullet_img, (20, 20))

    bullet_x = 0
    bullet_y = 480
    bullet_y_change = 10
    bullet_state = BULLET_READY  # Ready - you can't see the bullet on the screen
    return scaled_img, bullet_state, bullet_x, bullet_y, bullet_y_change


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    return math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) < 27


def reset_bullet_state(bullet_img, bullet_state, bullet_x, bullet_y, bullet_y_change, screen):
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = BULLET_READY
    if bullet_state == BULLET_FIRE:
        fire_bullet(screen, bullet_x, bullet_y, bullet_img)
        bullet_y -= bullet_y_change
    return bullet_state, bullet_y
