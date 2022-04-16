import time
import pygame

import global_variables
import player
from game import main
from functools import partial
from global_classes import Button
from global_classes import GuiSettings
from input_name_menu import ask_name
from perfomance import img_load
from settings_menu import settings_menu
from store_score import store_score
from store_score_menu import store_score_menu
from achievement_menu import achievement_menu
from achievements import achievements_save_to_file
from actual_stats import stats_save_to_file

pygame.init()
pygame.mixer.init()

cheats_on_sfx = pygame.mixer.Sound("./sounds/cheats_on.wav")

in_game: bool = False

background_file = f"./textures/bg/{global_variables.theme_api.texture_modifier}pacman2.jpg"


def play():
    global in_game
    in_game = True
    main()
    time.sleep(0.3)  # Костыль
    in_game = False  # Но почему ?
    store_score(player.score, ask_name())
    options_menu()  # Но зачем ?


def exit_game():
    global in_game
    in_game = True
    achievements_save_to_file()
    stats_save_to_file()


def sm():
    global background_file
    settings_menu()
    background_file = f"./textures/bg/{global_variables.theme_api.texture_modifier}pacman2.jpg"

def cheat(key):
    if key == 'd':
        global_variables.debug = 1
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("./sounds/debug_on.wav"))
    if key == 'g':
        global_variables.god = 1
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("./sounds/godmode_on.wav"))
    if key == 'i':
        global_variables.instant_win = 1
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("./sounds/instawin_on.wav"))
    if key == 'c':
        global_variables.coop = 1
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("./sounds/coop_on.wav"))

def options_menu():
    konami = [1073741906, 1073741906, 1073741905, 1073741905, 1073741904, 1073741903, 1073741904, 1073741903, 98, 97]
    text_color = (200,) * 3
    text_font = pygame.font.SysFont("segoeuisemibold", 32)
    try:
        global background_file
        main_screen = pygame.display.set_mode((1066, 600))
        settings = GuiSettings()
        clock = pygame.time.Clock()
        buttons = [
            Button(220 * 0 + 80, 530, 200, 50, (0, 0, 0), settings, "Играть!", play),
            Button(220 * 1 + 80, 530, 200, 50, (0, 0, 0), settings, "Таблица Рекордов", store_score_menu),
            Button(220 * 2 + 80, 530, 200, 50, (0, 0, 0), settings, "Настройки", sm),
            Button(220 * 3 + 80, 530, 200, 50, (0, 0, 0), settings, "Выйти из игры", exit_game),
            Button(220 * 4 + 80, 530, 50, 50, (0, 0, 0), settings, "A", achievement_menu)
        ]
        if global_variables.cheats:
            buttons.append(Button(980, 80,  25, 25, (0, 0, 0), settings, "-d", partial(cheat, 'd')),)
            buttons.append(Button(980, 120, 25, 25, (0, 0, 0), settings, "-g", partial(cheat, 'g')),)
            buttons.append(Button(980, 160, 25, 25, (0, 0, 0), settings, "-i", partial(cheat, 'i')),)
            buttons.append(Button(980, 200, 25, 25, (0, 0, 0), settings, "-c", partial(cheat, 'c')),)
        timeout = 0
        background_file = f"./textures/bg/{global_variables.theme_api.texture_modifier}pacman2.jpg"
        localcombo = konami
        while not in_game:
            timeout += 1
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    achievements_save_to_file()
                    stats_save_to_file()
                    return
                if event.type == pygame.KEYDOWN:
                    if not global_variables.cheats:
                        if event.key == localcombo[0]: 
                            localcombo = localcombo[1:]
                            if len(localcombo)==0:
                                global_variables.cheats = 1
                                pygame.mixer.Channel(1).play(cheats_on_sfx)
                                buttons.append(Button(980, 80,  25, 25, (0, 0, 0), settings, "-d", partial(cheat, 'd')),)
                                buttons.append(Button(980, 120, 25, 25, (0, 0, 0), settings, "-g", partial(cheat, 'g')),)
                                buttons.append(Button(980, 160, 25, 25, (0, 0, 0), settings, "-i", partial(cheat, 'i')),)
                                buttons.append(Button(980, 200, 25, 25, (0, 0, 0), settings, "-c", partial(cheat, 'c')),)
                        else:
                            localcombo = konami
                    if event.key == pygame.K_ESCAPE:
                        exit_game()
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_w] and pressed[pygame.K_t] and pressed[pygame.K_f] and timeout >= 100:
                        if background_file == "./textures/bg/pacman4.jpg":
                            background_file = f"./textures/bg/{global_variables.theme_api.texture_modifier}pacman2.jpg"
                            global_variables.easter = 0
                            timeout = 0
                        elif timeout >= 100:
                            background_file = "./textures/bg/pacman4.jpg"
                            global_variables.easter = 1
                            timeout = 0

            if global_variables.cheats:
                main_screen.blit(text_font.render(f"Cheats on ;)", False, text_color), (850, 20))

            for button in buttons:
                if not in_game and button.update(events) and button.action is exit_game:
                    break
            
            if in_game:
                break

            for button in buttons:
                button.draw(main_screen)

            pygame.display.flip()
            img = img_load(background_file)
            main_screen.blit(img, (0, 0))
            clock.tick(120)
        pygame.quit()
    except KeyboardInterrupt:
        pass
