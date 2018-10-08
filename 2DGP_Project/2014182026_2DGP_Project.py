from pico2d import *
import random

# 캐릭터 스프라이트의 머리는 4, 900 부터 X 40, Y 30 (글자위치 10)
# 몸통은 8, 850부터 X32, Y30, 머리로부터 Y를 15만큼 빼준다.
# 맵타일은 한칸에 X, Y 각 65


class Character:
    def __init__(self):
        self.x, self.y = 50, 50
        self.x_dir, self.y_dir = 0, 0
        self.left_move, self.right_move, self.up_move, self.down_move = False, False, False, False
        self.idling_timer = 0
        self.head, self.body = 0, 0
        self.head_frame , self.body_frame = 0, 0
        self.weapon = random.randint(1, 3)
        if self.weapon == 1:
            self.image = load_image('Gunner.png')
        elif self.weapon == 2:
            self.image = load_image('sniper.png')
        elif self.weapon == 3:
            self.image = load_image('cannoneer.png')

    def update(self):
        self.idling_timer = (self.idling_timer + 1) % 30

        if self.x_dir != 0 or self.y_dir != 0:
            self.body_frame = (self.body_frame + 1) % 10
            if self.x_dir > 0:
                self.x_dir -= 1
            elif self.x_dir < 0:
                self.x_dir += 1
            if self.y_dir > 0:
                self.y_dir -= 1
            elif self.y_dir < 0:
                self.y_dir += 1
        else:
            self.head = 0
            self.body = 0
            self.body_frame = 0

        if self.left_move:
            self.head = 6
            self.body = 1
            if self.x_dir > -15:
                self.x_dir -= 2
        if self.right_move:
            self.head = 2
            self.body = 1
            if self.x_dir < 15:
                self.x_dir += 2
        if self.up_move:
            self.head = 4
            self.body = 0
            if self.y_dir < 15:
                self.y_dir += 2
        if self.down_move:
            self.head = 0
            self.body = 0
            if self.y_dir > -15:
                self.y_dir -= 2
        if self.left_move and self.right_move:
            self.head = 0
            self.body = 0

        self.x += self.x_dir
        self.y += self.y_dir

        self.idling()

    def idling(self):
        if self.idling_timer == 10:
            self.head_frame += 1

        if self.head_frame == 1 and self.idling_timer == 13:  # 캐릭터가 눈을 감은지 3프레임이 지나면 눈을뜬다.
            self.head_frame -= 1

    def draw(self):
        self.image.clip_draw(8 + 32 * self.body_frame, 850 - 42 * self.body, 32, 30, self.x, self.y - 15)
        self.image.clip_draw(4 + 40 * self.head + 40 * self.head_frame, 900, 40, 30, self.x, self.y)


class Mouse:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.image = load_image('Target.png')

    def draw(self):
        self.image.clip_draw(0, 0, 50, 50, self.x, self.y)

class Map:
    def __init__(self):
        self.x, self.y = 25, 25
        self.number = 1
        self.image = load_image("Tiles.png")

    def draw(self):
        self.x, self.y = 25, 25
        while self.y < MAP_HEGIHT:
            while self.x < MAP_WIDTH:
                self.image.clip_draw((self.number - 1) * 65 + 2 + 5, 65 + 5, 50, 50, self.x, self.y)  # X값 + 2 는 파란선 부분제거용, X, Y 의+5는 테두리 자르기
                self.x += 50
            self.x = 25
            self.y += 50


def handle_events():
    global running
    global character
    global mouse
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_w:
                character.up_move = True

            elif event.key == SDLK_a:
                character.left_move = True

            elif event.key == SDLK_d:
                character.right_move = True

            elif event.key == SDLK_s:
                character.down_move = True

            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse.x, mouse.y = event.x, 768 - 1 - event.y
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_w:
                character.up_move = False

            elif event.key == SDLK_a:
                character.left_move = False

            elif event.key == SDLK_d:
                character.right_move = False

            elif event.key == SDLK_s:
                character.down_move = False


running = True
MAP_WIDTH = 4000
MAP_HEGIHT = 3000

open_canvas(1024, 768)
hide_cursor()

character = Character()
mouse = Mouse()
map = Map()


while running:
    character.update()
    clear_canvas()
    map.draw()
    character.draw()
    mouse.draw()
    update_canvas()
    delay(0.01)
    handle_events()
