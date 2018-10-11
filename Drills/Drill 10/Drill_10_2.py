import game_framework
from pico2d import *

import main_state

name = "Drill_10_2"
image = None
switch = None


def enter():
    global image, switch
    switch = False
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
    if switch:
        image.draw(400, 300)
    main_state.grass.draw()
    main_state.boy.draw()
    update_canvas()







def update():
    global switch
    if switch:
        switch = False
        delay(0.3)
    else:
        switch = True
        delay(0.15)


def pause():
    pass


def resume():
    pass






