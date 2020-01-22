from random import randint, shuffle

from ESCAPE.sprites.note import Thing


class Notes:
    def __init__(self, game, code):
        base_filename = 'images/note_with_number/*.png'
        self.sprites = []
        self.game = game
        x, y = 220, 60
        for i in range(4):
            x += 55
            s = randint(0, 50)
            self.sprites.append(Thing(x, y + s, base_filename.replace('*', code[i])))
        self.sprites.append(Thing(20, 00, 'images/things/books.png'))
        self.sprites.append(Thing(70, 50, 'images/things/pig.png'))
        shuffle(self.sprites)

    def update(self, clothes, rubbish):
        if clothes <= 1 and rubbish <=1:
            self.sprites[-1].update()
        if clothes < 5 and rubbish < 10:
            self.sprites[-2].update()
        if clothes < 8 and rubbish < 15:
            self.sprites[-3].update()
        if clothes < 10 and rubbish < 20:
            self.sprites[-4].update()
        if clothes < 21 and rubbish < 30:
            self.sprites[-5].update()
        if clothes < 25 and rubbish < 40:
            self.sprites[-6].update()

    def draw(self):
        for i in self.sprites:
            if i.show:
                self.game.screen.blit(i.image, i.pos)
