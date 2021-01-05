import numpy as np

class Player:
    def __init__(self, player_sign):
        self.sign = player_sign
        self.name = 'example'
        self.hriste = np.zeros((15, 15), int)
        self.op = -1
        self.I = 1



    def play(self, opponent_move):
        

        if opponent_move != None:
            row, col = opponent_move
            self.hriste[row, col] = self.op
        else:
            return (7, 7)
        print(self.hriste)
        self.check()
        self.hriste[row, col] = self.I
        return (row +1, col+1)

    def check(self):
        # vytáhnout zajímavý pozice znaky v řadě(pak potencionální (2 a 2 řady doplněním 1 znaku vytvořím 3 a 3, či 4 s jedním vynechaným, doplněním jednohovzniká řada))
        # zautočit za druhýho, jestli by bylo nebezpečí, defend na to místo, když ne útok sám

        #teď jen sloupečky a řadky; zapsat postupky- kolik, odkud dokud a jestli jsou ohraničený
        # porovnat s rizikovými kombinacemi
        # když nějakou najde, reagovat na ni

        self.postupky = {}
        postup = []
        misto = []
        for y in range(0,15):
            for x in range(0,15):
                if self.hriste[y, x] != 0:
                    misto.append((y,x))
                    postup.append(self.hriste[y, x])
                elif (self.hriste[y, x] == 0 or x == 14) and self.hriste[y, x-1] != 0 and len(misto) >1:
                    self.postupky[misto[0], misto[-1]] = postup
                    postup = []
                    misto = []

        for x in range(0,15):
            for y in range(0,15):
                if self.hriste[y, x] != 0:
                    misto.append((y,x))
                    postup.append(self.hriste[y, x])
                elif (self.hriste[y, x] == 0 or x == 14) and self.hriste[y, x-1] != 0 and len(misto) >1:
                    self.postupky[misto[0], misto[-1]] = postup
                    postup = []
                    misto = []


        print(self.postupky)

