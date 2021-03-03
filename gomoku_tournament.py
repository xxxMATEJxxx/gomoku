import traceback
import time
import pdb

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
            streak = value

        if streak >= WINNING_LENGTH:
            return 1
        if streak <= -WINNING_LENGTH:
            return -1
    return 0

class Board:
    SIZE = 15

    def generate_rows(self):
        rows = []
        for i in range(self.SIZE):
            row = []
            for j in range(self.SIZE):
                row.append(0)
            rows.append(row)
        return rows

    def generate_diagonals(self):
        diagonals = []
        delka = 1
        for i in range(self.SIZE):
            diagonal = []
            for j in range(delka):
                diagonal.append(0)
            diagonals.append(diagonal)
            delka += 1
        delka = 14
        for i in range(self.SIZE - 1):
            diagonal = []
            for j in range(delka):
                diagonal.append(0)
            diagonals.append(diagonal)
            delka -= 1
        return diagonals

    def __init__(self):
        self.rows = self.generate_rows()
        self.columns = self.generate_rows()
        self.diagonals_descending = self.generate_diagonals()
        self.diagonals_ascending = self.generate_diagonals()

    def new_turn(self, row, column, player):
        self.rows[row][column] = player
        self.columns[column][row] = player
        ascending_diagonal_number = row + column
        if (row + column < self.SIZE):
            self.diagonals_ascending[ascending_diagonal_number][column] = player
        else:
            self.diagonals_ascending[ascending_diagonal_number][self.SIZE - 1 - row] = player
        descending_diagonal_number = self.SIZE - 1 - row + column
        if (descending_diagonal_number < 15):
            self.diagonals_descending[descending_diagonal_number][column] = player
        else:
            self.diagonals_descending[descending_diagonal_number][row] = player

    def get_lines(self):
        return self.rows + self.columns + self.diagonals_ascending + self.diagonals_descending

    def get(self, row, col):
        return self.rows[row][col]
class GomokuTournament:
    def __init__(self, playerX, playerO, time_limit):
        self.playerX = playerX
        self.playerO = playerO
        self.timer = {}
        self.timer[playerX] = time_limit
        self.timer[playerO] = time_limit
        self.board = Board()
        self.history = []

    def game(self):
        print(f'started game X:{self.playerX.name} vs. O:{self.playerO.name}')
        coordsO = None
        coordsX = None
        while True:
            coordsX = self.player_move(self.playerX, coordsO)
            coordsX = self.placeSymbol(X, coordsX)
            if (self.whoWon() != 0):
                break
            coordsO = self.player_move(self.playerO, coordsX)
            coordsO = self.placeSymbol(O, coordsO)
            if (self.whoWon() != 0):
                break
            if (coordsX == None and coordsO == None):
                print('nobody played a valid move in this round. it is a split.')
                return 0
        winner = self.whoWon()
        return winner

    def player_move(self, player, opponent_move):
        coords = None
        start_time = time.time()
        print(f'{player.name} thinking...', flush=True)
        try:
            coords = player.play(opponent_move)
        except Exception as e:
            print(f'player {player.name} crashed')
            print(e)
            traceback.print_exc()
        duration = time.time() - start_time
        self.timer[player] -= duration
        print(f'{player.name} played {coords}')
        print(f'{player.name} has {self.timer[player]:.2f} s left')
        return coords


    def whoWon(self):
        if self.timer[self.playerX] < 0:
            print(f'{self.playerX.name} ran out of time')
            return -1
        if self.timer[self.playerO] < 0:
            print(f'{self.playerO.name} ran out of time')
            return 1

        for line in self.board.get_lines():
            score = whoWonRow(line)
            if score != 0: return score
        return 0

    def save_logs(self):
      with open('logs.txt', 'a') as output_file:
        output_file.write(f'X: {self.playerX.name} vs. O:{self.playerO.name}\n')
        for line in self.history:
          output_file.write(f'{"X" if line[0] == 1 else "O"}\t{line[1]}\t{line[2]}\n')

    def placeSymbol(self, player, coords):
        try:
            row, col = coords
            if row >= 15 or row < 0 or col >= 15 or col < 0:
                print(f'invalid coordinates {coords}')
                return None
            if self.board.get(row, col) != 0:
                print(f'invalid move. {coords} is already taken')
                return None
            self.board.new_turn(row, col, player)
            self.history.append((player, row, col))
            return (row, col)
        except Exception as err:
            print(err)
            print(f'cannot place on coordinates {coords}')
            return None
