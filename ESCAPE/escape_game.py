from random import randint

import pygame

from ESCAPE.core.base_game import BaseGame
from ESCAPE.core.camera import Camera
from ESCAPE.game_states.corridor import Corridor
from ESCAPE.game_states.personal_room import PersonalRoom
from ESCAPE.game_states.start_screen import StartScreen
from ESCAPE.game_states.titres import Titres


class MainGame(BaseGame):
    def __init__(self):
        super().__init__(700, 700)
        self.code = [str(randint(0, 9)) for i in range(4)]
        self.personal_code = [-1, -1, -1, -1]
        self.menu = StartScreen(self)
        self.camera = Camera(self)
        self.titres = Titres(self)
        self.room = PersonalRoom(self, self.code)
        self.corridor = Corridor(self, self.code)
        self.door = False
        self.all_sprites = pygame.sprite.Group()
        self.start_menu()

    def start_menu(self):
        a = self.menu.start()
        if a == 'titres':
            self.titres.start()
        elif a == 'start':
            self.game()

    def game(self):
        while not self.door:
            self.room.start()
            self.corridor.start()
