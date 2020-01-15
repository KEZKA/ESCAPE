from ESCAPE.core.base_sprite import BaseSprite


class CorridorSprite(BaseSprite):
    def __init__(self, game, x, y, size=None, angle=0):
        images = ['images/corridor/corridor_1.png',
                  'images/corridor/corridor_2.png',
                  'images/corridor/corridor_3.png',
                  'images/corridor/corridor_2.png']

        super().__init__(game, images, x, y, size, angle)
        self.add(game.corridor_group)
        self.anim_fps = 4
