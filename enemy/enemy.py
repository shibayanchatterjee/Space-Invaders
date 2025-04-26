import pygame as pyg


class Enemy:
    def __init__(self, image_path, x, y):
        self.image = pyg.image.load(image_path)
        self.image = pyg.transform.scale(self.image, (64, 64))
        self.init_x = x
        self.init_y = y
        self.enemy_x, self.enemy_y = self.init_x, self.init_y

    def x_movement(self, x_change):
        self.enemy_x += x_change
        if self.enemy_x <= 0:
            self.enemy_x = 0
        elif self.enemy_x >= 736:
            self.enemy_x = 736

    def y_movement(self, y_change):
        self.enemy_y += y_change
        if self.enemy_y <= 0:
            self.enemy_y = 0
        elif self.enemy_y >= 536:
            self.enemy_y = 536
