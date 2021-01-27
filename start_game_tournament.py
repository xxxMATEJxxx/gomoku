#!/usr/bin/python3

import os
from collections import Counter

#import window.player
import example.player
import numPatrik.player
import martins.player
import randomvalid.player
import svecova.player
import sebastian.player

from gomoku_tournament import GomokuTournament

TIME_LIMIT = 300

players_and_names = [
    (numPatrik.player, 'Patrik Černohorský'),
    (martins.player, 'Martin Spanel'),
    (randomvalid.player, 'random valid'),
    (svecova.player, 'Hana Svecova'),
    (sebastian.player, 'Sebastian'),
]
try:
    os.remove('logs.txt')
except Exception:
    pass
nplayers = len(players_and_names)
results = [[0 for i in range(nplayers)] for j in range(nplayers)]
for i in range(nplayers):
    for j in range(nplayers):
        if i == j: continue
        player_i, name_i = players_and_names[i]
        player_j, name_j = players_and_names[j]
       
        print(f'playing X {name_i} vs O {name_j}')
        
        player_x = player_i.Player(1)
        player_x.name = name_i
        
        player_o = player_j.Player(-1)
        player_o.name = name_j

        tournament = GomokuTournament(player_x, player_o, TIME_LIMIT)
        winner = tournament.game()
        tournament.save_logs()
        results[i][j] = winner
        if winner == 0:
            print('nobody won.')
        else:
            print(f'winner is {"X" if winner == 1 else "O"}: {name_i if winner == 1 else name_j}')

points = Counter()
print('results:')
for i in range(nplayers):
    for j in range(nplayers):
        if i == j: continue
        player_i, name_i = players_and_names[i]
        player_j, name_j = players_and_names[j]
        winner = results[i][j]
        print(f'{name_i} vs. {name_j}')
        if winner == 0:
            print('nobody won.')
            points[name_i] += 1
            points[name_j] += 1
        elif winner == 1:
            print(f'winner:\t\t\t"X": {name_i}')
            points[name_i] += 2
        else:
            print(f'winner:\t\t\t"O": {name_j}')
            points[name_j] += 2
print('scores (win 2 points, tie 1 point):')
for name in points:
    print(f'{name}: {points[name]}')

