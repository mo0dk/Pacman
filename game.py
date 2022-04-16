import pygame
import time

import global_variables
import player
# from change_theme import ThemeApi
from ghosts.blue_ghost import BlueGhostLogic
from ghosts.core import MainGhost
from ghosts.orange_ghost import OrangeGhostLogic
from ghosts.pink_ghost import PinkGhostLogic
from ghosts.red_ghost import RedGhostLogic
from ghosts.sounds import Sound
from layouts import map_with_sprites
from layouts import simplified
from perfomance import img_load
from achievements import achievements
from actual_stats import stats

resolution = w, h = 224 / 8 * global_variables.cell_size, 336 / 8 * global_variables.cell_size
last_time = 0
local_stage = 1


def render(window, matrix):  # Моя функция рендера карты и зёрен
    for i in range(len(matrix)):  # Y
        for j in range(len(matrix[i])):
            # X
            if matrix[i][j] == 5:
                pygame.draw.rect(
                    window, (0, 0, 0),
                    (global_variables.cell_size * j, global_variables.cell_size * i + 50,
                     global_variables.cell_size, global_variables.cell_size),
                    1
                )
                # Пустота окрашивается в чёрное   но зачем ?
            else:
                window.blit(
                    img_load(f'./textures/walls/{global_variables.theme_api.texture_modifier}{matrix[i][j]}.png',
                             global_variables.cell_size, global_variables.cell_size
                             ),
                    (global_variables.cell_size * j, global_variables.cell_size * i + 50)
                )
                # Всё остальное отрисовывается


def pause(clock: pygame.time.Clock, screen):
    global last_time
    global local_stage
    save = pygame.time.get_ticks()
    paused = True
    pygame.mixer.pause()
    pause_icon = img_load(f'./textures/pause.png')
    print("Game paused...")
    while paused:
        if pygame.time.get_ticks() % 1000 < 500:
            screen.blit(pause_icon, (screen.get_width() - 32, 0))
        else:
            screen.fill((0, 0, 0), (screen.get_width() - 32, 0, 32, 32))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print("Resuming...")
                    paused = False
                    pygame.mixer.unpause()
                    last_time += pygame.time.get_ticks() - save
        pygame.display.update()
        clock.tick(120)


def set_block_size(new_cell_size: int):
    global_variables.cell_size = new_cell_size
    global resolution, w, h
    resolution = w, h = 224 / 8 * global_variables.cell_size, 336 / 8 * global_variables.cell_size


def main():
    player.game_simplified_map = [i.copy() for i in map_with_sprites]
    player.game_map = [i.copy() for i in simplified]
    player.score = 0
    global_variables.dots = 0
    screen = pygame.display.set_mode(resolution)
    done = False
    pac1 = player.Pacman(
        w / 2 - (global_variables.cell_size / 2),
        h / 2 + 0.75 * global_variables.cell_size * global_variables.cell_size +
        global_variables.cell_size - (5 + global_variables.cell_size / 8 / 4) * global_variables.cell_size * (
                global_variables.cell_size / 8),
        screen,
        1
    )
    global_variables.pacs = [pac1]
    if global_variables.coop:
        pac2 = player.Pacman(
            w / 2 - (global_variables.cell_size / 2),
            h / 2 - (10 * global_variables.cell_size),
            screen,
            2)
        global_variables.pacs.append(pac2)
    flag = 0

    global last_time
    global local_stage

    if not global_variables.coop:
        orange_ghost = MainGhost(OrangeGhostLogic, screen)
        red_ghost = MainGhost(RedGhostLogic, screen)
        pink_ghost = MainGhost(PinkGhostLogic, screen)
        blue_ghost = MainGhost(BlueGhostLogic, screen)
        global_variables.ghosts = [orange_ghost, red_ghost, pink_ghost, blue_ghost]

    audio_sound = pygame.mixer.Sound("./sounds/game_start.wav")
    if global_variables.easter:
        audio_sound = pygame.mixer.Sound("./sounds/game_start_e.wav")

    audio_channel = pygame.mixer.Channel(0)
    audio_channel.play(audio_sound)

    if global_variables.easter:
        global_variables.theme_sound = pygame.mixer.Sound("./sounds/paradise_lost.wav")

    clock = pygame.time.Clock()
    stage = 1

    if not global_variables.coop:
        for ghost in global_variables.ghosts:
            global_variables.blue_trigger = 0
            global_variables.orange_trigger = 0
            ghost.reset_position()

    Sound().current_sound_index = 1

    start = time.monotonic()
    while not done:
        if not audio_channel.get_busy() and not global_variables.background_channel.get_busy():
            print("a")
            global_variables.background_channel.play(global_variables.theme_sound)
        trigger = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    pygame.mixer.pause()
                for pac in global_variables.pacs:
                    if not audio_channel.get_busy() and not pac.dead_channel.get_busy() and \
                            not pac.win_channel.get_busy():
                        pac.process_event(event)
                if event.key == pygame.K_p:
                    pause(clock, screen)
        screen.fill((0, 0, 0))
        render(screen, player.game_simplified_map)
        # MainGhost.draw_trigger_blocks(screen)
        if not global_variables.coop:
            for ghost in global_variables.ghosts:
                ghost.draw(screen)

            if global_variables.ghosts[0].scared and not flag:
                if global_variables.debug:
                    print("Scare detected")
                last_time += 7000
                flag = 1
            if local_stage == 1:
                if pygame.time.get_ticks() - last_time >= 20000:
                    local_stage = 2
                    flag = 0
                    if global_variables.debug:
                        print("Set AI mode runaway")
                    for ghost in global_variables.ghosts:
                        if ghost.ghost_logic.stay == 0:
                            ghost.ghost_logic.stage = 2
                            stage = 2
                    last_time = pygame.time.get_ticks()
            if local_stage == 2:
                if pygame.time.get_ticks() - last_time >= 7000:
                    local_stage = 1
                    flag = 0
                    if global_variables.debug:
                        print("Set AI mode chase")
                    for ghost in global_variables.ghosts:
                        if ghost.ghost_logic.stay == 0:
                            ghost.ghost_logic.stage = 1
                            stage = 1
                    last_time = pygame.time.get_ticks()

        elif not audio_channel.get_busy() and not pac1.dead and not pac1.win:
            for pac in global_variables.pacs:
                pac.upd([])

        for pac in global_variables.pacs:
            if pygame.time.get_ticks() % 500 < 250 or not audio_channel.get_busy() and not pac.paused:
                pac.draw()
            if not audio_channel.get_busy() and not pac.dead and not pac.win and \
                    not global_variables.coop and not pac.paused:
                if pac.in_energizer:
                    Sound().play_energizer_sound()
                else:
                    Sound().play_siren()
                pac.upd(global_variables.ghosts)
                for ghost in global_variables.ghosts:
                    ghost.update(pac, global_variables.ghosts, stage, trigger)

            elif pac.paused:
                if pygame.time.get_ticks() - pac.paused_time >= 2500 + 3500 * global_variables.easter:
                    pac.paused = 0
                    pac.paused_frame = 0
                    pac.status = 'unhit'
                    pac.vec = 0
                if pygame.time.get_ticks() % 500 < 250:
                    pac.status_eat = 0
                    pac.draw()

            done = done or (pac.dead and not pac.play_dead_sound()) or (pac.win and not pac.play_win_sound())

            if done:
                playtime = time.monotonic() - start
                stats['playtime'] += round(playtime)
            if pac.win:
                playtime = time.monotonic() - start
                if playtime <= 60:
                    achievements[3].Get()

        pygame.display.flip()
        clock.tick(120)
