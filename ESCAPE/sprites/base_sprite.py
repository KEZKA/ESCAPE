from ESCAPE.core.utils import load_image
from ESCAPE.core.base_game import BaseGame
import pygame

all_sprites = pygame.sprite.Group()


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)

        self.FPS = BaseGame(700, 700).FPS
        self.ticks = 0

        self.sprites = []
        self.anim_fps = 20

    def append_image(self, images, size=-1):
        for image in images:
            self.sprites.append(load_image(image, size))

    def update(self):
        if self.ticks % (self.FPS // self.anim_fps) == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.sprites)
            self.image = self.sprites[self.cur_frame]
