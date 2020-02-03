from random import randint
import tkinter
import numpy as np
import time
class Player:
    def __init__(self, player_sign):
        self.sign = player_sign
        self.name = 'bakabot'
        self.grid = np.zeros((15,15),int)
        self.firstplay = 'True'
    
    def ErCheck(self,row,col):
        if row<0 or col <0:
            row,col = 15,15
       # print(row,col)
        try:
            a =self.grid[row, col] 
            #print(a)
        except:
            a = 2
            #print(f'a = {a}')
        return (a)
        
    def HorCheckO (self,x,who,f):
        
        x2= x*who 
        scoreH =0
        countH=0
        count2H=0
        row=0
        col=0
        for i in range (15):
            rowCount = i
            for i in self.grid[i,:]:
                countH +=1
                if countH > 15:
                    countH = 0
                    countH +=1
                if countH <= 15:
                    row = rowCount
                    col= countH-1
                if i == who:
                    count2H += who
                elif i == -who:
                    count2H = 0
                elif i == 0:
                    count2H = 0
                if count2H ==x2 and f!=999 :
                    
                    if self.ErCheck (row,col+1) == 0 :
                        if self.ErCheck (row, col+3) == 0 and self.ErCheck (row, col+2)==0  and who == self.sign and self.ErCheck(row, col-x) != -self.sign and x == 2   :
                            return(row, col+2) 
                        return(row, col+1)
                    elif self.ErCheck(row, col-x) == 0 and (self.ErCheck(row, col+1) == who or self.ErCheck (row, col+1) == 2) :                        
                        return (row, col-x) 
                elif count2H ==x2 and  f==999:
                    if self.ErCheck (row, col+2) == -self.sign and self.ErCheck (row, col+1)==0  and self.ErCheck(row, col-x) != self.sign   :
                        return(row, col+1) 
                
        return (99,98)
        
    def VerCheckO (self,x,who,f):

        x2= x*who
        scoreV = 0
        countV=0
        count2V=0
        row=0
        col=0
        for i in range (15):
            rowCount = i       
            for i in self.grid[:,i]:
                countV +=1
                if countV > 15:
                    countV = 0
                    countV +=1
                if countV <= 15:
                    col = rowCount
                    row= countV-1
                if i == who:
                    count2V += who
                elif i == -who:
                    count2V = 0
                elif i == 0:
                    count2V = 0
                if count2V == x2 and f!=999:
                    if self.ErCheck (row+1,col) == 0:
                        if self.ErCheck (row+3, col) == 0 and self.ErCheck (row+2, col)==0  and who == self.sign and self.ErCheck(row-x, col) != -self.sign and x == 2   :
                            return(row+2, col)  
                        #print(f'ahoj{row-x}' )
                        return(row+1, col)
                    elif self.ErCheck(row-x, col) == 0 and (self.ErCheck (row+1, col) == who or self.ErCheck (row+1, col) == 2) :
                        #print(f'ahoj2{row-x}' )
                        return (row-x, col) 
                elif count2V == x2 and f==999:
                    if self.ErCheck (row+2, col) == -self.sign and self.ErCheck (row+1, col)==0  and self.ErCheck(row-x, col) != self.sign   :
                        return(row+1, col) 
        return (99,98)
           
    def DiagCheckO (self,x,who,f):
        x2= x*who
        scoreV = 0
        countV=0
        count2V=0
        col= -1
        row=0
        for i in range (15):
            row=-1
            col +=1
            col3 = col-1
            f= i-1
            d=self.grid.diagonal(f+1)
  #           print (d)
            for i in d:
                row +=1
                col3 +=1
 #               print (row)
  #              print(col3)
                if i == who:
                    count2V += who
                elif i == -who:
                    count2V = 0
                elif i == 0:
                    count2V = 0
                if count2V == x2 and f!=999:
                    if self.ErCheck (row+1, col3+1) == 0:
                        if self.ErCheck (row+3, col3+3) == 0 and self.ErCheck (row+2, col3+2)==0  and who == self.sign and self.ErCheck(row-x, col3-x) != -self.sign and x == 2   :
                            return(row+2, col3+2)  
                        return(row+1, col3+1)
                    elif self.ErCheck (row-x, col3-x) == 0 and (self.ErCheck (row+1,col3+1) == -who or self.ErCheck (row+1, col3+1) == 2) :
                        return (row-x, col3-x)   
                elif count2V == x2 and f==999:
                    return (98,98)
        return (98,98)
  
    def DiagCheckF (self,x,who,f):
        x2= x*who
        scoreV = 0
        countV=0
        count2V=0
        row= -1
        col=0
        for i in range (15):
            col=-1
            row +=1
            row3 = row-1
           
            d=self.grid.diagonal(-i)
          #  print (d)
            for i in d:
                row3 +=1
                col +=1
            #    print (row3)
          #      print(col)                
                if i == who:
                    count2V += who
                elif i == -who:
                    count2V = 0
                elif i == 0:
                    count2V = 0
                if count2V == x2  and f!=999:
                    if self.ErCheck (row3+1, col+1) == 0:
                        if self.ErCheck (row3+3, col+3) == 0 and self.ErCheck (row3+2, col+2)==0  and who == self.sign and self.ErCheck(row3-x, col-x) != -self.sign and x == 2   :
                            return(row3+2, col+2)
                        return(row3+1, col+1)
                    elif self.ErCheck(row3-x, col-x)  == 0 and (self.ErCheck (row3+1, col+1) == -who or self.ErCheck (row3+1, col+1)==2) :
                        return (row3-x, col-x)   
                elif count2V == x2 and f==999:
                    return (98,98)                                          
        return (98,98)    
   
    def DiagFlip (self,x,who,f):
        x2= x*who
        scoreV = 0
        countV=0
        count2V=0
        col= 16
        row=0
        for i in range (15):
            row=-1
            col -=1
            col3 = col
            
            d= np.fliplr(self.grid).diagonal(i)
            
            #print (d)
            for i in d:
                row +=1
                col3 -=1
            #print (row)
     #           print(col3)
                if i == who:
                    count2V += who
                elif i == -who:
                    count2V = 0
                elif i == 0:
                    count2V = 0
                if count2V == x2  and f!=999:
                    if self.ErCheck (row+1, col3-1) == 0:
                        if self.ErCheck (row+3, col3-3) == 0 and self.ErCheck (row+2, col3-2)==0  and who == self.sign and self.ErCheck(row-x, col3+x) != -self.sign and x == 2   :
                            return(row+2, col3-2) 
                        return(row+1, col3-1)
                    elif self.ErCheck(row-x, col3+x) == 0 and (self.ErCheck (row+1, col3-1) == -who  or self.ErCheck (row+1, col3-1)==2) :
                        return (row-x, col3+x) 
                elif count2V == x2 and f==999:
                    return (98,98)
        return (98,98)
    
    def DiagFlipO (self,x,who,f):
        x2= x*who
        scoreV = 0
        countV=0
        count2V=0
        col= 15
        row=-2
        for i in range (15):
            row +=1
            row3 = row
            col =15
            
            d= np.fliplr(self.grid).diagonal(-i)
            
            #print (d)
            for i in d:
                row3 +=1
                col -=1
           #     print (row3)
          #      print(col)
                if i == who:
                    count2V += who
                elif i == -who:
                    count2V = 0
                elif i == 0:
                    count2V = 0
                if count2V == x2  and f!=999:
                    if self.ErCheck (row3+1, col-1) == 0:
                        if self.ErCheck (row3+3, col-3) == 0 and self.ErCheck (row3+2, col-2)==0  and who == self.sign and self.ErCheck(row3-x, col+x) != -self.sign and x == 2   :
                            return(row3+2, col-2)
                        return(row3+1, col-1)
                    elif self.ErCheck(row3-x, col+x)  == 0 and (self.ErCheck (row3+1, col-1) == -who or self.ErCheck (row3+1, col-1) == 2) :
                        return (row3-x, col+x)
                elif count2V == x2 and f==999:
                    return (98,98)
        return (98,98)
        
    def Attack(self,num,f):
        who = self.sign
        f=0

        row,col = self.HorCheckO(num,who,f)
        if col ==98:
            row,col = self.VerCheckO(num,who,f)
            if col ==98:
                row,col = self.DiagCheckF(num,who,f)
                if col ==98:
                    row,col = self.DiagCheckO(num,who,f)
                    if col ==98:
                        row,col = self.DiagFlip(num,who,f)  
                        if col ==98:
                            row,col = self.DiagFlipO(num,who,f)                                            
        return (row,col)
        
    def Defend(self,num,f):
        who = -self.sign
        if f==1:
            f=999
            row,col = self.HorCheckO(num,who,f)
            if col ==98:
                row,col = self.VerCheckO(num,who,f)
            return(row,col)


        row,col = self.HorCheckO(num,who,f)
        if col ==98:
            row,col = self.VerCheckO(num,who,f)
            if col ==98:
                row,col = self.DiagCheckF(num,who,f)
                if col ==98:
                    row,col = self.DiagCheckO(num,who,f)
                    if col ==98:
                        row,col = self.DiagFlip(num,who,f)
                        if col ==98:
                            row,col = self.DiagFlipO(num,who,f)  
        return (row,col)
             
    def Crash(self,opponent_move): 
                      
        if opponent_move == None and self.firstplay == 'True':
            row,col = randint(0,14),randint(0,14)
            self.grid[row, col] = self.sign
            print(self.grid)
            self.firstplay = 'False'
            return(row,col)
        if opponent_move != None and self.firstplay != 'True':
            row, col = opponent_move
            self.grid[row, col] = -self.sign
            
        elif  opponent_move != None and self.firstplay == 'True':

            row, col = opponent_move
            self.grid[row, col] = -self.sign
            self.firstplay = 'False'
        return (98,98)      
        
    def play(self, opponent_move):
        time.sleep (0.1)
        
        #first play or crash
        row1, colI = self.Crash(opponent_move)
        if colI !=98:
            return (row1, colI)
          
        
        row1, colI = self.Attack(4,0)
        #print(self.grid)        
        if colI ==98:
            row1, colI = self.Defend(4,0)
            if colI ==98:
                row1, colI = self.Attack(3,0)
                if colI ==98:
                    row1, colI = self.Defend(2,1)
                    if colI ==98:
                        row1, colI = self.Defend(3,0)
                        if colI ==98:
                            row1, colI = self.Attack(2,0)
                            if colI ==98:
                                row1, colI = self.Attack(1,0)
                            
        
                            
        
        # if there's no space
        if colI ==98:    
            row1, colI = opponent_move
            while True:
                if self.ErCheck(row1+1,colI) != 0 and self.ErCheck(row1+1,colI)!= 2 :
                    row1 += 1            
                elif self.ErCheck(row1+1,colI) == 2:
                    while True:
                        if self.ErCheck(row1-1,colI) != 0:
                            row1 -=1       
                        else:
                            row1 -=1
                            break
                    break
                else:
                    row1 += 1
                    break
        self.grid[row1, colI] = self.sign
        print(self.grid)
        return (row1, colI)
