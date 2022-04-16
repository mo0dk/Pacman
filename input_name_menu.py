import pygame

import global_variables


def _remove_one_symbol(string):
    return string[:len(string) - 1]


def ask_name():
    if not global_variables.coop:
        main_screen = pygame.display.set_mode((1066, 600))
        clock = pygame.time.Clock()
        running = True

        text_font = pygame.font.SysFont("Arial", 46)
        result = ""
        frame = 0
        backspace_pressed = False
        time_when_backspace_pressed = None
        any_symbol_pressed = False
        symbol = ""
        time_when_any_symbol_pressed = None
        while running:
            frame += 1
            clock.tick(30)
            pygame.display.flip()
            main_screen.fill("black")

            pygame.draw.rect(main_screen, (33,) * 3, (0, 300, 1066, 46))
            text_width = text_font.size(result)[0]
            if frame % 24 <= 24 / 2:
                pygame.draw.rect(main_screen, "black", (text_width, 300, 0, 46), 1)
            main_screen.blit(
                text_font.render("Введите своё имя", False, "white"),
                (1066 // 2 - text_font.size("Введите своё имя")[0] // 2, 100)
            )
            main_screen.blit(
                text_font.render(result, False, "white"), (0, 300)
            )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # result = result.strip()
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        running = False
                    elif event.key == pygame.K_BACKSPACE:
                        result = _remove_one_symbol(result)
                        backspace_pressed = True
                        time_when_backspace_pressed = pygame.time.get_ticks()
                    else:
                        symbol = event.unicode
                        if event.key == pygame.K_TAB:
                            symbol = " " * 4
                        result += symbol
                        any_symbol_pressed = True
                        time_when_any_symbol_pressed = pygame.time.get_ticks()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_BACKSPACE:
                        backspace_pressed = False
                    if event.unicode == symbol:
                        any_symbol_pressed = False
                        symbol = ""

            if backspace_pressed and pygame.time.get_ticks() - time_when_backspace_pressed >= 500:
                if frame % 2 == 0:
                    result = _remove_one_symbol(result)
            if any_symbol_pressed and pygame.time.get_ticks() - time_when_any_symbol_pressed >= 500:
                if frame % 2 == 0:
                    result += symbol
        return result

    if global_variables.coop:
        main_screen = pygame.display.set_mode((1066, 600))
        clock = pygame.time.Clock()
        running = True

        text_font = pygame.font.SysFont("Arial", 46)
        result = ""
        frame = 0
        while running:
            frame += 1
            clock.tick(30)
            pygame.display.flip()
            main_screen.fill("black")
            win_score = ''
            text = ''
            if global_variables.pacs[0].score > global_variables.pacs[1].score:
                text = "Победа игрока 1"
                win_score = str(global_variables.pacs[0].score)
            elif global_variables.pacs[0].score < global_variables.pacs[1].score:
                text = "Победа игрока 2"
                win_score = str(global_variables.pacs[1].score)
            elif global_variables.pacs[0].score == global_variables.pacs[1].score:
                text = "Ничья"
                win_score = str(global_variables.pacs[1].score)
            if global_variables.pacs[0].lives == 0:
                text = "Победа игрока 2"
                win_score = str(global_variables.pacs[1].score)
            elif global_variables.pacs[1].lives == 0:
                text = "Победа игрока 1"
                win_score = str(global_variables.pacs[0].score)
            win_score += " очков"
            main_screen.blit(
                text_font.render(text, False, "white"),
                (1066 // 2 - text_font.size(text)[0] // 2, 100)
            )
            main_screen.blit(
                text_font.render("Игрок 1", False, "white"), (100, 250)
            )
            main_screen.blit(
                text_font.render(str(global_variables.pacs[0].score) + " очков", False, "white"), (100, 300)
            )
            main_screen.blit(
                text_font.render(str(global_variables.pacs[0].lives) + " жизней", False, "white"), (100, 350)
            )
            main_screen.blit(
                text_font.render("Игрок 2", False, "white"), (750, 250)
            )
            main_screen.blit(
                text_font.render(str(global_variables.pacs[1].score) + " очков", False, "white"), (750, 300)
            )
            main_screen.blit(
                text_font.render(str(global_variables.pacs[1].lives) + " жизней", False, "white"), (750, 350)
            )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # result = result.strip()
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN or \
                            event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                        running = False
        return result
