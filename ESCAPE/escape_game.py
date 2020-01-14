import pygame

from ESCAPE.core.base_game import BaseGame
from ESCAPE.game_states.personal_room import PersonalRoom
from ESCAPE.game_states.start_screen import StartScreen


class MainGame(BaseGame):
    def __init__(self):
        super().__init__(700, 700)
        self.menu = StartScreen(self)
        self.room = PersonalRoom(self)
        self.all_sprites = pygame.sprite.Group()
        self.start_menu()

    def start_menu(self):
        a = self.menu.start()
        if a == 'titres':
            pass
        elif a == 'start':
            self.game()

    def game(self):
        self.room.start()