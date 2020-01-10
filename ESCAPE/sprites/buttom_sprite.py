import pygame

from ESCAPE.core.base_sprite import BaseSprite


class ButtomSprite(BaseSprite):
    def __init__(self, game, x, y, size, text):
        images = []
        self.img = pygame.Surface(size)
        self.img.get_width()
        self.img.fill(pygame.Color(51,150,200))
        self.interior_rect=(5,5, size[0] - 10, size[1] - 10)
        self.img.fill(pygame.Color(102, 217, 255), rect=self.interior_rect)
        super().__init__(game, images, x, y, size, angle=0)
        self.add(game.buttom_group)
        self.anim_fps = 0
        font = pygame.font.Font(None, 30)
        text = font.render(text, 1, pygame.Color('white'))
        self.img.blit(text, (10,  10))

    def mouse(self):
        self.img.fill(pygame.Color(40, 119, 158), rect=self.interior_rect)

    def append_image(self, images, size, angle):
        self.sprites.append(self.img)

    def update(self):
        pass