import pygame

from ESCAPE.core.base_sprite import BaseSprite


class HeroSprite(BaseSprite):
    def __init__(self, game, x, y, size=None):
        images = ['images/hero.png']
        # TODO numerous pictures of a hero and a standalone directory
        # TODO handel events
        super().__init__(game, images, x, y, size)
        self.add(game.hero_group)
        self.anim_fps = 10
        self.pos = (x, y)

    def get_event_room(self, event):
        step = 10
        if event.type == pygame.KEYDOWN:
            x, y = self.rect.x, self.rect.y
            new_x, new_y = x, y
            if event.key == pygame.K_RIGHT:
                new_x, new_y = x + step, y
            if event.key == pygame.K_LEFT:
                new_x, new_y = x - step, y
            if event.key == pygame.K_UP:
                new_x, new_y = x, y - step
            if event.key == pygame.K_DOWN:
                new_x, new_y = x, y + step
            if 470 < new_x < 561 and 675 < y:
                self.game.stop()
            if self.game.screen_img.check(new_x + 30, new_y + 110):
                self.rect.x, self.rect.y = new_x, new_y
                self.pos = (new_x, new_y)
