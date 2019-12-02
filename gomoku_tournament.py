import numpy as np

GRID_SIZE = 15
WINNING_LENGTH = 5

X = 1
O = -1

def whoWonRow(row):
    streak = 0
    for value in row:
        if streak >= 0 and value == 1:
            streak += 1
        elif streak <= 0 and value == -1:
            streak -= 1
        else:
            streak = 0

        if streak >= WINNING_LENGTH:
            return 1
        if streak <= -WINNING_LENGTH:
            return -1
    return 0
  

class GomokuTournament:
    def __init__(self, playerX, playerO):
        self.playerX = playerX
        self.playerO = playerO
        self.grid = np.zeros((GRID_SIZE, GRID_SIZE), int)
        self.history = []
    def game(self):
        coordsO = None
        coordsX = None
        while True:
            coordsX = self.playerX.play(coordsO)
            self.placeSymbol(X, coordsX)
            if (self.whoWon() != 0):
                break
            coordsO = self.playerO.play(coordsX)
            self.placeSymbol(O, coordsO)
            if (self.whoWon() != 0):
                break
        return self.whoWon()

    def whoWon(self):
        score = 0
        for i in range(15):
            score += whoWonRow(self.grid[i,:]) # check i-th row
            score += whoWonRow(self.grid[:,i]) # check i-th column
            score += whoWonRow(self.grid.diagonal(i+1)) # check diagonals, upper right
            score += whoWonRow(self.grid.diagonal(-i)) # check diagonals, lower left
            score += whoWonRow(np.fliplr(self.grid).diagonal(i+1)) # check diagonals, upper left
            score += whoWonRow(np.fliplr(self.grid).diagonal(-i)) # check diagonals, lower right
        return score

    def save_logs(self):
      with open('logs.txt', 'w+') as output_file:
        output_file.write(f'X: {self.playerX.name} vs. O:{self.playerO.name}')
        for line in self.history:
          output_file.write(f'{"X" if line[0] == 1 else "O"}\t{line[1]}\t{line[2]}')

    def placeSymbol(self, player, coords):
        try:
            row, col = coords
            if row >= 15 or row < 0 or col >= 15 or col < 0:
                print(f'invalid coordinates {coords}')
                return
            if self.grid[row, col] != 0:
                print(f'invalid move. {coords} is already taken')
                return
            self.grid[row, col] = player
            self.history.append((player, row, col))
        except Exception as err:
            print(err)
            print(f'cannot place on coordinates {coords}')
