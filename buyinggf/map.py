import numpy  as np

X = 1
O = -1

class Map:
    def __init__(self):
      self.plan = np.zeros((15,15), dtype=int)
      
    def recieve_values(self, who, coords): # who určuje který hráč, coords nejdřív x, pak y      
      if(coords == None or self.plan[int(coords[0]), int(coords[1])] != 0):
        print("Wrong Move")
        return
      else:
        ("Move saved")
        self.plan[int(coords[0]), int(coords[1])] = who
      
    def get_board(self):
      self.board = np.array(self.plan) #copy of plan
      return (self.board) #easy way to get the nparray of the plan
