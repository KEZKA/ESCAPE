import pygame

from ESCAPE.core.base_sprite import BaseSprite
from ESCAPE.core.utils import load_font


class ButtonSprite(BaseSprite):
    def __init__(self, game, x, y, size, text, function):
        images = []
        self.function = function
        self.img = pygame.Surface(size)
        self.img.fill(pygame.Color(51, 150, 200))
        self.interior_rect = (5, 5, size[0] - 10, size[1] - 10)
        self.img.fill(pygame.Color(102, 217, 255), rect=self.interior_rect)
        self.img_button_down = pygame.Surface(size)
        self.img_button_down.fill(pygame.Color(51, 150, 200))
        self.img_button_down.fill(pygame.Color(40, 119, 158), rect=self.interior_rect)
        super().__init__(game, images, x, y, size, angle=0)
        self.add(game.button_group)
        font = load_font('fonts/game_font.ttf', 40)
        text = font.render(text, 1, pygame.Color('white'))
        self.img.blit(text, ((size[0] - text.get_width()) // 2, 0))
        self.img_button_down.blit(text, ((size[0] - text.get_width()) // 2, 0))
        self.flag = False

    def append_image(self, images, size, angle):
        self.sprites.append(self.img)
        self.sprites.append(self.img_button_down)

    def update(self, event):
        if pygame.sprite.spritecollideany(self, self.game.arrow) and self.flag:
            self.function()
        elif pygame.sprite.spritecollideany(self, self.game.arrow):
            super().update()
            self.flag = True

