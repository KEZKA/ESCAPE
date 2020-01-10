import pygame

from ESCAPE.core.utils import load_image


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, game, images, x, y, size=None, angle=0):
        super().__init__(game.all_sprites)
        self.FPS = game.FPS
        self.ticks = 0
        self.cur_frame = 0
        self.sprites = []
        self.anim_fps = 20
        self.append_image(images, size, angle)
        self.rect = self.sprites[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = self.sprites[self.cur_frame]

    def append_image(self, images, size, angle):
        for image in images:
            img = load_image(image, size, angle=angle)
            self.sprites.append(img)

    def update(self):
        if self.ticks % (self.FPS // self.anim_fps) == 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.sprites)
            self.image = self.sprites[self.cur_frame]
        self.ticks += 1
