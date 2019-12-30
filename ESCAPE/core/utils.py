import os

import pygame


def fullname(name):
    return os.path.abspath(name)


def load_image(name, size=None, color_key=None):
    image = pygame.image.load(fullname(name)).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    return image
