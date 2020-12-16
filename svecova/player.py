import numpy as np
from random import randint

class Player:
  def __init__(self, player_sign):
    self.sign = player_sign
    self.name = 'example'
    self.grid = np.zeros((15,15))
  def play(self, opponent_move):
#   if opponent_move == None:
#     return (7, 7)
    row, col = opponent_move
    self.grid[row, col] = -self.sign
    if self.grid[row, col+1] == 0:
      return (row, col+1)
    elif self.grid[row-1, col+1] == 0:
      return (row-1, col+1)
    else:
      return (randint(1,15), randint(1,15))
