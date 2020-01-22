import random

import pygame

from ESCAPE.core.base_game_state import BaseGameStates
from ESCAPE.core.utils import fullname
from ESCAPE.sprites.button_sprite import ButtonSprite
from ESCAPE.sprites.crystal_sprite import CrystalSprite


class StartScreen(BaseGameStates):
    def __init__(self, game):
        super().__init__(game)
        self.FPS = game.FPS
        pygame.mixer.music.load(fullname('music/background.mp3'))
        pygame.mixer.music.play(-1)
        self.crystal_group = pygame.sprite.Group()
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
        ButtonSprite(self, 200, 200, (300, 50), 'Начать', self.start_bt)
        ButtonSprite(self, 200, 300, (300, 50), 'Об авторах', self.titres)
        ButtonSprite(self, 200, 400, (300, 50), 'Выход', self.game.terminate)


    def render(self):
        super().render()
        self.screen.fill(pygame.Color('black'))
        self.crystal_group.draw(self.screen)
        self.crystal_group.update()
        self.button_group.draw(self.screen)
        self.arrow.draw(self.screen)

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                self.button_group.update(event)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                self.button_group.update(event)

    def start_bt(self):
        self.stop()
        self.btn = 'start'

    def titres(self):
        self.stop()
        self.btn = 'titres'

    def execution(self):
        super().execution()
        return self.btn

    def start(self):
        self.is_running = True
        return self.execution()
