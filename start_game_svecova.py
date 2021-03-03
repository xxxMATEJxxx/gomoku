import window.player
import svecova.player02
import svecova.player01
import sebastian.player
import martins.player
import lionel.player
import janmrzilek.player
from gomoku_tournament import GomokuTournament

playerX = window.player.Player(1)
playerO = janmrzilek.player.Player(-1)

tournament = GomokuTournament(playerX, playerO, 300)
winner = tournament.game()
tournament.save_logs()
print(f'winner is {winner}')
