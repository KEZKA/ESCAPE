import pygame

from ESCAPE.core.utils import load_image


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, game, images, x, y, size=None):
        super().__init__(game.all_sprites)
        self.FPS = game.FPS
        self.ticks = 0
        self.cur_frame = 0
        self.sprites = []
        self.anim_fps = 20
        self.append_image(images, size)
        self.rect = self.rect.move(x,y)

    def append_image(self, images, size=None):
        for image in images:
            self.sprites.append(load_image(image, size))

    def update(self):
        if self.ticks % (self.FPS // self.anim_fps) == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.sprites)
            self.image = self.sprites[self.cur_frame]
