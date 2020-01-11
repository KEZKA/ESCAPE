import os
import pygame

<<<<<<< HEAD
# TODO: непонятно что это за фигня полное имя картинки не загружается как надо(когда не указывешь в ручную полный путь)

=======
>>>>>>> KEZKA
def fullname(name):
    return os.path.join(os.path.dirname(__file__), '..', 'resources', name)


def load_image(name, size=None, angle=0):
<<<<<<< HEAD
    image = pygame.image.load(name)
=======
    image = pygame.image.load(fullname(name))
>>>>>>> KEZKA
    if size:
        image = pygame.transform.scale(image, size)
        image = pygame.transform.rotate(image, angle)
    return image

