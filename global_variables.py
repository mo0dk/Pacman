from typing import List, TYPE_CHECKING

import pygame

from change_theme import ThemeApi

if TYPE_CHECKING:
    from ghosts.core import MainGhost

coop = 0
instant_win = 0
god = 0
debug = 0
datetime_format = "%d.%m.%Y %H:%M:%S"
orange_trigger = 0
blue_trigger = 0
difficulty = 1
easter = 0
dots = 0
pacs = []
cell_size = 16
cheats = 1
ghosts: List["MainGhost"] = []
theme_api = ThemeApi()

pygame.mixer.init()
# Почему в global_variables.py, а не в game.py? Потому что, файл с музыкой очень большой, и pygame-у нужно время что бы
# его загрузить в память и обработать.
# Зачем нужен open(), почему просто не написать имя файла? Потому что, по крайней мере на Lubuntu файл загружается
# быстрее.
with open("./sounds/pacman_theme.wav", "rb") as file:
    theme_sound = pygame.mixer.Sound(file)

background_channel = pygame.mixer.Channel(5)
background_channel.set_volume(0.4)
