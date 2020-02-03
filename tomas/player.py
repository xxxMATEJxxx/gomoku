import time


class Player:

    def __init__(self, player_sign):
        self.sign = player_sign
        self.name = 'example'
        self.middleman = Middleman(player_sign)
        self.ValueMaker = Evaluator(player_sign)
        game_field = self.middleman.blankList()
        self.value_list = self.middleman.blankList()
        self.game_field = game_field

    def play(self, opponent_move):
        
        value_list = self.value_list
        if opponent_move == None:
            self.playedNone()
        else:
            (row, col) = opponent_move

            if self.sign == -1:
                self.game_field[row][col] = 1
            else:
                self.game_field[row][col] = -1
            value_list = self.ValueMaker.evaluate(self.game_field,
                    value_list, opponent_move)

        # for i in range(15):
            # print(value_list[i])

        maximum = 0
        maximumPos = [0, 0]
        for i in range(15):
            for j in range(15):
                if value_list[i][j] > maximum:
                    maximum = value_list[i][j]
                    maximumPos = [i, j]

        # for i in range(15):
        #    print(self.game_field[i])

        i = maximumPos[0]
        j = maximumPos[1]
        if self.sign == -1:
            self.game_field[i][j] = -1
        else:
            self.game_field[i][j] = 1
        value_list[i][j] = -499999
        return (i, j)

    def playedNone(self):
        print ("I haven't programmed this path yet.")

        # this should not crash

class Middleman:

    def __init__(self, player_sign):
        self.player_sign = player_sign

    def blankList(self):
        blank = [[0 for x in range(15)] for y in range(15)]
        return blank

    def getLine(self, game_field, lineNumber):
        return game_field[lineNumber]

    def getColumn(self, game_field, columnNumber):
        line = []
        for i in range(15):
            line.append(game_field[i][columnNumber])

        return line

    def getDiagonal(self, game_field):

        # 21 /
        # 21 \
        # = 42 lines total
        # Diagonals are all returned and must be evaluated all every time (for now)
        # the values are written down in corresponding set of values which is then
        # used in function of this instance setDiagonals

        lines = []
        temp = []
        for i in range(11):
            for j in range(i + 5):
                temp.append(game_field[i + 4 - j][j])
            lines.append(temp)
            temp = []
        for i in range(10):
            for j in range(14 - i):
                temp.append(game_field[14 - j][i + 1 + j])
            lines.append(temp)
            temp = []
        for i in range(11):
            for j in range(5 + i):
                temp.append(game_field[4 + i - j][14 - j])
            lines.append(temp)
            temp = []
        for i in range(10):
            for j in range(14 - i):
                temp.append(game_field[14 - j][14 - j - i])
            lines.append(temp)
            temp = []
        return lines

    def setDiagonal(self, diagonalValues):

        # this function converts the values for diagonals back 
        # into a 15x15 field and adds them in the value field.

        lineNumber = 0
        value_list = self.blankList()
        for i in range(11):
            for j in range(i + 5):
                value_list[i + 4 - j][j] = value_list[i + 4 - j][j] \
                    + diagonalValues[lineNumber][j]
            lineNumber = lineNumber + 1
        for i in range(10):
            for j in range(14 - i):
                value_list[14 - j][i + 1 + j] = value_list[14 - j][i
                        + 1 + j] + diagonalValues[lineNumber][j]
            lineNumber = lineNumber + 1
        for i in range(11):
            for j in range(5 + i):
                value_list[4 + i - j][14 - j] = value_list[4 + i
                        - j][14 - j] + diagonalValues[lineNumber][j]
            lineNumber = lineNumber + 1
        for i in range(10):
            for j in range(14 - i):
                value_list[14 - j][14 - j - i] = value_list[14 - j][14
                        - j - i] + diagonalValues[lineNumber][j]
            lineNumber = lineNumber + 1
        return value_list


class Evaluator:

    def __init__(self, player_sign):
        self.Values = Middleman(player_sign)
        self.player_sign = player_sign

    def evaluate(
        self,
        game_field,
        value_list,
        opponent_move,
        ):
        Values = self.Values
        (row, col) = opponent_move
        temp = self.quickValue(Values.getLine(game_field, row), True)

        for i in range(15):
            value_list[row][i] = value_list[row][i] + temp[i]
            value_list[i][col] = value_list[i][col] \
                + self.quickValue(Values.getColumn(game_field, col),
                                  True)[i]

        # Diagonals

        diagonalList = Values.getDiagonal(game_field)
        diagonalValues = []
        for i in range(len(diagonalList)):
            diagonalValues.append(self.quickValue(diagonalList[i],
                                  True))
        diagonalValueList = Values.setDiagonal(diagonalValues)

        for i in range(15):
            for j in range(15):
                value_list[i][j] = value_list[i][j] \
                    + diagonalValueList[i][j]

        return value_list

    def quickValue(self, line, isForward):
        length = len(line)
        lineValue = [0 for x in range(length)]

        # X has the sign 1
        # O has the sign -1

        XinRow = 0
        OinRow = 0
        emptyRow = 0
        beforeRow = -1
        for i in range(length):
            fwVal = line[i]
            if fwVal == 0:
                if XinRow == 4:
                    lineValue[i] = 99999
                elif OinRow == 4:
                    lineValue[i] = 49999
                elif XinRow == 3 and beforeRow == -1:
                    lineValue[i] = 30000
                elif XinRow == 3:
                    lineValue[i] = 20000
                elif OinRow == 4:
                    lineValue[i] = 69999
                elif OinRow > 2:
                    lineValue[i] = 1999

                if beforeRow == 0:
                    lineValue[i] = lineValue[i] + OinRow * 10 + XinRow \
                        * 5
                elif beforeRow == 1:
                    lineValue[i] = lineValue[i] + OinRow * 10
                elif beforeRow == -1:
                    lineValue[i] = lineValue[i] + XinRow * 15

                if XinRow > 0:
                    lineValue[i] = lineValue[i] + 6 ^ XinRow
                if OinRow > 0:
                    lineValue[i] = lineValue[i] + 4 ^ OinRow
                if OinRow == 4:
                    if beforeRow == 1:
                        lineValue[i] = lineValue[i] + 59999
                    else:
                        lineValue[i] = lineValue[i] + 39999

                emptyRow = emptyRow + 1
                if XinRow > 0:
                    XinRow = 0
                    beforeRow = 1
                if OinRow > 0:
                    OinRow = 0
                    beforeRow = -1

            if fwVal == 1:
                XinRow = XinRow + 1
                if OinRow > 0:
                    OinRow = 0
                    beforeRow = -1
                if emptyRow > 0:
                    emptyRow = 0
                    beforeRow = 0
                lineValue[i] = -9999
            if fwVal == -1:
                OinRow = OinRow + 1
                if XinRow > 0:
                    XinRow = 0
                    beforeRow = 1
                if emptyRow > 0:
                    emptyRow = 0
                    beforeRow = 0
                lineValue[i] = -9999

        if isForward:
            reversedLine = []
            for i in range(length):
                reversedLine.append(line[length - i - 1])
            reverseLineValue = self.quickValue(reversedLine, False)
            for i in range(len(lineValue)):
                lineValue[i] = lineValue[i] + reverseLineValue[length
                        - i - 1]

        return lineValue


player = Player(-1)
