from functools import partial

import pygame

import global_variables
import store_settings
from game import set_block_size
from global_classes import Button, GuiSettings


def set_easy_difficulty():
    global_variables.difficulty = 0.5


def set_normal_difficulty():
    global_variables.difficulty = 1


def set_hard_difficulty():
    global_variables.difficulty = 1.5


def settings_menu():
    main_screen = pygame.display.set_mode((1066, 600))
    text_color = (255,) * 3
    settings = GuiSettings(button_color=text_color, button_color_hover=(127,) * 3)
    btn_easy = Button(60 + main_screen.get_width() // 4 / 2 + 80, 80, 200, 50,
                      (0, 0, 0), settings, "Лёгкая", set_easy_difficulty)
    btn_norm = Button(260 * 1 + 60 + main_screen.get_width() // 4 / 2 + 80, 80, 200, 50,
                      (0, 0, 0), settings, "Нормальная", set_normal_difficulty)
    btn_hard = Button(260 * 2 + 60 + main_screen.get_width() // 4 / 2 + 80, 80, 200, 50,
                      (0, 0, 0), settings, "Сложная", set_hard_difficulty)
    btn_small = Button(60 + main_screen.get_width() // 4 / 2 + 80, 180, 200, 50,
                       (0, 0, 0), settings, "Маленький", partial(set_block_size, 8))
    btn_med = Button(260 * 1 + 60 + main_screen.get_width() // 4 / 2 + 80, 180, 200, 50,
                     (0, 0, 0), settings, "Средний", partial(set_block_size, 10))
    btn_big = Button(260 * 2 + 60 + main_screen.get_width() // 4 / 2 + 80, 180, 200, 50,
                     (0, 0, 0), settings, "Большой", partial(set_block_size, 16))
    btn_classic_theme = Button(20 + main_screen.get_width() // 4 / 2 + 120, 280, 200, 50,
                               (0, 0, 0), settings, "Классические",
                               partial(setattr, global_variables.theme_api, "textures_mode",
                                       store_settings.TextureSetting.classic))
    btn_alternative_theme = Button(20 + 260 * 1 + main_screen.get_width() // 4 / 2 + 120, 280, 200, 50,
                                   (0, 0, 0), settings, "Альтернативные",
                                   partial(setattr, global_variables.theme_api, "textures_mode",
                                           store_settings.TextureSetting.alternative))
    btn_auto_theme = Button(20 + 260 * 2 + main_screen.get_width() // 4 / 2 + 120, 280, 200, 50,
                            (0, 0, 0), settings, "Автоматические",
                            partial(setattr, global_variables.theme_api, "textures_mode",
                                    store_settings.TextureSetting.automatic))
    buttons = [btn_easy, btn_norm, btn_hard,
               btn_small, btn_med, btn_big,
               btn_classic_theme, btn_alternative_theme, btn_auto_theme]
    text_font = pygame.font.SysFont("segoeuisemibold", 24)
    running = True
    back_color = "black"
    settings_changed = False
    while running:
        if pygame.event.peek(pump=True):
            events = pygame.event.get()
            main_screen.fill(back_color)
            main_screen.blit(
                text_font.render("Настройки", False, text_color),
                (
                    main_screen.get_width() // 2 - text_font.size("Настройки")[0] // 2,
                    20
                )
            )

            dif_str: str
            txt_str: str
            size_str: str
            if global_variables.difficulty == 0.5:
                dif_str = "Легкая"
            elif global_variables.difficulty == 1.5:
                dif_str = "Сложная"
            else:
                dif_str = "Нормальная"
            if global_variables.theme_api.textures_mode is store_settings.TextureSetting.automatic:
                txt_str = "Автоматически"
            elif global_variables.theme_api.textures_mode is store_settings.TextureSetting.classic:
                txt_str = "Классические"
            else:
                txt_str = "Альтернативные"
            if global_variables.cell_size == 8:
                size_str = "Маленький"
            elif global_variables.cell_size == 10:
                size_str = "Средний"
            else:
                size_str = "Большой"

            main_screen.blit(text_font.render("Сложность", False, text_color), (20, 95))
            main_screen.blit(text_font.render("Размер экрана", False, text_color), (20, 195))
            main_screen.blit(text_font.render(f"Настройка текстур", False, text_color), (20, 295))
            main_screen.blit(text_font.render(f"Текущая настройка текстур:  {txt_str}", False, text_color), (20, 350))
            main_screen.blit(text_font.render(f"Текущая сложность:  {dif_str}", False, text_color), (20, 400))
            main_screen.blit(text_font.render(f"Текущий размер экрана:  {size_str}", False, text_color), (20, 450))

            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            for button in buttons:
                if button.update(events):
                    settings_changed = True

            for button in buttons:
                button.draw(main_screen)

            pygame.display.flip()
    if settings_changed:
        store_settings.store_settings()
