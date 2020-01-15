from ESCAPE.core.base_sprite import BaseSprite


class RoomSprite(BaseSprite):
    def __init__(self, game, x, y, size=None, angle=0):
        images = ['images/room.png']
        super().__init__(game, images, x, y, size, angle)

    def check(self, x, y):
        return not (0 <= y <= 120 and x < 270) and not (300 <= y <= 525 and 550 < x) \
               and not (550 <= y and x < 483) and (200 <= x <= 640 and 0 <= y <= 670)