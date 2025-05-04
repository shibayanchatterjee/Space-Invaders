import pygame as pyg

import src.player.player as Player

player = Player.Player()

# Constants
SCREEN_ICON_PATH = '.\src\screen\space-invaders.png'

class Screen:
    def __init__(self, width=800, height=600, title='Space Invaders'):
        self.width = width
        self.height = height
        self.title = title
        self.icon_path = SCREEN_ICON_PATH
        self.bg_color = (200, 200, 200)
        self.screen = None
        self.icon = None

    def initialize(self):
        self.screen = pyg.display.set_mode((self.width, self.height))
        pyg.display.set_caption(self.title)
        self.icon = pyg.image.load(self.icon_path)
        pyg.display.set_icon(self.icon)

        self.width = 800
        self.height = 600
        self.screen = pyg.display.set_mode((self.width, self.height))
        pyg.display.set_caption('Space Invaders')
        pyg.display.set_icon(self.icon)

    def  fill(self):
        self.screen.fill(self.bg_color)

