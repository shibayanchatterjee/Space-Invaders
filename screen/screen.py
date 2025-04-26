import pygame as pyg

class Screen:
    def __init__(self, width=800, height=600, title='Space Invaders',
                 icon_path='rocket.png'):
        self.width = width
        self.height = height
        self.title = title
        self.icon_path = icon_path
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
        icon = pyg.image.load('../player/rocket.png')
        pyg.display.set_icon(icon)

    def  fill(self):
        self.screen.fill(self.bg_color)

