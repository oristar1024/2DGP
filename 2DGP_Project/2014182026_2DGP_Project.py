from pico2d import *
import random
weapon = random.randint(1, 3)
running = True
MAP_WIDTH = 4000
MAP_HEGIHT = 3000
map_number = 1
# 캐릭터 스프라이트의 머리는 4, 900 부터 X 40, Y 30 (글자위치 10)
# 몸통은 8, 850부터 X32, Y30, 머리로부터 Y를 15만큼 빼준다.
# 맵타일은 한칸에 X, Y 각 65
def handle_events():
    global running
    global character_head, character_body
    global x_dir, y_dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_w:
                y_dir += 1

            elif event.key == SDLK_a:
                x_dir -= 1

            elif event.key == SDLK_d:
                x_dir += 1

            elif event.key == SDLK_s:
                y_dir -= 1

            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w:
                y_dir -= 1

            elif event.key == SDLK_a:
                x_dir += 1

            elif event.key == SDLK_d:
                x_dir -= 1

            elif event.key == SDLK_s:
                y_dir += 1


idling_timer = 0 # idling을 할 순간을 결정하는 타이머
x_dir = 0 # 캐릭터의 x방향
y_dir = 0 # 캐릭터의 y방향
character_idling = False
character_head = 0
character_head_frame = 0
character_body_frame = 0
character_body = 0
character_x = 50
character_y = 50
open_canvas()

map = load_image("Tiles.png")

def draw_map():
    global map_number
    x = 25
    y = 25
    while y < MAP_HEGIHT:
        while x < MAP_WIDTH:
            map.clip_draw((map_number - 1) * 65 + 2 + 5, 65 + 5, 50, 50, x, y) # X값 + 2 는 파란선 부분제거용, X, Y 의+5는 테두리 자르기
            x += 50
        x = 25
        y += 50


if weapon == 1:
    character = load_image('Gunner.png')
elif weapon == 2:
    character = load_image('sniper.png')
elif weapon == 3:
    character = load_image('cannoneer.png')


while running:
    idling_timer = (idling_timer+1) % 20

    if x_dir != 0 or y_dir != 0:
        character_body_frame = (character_body_frame+1) % 10
    else:
        character_head = 0
        character_body = 0
        character_body_frame = 0

    if y_dir == 1:
        character_head = 4
        character_body = 0
    elif y_dir == -1:
        character_head = 0
        character_body = 0
    elif x_dir == 1:
        character_head = 2
        character_body = 1
    elif x_dir == -1:
        character_head = 6
        character_body = 1

    character_x += x_dir*10
    character_y += y_dir*10
    if idling_timer == 10:
        character_idling = True
        character_head_frame += 1

    if character_head_frame == 1 and idling_timer == 13: # 캐릭터가 눈을 감은지 3프레임이 지나면 눈을뜬다.
        character_head_frame -= 1
        character_idling = False


    clear_canvas()
    draw_map()
    character.clip_draw(8 + 32*character_body_frame, 850 - 42*character_body, 32, 30, character_x, character_y - 15)
    character.clip_draw(4 + 40*character_head + 40*character_head_frame, 900, 40, 30, character_x, character_y)
    update_canvas()
    delay(0.05)
    handle_events()
