import pygame

from .background import *
from .bullet import *
from .enemy import *
from .player import *


def space_invader():
    pyg.init()
    global screen

    screen, background = setup_screen_and_sound()
    setup_caption_icon()
    font, score_value, text_x, text_y = setup_score()
    over_font = pyg.font.Font(SCORE_FONT_TYPE, 64)

    player_x, player_x_change, player_y, player_y_change, scaled_img = setup_player()
    enemy_images, enemy_x, enemy_x_change, enemy_y, enemy_y_change = setup_enemy()
    bullet_img, bullet_state, bullet_x, bullet_y, bullet_y_change = setup_bullet()

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    running = pause_game(running, screen)
                elif event.key == pyg.K_LEFT:
                    player_x_change = -5
                if event.key == pygame.K_RIGHT:
                    player_x_change = 5
                elif event.key == pyg.K_SPACE and bullet_state == BULLET_READY:
                    bullet_sound = mixer.Sound(BULLET_SOUND_PATH)
                    bullet_sound.play()
                    bullet_x = player_x + 28
                    bullet_y = player_y + 33
                    fire_bullet(screen, bullet_x, bullet_y, bullet_img)
            elif event.type == pygame.KEYUP and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                player_x_change = 0

        player_x = player_movement(player_x, player_x_change)

        # Enemy movement
        for i in range(NUM_OF_ENEMIES):
            # Game Over
            if enemy_y[i] > 440:
                for j in range(NUM_OF_ENEMIES):
                    enemy_y[j] = 2000
                game_over_text(screen, 200, 250, over_font)
                break

            # Enemy movement and direction change
            enemy_x[i] += enemy_x_change[i]
            if enemy_x[i] <= 0 or enemy_x[i] >= 736:
                enemy_x_change[i] *= -1
                enemy_y[i] += enemy_y_change[i]

            # Collision
            collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
            if collision:
                explosion_sound = mixer.Sound(
                    EXPLOSION_SOUND_PATH)
                explosion_sound.play()
                bullet_y = 480
                bullet_state = BULLET_READY
                score_value += 1
                enemy_x[i] = random.randint(0, 735)
                enemy_y[i] = random.randint(50, 150)

            enemy(screen, enemy_x[i], enemy_y[i], enemy_images[i])
        bullet_state, bullet_y = reset_bullet_state(bullet_img, bullet_state, bullet_x, bullet_y, bullet_y_change,
                                                    screen)

        player(screen, player_x, player_y, player_img=scaled_img)
        show_score(screen, text_x, text_y, score_value, font)
        pyg.display.update()
