import game_framework
from pico2d import *
import main_state


name = "Drill_10_1"
image = None


def enter():
    pass


def exit():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def draw():
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass






