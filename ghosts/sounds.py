from typing import TypeVar

import pygame.mixer
import global_variables

C = TypeVar("C")


def singleton(class_: C):
    instances = {}

    def get_instance(*args, **kwargs) -> C:
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Sound:
    def __init__(self):
        self.current_sound_index = 1
        self.siren_channel = pygame.mixer.Channel(4)
        self.siren_1 = pygame.mixer.Sound("./sounds/siren_1.wav")
        self.siren_2 = pygame.mixer.Sound("./sounds/siren_2.wav")
        self.siren_3 = pygame.mixer.Sound("./sounds/siren_3.wav")
        self.siren_4 = pygame.mixer.Sound("./sounds/siren_4.wav")
        self.siren_5 = pygame.mixer.Sound("./sounds/siren_5.wav")
        self.power_pellet_sound = pygame.mixer.Sound("./sounds/power_pellet.wav")
        self.playing_energizer = False

    def play_siren(self):
        if self.playing_energizer and not global_variables.easter:
            self.siren_channel.stop()
            self.playing_energizer = False
        if not self.siren_channel.get_busy() and not global_variables.easter:
            if self.current_sound_index == 1:
                self.siren_channel.play(self.siren_1)
            if self.current_sound_index == 2:
                self.siren_channel.play(self.siren_2)
            if self.current_sound_index == 3:
                self.siren_channel.play(self.siren_3)
            if self.current_sound_index == 4:
                self.siren_channel.play(self.siren_4)
            if self.current_sound_index == 5:
                self.siren_channel.play(self.siren_5)

    def play_energizer_sound(self):
        if not self.playing_energizer and not global_variables.easter:
            self.siren_channel.stop()
            self.playing_energizer = True
        if not self.siren_channel.get_busy() and not global_variables.easter:
            self.siren_channel.play(self.power_pellet_sound)
