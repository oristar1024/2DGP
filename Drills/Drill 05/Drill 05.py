from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

points = [203, 535], [132, 243], [535, 470], [477, 203], [715, 136], [316, 225], [510, 92], [692, 518], [682, 336], [712, 349]

frame = 0
motion = 100 # 캐릭터의 이동방향을 표현하는 스프라이트 시트의 y값
x = 30
y = 30

def move_to_point(px, py):
    global x, y, frame, motion
    xmove = (px - x) / 40
    ymove = (py - y) / 40
    for i in range (1, 40+1):
        if xmove < 0:
            motion = 0
        else:
            motion = 100
        clear_canvas()
        character.clip_draw(frame * 100, motion, 100, 100, x, y)
        update_canvas()
        x += xmove
        y += ymove
        frame = (frame + 1) % 8
        delay(0.05)

while 1:
    move_to_point(300, 300)
    move_to_point(100, 100)
close_canvas()

