from pico2d import *

class Item:
    def __init__(self):
        self.type = 0
        self.x = 0
        self.y = 0
        self.image = load_image('Item.png')
        self.draw = False

    def draw(self):
        if self.type == 1:
            self.image.clip_draw(0, 0, 68, 68, self.x, self.y)
        elif self.type == 2:
            self.image.clip_draw(68 *2, 0, 68, 68, self.x, self.y)
