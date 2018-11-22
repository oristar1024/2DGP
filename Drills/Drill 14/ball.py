import random
from pico2d import *
import game_world
import game_framework
import main_state

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(250, 1600), random.randint(50, 1050), 0

    def get_bb(self):
        return self.x - 10 - main_state.boy.bg.window_left , self.y - 10- main_state.boy.bg.window_bottom, self.x + 10- main_state.boy.bg.window_left, self.y + 10 - main_state.boy.bg.window_bottom

    def draw(self):
        self.image.draw(self.x - main_state.boy.bg.window_left, self.y - main_state.boy.bg.window_bottom)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

