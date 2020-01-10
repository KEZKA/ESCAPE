from ESCAPE.core.base_sprite import BaseSprite

# ??????????????????????????????????????????????
class CrystalSprite(BaseSprite):
    def __init__(self, game, x, y, size=None, angle=0):
        images = ['/Users/baa/Desktop/ESCAPE/ESCAPE/resources/images/crystal/crystal_1.png',
                  '/Users/baa/Desktop/ESCAPE/ESCAPE/resources/images/crystal/crystal_2.png',
                  '/Users/baa/Desktop/ESCAPE/ESCAPE/resources/images/crystal/crystal_3.png',
                  '/Users/baa/Desktop/ESCAPE/ESCAPE/resources/images/crystal/crystal_4.png',
                  '/Users/baa/Desktop/ESCAPE/ESCAPE/resources/images/crystal/crystal_5.png',
                  '/Users/baa/Desktop/ESCAPE/ESCAPE/resources/images/crystal/crystal_6.png',
                  '/Users/baa/Desktop/ESCAPE/ESCAPE/resources/images/crystal/crystal_7.png',
                  '/Users/baa/Desktop/ESCAPE/ESCAPE/resources/images/crystal/crystal_8.png']
        super().__init__(game, images, x, y, size, angle)
        self.add(game.crystal_group)
        self.anim_fps = 10
