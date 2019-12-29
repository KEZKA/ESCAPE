import pygame

from ESCAPE.core.base_game_state import BaseGameStates


class StartScreen(BaseGameStates):
    def __init__(self, game):
        super().__init__(game)

    def render(self):
        super().render()
        self.game.screen.fill(pygame.Color('black'))