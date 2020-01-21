from random import randint

import pygame

from ESCAPE.core.base_game_state import BaseGameStates
from ESCAPE.sprites.clothes_sprite import ClothesSprite
from ESCAPE.sprites.crystal_sprite import CrystalSprite
from ESCAPE.sprites.hero_sprite import HeroSprite
from ESCAPE.sprites.notes_on_board import Notes
from ESCAPE.sprites.room_sprite import RoomSprite
from ESCAPE.sprites.rubbish_sprites import RubbishSprite


class PersonalRoom(BaseGameStates):
    def __init__(self, game, code):
        super().__init__(game)
        self.FPS = game.FPS
        self.hero_group = pygame.sprite.Group()
        self.crystal_group = pygame.sprite.Group()
        self.rubbish_group = pygame.sprite.Group()
        self.notes = Notes(self, code)
        self.clothes_group = pygame.sprite.Group()
        self.rubbish_room = RoomSprite(self, 0, 0, mask='images/room/room_rubbish_mask.png')
        self.screen_img = RoomSprite(self, 0, 0, mask='images/room/room_hero_mask.png')
        for i in range(10):
            x,y, angle, size = randint(50,650), randint(50,650), randint(0,10), randint(30,60)
            CrystalSprite(self, x-20, y-20, size=(size+10, size+10), angle=angle-10)
            CrystalSprite(self, x, y, size = (size, size), angle=angle)
            CrystalSprite(self, x-30, y+20, size=(size-10, size-10), angle=angle+10)
        self.hero = HeroSprite(self, 350, 350, size=(60, 120))
        while len(self.rubbish_group) != 50:
            x, y, angle = randint(0, 700), randint(0, 700), randint(0, 360)
            RubbishSprite(self, x, y, angle=angle)
        while len(self.clothes_group) != 30:
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
