from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

points = [203, 535], [132, 243], [535, 470], [477, 203], [715, 136], [316, 225], [510, 92], [692, 518], [682, 336], [712, 349]

frame = 0
motion = 100 # 캐릭터의 이동방향을 표현하는 스프라이트 시트의 y값
x = 25
y = 50

def move_to_point(px, py):
    global x, y, frame, motion
        clear_canvas()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, motion, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

while 1:
    for px, py in points:
        move_to_point()
        
close_canvas()

