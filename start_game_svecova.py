import window.player
import svecova.player
import sebastian.player
from gomoku_tournament import GomokuTournament

playerX = window.player.Player(1)
playerO = svecova.player.Player(-1)

tournament = GomokuTournament(playerX, playerO, 300)
winner = tournament.game()
tournament.save_logs()
print(f'winner is {winner}')
