FUTURE = 0
WIN = 5

class Player:
  def __init__(self, player_sign, board = None, deep = 0):
    self.deep = deep
    self.sign = player_sign
    self.name='basicplayer'
    if self.sign == -1:
      self.sign = 'O'
      self.op_sign = 'X'
    else:
      self.sign = 'X'
      self.op_sign = 'O'
      
    self.board = Board(board, 15, self.sign)


  def play(self, opponent_move):
    if opponent_move == None:
      if self.board.price == 0:
        self.board.write(self.sign, 7, 7)
        return (7, 7)
    else:
      col, row = opponent_move
      self.board.write(self.op_sign, row, col)
    option = self.think()
    self.board.write(self.sign, option[-1][0], option[-1][1])
    self.board.print_()
    return(option[-1][-1], option[-1][0])

  def think(self):
    options = []
    is_cross = self.sign == 'X'
    limit=0
    for x in range(15):
      for y in range(15):
        if self.board.scheme[y][x] == 0:
          copy_ = self.board.make_copy()
          copy_.write(self.sign, x, y)
          if is_cross:
            cond = copy_.points > limit
          else:
            cond = copy_.points < limit
          done = False
          if len(options) == 0:
            options.append([copy_,(x, y)])
          elif (len(options) <= 10) or cond:
            for o in range(len(options)):
              if is_cross:
                cond = copy_.points < options[o][0].points
              else:
                cond = copy_.points > options[o][0].points
              if cond:
                options = options[:o]+[[copy_,(x, y)]]+options[o:]
                done = True
                break
            if not done:
              options.append([copy_,(x, y)])
            if len(options) > 10:
              trash = options.pop(0)
              del(trash)
            limit = options[0][0].points
          else: del(copy_)

    if self.deep >= FUTURE:
      best = [options[-1][0].points, options[-1][1]]
    else:
      best = [self.real_price(options[-1][0]),options[-1][1]]
      for i in range(2,len(options)+1):
        opt=options[-i]
        real_points = self.real_price(opt[0])
        if is_cross:
          cond = real_points > best[0]
        else:
          cond = real_points < best[0]
        if cond:
          best = [real_points, opt[1]]
    return(best)                                      #best = [points, (x, y)]
  
  def real_price(self, testboard):
    mindplayer = Mindplayer(self.op_sign, testboard, self.deep+1)
    price = mindplayer.think()
    del(mindplayer)
    return(price[0])
    
    
    
class Mindplayer(Player):
  def __init__(self, player_sign, board, deep):
    super().__init__(player_sign)
    self.board = board
    self.deep = deep


class Board:
  def __init__(self, previous_, n, sign):
    self.sign = sign
    if sign == 'X':
      self.op_sign = 'O'
    else:
      self.op_sign = 'X'
    self.n = n
    self.scheme = []                # coords - [y][x]
    self.points = 0
    line=[0]*n
    for i in range(n):
      self.scheme.append(line[:])
    self.rows = [0]*n
    self.columns = [0]*n
    self.uprigs = {}                 # / diagonal - index = x+y
    for i in range(0, 2*n-1):
      self.uprigs[i] = 0
    self.dorigs = {}                 # \ diagonal - index = x-y
    for i in range(0,n):
      self.dorigs[i] = 0
      self.dorigs[-i] = 0

    if previous_ != None:
      for i in range(n):
        self.scheme[i] = previous_.scheme[i][:]
      self.rows = previous_.rows[:]
      self.columns = previous_.columns[:]
      for key in previous_.uprigs:
        self.uprigs[key] = previous_.uprigs[key]
      for key in previous_.dorigs:
        self.dorigs[key] = previous_.dorigs[key]
      self.points = previous_.points
  def write(self,xo,x,y):
    self.scheme[y][x] = xo
    row = self.scheme[y][:]
    column = []
    for i in range(self.n):
      column.append(self.scheme[i][x])
    dorig = []
    index = x-y
    if index>0:
      for i in range(self.n-index):
        dorig.append(self.scheme[i][i+index])
    else:
      for i in range(self.n+index):
        dorig.append(self.scheme[i-index][i])
    uprig = []
    index = x+y
    if index <= self.n-1:
      for i in range(index+1):
        uprig.append(self.scheme[i][index-i])
    else:
      for i in range(index-(self.n-1),self.n):
        uprig.append(self.scheme[i][index-i])      
    row_v = self.price(row)
    column_v = self.price(column)
    dorig_v = self.price(dorig)
    uprig_v = self.price(uprig)
    increase = 0
    increase += row_v - self.rows[y]
    self.rows[y] = row_v
    increase += column_v-self.columns[x]
    self.columns[x] = column_v
    if dorig_v:
      increase += dorig_v-self.dorigs[x-y]
      self.dorigs[x-y] = dorig_v
    if uprig_v:
      increase += uprig_v-self.uprigs[x+y]
      self.uprigs[x+y] = uprig_v
    self.points += increase

  def price(self,line):
    length_ = len(line)
    if length_ < WIN:
      return(None)
    x = 0
    o = 0
    if self.sign == 'X':
      o = 1
    else:
      x = 1
    price = 0
    for i in range(WIN):
      if line[i] == 'X':
        x += 1
      if line[i] == 'O':
        o += 1
    for i in range(length_ - WIN+1):
      if (x != 0) and (o != 0):
        pass
      elif (x != 0):
        price += 1000**x
      elif (o != 0):
        price -= 1000**o
      try:
        if line[i] == 'X':
          x -= 1
        elif line[i] == 'O':
          o -= 1
        if line[i+WIN] == 'X':
          x += 1
        elif line[i+WIN] == 'O':
          o += 1
      except:
        pass
    return(price) 

  def print_(self):
    for row in self.scheme:
      line = []
      for ch in row:
        if ch == 0:
          line.append('_')
        else:
          line.append(ch)
      print(line,'\n')

  def make_copy(self):
    next_ = Board(self, self.n, self.sign)
    return(next_)
  

# ~ print(1, price([0,0,'X','X',0,0,0,0,0,0,0,'O','O',0,0]))
# ~ print(2, price([0,0,'X','X','X',0,0,0,0,0,0,'O','O',0,0]))
# ~ print(3, price([0,0,'X','X','X','O',0,0,0,0,0,0,0,0,0]))
# ~ print(4, price([0,'X','X','X','O',0,0,0,0,0,0,0,0,0,0]))
# ~ print(5, price([0,0,0,'X','X','X','O',0,0,0,0,0,0,0,0]))
          
