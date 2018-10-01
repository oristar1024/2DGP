from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

frame = 0
motion = 100 # 캐릭터의 이동방향을 표현하는 스프라이트 시트의 y값
x = 25
y = 50

def move_to_point(p1, p2):
    global x, y, frame, motion
    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        clear_canvas()
        if p1[0] > p2[0]: # 왼쪽을 바라볼때
            motion = 0
        else:
            motion = 100
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, motion, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

i=0
points = [(random.randint(0 + 50, KPU_WIDTH - 50), random.randint(0 + 50, KPU_HEIGHT - 50)) for i in range(20)]

while 1:
    move_to_point(points[i-1], points[i])
    i = (i + 1) % 20
        
close_canvas()

