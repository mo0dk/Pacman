import pygame

from global_variables import datetime_format
from store_score import get_scores, max_store


def render_scores(main_screen: pygame.Surface, text_font: pygame.font.Font, color):
    scores = list(get_scores())
    if scores:
        max_len_index = len(str(len(scores) + 1))
        max_len_datetime = len(
            max(scores, key=lambda item: len(item.datetime.strftime(datetime_format))).datetime.strftime(
                datetime_format)
        )
        max_len_nickname = len(max(scores, key=lambda item: len(item.nickname)).nickname)
        for index, score in enumerate(get_scores()):
            text = f"{str(index + 1): <{max_len_index}} " \
                   f"{score.datetime.strftime(datetime_format): <{max_len_datetime}} " \
                   f"{score.nickname: <{max_len_nickname}} " \
                   f"{score.score}"
            pos = (
                round(main_screen.get_width() * 0.0140),
                main_screen.get_height() // (max_store + 1) * (index + 2)
            )
            main_screen.blit(
                text_font.render(text, False, color),
                pos
            )


def store_score_menu():
    main_screen = pygame.display.set_mode((1066, 600))
    running = True
    pygame.font.init()
    text_font = pygame.font.SysFont("Consolas", 32)

    back_color = "black"
    text_color = "white"
    while running:
        if pygame.event.peek(pump=True):
            main_screen.fill(back_color)

            main_screen.blit(
                text_font.render("Таблица рекордов", False, text_color),
                (
                    main_screen.get_width() // 2 - text_font.size("Таблица рекордов")[0] // 2,
                    main_screen.get_height() // (max_store + 1)
                )
            )
            render_scores(main_screen, text_font, text_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            pygame.display.flip()
