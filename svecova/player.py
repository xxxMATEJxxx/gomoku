import numpy as np
from random import randint

class Player:
  def __init__(self, player_sign):
    self.sign = player_sign
    self.name = 'example'
    self.grid = np.zeros((15,15))
    self.r = -1
    self.c = -1
    self.round = 0
  def play(self, opponent_move):
#   if opponent_move == None:
#     return (7, 7)
    row, col = opponent_move
    self.grid[row, col] = -self.sign
    if self.round < 2:
      if self.grid[row, col+1] == 0 and col < 15:
        self.round = self.round + 1
        self.r = row
        self.c = col+1
        return (row, col+1)
      else: 
        self.round = self.round + 1
        self.r = row
        self.c = col-1
        return(row, col-1)
    else:
      if self.grid[self.r+1, self.c] == 0 and self.r < 15:
        r = self.r+1
        c = self.c
        self.r = self.r+1
        self.c = self.c
        return(r, c)
      elif self.grid[self.r+1, self.c+1] == 0 and self.r < 15 and self.c < 15:
        r = self.r+1
        c = self.c+1
        self.r = self.r+1
        self.c = self.c+1
        return(r, c)
      elif self.grid[self.r+1, self.c-1] == 0 and self.r < 15 and self.c >0:
        r = self.r+1
        c = self.c-1
        self.r = self.r+1
        self.c = self.c-1
        return(r, c)
      elif self.grid[self.r-1, self.c] == 0 and self.r > 0:
        r = self.r-1
        c = self.c
        self.r = self.r-1
        self.c = self.c
      elif self.grid[self.r-1, self.c+1] == 0 and self.r > 0 and self.c < 15:
        r = self.r-1
        c = self.c
        self.r = self.r-1
        self.c = self.c
      elif self.grid[self.r-1, self.c-1] == 0 and self.r > 0 and self.c >0:
        r = self.r-1
        c = self.c
        self.r = self.r-1
        self.c = self.c
        return(r, c)
      else:
        r = randint(0,14)
        c = randint(0,14)
        self.r = r
        self.c = c
        return(r, c)
