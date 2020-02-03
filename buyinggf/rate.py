import numpy as np
import random

X = 1
O = -1
PLAN_SIZE = 15

patterns = [
    (2, np.array(
      [0, 1, 0]
    )),
    (10, np.array(
      [0, 1, 1, 0]
    )),
    (100, np.array(
      [0, 1, 1, 1, 0]
    )),
    (10000, np.array(
      [0, 1, 1, 1, 1, 0]
    )),
    (500, np.array(
      [-1, 1, 1, 1, 1, 0]
    )),
    (500, np.array(
      [0, 1, 1, 1, 1, -1]
    )),
    (5000, np.array(
      [1, 1, 0, 1, 1]
    )),
    (5, np.array(
      [0, 1, 0, 1, 0]
    )),
    (69, np.array(
      [0, 1, 1, 0, 1, 0]
    )),
    (69, np.array(
      [0, 1, 1, 0, 1, 0]
    )),
    (50, np.array(
      [-1, 1, 1, 1, 0]
    )),
    (50, np.array(
      [0, 1, 1, 1, -1]
    )),
    (5, np.array(
      [-1, 1, 1, 0]
    )),
    (5, np.array(
      [0, 1, 1, -1]
    )),
    (1, np.array(
      [-1, 1, 0]
    )),
    (1, np.array(
      [-1, 1, 0]
    )),
    (880, np.array(
      [0, 1, 0, 1, 1, 1, 0]
    )),
    (880, np.array(
      [0, 1, 1, 1, 0, 1, 0]
    )),
]

def whoWonRow(row, sign):
    """Returns number of signs in a given row"""
    streak = 0
    ret = 0
    for i in patterns:
      patt = i[1]
      for j in range(len(row)-len(patt)):
        for k in range(len(patt)):
          if patt[k] == row[j+k]:
            ret += i[0]
    return ret
    
def whoWon(board, whosign):
        """Scores given board"""
        score = 0
        for i in range(PLAN_SIZE):
            score += whoWonRow(board[i,:], whosign) # check i-th row
            score += whoWonRow(board[:,i], whosign) # check i-th column
            score += whoWonRow(board.diagonal(i+1), whosign) # check diagonals, upper right
            score += whoWonRow(board.diagonal(-i), whosign) # check diagonals, lower left
            score += whoWonRow(np.fliplr(board).diagonal(i+1), whosign) # check diagonals, upper left
            score += whoWonRow(np.fliplr(board).diagonal(-i), whosign) # check diagonals, lower right
            
        return score

def rate(who, board):
    print("rate")
    moves = [] 
    for row in range(np.shape(board.plan)[0]):
        for column in range(np.shape(board.plan)[1]):                                    
            if not board.plan[column,row]:                
                moving_board = board.get_board()
                moving_board[column, row] = who                
                this_score = whoWon(moving_board, who)            
                moves.append((this_score,column,row))                
    moves = sorted(moves)
    ret = np.array(moves[-10:])
    return ret


#(([],[]),x)
