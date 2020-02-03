import numpy as np
import random
from random import randint
players = [-1, 1]

grid_size = 15

content = [[0]*grid_size for n in range(grid_size)]
grid = np.array(content)
minx = 0
maxx = 0
miny = 0
maxy = 0


best_draft = (0, 0)
  
class Player:
  def __init__(self, player_sign):
      self.sign = player_sign
      if self.sign == 1:
        self.opponent_sign = -1
      else:
        self.opponent_sign = 1
      self.name = 'mateju'
      
  minx = -1
  maxx = -1
  miny = -1
  maxy = -1
        
  all_patterns = [
    (10000000, [1,1,1,1,1]),
    (2, [0,1,0]),
    (10, [0,1,1,0]),
    (10, [0,1,0,1,0]),
    (500, [-1,1,1,1,0]),
    (500, [0,1,1,1,-1]),
    (1000, [0,1,1,1,1,-1]),
    (1000, [-1,1,1,1,1,0]),
    (5000, [0,1,1,1,0]),
    (100000, [0,1,1,1,1,0]),   
    (10000000, [-1,-1,-1,-1,-1]),
    (2, [0,-1,0]),
    (10, [0,-1,-1,0]),
    (10, [0,-1,0,-1,0]),
    (500, [1,-1,-1,-1,0]),
    (500, [0,-1,-1,-1,1]),
    (1000, [0,-1,-1,-1,-1,1]),
    (1000, [1,-1,-1,-1,-1,0]),
    (5000, [0,-1,-1,-1,0]),
    (100000, [0,-1,-1,-1,-1,0])
    ]
  
  terminal_patterns = [
    (1, [1,1,1,1,1]),
    (1, [-1,-1,-1,-1,-1]),
    ]  

  def evaluate_row(self, row, patterns, bonus_sign):
      row_score = 0
      for pattern_score, pattern in patterns:
          for i in range(len(row) - len(pattern)):
              if np.all(pattern == row[i:i+len(pattern)]):
                  row_score += pattern_score*bonus_sign
      return row_score

  def evaluate(self, text_grid, patterns, minx, maxx, miny, maxy, bonus_sign):
          score = 0
          subgrid = text_grid[minx:maxx+1, miny:maxy+1]
          flipped_subgrid = np.flip(subgrid, 0)
          for i in range(maxx-minx+1):
              score += self.evaluate_row(subgrid[i,:], patterns, bonus_sign)
          for i in range(maxy-miny+1):
              score += self.evaluate_row(subgrid[:,i], patterns, bonus_sign)
          for i in range (maxx+maxy-1):
              score += self.evaluate_row(np.diag(subgrid, i-maxy), patterns, bonus_sign)
              score += self.evaluate_row(np.diag(flipped_subgrid, i-maxx), patterns, bonus_sign)
          return score
      
  def is_terminal_node (self, text_grid, minx, maxx, miny, maxy, bonus_sign):
     if self.evaluate(text_grid, self.terminal_patterns, minx, maxx, miny, maxy, bonus_sign) > 0:
         return True 
     return not self.can_play(text_grid)
     
  def can_play(self, text_grid):
      for i in range(grid_size):
            for j in range(grid_size):
                if text_grid[i][j] == 0:
                    return True
      return False
     
  def alphabeta(self, text_grid, depth, alpha, beta, maximizingPlayer, minx, maxx, miny, maxy):
    step = (None, None)
    bonus_sign = self.sign if maximizingPlayer else self.opponent_sign
    if depth == 0 or self.is_terminal_node(text_grid, minx, maxx, miny, maxy, bonus_sign) == True:
        return (self.evaluate(text_grid, self.all_patterns, minx, maxx, miny, maxy, bonus_sign), step)
    if maximizingPlayer == True:
        value = -2000000000
        should_break = False
        for i in range(minx, maxx+1):
            for j in range(miny, maxy+1):
                if text_grid[i, j] == 0:
                    text_grid[i, j] = self.sign
                    child_value = self.alphabeta(text_grid, depth - 1, alpha, beta, False, max(0, min(minx, i-1)), min(grid_size - 1,max(maxx, i+1)), max(0, min(miny, j-1)), min(grid_size - 1,max(maxy, j+1)))[0]
                    if value < child_value:
                        value = child_value
                        step = (i, j)
                    alpha = max(alpha, value)
                    text_grid[i, j] = 0
                    if alpha >= beta:
                        should_break = True
                        break
            if should_break:
                break
        return (value, step)
    else:
        value = 2000000000
        should_break = False
        for i in range(minx, maxx+1):
            for j in range(miny, maxy+1):
                if text_grid[i, j] == 0:
                    text_grid[i, j] = self.opponent_sign
                    child_value = self.alphabeta(text_grid, depth - 1, alpha, beta, True, max(0, min(minx, i-1)), min(grid_size - 1,max(maxx, i+1)), max(0, min(miny, j-1)), min(grid_size - 1,max(maxy, j+1)))[0]
                    value = min(value, child_value)
                    beta = min(beta, value)
                    text_grid[i, j] = 0
                    if alpha >= beta:
                        should_break = True
                        break
            if should_break:
                break
        return (value, step)
       
  
  def play(self, opponent_move):
      if opponent_move == None:
        if grid[7, 7] == 0:
          self.minx = 6
          self.maxx = 8
          self.miny = 6
          self.maxy = 8
          return (7, 7)
      else:
        i = opponent_move[0]
        j = opponent_move[1]
        grid[i, j] = self.opponent_sign
        
      self.minx = max(0, i-1 if self.minx == -1 else min(self.minx, i-1))
      self.maxx = min(grid_size - 1,i+1 if self.maxx == -1 else max(self.maxx, i+1))
      self.miny = max(0, j-1 if self.miny == -1 else min(self.miny, j-1))
      self.maxy = min(grid_size - 1,j+1 if self.maxy == -1 else max(self.maxy, j+1))
      best_draft = self.alphabeta (grid, 2, -2000000000, 2000000000, True, self.minx, self.maxx, self.miny, self.maxy)
      draft_value = best_draft[0]
      draft_step = best_draft[1]
      i = draft_step[0]
      j = draft_step[1]
      grid[i, j] = self.sign
      self.minx = max(0, min(self.minx, i-1))
      self.maxx = min(grid_size - 1,max(self.maxx, i+1))
      self.miny = max(0, min(self.miny, j-1))
      self.maxy = min(grid_size - 1,max(self.maxy, j+1))
      return draft_step

