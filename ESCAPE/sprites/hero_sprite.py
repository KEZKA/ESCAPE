from ESCAPE.core.base_sprite import BaseSprite


class HeroSprite(BaseSprite):
    def __init__(self, game, x, y, size=None, angle=0):
        images = ['images/hero.png']
        # TODO numerous pictures of a hero and a standalone directory

        super().__init__(game, images, x, y, size, angle)
        self.add(game.hero_group)
        self.anim_fps = 10
