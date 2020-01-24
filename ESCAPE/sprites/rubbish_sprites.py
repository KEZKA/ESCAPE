import pygame

from ESCAPE.core.base_sprite import BaseSprite


class RubbishSprite(BaseSprite):
    def __init__(self, game, x, y, angle=0):
        self.in_hand = False
        images = ['images/things/rubbish.png']
        size = (25, 25)

        super().__init__(game, images, x, y, size, angle)
        if not pygame.sprite.collide_mask(self, game.rubbish_room) \
                and not pygame.sprite.spritecollideany(self, self.game.rubbish_group):
            self.add(game.rubbish_group)

    def update(self, event):
        if not self.in_hand:
            k = pygame.sprite.spritecollideany(self, self.game.hero_group)
            if k:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.game.hero.rubbish <= 5:
                        self.in_hand = True
                        self.game.rubbish_group.remove(self)
                        self.game.hero.rubbish += 1
