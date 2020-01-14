import pygame

from ESCAPE.core.base_sprite import BaseSprite


class BaseRubbishSprite(BaseSprite):
    def __init__(self, game, x, y, image, angle=0):
        images = [image]
        size = (30, 30)
        if self.check(x, y):
            super().__init__(game, images, x, y, size, angle)
            self.add(game.rubbish_group)

    def update(self):
        if pygame.sprite.spritecollideany(self, self.game.arrow):
            move_x = self.rect.x - (self.game.arrow_sprite.rect.x - self.rect.x)
            move_y = self.rect.y - (self.game.arrow_sprite.rect.y - self.rect.y)
            if self.check(move_x, move_y):
                self.rect.x = move_x
                self.rect.y = move_y

    def check(self, x, y):
        return not (0 <= y <= 120 and x < 270) and not (300 <= y <= 525 and 550 < x) \
               and not (550 <= y and x < 483) and (200 <= x <= 640 and 0 <= y <= 670)


class NoteInRubbish(BaseRubbishSprite):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, 'images/note_in_rubbish.png')


class RubbishSprite(BaseRubbishSprite):
    def __init__(self, game, x, y, angle=0):
        super().__init__(game, x, y, 'images/rubbish.png')
