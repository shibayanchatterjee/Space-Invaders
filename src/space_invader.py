import pygame as pyg

from src.screen.screen import Screen

pyg.init()
screen = Screen()


def space_invader():
    # Initialize the game
    screen.initialize()

    # Set the background color

    running = True
    while running:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False
