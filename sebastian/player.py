import random

PATTERNS = [
    (10000000000000000, 'xxxxx'),
    (-100000000000000000, 'ooooo'),
    
    (100000000, ' xxxx '),
    (-1000000000, ' oooo '), 

    (-100000000000, 'oxxxx '),
    (-100000000000, ' xxxxo'),

    (-10000000000, 'xoooo '),
    (-10000000000, ' oooox'),

    (-100000000, 'oo oo'),   # O O _ O O

    (1000000, '  xxx  '),  # _ _ X X X _ _
    (-1000000, '  ooo  '), # _ _ O O O _ _ 
    
    (-100, ' o o '),    
    
    (10, '   xx   '), # _ _ _ X X _ _ _
    (-10, '   oo   '),# _ _ _ O O _ _ _ 

    (1000, 'xooox'),
    (1000, 'xooox'),
    (1000, 'xooo'),
    (1000, 'ooox'),
    
    (-10000000, ' oo o'),
    (-10000000, 'oo o '),
    (-10000000, ' o oo'),
    (-10000000, 'o oo '),
    
    (-100000000, 'xx  o'),
    (-100000000, 'o  xx')
    
    

]
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

    def row_to_string(self, row):
        output = ''
        for i in row:
            if (i == 0):
                output += ' '
            if (i == 1):
                output += 'x'
            if (i == -1):
                output += 'o'
        return output

    def evaluate_row(self, row):
        string_row = self.row_to_string(row)
        total_score = 0
        for pattern in PATTERNS:
            score, p = pattern
            if p in string_row:
                print(f'found pattern {p} in {row}')
                total_score += score
        return total_score


    def evaluate_position(self):
        total_score = 0
        for row in self.rows:
            total_score += self.evaluate_row(row)
        for col in self.columns:
            total_score += self.evaluate_row(col)
        for asc in self.diagonals_ascending:
            total_score += self.evaluate_row(asc)
        for desc in self.diagonals_descending:
            total_score += self.evaluate_row(desc)
        return total_score

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
        #self.print_all()

    def get(self, row, col):
        return self.rows[row][col]

    def print_all(self):
        print('rows')
        for row in self.rows:
            print(row)
        print('cols')
        for col in self.columns:
            print(col)
        print('desc')
        for d in self.diagonals_descending:
            print(d)
        print('asc')
        for d in self.diagonals_ascending:
            print(d)

class Player:
    def __init__(self, player_sign):
        self.sign = 1
        self.opponent_sign = -1
        self.name = 'Sebastian bot'
        self.board = Board()
        random.seed(17)

    def pick_random_valid_turn(self):
        while True:
            row = random.randint(0, 14)
            col = random.randint(0, 14)
            if (self.board.get(row, col) == 0): return (row, col)

    def pick_best_turn(self):
        best_score = -float('inf')
        best_turn = None
        for row in range(15):
            for col in range(15):
                if (self.board.get(row, col) != 0): continue
                self.board.new_turn(row, col, self.sign)
                score = self.board.evaluate_position()
                if score > best_score:
                    best_turn = (row, col)
                    best_score = score
                self.board.new_turn(row, col, 0)
        return best_turn

    def play(self, opponent_move):
        if opponent_move != None:
            row, col = opponent_move
            self.board.new_turn(row, col, self.opponent_sign)
        #my_turn_row, my_turn_col = self.pick_random_valid_turn()
        my_turn_row, my_turn_col = self.pick_best_turn()
        self.board.new_turn(my_turn_row, my_turn_col, self.sign)
        return my_turn_row, my_turn_col
