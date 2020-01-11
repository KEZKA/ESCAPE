from ESCAPE.core.base_sprite import BaseSprite


class Arrow(BaseSprite):
    def __init__(self, game, x, y):
        images = ['images/cursor.png']
        super().__init__(game, images, x, y, size=(40, 40))
        self.add(game.arrow)

    def update(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        print(self.rect.x, self.rect.y)