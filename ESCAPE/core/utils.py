import os
import pygame

# TODO: непонятно что это за фигня полное имя картинки не загружается как надо(когда не указывешь в ручную полный путь)

def fullname(name):
    return os.path.abspath(name)


def load_image(name, size=None, angle=0):
    image = pygame.image.load(name)
    if size:
        image = pygame.transform.scale(image, size)
        image = pygame.transform.rotate(image, angle)
    return image

