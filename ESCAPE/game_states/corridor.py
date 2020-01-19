import pygame

from ESCAPE.core.base_game_state import BaseGameStates
from ESCAPE.sprites.corridor_sprite import CorridorSprite
from ESCAPE.sprites.hero_sprite import HeroSprite


class Corridor(BaseGameStates):
    def __init__(self, game):
        super().__init__(game)
        self.FPS = game.FPS

        self.corridor_group = pygame.sprite.Group()
        self.crystal_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group()

        self.corridor = CorridorSprite(self, 0, 0)
        self.hero = HeroSprite(self, 180, 240)

    def render(self):
        super().render()
        self.screen.fill(pygame.Color('black'))
        self.corridor_group.draw(self.screen)
        self.corridor_group.update()
        self.crystal_group.draw(self.screen)
        self.crystal_group.update()
        self.hero_group.draw(self.screen)
        self.hero_group.update()

    def handle_event(self, event):
        super().handle_event(event)
        self.hero.get_event(event)
        if pygame.sprite.collide_mask(self.hero, self.corridor):
            self.hero.anti_move()
