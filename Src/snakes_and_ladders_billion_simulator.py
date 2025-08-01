# -*- coding: utf-8 -*-
"""Snakes And Ladders Billion Simulator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q_osEIDsINd170p9gYxaWZIRy5QidMyw
"""

import random
import csv
import json
import pandas as pd
from tqdm import tqdm

try:
    from google.colab import files
    HAVE_COLAB = True
except ImportError:
    HAVE_COLAB = False

N_BOARDS = 100             # Reduce for manageability (adjustable)
GAMES_PER_BOARD = 1000     # Reduce for manageability (adjustable)
MAX_SNAKES = 10
MAX_LADDERS = 10

def generate_board(max_snakes=MAX_SNAKES, max_ladders=MAX_LADDERS):
    snakes, ladders, used = [], [], set()
    while len(snakes) < max_snakes:
        head = random.randint(20, 99)
        tail = random.randint(1, head - 1)
        if head not in used and tail not in used:
            snakes.append((head, tail))
            used.update([head, tail])
    while len(ladders) < max_ladders:
        bottom = random.randint(1, 90)
        top = random.randint(bottom + 1, 100)
        if bottom not in used and top not in used and top not in [s[0] for s in snakes]:
            ladders.append((bottom, top))
            used.update([bottom, top])
    board_map = {h: t for h, t in snakes + ladders}
    return board_map, snakes, ladders

def simulate_game_with_steps(board_map, game_id, board_id):
    pos = 0
    turn = 0
    journey_log = []
    while pos < 100:
        roll = random.randint(1, 6)
        if pos + roll <= 100:
            start_pos = pos
            new_pos = pos + roll
            end_pos = board_map.get(new_pos, new_pos)
            move_type = "normal"
            if new_pos in board_map:
                move_type = "ladder" if end_pos > new_pos else "snake"
            pos = end_pos
            journey_log.append({
                "game_id": game_id,
                "board_id": board_id,
                "turn": turn + 1,
                "roll": roll,
                "start_pos": start_pos,
                "end_pos": pos,
                "move_type": move_type
            })
        turn += 1
    return journey_log

boards_meta = []
journeys = []

game_id = 0
for board_id in tqdm(range(N_BOARDS), desc="Generating Boards"):
    board_map, snakes, ladders = generate_board()
    boards_meta.append({
        'board_id': board_id,
        'snakes': json.dumps(snakes),
        'ladders': json.dumps(ladders)
    })
    for _ in range(GAMES_PER_BOARD):
        game_journey = simulate_game_with_steps(board_map, game_id, board_id)
        journeys.extend(game_journey)
        game_id += 1

boards_df = pd.DataFrame(boards_meta)
boards_df.to_csv("boards_turn_level.csv", index=False)

journey_df = pd.DataFrame(journeys)
journey_df.to_csv("game_journeys_turn_level.csv", index=False)

print("✅ Saved:")
print("- boards_turn_level.csv")
print("- game_journeys_turn_level.csv")