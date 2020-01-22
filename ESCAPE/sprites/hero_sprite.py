import pygame

from ESCAPE.core.base_sprite import BaseSprite


class HeroSprite(BaseSprite):
    def __init__(self, game, x, y, size=None):
        images = ['images/hero.png']

        super().__init__(game, images, x, y, size)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.general_x = x
        self.general_y = y
        self.pos = (x, y)
        self.last_move = None
        self.step = 10
        self.add(game.hero_group)
        self.anim_fps = 10
        self.rubbish = 0
        pygame.key.set_repeat(10)

    def get_event(self, event):
        step = self.step
        if event.type == pygame.KEYDOWN:
            x, y = self.rect.x, self.rect.y
            new_x, new_y = x, y
            if event.key == pygame.K_RIGHT:
                new_x, new_y = x + step, y
                self.general_x += step
                self.last_move = 'right'
            if event.key == pygame.K_LEFT:
                new_x, new_y = x - step, y
                self.general_x -= step
                self.last_move = 'left'
            if event.key == pygame.K_UP:
                new_x, new_y = x, y - step
                self.general_y -= step
                self.last_move = 'up'
            if event.key == pygame.K_DOWN:
                new_x, new_y = x, y + step
                self.general_y += step
                self.last_move = 'down'
            self.rect.x, self.rect.y = new_x, new_y
            self.pos = (new_x, new_y)

    def anti_move(self):
        step = self.step
        x, y = self.rect.x, self.rect.y
        new_x, new_y = x, y
        if self.last_move == 'right':
            new_x, new_y = x - step, y
            self.general_x -= step
        if self.last_move == 'left':
            new_x, new_y = x + step, y
            self.general_x += step
        if self.last_move == 'up':
            new_x, new_y = x, y + step
            self.general_y += step
        if self.last_move == 'down':
            new_x, new_y = x, y - step
            self.general_y -= step
        self.rect.x, self.rect.y = new_x, new_y
        self.pos = (new_x, new_y)

    def get_event_room(self, event):
        x, y = self.rect.x, self.rect.y
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if 600 < x < 670 and 470 < y < 600:
                    self.rubbish = 0
        self.get_event(event)