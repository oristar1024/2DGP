from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def move_to_point(px, py):
    global cx, cy, frame, motion
    global move
    move = True
    xmove = (px - cx) / 40  # 현재점에서 다음점까지의 증가값을 40개로 나눴다.
    ymove = (py - cy) / 40
    for i in range(1, 40 + 1):  # 40번에걸쳐 다음점으로 이동
        if move:
            if xmove < 0:  # 왼쪽으로 이동해야할때
                motion = 0
            else:
                motion = 100
            clear_canvas()
            kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
            mouse.clip_draw(0, 0, 100, 100, mx, my)
            character.clip_draw(frame * 100, motion, 100, 100, cx, cy)
            update_canvas()
            cx += xmove
            cy += ymove
            frame = (frame + 1) % 8
            handle_events()
            delay(0.05)
    move = False


def handle_events():
    global running
    global mx, my
    global cx, cy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x , KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            move_to_point(mx-50, my+50)




open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
mouse = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
mx, my = KPU_WIDTH // 2, KPU_HEIGHT // 2
cx, cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
motion = 1
move = False
hide_cursor()

while running:
    if move == False:
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, motion, 100, 100, cx, cy)
        mouse.clip_draw(0, 0, 100, 100, mx, my)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
        handle_events()

close_canvas()




