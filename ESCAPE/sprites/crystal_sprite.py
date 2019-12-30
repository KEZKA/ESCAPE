import pygame
from ESCAPE.core.base_sprite import BaseSprite


class CrystalSprite(BaseSprite):
    def __init__(self):
        super().__init__()
        self.append_image(['crystal\crystal_{}.png'.format(number)
                           for number in range(1, 9)], (100, 100))
        self.anim_fps = 5

        self.rect = pygame.Rect(0, 0, 100, 100)
        self.cur_frame = 0
        self.image = self.sprites[self.cur_frame]
