from pico2d import *
import random
weapon = 1
# 캐릭터 스프라이트의 머리는 X 40, Y 30 (글자위치 10)
open_canvas()
if weapon == 1:
    character = load_image('Gunner.png')
elif weapon == 2:
    character = load_image('sniper.png')
elif weapon == 3:
    character = load_image('cannoneer.png')
while True:
    character.clip_draw(0, 900, 40, 30, 100, 100)
    update_canvas()