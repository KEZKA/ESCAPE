import pygame

from ESCAPE.core.base_sprite import BaseSprite
from ESCAPE.core.utils import load_image


class RoomSprite(BaseSprite):
    def __init__(self, game, x, y, size=None, mask='images/room/room_hero_mask.png'):
        images = ['images/room/room.png']

        self.image = load_image(mask)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 700

        super().__init__(game, images, x, y, size)
