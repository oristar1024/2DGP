from pico2d import *
import random
weapon = random.randint(1, 3)
running = True
MAP_WIDTH = 4000
MAP_HEGIHT = 3000
map_number = 1
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

idling_timer = 0 #idling을 할 순간을 결정하는 타이머
character_idling = False
character_head = 0
character_head_frame = 0
character_body_frame = 0
character_body = 0
open_canvas()

map = load_image("Tiles.png")

def draw_map():
    global map_number
    x = 0
    y = 0
    while y < MAP_HEGIHT:
        while x < MAP_WIDTH:
            map.clip_draw((map_number - 1) * 50, 0, 50, 50, x, y)
            x += 50
        y += 50


if weapon == 1:
    character = load_image('Gunner.png')
elif weapon == 2:
    character = load_image('sniper.png')
elif weapon == 3:
    character = load_image('cannoneer.png')


while running:
    idling_timer = (idling_timer+1) % 20
    character_body_frame = (character_body_frame+1) % 10
    if idling_timer == 10:
        character_idling = True
        character_head_frame = 1
    if character_head_frame == 1 and idling_timer == 13: # 캐릭터가 눈을 감은지 3프레임이 지나면 눈을뜬다.
        character_head_frame = 0
        character_idling = False
    clear_canvas()
    draw_map()
    character.clip_draw(8 + 32*character_body_frame, 850 - 50*character_body, 32, 30, 100, 100 - 15)
    character.clip_draw(4 + 40*character_head + 40*character_head_frame, 900, 40, 30, 100, 100)
    update_canvas()
    delay(0.05)
    handle_events()
