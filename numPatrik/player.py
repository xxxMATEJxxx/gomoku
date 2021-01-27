import numpy as np

class Board:
    def __init__(self):
        self.SIZE = 15
        self.rows = np.zeros((15, 15), dtype="i")
        self.columns = np.zeros((15, 15), dtype="i")
        self.diagonals_asc = self.generate_diagonals()
        self.diagonals_disc = self.generate_diagonals()
        self.sets = {
                    "010": 5,
                     "0110": 50,
                     "01110": 100,
                     "11110": 150,
                     "01111": 151,
                     "011110": 152,
                     "210":3,
                     "2110": 10,
                     "21110" :40,
                     "211110" : 153,
                     "2" : 1,
                     "012": 2,
                     "0112": 11,
                     "01112": 40,
                     "011112": 154,
                     "22220": 140,
                     "02222": 141,
                     "0220": 49,
                     "122220": 142,
                     "022221" : 143,
                     "02220": 99,

                     }

        self.sign = 1
        self.opponent_sign = 2


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

    def checkingOP (self):
        story = ""
        choices = []
        BOARD = [self.rows, self.columns, self.diagonals_asc, self.diagonals_disc]
        for type in BOARD:
            for row in type:
                for char in row:
                    story += str(char)
                story += ","


        for combination in self.sets.keys():
            comPlace =story.find(combination)
            if comPlace > 0:
                choices.append((comPlace, combination, self.sets[combination]))


        best = (88,"0",0) # pozměnit tak, aby na zač dávalo nějaké pěkné souřadnice
        for chance in choices:
            if best[2] < chance[2]:
                best = chance

        print(best)
        return self.placing(best)

    def placing(self, best):
        print(best)
        thePlace = best[0] + best[1].find("0")
        if thePlace < 480:
            if thePlace > 240: thePlace -= 240
            self.y = thePlace // 16
            self.x = thePlace % 16
        else: #diagonals
            p = -1 #souřadnice od nuly
            asc_dis = 1
            thePlace -= 480
            if thePlace < 135 or  254< thePlace < 389 :
                if thePlace < 135: asc_dis = -1
                for pp in range (2,17):
                    p += pp
                    if thePlace < p:
                        self.x = thePlace - p - 1
                        self.y = pp - 3 + self.x * asc_dis #protože čárky, zač. 1, a protoře číslo se nachzí o jednu řadu níž

            elif 135 < thePlace < 254 or thePlace > 389: # když se to nachází v druhé polovině mezi zmenšujími se
                row = 0
                if thePlace > 389:
                    thePlace -= 389
                    asc_dis = 0
                else: thePlace -= 135
                for pp in range (2,16):
                    pp = 16-pp
                    row += 1
                    p += pp
                    if thePlace < p:

                        self.y = 15*asc_dis - thePlace -1
                        self.x = row + thePlace

        return (self.y, self.x)




        #převedení best/chance na souřadnic vhodného tahu a vrácení jich

    def new_turn(self, row, column, player):
        self.rows[row][column] = player
        self.columns[column][row] = player
        ascending_diagonal_number = row + column
        if (row + column < self.SIZE):
            self.diagonals_asc[ascending_diagonal_number][column] = player
        else:
            self.diagonals_asc[ascending_diagonal_number][self.SIZE - 1 - row] = player
        descending_diagonal_number = self.SIZE - 1 - row + column
        if (descending_diagonal_number < 15):
            self.diagonals_disc[descending_diagonal_number][column] = player
        else:
            self.diagonals_disc[descending_diagonal_number][row] = player





b = Board()
b.checkingOP()



class Player:
    def __init__(self, player_sign):
        self.sign = 1
        self.opponent_sign = 2
        self.name = 'Patrik'
        self.board = Board()

    def play(self, opponent_move):
        if opponent_move != None:
            row, col = opponent_move
            self.board.new_turn(row, col, self.opponent_sign)

        my_turn_row, my_turn_col = self.board.checkingOP()
        self.board.new_turn(my_turn_row, my_turn_col, self.sign)
        print(self.board.rows, self.board.columns, self.board.diagonals_asc, self.board.diagonals_disc)
        return my_turn_row, my_turn_col
