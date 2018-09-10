from pico2d import *  
import math     
open_canvas()     
grass = load_image('grass.png')  
character = load_image('character.png')  
x=400  
y=90  
seta = 270

while(True):  
     seta = seta+1  
     while (x < 750):  
         clear_canvas_now()  
         grass.draw_now(400, 30)  
         character.draw_now(x, y)  
         x = x+2  
         delay(0.01)  
     while (y < 550):  
         clear_canvas_now()  
         grass.draw_now(400, 30)  
         character.draw_now(x, y)  
         y = y+2  
         delay(0.01)  
     while (x > 50):  
         clear_canvas_now()  
         grass.draw_now(400, 30)  
         character.draw_now(x, y)  
         x = x-2  
         delay(0.01)  
     while (y > 90):  
         clear_canvas_now()  
         grass.draw_now(400, 30)  
         character.draw_now(x, y)  
         y = y-2  
         delay(0.01)  
     while (x < 400):
         clear_canvas_now()  
         grass.draw_now(400, 30)  
         character.draw_now(x, y)  
         x = x+2  
         delay(0.01)  
     while (seta % 360 != 270):  
        clear_canvas_now()  
        grass.draw_now(400, 30)  
        character.draw_now(x, y)  
        x = math.cos(math.radians(seta)) * 230 + 400  
        y = math.sin(math.radians(seta)) * 230 + 320  
        seta = seta+1  
        delay(0.01)  

close_canvas()  
