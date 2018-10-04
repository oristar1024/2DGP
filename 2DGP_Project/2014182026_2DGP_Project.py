from pico2d import *
import random
weapon = 1
running = True
# 캐릭터 스프라이트의 머리는 0, 900 부터 X 40, Y 30 (글자위치 10)
# 몸통은 850부터 동일, 머리로부터 Y를 15만큼 빼준다.

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

open_canvas()
if weapon == 1:
    character = load_image('Gunner.png')
elif weapon == 2:
    character = load_image('sniper.png')
elif weapon == 3:
    character = load_image('cannoneer.png')
while running:
    character.clip_draw(15, 850, 20, 30, 100, 100 - 15)
    character.clip_draw(0, 900, 40, 30, 100, 100)
    update_canvas()
    handle_events()
