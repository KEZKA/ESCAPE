import pygame

from ESCAPE.core.base_sprite import BaseSprite


class BaseRubbishSprite(BaseSprite):
    def __init__(self, game, x, y, image, angle=0):
        images = [image]
        size = (25, 25)
        super().__init__(game, images, x, y, size, angle)
        if self.game.screen_img.check(x, y) and self.game.screen_img.check(x+20, y+20):
            self.add(game.rubbish_group)

    def update(self, event):
        if pygame.sprite.spritecollideany(self, self.game.hero_group):
            move_x = self.rect.x - (self.game.hero.rect.x - self.rect.x)
            move_y = self.rect.y - (self.game.hero.rect.y - self.rect.y)
            if self.game.screen_img.check(move_x+20, move_y+20) and self.game.screen_img.check(move_x, move_y) \
                    and 0 < move_x < 680 and 0 < move_y < 680:
                self.rect.x = move_x
                self.rect.y = move_y


class NoteInRubbish(BaseRubbishSprite):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, 'images/note_in_rubbish.png')

    def update(self, event):
        if pygame.sprite.spritecollideany(self, self.game.hero_group):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass



class RubbishSprite(BaseRubbishSprite):
    def __init__(self, game, x, y, angle=0):
        super().__init__(game, x, y, 'images/rubbish1.png')
