import pygame

from ESCAPE.core.base_game import BaseGame
from ESCAPE.game_states.start_screen import StartScreen


class MainGame(BaseGame):
    def __init__(self):
        super().__init__(700, 700)
        self.menu = StartScreen(self)
        self.all_sprites = pygame.sprite.Group()
        self.start_game()

    def start_game(self):
        self.menu.start()
