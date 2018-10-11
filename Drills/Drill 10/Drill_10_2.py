import game_framework
from pico2d import *


name = "Drill_10_2"
image = None


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






