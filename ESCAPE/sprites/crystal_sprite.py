import pygame
from ESCAPE.core.base_sprite import BaseSprite


class CrystalSprite(BaseSprite):
    def __init__(self,game, x, y, size=None):
        images = ['crystal_1.png','crystal_2.png','crystal_3.png','crystal_4.png',
                  'crystal_5.png','crystal_6.png','crystal_7.png','crystal_8.png']
        super().__init__(game, images, x, y, size)
        self.anim_fps = 5
