import pygame

from ESCAPE.core.base_sprite import BaseSprite
from ESCAPE.core.utils import load_font


class TextSprite(BaseSprite):
    def __init__(self, game, x, y, size, texts):
        images = []
        self.screen_text = pygame.Surface(size)
        self.screen_text.fill(pygame.Color(102, 217, 255))
        self.interior_rect = (5, 5, size[0] - 10, size[1] - 10)
        self.screen_text.fill(pygame.Color('black'), rect=self.interior_rect)
        super().__init__(game, images, x, y, size, angle=0)
        self.add(game.text_group)
        font = load_font('fonts/game_font.ttf', 35)
        y = 0
        for text in texts.split('\n'):
            text = font.render(text, 1, pygame.Color(102, 217, 255))
            self.screen_text.blit(text, ((size[0] - text.get_width()) // 2, y))
            y += text.get_height() + 20

    def append_image(self, images, size, angle):
        self.sprites.append(self.screen_text)
