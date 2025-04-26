import pygame as pyg


class Controls:
    def __init__(self):
        self._controls = {}

    def manage_controls(self, event):
        match event:
            case pyg.QUIT:
                return False
            case _:
                print("Invalid event type")
