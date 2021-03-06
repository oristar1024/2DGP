from pico2d import *
import random
import CharacterProjectile
import main_state


class Character:
    def __init__(self):
        self.x, self.y = 100, 100
        self.x_dir, self.y_dir = 0, 0
        self.left_move, self.right_move, self.up_move, self.down_move = False, False, False, False
        self.idling_timer = 0
        self.head, self.body = 0, 0
        self.head_frame , self.body_frame = 0, 0
        self.weapon = random.randint(1, 3)
        self.can_attack = True
        self.attack_delay_checker = 0
        self.bomb_range = 120

        if self.weapon == 1:
            self.image = load_image('assassin.png')
            self.range = 600
            self.bullet_speed = 50
            self.damage = 20
        elif self.weapon == 2:
            self.image = load_image('sniper.png')
            self.range = 720
            self.bullet_speed = 60
            self.damage = 80
        else:
            self.image = load_image('cannoneer.png')
            self.range = 480
            self.bullet_speed = 40
            self.damage = 60

    def update(self):
        self.idling_timer = (self.idling_timer + 1) % 30

        if self.weapon == 1 and self.can_attack == False:
            if self.attack_delay_checker == self.idling_timer - 2 or self.attack_delay_checker == self.idling_timer + 28:
                main_state.character_projectile[main_state.projectile_array_index] = CharacterProjectile.CharacterProjectile()
                main_state.projectile_array_index = (main_state.projectile_array_index + 1) % 30
            elif self.attack_delay_checker == self.idling_timer - 4 or self.attack_delay_checker == self.idling_timer + 26:
                main_state.character_projectile[main_state.projectile_array_index] = CharacterProjectile.CharacterProjectile()
                main_state.projectile_array_index = (main_state.projectile_array_index + 1) % 30
            elif self.attack_delay_checker == self.idling_timer - 6 or self.attack_delay_checker == self.idling_timer + 24:
                main_state.character_projectile[main_state.projectile_array_index] = CharacterProjectile.CharacterProjectile()
                main_state.projectile_array_index = (main_state.projectile_array_index + 1) % 30
            elif self.attack_delay_checker == self.idling_timer - 8 or self.attack_delay_checker == self.idling_timer + 22:
                main_state.character_projectile[main_state.projectile_array_index] = CharacterProjectile.CharacterProjectile()
                main_state.projectile_array_index = (main_state.projectile_array_index + 1) % 30

        if self.attack_delay_checker == self.idling_timer - 10 or self.attack_delay_checker == self.idling_timer + 20:
            self.can_attack = True

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
        if self.body == 1 and self.left_move:
            self.image.clip_composite_draw(8 + 32 * self.body_frame, 850 - 42 * self.body, 32, 30, 0, 'h', self.x, self.y - 15, 32, 30)
        else:
            self.image.clip_draw(8 + 32 * self.body_frame, 850 - 42 * self.body, 32, 30, self.x, self.y - 15)
        self.image.clip_draw(4 + 40 * self.head + 40 * self.head_frame, 900, 40, 30, self.x, self.y)
