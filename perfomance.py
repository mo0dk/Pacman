from functools import lru_cache

import pygame.image


@lru_cache
def img_load(path, x=-1, y=-1):
    img = pygame.image.load(path)
    if x > 0 and y > 0:
        img = pygame.transform.scale(img, (x, y))
    img = img.convert_alpha()
    return img
