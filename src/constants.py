import os

NUM_OF_ENEMIES = 1

SPACE_INVADERS_TEXT = "Space Invaders"
BULLET_READY = "ready"  # Ready - you can't see the bullet on the screen
BULLET_FIRE = "fire"  # Bullet is currently moving

BACKGROUND_IMAGE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'background.png'))
BACKGROUND_MUSIC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'background.wav'))
PLAYER_IMAGE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'rocket.png'))
SPACE_INVADERS_ICON = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'space-invaders.png'))
EXPLOSION_SOUND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'explosion.wav'))
BULLET_SOUND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'laser.wav'))
BULLET_IMAGE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'bullet.png'))
ENEMY_IMAGE_RED_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'ghost-red.png'))
ENEMY_IMAGE_BLUE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'ghost-blue.png'))
ENEMY_IMAGE_BLACK_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'ghost-black.png'))
START_BUTTON_IMAGE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'start-button.png'))
STOP_BUTTON_IMAGE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'stop-button.png'))
PAUSE_BUTTON_IMAGE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src', 'utils', 'pause-button.png'))

SCORE_FONT_TYPE = 'freesansbold.ttf'
