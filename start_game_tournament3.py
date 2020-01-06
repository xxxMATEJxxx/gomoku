#import window.player
import example.player

import buyinggf.player
import stepan.player
import timotej.player
import tomas.player

from gomoku_tournament import GomokuTournament

TIME_LIMIT = 300

players_and_names = [
    (buyinggf.player, 'BuyingGF'),
#    (window.player, 'Martin Španěl'),
#    (example.player, 'example'),
    (stepan.player, 'Štěpán'),
    (timotej.player, 'Tim'),
    (tomas.player, 'Tomáš'),
]

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
        else:
            print(f'winner:\t\t\t{"X" if winner == 1 else "O"}: {name_i if winner == 1 else name_j}')
