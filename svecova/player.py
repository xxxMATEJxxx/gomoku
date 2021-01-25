import numpy as np
from random import randint

class Player:
  def __init__(self, player_sign):
    self.sign = player_sign
    self.name = 'Hana Svecova'
    self.grid = np.zeros((15,15))
    self.r = -1                            # mé souřadnice řádku
    self.c = -1                            # mé souřadnice sloupce
    self.round = 0
  def play(self, opponent_move):
    if opponent_move == None:
        r = randint(4,10)
        c = randint(4,10)
        self.r = r
        self.c = c
        self.grid[r, c] = self.sign
        return(r, c)

    row, col = opponent_move
    self.grid[row, col] = -self.sign
    r, c = self.pick_turn(row, col)
    self.grid[r, c] = self.sign
    return (r, c)

  def pick_random_valid_turn(self):
    while True:
      row = random.randint(0, 14)
      col = random.randint(0, 14)
      if (self.board.get(row, col) == 0): return (row, col)

  def pick_turn(self, row, col):
    if self.round < 2:                             # pokud je počet kol menší než dva
      if col < 14 and self.grid[row, col+1] == 0:  # pokud je v pravo od posledního tahu oponenta místo a zároveň nejsme na kraji
        print((row, col))
        self.round = self.round + 1                # počet kol se o jedno zvýší
        self.r = row                               # mé souřadnice řádku se nastaví na souřadnice oponenta
        self.c = col+1                             # mé souřadnice řádku se nastaví na o jedno vyšší než souřadnice oponenta
        return (row, col+1)                        # křížek se nakreslí v pravo od oponenta
      else:                                        # pokud není místo vpravo,
        self.round = self.round + 1
        self.r = row
        self.c = col-1
        return(row, col-1)                         # křížek se nakreslí vlevo
    else:
      r, c = self.pick_expansive_turn()
      return (r, c)

  def pick_expansive_turn(self):
      if self.r < 14 and self.grid[self.r+1, self.c] == 0: # pokud je místo pod posledním naším umístěním,
        r = self.r+1
        c = self.c
        self.r = self.r+1
        self.c = self.c
        self.grid[r,c] = self.sign
        return(r, c)                                       # nakreslí se křížek pod posledním naším umístěním
      elif self.r > 0 and self.grid[self.r-1, self.c] == 0:
        r = self.r-1
        c = self.c
        self.r = self.r-1
        self.c = self.c
        return(r, c)                                       # nahoru o 1
      elif self.r > 0 and self.grid[self.r-1, self.c] == self.sign:  
        r = self.r-2
        c = self.c
        self.r = self.r-2
        self.c = self.c
        return(r, c)                                       # nahoru o 2
      elif self.r > 0 and self.grid[self.r-2, self.c] == self.sign:  #???
        r = self.r-3
        c = self.c
        self.r = self.r-3
        self.c = self.c
        return(r, c)                                       # nahoru o 3
      elif self.r < 14 and self.c < 14 and self.grid[self.r+1, self.c+1] == 0:
        r = self.r+1
        c = self.c+1
        self.r = self.r+1
        self.c = self.c+1
        return(r, c)                                       # vpravo dole
      elif self.r < 14 and self.c >0 and self.grid[self.r+1, self.c-1] == 0:
        r = self.r+1
        c = self.c-1
        self.r = self.r+1
        self.c = self.c-1
        return(r, c)                                       # vlevo dole
      elif self.r > 0 and self.c > 0 and self.grid[self.r-1, self.c-1] == 0:
        r = self.r-1
        c = self.c-1
        self.r = self.r-1
        self.c = self.c-1
        return(r, c)                                       # vlevo nahoře
      elif self.r > 0 and self.c < 14 and self.grid[self.r-1, self.c-1] == 0:
        r = self.r-1
        c = self.c+1
        self.r = self.r-1
        self.c = self.c+1
        return(r, c)                                       # vpravo nahoře
      else:
        r, c = pick_random_valid_turn()
        return(r,c)
#        r = randint(4,10)
#        c = randint(4,10)
#        self.r = r
#        self.c = c
#        return(r, c)
