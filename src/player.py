import pygame as pyg

from .constants import PLAYER_IMAGE_PATH


def setup_player():
    player_img = pyg.image.load(PLAYER_IMAGE_PATH)
    scaled_img = pyg.transform.scale(player_img, (100, 100))
    player_x = 370
    player_y = 480
    player_x_change = 0
    player_y_change = 0
    return player_x, player_x_change, player_y, player_y_change, scaled_img


def player(screen, x, y, player_img):
    screen.blit(player_img, (x, y))


def player_movement(player_x, player_x_change):
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    return player_x
