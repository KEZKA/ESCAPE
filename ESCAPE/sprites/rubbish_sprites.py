import pygame

from ESCAPE.core.base_sprite import BaseSprite


class BaseRubbishSprite(BaseSprite):
    def __init__(self, game, x, y, image, angle=0):
        self.in_hand = False
        images = [image]
        size = (25, 25)

        super().__init__(game, images, x, y, size, angle)
        if not pygame.sprite.collide_mask(self, game.rubbish_room):
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


class NoteInRubbish(BaseRubbishSprite):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, 'images/rubbish/note_in_rubbish.png')


class RubbishSprite(BaseRubbishSprite):
    def __init__(self, game, x, y, angle=0):
        super().__init__(game, x, y, 'images/rubbish/rubbish1.png')
