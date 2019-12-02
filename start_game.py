import window.player
import example.player
from gomoku_tournament import GomokuTournament

playerX = window.player.Player(1)
playerO = example.player.Player(-1)

tournament = GomokuTournament(playerX, playerO)
winner = tournament.game()
tournament.save_logs()
print(f'winner is {winner}')
