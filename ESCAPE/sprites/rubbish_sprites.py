import pygame

from ESCAPE.core.base_sprite import BaseSprite


class BaseRubbishSprite(BaseSprite):
    def __init__(self, game, x, y, image, angle=0):
        images = [image]
        size = (30, 30)
        super().__init__(game, images, x, y, size, angle)
        if self.game.screen_img.check(x, y):
            self.add(game.rubbish_group)

    def update(self):
        if pygame.sprite.spritecollideany(self, self.game.hero_group):
            move_x = self.rect.x - (self.game.hero.rect.x - self.rect.x)
            move_y = self.rect.y - (self.game.hero.rect.y - self.rect.y)
            if self.game.screen_img.check(move_x, move_y):
                self.rect.x = move_x
                self.rect.y = move_y


class NoteInRubbish(BaseRubbishSprite):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, 'images/note_in_rubbish.png')


class RubbishSprite(BaseRubbishSprite):
    def __init__(self, game, x, y, angle=0):
        super().__init__(game, x, y, 'images/rubbish.png')
