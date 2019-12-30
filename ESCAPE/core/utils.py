import os
import pygame


def load_image(name, size=-1, color_key=None):
    fullname = os.path.join('..', 'resources', 'images', name)
    image = pygame.image.load(fullname).convert_alpha()
    if size != -1:
        image = pygame.transform.scale(image, size)
    return image

