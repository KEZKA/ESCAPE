import pygame

from ESCAPE.core.base_sprite import BaseSprite


class RoomSprite(BaseSprite):
    def __init__(self, game, x, y, size=None, angle=0):
        images = ['images/room.png']
        super().__init__(game, images, x, y, size, angle)

    def check(self, x, y):
        a = [pygame.Rect(0, 0, 700, 202),
             pygame.Rect(0, 202, 120, 288),
             pygame.Rect(571, 202, 129, 85),
             pygame.Rect(0, 675, 470, 25),
             pygame.Rect(561, 675, 139, 25),
             pygame.Rect(163, 579, 225, 121)]
        return not any([i.collidepoint(x,y) for i in a])
