import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import main_state

name = "LankingState"

def enter():
    with open('langking_data.json' , 'r') as f:
        lanking_list = json.load(f)

    game_rank = None
    for data in lanking_list:
        if data['record'] < main_state.game_record:
            game_rank = data['rank']
            while game_rank < 10:
                lanking_list[game_rank]['record'] = lanking_list[game_rank - 1]['record']
            data['record'] = main_state.game_record
            break

    with open('lanking_data.json', 'wb') as f:
        pickle.dump(lanking_list, f)
