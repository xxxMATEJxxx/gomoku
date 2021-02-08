import random
import numpy as np
PATTERNS = [
    (1000000000000000, 'xxxxx'),
    (-1000000000000000, 'ooooo'),
    (5,'xx___'),
    (5,'___xx'),
    (10, '___xx___'),
    (100000, '__xxx__'),
    (10000000, '_xxxx_'),
    (-10, '___oo___'),
    (-100000, '__ooo__'),
    (-10000000, '_oooo_'),  
    (10000, 'xooox'),
    (10000, 'xooo'),
    (10000, 'ooox'),
    (10000, 'ooxoo'),
    (1000000, '_xx_x'),
    (1000000, 'xx_x_'),
    (1000000, '_x_xx'),
    (1000000, 'x_xx_'),
    (-10000000, '_oo_o'),
    (-10000000, 'oo_o_'),
    (-10000000, '_o_oo'),
    (-10000000, 'o_oo_'),
    
    
]

class Board:
    SIZE = 15
    def swapItems(self,p,pos1,pos2):
        result = ""
        plist = p.split()
        print(plist)
        plist[pos1],plist[pos2] = plist[pos2],plist[pos1]
        for i in plist:
            result += i
        return result
    def generatePatternTypes(self):
        #NEFUNKČNÍ ZAÍM
        result = []
        p = ""
        for pattern in PATTERNS:
            if(len(pattern[1].replace("_","")) >= 3 and len(pattern[1].replace("_","")) < 5):
                result = []
                length = len(pattern[1])-1
                for i in range(length):
                    print(i)
                    p = self.swapItems(pattern[1],0,i)
                    result.append((pattern[0],p))
                    p= self.swapItems(p,i,0)
        for r in result:
            PATTERNS.append(pattern)
        print(PATTERNS)
    def generate_rows(self):
        return np.zeros((15,15))

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
    def isFirstRound(self):
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                if (self.rows[x][y] == 1 or self.rows[x][y]== -1):
                    return False
        print("1st round")
        return True
    def __init__(self):
        self.rows = self.generate_rows()
        self.columns = self.generate_rows()
        self.diagonals_descending = self.generate_diagonals()
        self.diagonals_ascending = self.generate_diagonals()
        #self.generatePatternTypes()

    def row_to_string(self, row):
        output = ''
        for i in row:
            if (i == 0):
                output += '_'
            elif (i == 1):
                output += 'x'
            else:
                output += 'o'
        return output

    def evaluate_row(self, row):
        string_row = self.row_to_string(row)
        total_score = 0
        index = 0
        current_pattern = ""
        for pattern in PATTERNS:
            score, p = pattern
            if p in string_row and p.replace("_","") != current_pattern:
                print(f'found pattern {p} in {row}')
                total_score += score
                current_pattern = p.replace(" ","")
        return total_score
    def evaluate_position(self):
        total_score = 0
        for row in self.rows:
            total_score += self.evaluate_row(row)
        for column in self.columns:
            total_score += self.evaluate_row(column)
        for diaga in self.diagonals_ascending:
            total_score += self.evaluate_row(diaga)
        for diagd in self.diagonals_descending:
            total_score += self.evaluate_row(diagd)
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

    def get(self, row, col):
        return self.rows[row][col]
class Player:
    def __init__(self, player_sign):
        self.sign = 1
        self.opponent_sign = -1
        self.name = 'Glonk1.0-SpanelBased'
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
        if(self.board.isFirstRound()):
            print("Hé heheheheh")
            my_turn_row, my_turn_col = self.pick_random_valid_turn()
            self.board.new_turn(my_turn_row,my_turn_col,self.sign)
        else:
            my_turn_row, my_turn_col = self.pick_best_turn()
            self.board.new_turn(my_turn_row, my_turn_col, self.sign)
        return my_turn_row, my_turn_col