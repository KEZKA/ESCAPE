from ESCAPE.core.base_sprite import BaseSprite


class RoomSprite(BaseSprite):
    def __init__(self, game, x, y, size=None, angle=0):
        images = ['images/room.png']
        super().__init__(game, images, x, y, size, angle)