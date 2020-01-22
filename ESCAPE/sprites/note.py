from ESCAPE.core.utils import load_image


class Thing:
    def __init__(self, x, y, image):
        self.image = load_image(image)
        self.show = False
        self.pos = (x, y)

    def update(self):
        self.show = True