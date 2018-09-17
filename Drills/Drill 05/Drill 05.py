from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

points = [203, 535], [132, 243], [535, 470], [477, 203], [715, 136], [316, 225], [510, 92], [692, 518], [682, 336], [712, 349]

def move_to_point(x, y):
    pass

x = 30
y = 30

while 1:
    move_to_point(x, y)
close_canvas()

