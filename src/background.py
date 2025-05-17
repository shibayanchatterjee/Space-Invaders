import pygame as pyg
from pygame import mixer

from .constants import *


def setup_score():
    score_value = 0
    font = pyg.font.Font(SCORE_FONT_TYPE, 20)
    text_x = 10
    text_y = 10
    return font, score_value, text_x, text_y


def setup_caption_icon():
    # Caption and icon
    pyg.display.set_caption(SPACE_INVADERS_TEXT)
    icon = pyg.image.load(SPACE_INVADERS_ICON)
    pyg.display.set_icon(icon)


def pause_game(running, screen):
    paused = True
    while paused:
        pause_button = Button(100, 400, pyg.image.load(PAUSE_BUTTON_IMAGE_PATH))
        pause_button.draw(screen)

        for pause_event in pyg.event.get():
            if pause_event.type == pyg.QUIT:
                running = False
                paused = False
            if pause_event.type == pyg.KEYDOWN and pause_event.key == pyg.K_ESCAPE:
                paused = False
        pyg.time.wait(100)
    return running


def setup_screen_and_sound():
    screen = pyg.display.set_mode((800, 600))
    background = pyg.image.load(BACKGROUND_IMAGE_PATH)
    mixer.music.load(BACKGROUND_MUSIC_PATH)
    mixer.music.play(-1)
    return screen, background


def show_score(screen, x, y, score_value, font):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text(screen, x, y, over_font):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (x, y))


class Button(object):
    def __init__(self, x, y, image):
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


start_button = Button(100, 200, pyg.image.load(START_BUTTON_IMAGE_PATH))
stop_button = Button(100, 300, pyg.image.load(STOP_BUTTON_IMAGE_PATH))
