from random import randint

import pygame

from ESCAPE.core.base_sprite import BaseSprite


class ClothesSprite(BaseSprite):
    def __init__(self, game, x, y, angle):
        self.in_hand = False
        images = [['images/things/sock.png'],
                  ['images/things/sock2.png'],
                  ['images/things/t-shirt.png'],
                  ['images/things/t-shirt.png']]
        super().__init__(game, images[randint(0, 3)], x, y, size=(50, 50), angle=angle)
        if not pygame.sprite.collide_mask(self, game.rubbish_room) \
                and not pygame.sprite.spritecollideany(self, self.game.clothes_group):
            self.add(game.clothes_group)

    def update(self, event):
        if not self.in_hand:
            k = pygame.sprite.spritecollideany(self, self.game.hero_group)
            if k:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.game.hero.clothes <= 3:
                        self.in_hand = True
                        self.game.clothes_group.remove(self)
                        self.game.hero.clothes += 1
