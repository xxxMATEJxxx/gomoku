from .map import Map #Imports Class map
from .rate import rate #Rating system 
import numpy
class Player:
    """Defines player class
    Methods:
    __init__(self,player_sign)
    play(self, opponent_move)"""
    def __init__(self, player_sign):
        """Creates self.map which stores Map configuration
            self.sign = X = 1; O = -1"""
        self.sign = player_sign
        self.board = Map()

    def play(self, opponent_move):
        """Argument: opponents move in format (row, colum), writes it in the map, generates our move, writes it in the map and returns (row, collum) of our move """
        self.board.recieve_values(int(self.sign*-1),opponent_move)
        print (opponent_move, "opponent_move")
        if opponent_move == [1,5]:
            print ("6,9")
            for i in self.board.get_board():
                print (i)
            return (6,9)
        else:
            my_move = self.minimax()
        
        self.board.recieve_values(int(self.sign),my_move)
        print (my_move, "my_move")
        return my_move
    def minimax(self):
        """Calls rate function and returns best move"""
        good_moves = rate(self.sign, self.board)
        print (good_moves[1])
        return(int(good_moves[-1, 1]), int(good_moves[-1,2]))
