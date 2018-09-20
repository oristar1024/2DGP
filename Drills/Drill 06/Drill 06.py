from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x + 50, KPU_HEIGHT - 1 - event.y - 50
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
mouse = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
mx, my = KPU_WIDTH // 2, KPU_HEIGHT // 2
cx, cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
motion = 1
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.clip_draw(0, 0, 100, 100, mx, my)
    character.clip_draw(frame * 100, 100 * motion, 100, 100, cx, cy)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()




