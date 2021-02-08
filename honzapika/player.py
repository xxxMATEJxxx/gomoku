import random

PATTERNS = [
    (1000000000000000, 'xxxxx'),
    (-1000000000000000, 'ooooo'),
    (1, '   xx   '),
    (-1, '   oo   '),
    (-10000000, '  ooo  '),
    (10000000, '  xxx  '),
    (10000, '  o xxx x   '),
    (-10000, ' x ooo o   '),
    (1000,  '  x oooxo  '),
    # TODO doplnit vzory
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
                #total_score = total_score + score
        return total_score


    def evaluate_position(self):
        total_score = 0
        for row in self.rows:
            total_score += self.evaluate_row(row)
        for col in self.columns:
            total_score += self.evaluate_column(column)
        # TODO hodnotit i sloupce a diagonaly
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
        self.sign = player_sign
        self.opponent_sign = -player_sign
        self.name = 'Honza Pika'
        self.board = Board()
        random.seed(17)

    def streak_control(self):
        pass

    def pick_random_valid_turn(self):   #vybere náhodny validní pole pro hraní
        while True:
            row = random.randint(0, 14)
            col = random.randint(0, 14)
            if (self.board.get(row, col) == 0): return (row, col)

    def play(self, opponent_move):
        if opponent_move == None:
           return (7,7)
        row, col = opponent_move
        print (opponent_move)
        self.board.new_turn(row, col, self.opponent_sign)
        my_turn_row, my_turn_col = (row+1, col+1)
        self.board.new_turn(my_turn_row, my_turn_col, self.sign)
        my_turn = (row+1, col+1)
        return my_turn
