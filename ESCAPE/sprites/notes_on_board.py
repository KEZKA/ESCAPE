from ESCAPE.sprites.note import Thing
from random import randint


class Notes:
    def __init__(self, game, code):
        base_filename = 'images/note_with_number/*.png'
        self.sprites = []
        self.game = game
        x, y = 220, 60
        for i in range(4):
            x += 55
            s = randint(0,50)
            self.sprites.append(Thing(x, y+s, base_filename.replace('*', code[i])))

    def draw(self):
        for i in self.sprites:
            if i.show:
                self.game.screen.blit(i.image, i.pos)