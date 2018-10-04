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
    global frame, x, y, motion
    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2


while 1:
    #draw_curve_4_points()
    pass

        
close_canvas()

