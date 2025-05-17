import random

import pygame as pyg

from .constants import *


def enemy(screen, x, y, enemy_img):
    screen.blit(enemy_img, (x, y))


def setup_enemy():
    enemy_images = []
    enemy_x = []
    enemy_y = []
    enemy_x_change = []
    enemy_y_change = []
    for i in range(NUM_OF_ENEMIES):
        decide_enemy_type(enemy_images, i)

        enemy_x.append(i * random.randint(0, 10))
        enemy_y.append(random.randint(0, 50))
        enemy_x_change.append(1)
        enemy_y_change.append(40)

    return enemy_images, enemy_x, enemy_x_change, enemy_y, enemy_y_change


def decide_enemy_type(enemy_images, i):
    if i % 2 == 0:
        enemy_image = pyg.image.load(ENEMY_IMAGE_RED_PATH)
        enemy_images.append(pyg.transform.scale(enemy_image, (60, 60)))
    else:
        enemy_image = pyg.image.load(ENEMY_IMAGE_BLUE_PATH)
        enemy_images.append(pyg.transform.scale(enemy_image, (60, 60)))
