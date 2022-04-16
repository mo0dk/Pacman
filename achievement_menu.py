import pygame

from actual_stats import stats
from achievements import achievements

def statsTest():
    if stats['kills'] <= achievements[0].goal:
        achievements[0].current = stats['kills']
    else:
        achievements[0].current = achievements[0].goal
    if stats['wins'] <= achievements[1].goal:
        achievements[1].current = stats['wins']
    else:
        achievements[1].current = achievements[1].goal
    if stats['playtime'] <= achievements[2].goal:
        achievements[2].current = stats['playtime']
    else:
        achievements[2].current = achievements[2].goal

def render_achievements(screen: pygame.Surface, color):
    ach_name_font = pygame.font.SysFont("Consolas", 32)
    ach_desc_font = pygame.font.SysFont("Consolas", 24)
    topY = 100
    for i in range(len(achievements)):
        if achievements[i].progress() < 0.5:
            progressBarColor = (200, 400 * achievements[i].progress(), 0)
        else:
            progressBarColor = (400 * (1 - achievements[i].progress()), 200, 0)
        pygame.draw.rect(screen, (200, 200, 200), (133, topY + 100 * i, 800, 75), 3)
        pygame.draw.rect(screen, progressBarColor, (135, topY + 2 + 100 * i, 796 * achievements[i].progress(), 71))
        name = achievements[i].name
        namePos = (150, topY + 5 + 100 * i)
        screen.blit(ach_name_font.render(name, False, color), namePos)
        desc = achievements[i].description
        descPos = (150, topY + 45 + 100 * i)
        screen.blit(ach_desc_font.render(desc, False, color), descPos)
        if achievements[i].countable:
            progress = f"{achievements[i].current} / {achievements[i].goal} ({round(achievements[i].progress() * 100, 1)}%)"
            progressPos = (650, topY + 45 + 100 * i)
            screen.blit(ach_desc_font.render(progress, False, color), progressPos)

def achievement_menu():
    statsTest()
    screen = pygame.display.set_mode((1066, 600))
    running = True
    pygame.font.init()
    head_font = pygame.font.SysFont("Consolas", 48)

    back_color = "black"
    text_color = "white"
    while running:
        if pygame.event.peek(pump=True):
            screen.fill(back_color)

            screen.blit(head_font.render("Достижения", False, text_color), (screen.get_width() // 2 - head_font.size("Достижения")[0] // 2, 20))
            render_achievements(screen, text_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            pygame.display.flip()
