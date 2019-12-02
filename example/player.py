class Player:
    def __init__(self, player_sign):
        self.sign = player_sign
        self.name = 'example'
    def play(self, opponent_move):
        if opponent_move == None:
            return (7, 7)
        row, col = opponent_move
        return (row, col+1)
