from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')

frame = 0
motion = 100 # 캐릭터의 이동방향을 표현하는 스프라이트 시트의 y값
x = 25
y = 50

def draw_curve_4_points(p1, p2, p3, p4):
    global frame, tx, x, y, motion
    # draw p2-p3
    for i in range(0, 100, 2):
        tx = x
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        clear_canvas()
        if x < tx:
            motion = 0
        elif x < tx:
            motion = 100
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, motion, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

points = [(random.randint(0 + 50, KPU_WIDTH - 50), random.randint(0 + 50, KPU_HEIGHT- 50)) for i in range(10)]
i = 0

while 1:
    #draw_curve_4_points()
    pass

        
close_canvas()

