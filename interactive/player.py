class Player:
    def __init__(self, player_sign):
        self.sign = player_sign

    def play(self, opponent_move):
        print(f'opponent played {opponent_move}')
        print('your move?')
        row = int(input('row'))
        col = int(input('col'))
        return (row, col)