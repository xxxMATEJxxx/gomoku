import random as rd
import numpy as np

table = np.zeros((15,15))
five_lines=[]
four_lines=[]
three_lines=[]
two_lines=[]
one_lines=[]
list_cat=[one_lines,two_lines,three_lines,four_lines,five_lines] 
loc=[[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]

def oukejability(*args):
    for i in args:
        if i[0]>14 or i[0]<0 or i[1]>14 or i[1]<0:
            return False
    return True

def check_surroundings(c1,c2,p,loc):
    s_coor = []
    for a,b in loc:
        if c1+a<15 and c2+b<15:
            if table[c1+a, c2+b] == p: 
                s_coor.append(np.array([c1+a, c2+b]))
    s_coor.append([c1,c2])
    return s_coor
    
def find_line(cor,lvl,p):
    start=cor
    end=cor
    l1=[-1,-2,-3,-4]
    l2=[1,2,3,4]
    lg=1

    for i in l1:
        if (cor[0]+lvl[0]*i<15 and cor[0]+lvl[0]*i>=0) and (cor[1]+lvl[1]*i<15 and cor[1]+lvl[1]*i>=0):
            a,b=lvl
            x = (cor[0]+lvl[0]*i)
            l=cor[1]
            k=lvl[1]
            y = (cor[1]+lvl[1]*i)
            x=int(x)
            y=int(y)
            if table[x,y]==p:
                lg+=1
                end=np.array([x,y])
            else:
                break
    
    for i in l2:
        if (cor[0]+lvl[0]*i<15 and cor[0]+lvl[0]*i>=0) and (cor[1]+lvl[1]*i<15 and cor[1]+lvl[1]*i>=0):
            x = int(cor[0]+lvl[0]*i)
            y = int(cor[1]+lvl[1]*i)
            if table[x,y]==p:
                lg+=1
                start=np.array([x,y])
            else:
               break
    if start[0] - end[0] > 0 or (start[0]==end[0] and start[1]-1==end[1]):
        start, end = end, start
    categorize_line(line(start,end,lvl,lg,p))

class line:
    def __init__(self,start,end,step,length,player):
        self.start = start
        self.end = end
        self.step = np.array(step)
        self.player=player
        self.x_s,self.y_s=self.start
        self.x_e,self.y_e=self.end
        self.coos=[]
        self.length = length
        self.attributes=[self.start,self.end,self.step,self.player]
        self.check_step()
        self.find_constep()
        self.update_yourself()
    
    def check_step(self):
        if oukejability(np.array(self.end)+self.step):
            if table[(self.end[0]+self.step[0]),(self.end[1]+self.step[1])]==self.player:
                self.step[0],self.step[1]=-self.step[0],-self.step[1]
        
    def update_yourself(self):
        self.after_end_c=(self.end+self.step)
        if oukejability(self.after_end_c):
            self.after_end=table[self.end[0]+self.step[0],self.end[1]+self.step[1]]
        else:
            self.after_end=None
        self.before_start_c=self.start-self.step
        if oukejability(self.before_start_c):
            self.before_start=table[self.start[0]-self.step[0],self.start[1]-self.step[1]]
        else:
            self.before_start=None      
        if (self.step)[0]==0:
            self.length=(np.array(self.end)-np.array(self.start))[1]/self.step[1]
        else:
            self.length=(np.array(self.end)-np.array(self.start))[0]/self.step[0]
        self.length=self.length.astype(int)
        self.length=abs(self.length)
        self.length+=1
        self.check_step()
    
    def check(self):    
        for i in range(self.length):
            if table[(self.start+self.step*i-self.step)[0],(self.start+self.step*i-self.step)[1]]!=self.player:
                return False
            return True

    def find_constep(self):
        i,j = self.step
        self.new_step=np.array([j,-i])
              
def update(lines_list):
    for i in lines_list:
        i.update_yourself()
        
def categorize_line(line_obj):
    for i in list_cat:
        update(i)
        for k in i:
            if not k.check:
                del k
    if line_obj.after_end == -line_obj.player and line_obj.before_start == -line_obj.player:
        del line_obj
        return
    for i in list_cat[line_obj.length-1]:
        if i.start[0]==line_obj.start[0] and i.start[1]==line_obj.start[1] and i.end[0]==line_obj.end[0] and i.end[1]==line_obj.end[1] and (i.step==line_obj.step).all() and i.player==line_obj.player:
            del line_obj
            return
    list_cat[line_obj.length-1].append(line_obj)
    
def find_play_list(list_cat):
    list_cat=[one_lines,two_lines,three_lines,four_lines]
    play_list=[]
    new_play_list=[]
    ind=0
    for i in list_cat:
        update(i)
        for k in i:
            if not k.check:
                del k
        for x in i:
            if x.length!=list_cat.index(i)+1:
                categorize_line(x)
    for i,value in enumerate(list_cat):
        for k in value:
            if is_space_left(k.start,k.end,k.step,k.length,k.player):
                if k.player==1:    ind=1
                if k.after_end==0:
                    for z in range((i*4+1)):
                        play_list.append(k.after_end_c)
                if k.before_start==0:
                    for z in range((i*4+1)):
                        play_list.append(k.before_start_c)
                if k.length==4 and k.before_start==0:
                    for x in range(40+20*ind):
                        play_list.append(k.before_start_c)
                if k.length==4 and k.after_end==0:
                    for x in range(40+20*ind):
                        play_list.append(k.after_end_c)
                if k.length==3 and oukejability(k.before_start_c-k.step,k.after_end_c+k.step):
                    if k.before_start==0 and k.after_end==0: 
                        for z in range(15):
                            play_list.append(k.before_start_c)
                            play_list.append(k.after_end_c)
                    if (k.before_start==0 and table[(k.before_start_c-k.step)[0],(k.before_start_c-k.step)[1]]==k.player):
                        for z in range(20):
                            play_list.append(k.before_start_c)
                    if (k.after_end==0 and table[(k.after_end_c+k.step)[0],(k.after_end_c+k.step)[1]]==k.player):
                        for z in range(20):
                            play_list.append(k.after_end_c)
                if oukejability(k.before_start_c-k.step,k.after_end_c+k.step):
                    if k.before_start==0 and table[(k.before_start_c-k.step)[0],(k.before_start_c-k.step)[1]]==k.player:
                        for z in range(((k.length+check_line_length(k.before_start_c-k.step,k.step,k.player))*4+1)//2):
                            play_list.append(k.before_start_c)
                    if (k.after_end==0 and table[(k.after_end_c+k.step)[0],(k.after_end_c+k.step)[1]]==k.player):
                        for z in range(((k.length+check_line_length(k.after_end_c+k.step,k.step,k.player))*4+1)//2):
                            play_list.append(k.after_end_c)
                ind=0
    for i in play_list:
        if oukejability(i):
            if table[i[0],i[1]]==0:
                new_play_list.append(i)
    return(find_the_frequentest(new_play_list))

def is_space_left(start,end,step,length,player):
    l=5-length
    cor_S=start-step
    cor_E=end+step
    if oukejability(cor_S):
        while l>0 and oukejability(cor_S) and table[cor_S[0],cor_S[1]]!=-player:
            l-=1
            cor_S-=step
    if oukejability(cor_E):
        while l>0 and oukejability(cor_E) and table[cor_E[0],cor_E[1]]!=-player:
            l-=1
            cor_E+=step
    if l<=0:
        return True
    return False

def check_line_length(coor,step,player):
    length=0
    while oukejability(coor) and table[coor[0],coor[1]]==player:
        length+=1
        coor=coor+step
    return length
        
def find_the_frequentest(play_list):
    dict_a={}
    dict_c={}
    for i,value in enumerate(play_list):
        if not dict_a:
            dict_a[i]=value
            dict_c[i]=1
        else:
            key_list=list(dict_a.keys())
            position=positioning(dict_a,dict_c,value,key_list)
            if position!=-1:
                number = key_list[position]
                dict_c[number]=dict_c[number]+1
            else:
                dict_a[i]=value
                dict_c[i]=1
    number = max(dict_c, key=dict_c.get)
    return dict_a[number]

def positioning(dict_a,dict_c,value,key_list):
    position=-1
    value_list=list(dict_a.values())
    for i, what in enumerate(value_list):
        if what[0]==value[0] and what[1]==value[1]:
            position=i
            break
    return position

def start(cor,p,loc):
    sur_list=check_surroundings(cor[0],cor[1],p,loc)
    lll=np.array([[0,1],[1,1],[1,0],[1,-1]])
    if len(sur_list)==1:
        for kk in lll:
            find_line(cor,kk,p)
    else:
        sur_list.pop()
        for i in sur_list:
            lvl = np.array(cor)-np.array(i)
            for vz in lll:
                if np.all(np.in1d((np.array(i)-np.array(cor)),vz)):
                    lvl = np.array(i)-np.array(cor)
            find_line(cor,lvl.tolist(),p)
            
def working(row,col):
    table[row,col]=-1
    start([row,col],-1,loc)
    my_cor=find_play_list(list_cat)
    i,j=my_cor
    table[i,j]=1
    start(my_cor,1,loc)
    return my_cor

class Player:
    def __init__(self, player_sign):
        self.sign = player_sign
        self.name = 'Kilbot'
    def play(self, opponent_move):
        if opponent_move == None:
            my_cor=find_play_list(list_cat)
            i,j=my_cor
            table[i,j]=1
            start(my_cor,1,loc)
            return (i,j)
        row, col = opponent_move
        i,j = working(row,col)
        return (i,j)
