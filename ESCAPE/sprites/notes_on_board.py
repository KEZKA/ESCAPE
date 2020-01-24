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
        shuffle(self.sprites)
        self.sprites.append(Thing(20, 00, 'images/things/books.png'))
        self.sprites.append(Thing(70, 50, 'images/things/pig.png'))

    def update(self, clothes, rubbish):
        print(clothes, rubbish)
        if clothes <= 3 and rubbish <= 3:
            self.sprites[-1].update()
        if clothes < 2 and rubbish < 5:
            self.sprites[-2].update()
        if clothes < 8 and rubbish < 15:
            self.sprites[-3].update()
        if clothes < 15 and rubbish < 16:
            self.sprites[-4].update()
        if clothes < 18 and rubbish < 17:
            self.sprites[-5].update()
        if clothes < 19 and rubbish < 19:
            self.sprites[-6].update()

    def draw(self):
        for i in self.sprites:
            if i.show:
                self.game.screen.blit(i.image, i.pos)
