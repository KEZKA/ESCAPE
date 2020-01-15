from random import randint

import pygame

from ESCAPE.core.base_game_state import BaseGameStates
from ESCAPE.sprites.crystal_sprite import CrystalSprite
from ESCAPE.sprites.hero_sprite import HeroSprite
from ESCAPE.sprites.room_sprite import RoomSprite
from ESCAPE.sprites.rubbish_sprites import NoteInRubbish, RubbishSprite


class PersonalRoom(BaseGameStates):
    def __init__(self, game):
        super().__init__(game)
        self.FPS = game.FPS
        self.hero_group = pygame.sprite.Group()
        self.crystal_group = pygame.sprite.Group()
        self.rubbish_group = pygame.sprite.Group()
        self.screen_img = RoomSprite(self, 0, 0)
        NoteInRubbish(self, 350, 350)
        CrystalSprite(self, 590, 15, (50, 50))
        CrystalSprite(self, 597, 19, (30, 30))
        CrystalSprite(self, 570, 45, (40, 40), angle=30)
        CrystalSprite(self, 615, 70, (30, 30), angle=-20)
        self.hero = HeroSprite(self, 350, 350, size=(100, 100))
        while len(self.rubbish_group) != 200:
            x, y, angle = randint(200, 650), randint(0, 700), randint(0, 360)
            RubbishSprite(self, x, y, angle=angle)

    def render(self):
        super().render()
        self.screen.fill(pygame.Color('black'))
        self.screen.blit(self.screen_img.image, (0, 0))
        self.crystal_group.draw(self.screen)
        self.crystal_group.update()
        self.rubbish_group.update()
        self.rubbish_group.draw(self.screen)
        self.hero_group.draw(self.screen)

    def handle_event(self, event):
        super().handle_event(event)
        self.hero.get_event(event)
