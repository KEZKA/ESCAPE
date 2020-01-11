import random

import pygame

from ESCAPE.core.base_game_state import BaseGameStates
from ESCAPE.sprites.button_sprite import ButtonSprite
from ESCAPE.sprites.crystal_sprite import CrystalSprite


class StartScreen(BaseGameStates):
    def __init__(self, game):
        super().__init__(game)
        self.FPS = game.FPS
        self.crystal_group = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.button_group = pygame.sprite.Group()
        CrystalSprite(self, 0, 400)
        CrystalSprite(self, 400, 450, size=(250, 250), angle=30)
        CrystalSprite(self, 500, -50, angle=180, size=(250, 250))
        CrystalSprite(self, -80, -50, angle=200, size=(180, 180))
        for k in range(0, 700, 100):
            CrystalSprite(self, -50 + k, 590, size=(120, 120), angle=50)
            CrystalSprite(self, -10 + k, 590, size=(140, 140), angle=-20)
            CrystalSprite(self, 520 - k, -70, size=(120, 120), angle=140)
            CrystalSprite(self, 600 - k, -40, size=(110, 110), angle=190)
        for _ in range(100):
            x, y = random.randint(0, 700), random.randint(0, 700)
            CrystalSprite(self, x, y, size=(5, 5))
        ButtonSprite(self, 200, 200, (300, 50), 'Начать')
        ButtonSprite(self, 200, 300, (300, 50), 'Титры')

    def render(self):
        super().render()
        self.screen.fill(pygame.Color('black'))
        self.crystal_group.draw(self.screen)
        self.crystal_group.update()
        self.button_group.draw(self.screen)
