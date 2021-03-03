import random
patterns=[
(1000000000000,"xxxxx"),
(-1000000000000,"ooooo"),
(5000,"  xx  "),
(-5000,"  oo  "),
(60000," x xx "),
(-60000," o oo "),
(2000000,"xooo x"),
(1000000,"  xxx  "),
(-1000000,"  ooo  "),
(15000 ,"x xx xo"),
(10000000," xxxx "),
(-10000000," oooo "),
(500000,"xxx  "),
(500000,"  xxx"),
(-500000,"ooo  "),
(-500000,"  ooo"),
(60000,"xoo  x"),
(60000,"x oo x"),
(60000,"x  oox"),
(2000,"xx   "),
(2000,"   xx"),
(-2000,"oo   "),
(-2000,"   oo"),
(1,"    x    "),
(-10,"    o    "),
(2,"     x     "),
(4,"      x      "),
(8,"       x       "),
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

    def get(self,row,col):
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
    def row_to_string(self,row):
        output=" "
        for i in row:
            if i==0:
                output += " "
            if i==1:
                output += "x"
            if i==-1:
                output += "o"
        return output
    def evaluate_row(self,row):
        string_row=self.row_to_string(row)
        total_score=0
        for pattern in patterns:
            score, p = pattern
            if p in string_row:
                total_score += score
        return total_score	
    def evaluate_position(self):
        score=0
        for row in self.rows:
            score += self.evaluate_row(row)
        for row in self.columns:
            score += self.evaluate_row(row)
        for row in self.diagonals_ascending:
            score += self.evaluate_row(row)
        for row in self.diagonals_descending:
            score += self.evaluate_row(row)
        return score
class Player:
    def __init__(self, player_sign):
        self.sign = 1
        self.opponent_sign = -1
        self.name = 'Vrba'
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
