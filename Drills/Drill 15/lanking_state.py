import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import main_state
import world_build_state

name = "LankingState"

ranking_list = None
font = None

def enter():
    global font
    global ranking_list
    font = load_font('ENCR10B.TTF', 20)
    with open('lanking_data.json' , 'rb') as f:
        ranking_list = json.load(f)
    game_rank = None
    for data in ranking_list:
        if data['record'] < main_state.game_record:
            game_rank = data['rank']
            i = 9
            while i >= game_rank:
                ranking_list[game_rank]['record'] = ranking_list[game_rank - 1]['record']
                i -= 1
            data['record'] = main_state.game_record
            break
    rank_list = json.dumps(ranking_list)
    f = open("lanking_data.json", 'w')
    f.write(rank_list)
    f.close()

def update():
    pass

def draw():
    global ranking_list
    global font
    clear_canvas()
    i = 600
    for data in ranking_list:
        font.draw(300, i, 'rank: %d' % data['rank'], (0, 0, 0))
        font.draw(600, i, 'record: %3f' % data['record'], (0, 0, 0))
        i-= 30
    update_canvas()

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)