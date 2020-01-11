import pygame

from ESCAPE.core.base_sprite import BaseSprite
from ESCAPE.core.utils import load_font


class ButtonSprite(BaseSprite):
    def __init__(self, game, x, y, size, text):
        images = []
        self.img = pygame.Surface(size)
        self.img.get_width()
        self.img.fill(pygame.Color(51, 150, 200))
        self.interior_rect = (5, 5, size[0] - 10, size[1] - 10)
        self.img.fill(pygame.Color(102, 217, 255), rect=self.interior_rect)
        super().__init__(game, images, x, y, size, angle=0)
        self.add(game.button_group)
        self.anim_fps = 0
        font = load_font('fonts/game_font.ttf', 40)
        text = font.render(text, 1, pygame.Color('white'))
        self.img.blit(text, ((size[0] - text.get_width()) // 2, 0))

    def mouse(self):
        self.img.fill(pygame.Color(40, 119, 158), rect=self.interior_rect)

    def append_image(self, images, size, angle):
        self.sprites.append(self.img)

    def update(self):
        pass
