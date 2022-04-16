from dataclasses import dataclass
from typing import Tuple

import pygame


class Button:
    def __init__(self, x, y, width, height, outline, settings, text="", action=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.settings = settings
        self.action = action
        self.outline = outline

    def draw(self, screen):
        if self.outline:
            pygame.draw.rect(screen, self.outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        color = self.settings.button_color if not self.is_over(
            pygame.mouse.get_pos()) else self.settings.button_color_hover
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            pygame.font.init()
            font = pygame.font.SysFont('segoeuisemibold', self.settings.text_size)
            text = font.render(self.text, True, (0, 0, 0))
            screen.blit(
                text,
                (
                    self.x + (self.width / 2 - text.get_width() / 2),
                    self.y + (self.height / 2 - text.get_height() / 2)
                )
            )

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN \
                    and self.is_over(pygame.mouse.get_pos()) \
                    and self.action:
                self.action()
                return True
        return False

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


@dataclass
class GuiSettings:
    text_size: int = 20
    button_color: Tuple[int, int, int] = (93, 0, 255)
    button_color_hover: Tuple[int, int, int] = (174, 127, 255)

# class GuiSettingsForOptions:
#     def __init__(self):
#         self.text_size = 20
#         self.button_color = (255, 255, 255)
#         self.button_color_hover = (120, 120, 120)
