import random

import pygame

from ESCAPE.core.base_game_state import BaseGameStates
from ESCAPE.core.utils import fullname
from ESCAPE.sprites.button_sprite import ButtonSprite
from ESCAPE.sprites.crystal_sprite import CrystalSprite
from ESCAPE.sprites.text_sprite import TextSprite


class Titres(BaseGameStates):
    def __init__(self, game):
        super().__init__(game)
        self.FPS = game.FPS
        self.text_group = pygame.sprite.Group()
        self.crystal_group = pygame.sprite.Group()
        self.button_group = pygame.sprite.Group()
        for _ in range(100):
            x, y = random.randint(0, 700), random.randint(0, 700)
            CrystalSprite(self, x, y, size=(5, 5))
        ButtonSprite(self, 200, 600, (300, 50), 'Выход', self.game.terminate)
        text = '''Мы очень благодарны вам за ваше внимание!
        Мы будем стараться и дорабатывать 
        наш проект.
        
        
        
        авторы: KEZKA, ridering'''
        TextSprite(self, 0,0,(700, 600), text)


    def render(self):
        super().render()
        self.screen.fill(pygame.Color('black'))
        self.text_group.draw(self.screen)
        self.crystal_group.draw(self.screen)
        self.button_group.draw(self.screen)
        self.arrow.draw(self.screen)

    def handle_event(self, event):
        super().handle_event(event)
        self.crystal_group.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                self.button_group.update(event)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                self.button_group.update(event)
