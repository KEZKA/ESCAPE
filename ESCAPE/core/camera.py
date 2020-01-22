class Camera:
    def __init__(self, game):
        self.game = game
        self.dx = 0
        self.dy = 0
        self.ny = 240
        self.is_start = True

    def start_camera(self):
        self.dx = -2100
        self.dy = -2100

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, x, y):
        if self.is_start:
            self.start_camera()
            self.is_start = False
        else:
            self.dx = 0
            self.dy = 0
            if 260 < self.game.corridor.hero.general_x < 2360:
                self.dx = -(x - self.game.width // 2 + self.game.corridor.hero.rect.w // 2)
            elif 20 > self.game.corridor.hero.general_x and self.game.corridor.hero.general_y <= 2270:
                if 360 <= self.game.corridor.hero.general_y <= 380 or \
                        1060 <= self.game.corridor.hero.general_y <= 1080 or \
                        1760 <= self.game.corridor.hero.general_y <= 1780:
                    self.dy = -700
                    self.game.corridor.hero.general_y += 600
                    self.game.corridor.hero.rect.y += 600

                if 700 <= self.game.corridor.hero.general_y <= 750 or \
                        1400 <= self.game.corridor.hero.general_y <= 1450 or \
                        2100 <= self.game.corridor.hero.general_y <= 2150:
                    self.dy = 700
                    self.game.corridor.hero.general_y -= 440
                    self.game.corridor.hero.rect.y -= 440
