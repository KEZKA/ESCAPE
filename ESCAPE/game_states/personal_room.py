from random import randint

import pygame

from ESCAPE.core.base_game_state import BaseGameStates
from ESCAPE.core.utils import fullname
from ESCAPE.sprites.clothes_sprite import ClothesSprite
from ESCAPE.sprites.crystal_sprite import CrystalSprite
from ESCAPE.sprites.hero_sprite import HeroSprite
from ESCAPE.sprites.notes_on_board import Notes
from ESCAPE.sprites.room_sprite import RoomSprite
from ESCAPE.sprites.rubbish_sprites import RubbishSprite
from ESCAPE.sprites.text_sprite import TextSprite


class PersonalRoom(BaseGameStates):
    def __init__(self, game, code, save_inf=None):
        super().__init__(game)
        self.FPS = game.FPS
        self.sound = pygame.mixer.Sound(fullname('music/put.ogg'))
        if save_inf:
            self.quantity = save_inf

        self.hero_group = pygame.sprite.Group()
        self.crystal_group = pygame.sprite.Group()
        self.rubbish_group = pygame.sprite.Group()
        self.notes = Notes(self, code)
        self.clothes_group = pygame.sprite.Group()
        self.rubbish_room = RoomSprite(self, 0, 0, mask='images/room/room_rubbish_mask.png')
        self.screen_img = RoomSprite(self, 0, 0, mask='images/room/room_hero_mask.png')
        CrystalSprite(self,  20, 20, size=(30, 30), angle=10)

        self.hero = HeroSprite(self, 350, 350, size=(60, 120))
        while len(self.rubbish_group) != self.quantity[0]:
            x, y, angle = randint(0, 700), randint(0, 700), randint(0, 360)
            RubbishSprite(self, x, y, angle=angle)
        while len(self.clothes_group) != self.quantity[1]:
            x, y, angle = randint(0, 700), randint(0, 700), randint(0, 360)
            ClothesSprite(self, x, y, angle=angle)

    def render(self):
        super().render()
        self.screen.fill(pygame.Color('black'))
        self.screen.blit(self.screen_img.image, (0, 0))
        self.crystal_group.draw(self.screen)
        self.rubbish_group.draw(self.screen)
        self.notes.draw()
        self.clothes_group.draw(self.screen)
        self.hero_group.draw(self.screen)

    def handle_event(self, event):
        super().handle_event(event)
        self.hero.get_event_room(event)
        if pygame.sprite.collide_mask(self.hero, self.screen_img):
            self.hero.anti_move()
        self.rubbish_group.update(event)
        self.clothes_group.update(event)
        self.crystal_group.update()
        self.notes.update(len(self.clothes_group), len(self.rubbish_group))
        x, y = self.hero.pos
        if y + 120 > 690:
            self.stop()
            self.hero.rect.y -= 100
            self.hero.pos = x, y - 100
