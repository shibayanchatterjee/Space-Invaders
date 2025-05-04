import pygame as pyg

# Constants
PLAYER_PATH = r'.\src\player\rocket.png'


class Player:
    def __init__(self):
        self.player_img = pyg.image.load(PLAYER_PATH)
        self.player_init_x = 370
        self.player_init_y = 480
        self.player_x, self.player_y = self.player_init_x, self.player_init_y

    def x_movement(self, x_change):
        self.player_x += x_change
        if self.player_x <= 0:
            self.player_x = 0
        elif self.player_x >= 736:
            self.player_x = 736

    def y_movement(self, y_change):
        self.player_y += y_change
        if self.player_y <= 0:
            self.player_y = 0
        elif self.player_y >= 536:
            self.player_y = 536
