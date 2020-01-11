import os
import pygame


def fullname(name):
    return os.path.join(os.path.dirname(__file__), '..', 'resources', name)


def load_image(name, size=None, angle=0):
    image = pygame.image.load(fullname(name))
    if size:
        image = pygame.transform.scale(image, size)
        image = pygame.transform.rotate(image, angle)
    return image


def load_font(name, size):
    font = pygame.font.Font(fullname(name), size)
    return font
