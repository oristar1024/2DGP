from pico2d import *
import random
weapon = random.randint(1, 3)
running = True
# 캐릭터 스프라이트의 머리는 4, 900 부터 X 40, Y 30 (글자위치 10)
# 몸통은 8, 850부터 X32, Y30, 머리로부터 Y를 15만큼 빼준다.

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_w:
                character_head = 4
                character_body = 0
            elif event.key == SDLK_ESCAPE:
                running = False

character_idling = False
character_head = 0
character_head_frame = 0
character_body_frame = 0
character_body = 0
open_canvas()
if weapon == 1:
    character = load_image('Gunner.png')
elif weapon == 2:
    character = load_image('sniper.png')
elif weapon == 3:
    character = load_image('cannoneer.png')
while running:
    character_body_frame = (character_body_frame+1) % 10
    if character_body_frame == 9:
        character_idling = True
    if character_head_frame == 1 and character_body_frame == 2:
        character_head_frame = 0
        character_idling = False
    if character_idling and character_body_frame == 8:
        character_head_frame = (character_head_frame+1) % 2
    clear_canvas()
    character.clip_draw(8 + 32*character_body_frame, 850 - 50*character_body, 32, 30, 100, 100 - 15)
    character.clip_draw(4 + 40*character_head + 40*character_head_frame, 900, 40, 30, 100, 100)
    update_canvas()
    delay(0.05)
    handle_events()
