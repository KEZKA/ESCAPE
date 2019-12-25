import pygame

from ESCAPE.core.base_process import BaseGameProcess


class StartScreen(BaseGameProcess):
    def __init__(self, game):
        super().__init__(game)

    def render(self):
        super().render()
        self.game.screen.fill(pygame.Color('black'))