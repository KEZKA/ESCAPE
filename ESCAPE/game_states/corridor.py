import pygame

from ESCAPE.core.base_game_state import BaseGameStates
from ESCAPE.sprites.corridor_sprite import CorridorSprite
from ESCAPE.sprites.hero_sprite import HeroSprite


class Corridor(BaseGameStates):
    def __init__(self, game, code):
        super().__init__(game)
        self.FPS = game.FPS

        self.corridor_group = pygame.sprite.Group()
        self.crystal_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group()
        self.code = code
        self.door = False

        self.corridor = CorridorSprite(self, 0, 0)
        self.hero = HeroSprite(self, 2180, 2340)

    def loop(self):
        self.hero.update()
        self.game.camera.update(self.hero.rect.x, self.hero.rect.y)
        self.game.camera.apply(self.hero)
        for tile in self.corridor_group.sprites():
            self.game.camera.apply(tile)
        if self.hero.general_x <= 200 and self.hero.general_y <= 220:
            self.game.door = True
        else:
            self.game.door = False

        if self.hero.personal_code == self.code:
            self.game.corridor.stop()
            self.game.titres.start(resaving=True)

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
        if self.hero.general_x > 2350:
            self.stop()
            self.hero.general_x -= 100
            self.hero.rect.x -= 100
