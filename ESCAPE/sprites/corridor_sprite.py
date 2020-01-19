import pygame
from ESCAPE.core.base_sprite import BaseSprite
from ESCAPE.core.utils import load_image


class CorridorSprite(BaseSprite):
    def __init__(self, game, x, y, size=None, angle=0):
        images = ['images/corridor/corridor_1.png',
                  'images/corridor/corridor_2.png',
                  'images/corridor/corridor_3.png',
                  'images/corridor/corridor_2.png']

        self.image = load_image('images/corridor/corridor_mask.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 2800

        super().__init__(game, images, x, y, size, angle)
        self.add(game.corridor_group)
        self.anim_fps = 4
