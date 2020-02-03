class Player:
  def __init__(self, player_sign):
    self.sign = player_sign
    self.name="stepanMK2"
    self.pole=[] #seznam: 225 cisel, prazdne 0, X=1, O=-1
    for i in range(15*15):
      self.pole.append(0)
    self.seznam_skupin=[] #seznam: vsechny hodnocene skupiny(sloupec/radek/uhlopricka),[[,index,index,...],[,index,index,...],...]
    self.seznam_hodnot=[] #seznam: vsechny hodnoty skupin
    for y in range(0,15): #radky
      self.seznam_skupin.append([])
      self.seznam_hodnot.append(0)
      for x in range(0,15):
        index=y*15+x
        self.seznam_skupin[-1].append(index)
    for x in range(0,15): #sloupce
      self.seznam_skupin.append([])
      self.seznam_hodnot.append(0)
      for y in range(0,15):
        index=y*15+x
        self.seznam_skupin[-1].append(index)
    for a in range(4,25): #uhlopricky 1
      self.seznam_skupin.append([])
      self.seznam_hodnot.append(0)
      alfa=0
      if a>=15:
        alfa=a-14
      for b in range(alfa,a+1):
        index=a+14*b
        if index>220:
          break
        self.seznam_skupin[-1].append(index)
    for a in range(-10,11): #uhlopricky 2
      self.seznam_skupin.append([])
      self.seznam_hodnot.append(0)
      alfa=0
      beta=15
      if a<=0:
        alfa=-a
      else:
        beta=-a+15
      for b in range(alfa,beta):
        index=a+16*b
        self.seznam_skupin[-1].append(index)
    #seznam skupin je spravne

  def play(self, opponent_move):
    tah=112
    if opponent_move!=None:
      y, x = opponent_move
      index=15*y+x
      self.pole[index]=-self.sign
      self.seznam_hodnot=self.prepocti([index],-self.sign)
      tah=self.vyber_tah(self.sign)
    self.pole[tah]=self.sign
    self.seznam_hodnot=self.prepocti([tah],self.sign)
    return (int(tah/15), tah%15)
  
  def vyber_tah(self, hrac):
    moznosti=self.najdi_tahy([])
    hodnoty=[]
    for moznost in range(len(moznosti)):
      indexy=[moznosti[moznost]]
      hodnota_ted=sum(self.seznam_hodnot)
      hodnota_potom=sum(self.prepocti(indexy,self.sign))
      hodnota_tahu=hodnota_potom-hodnota_ted
      hodnoty.append(hodnota_tahu)
    for i in range(len(moznosti)):
      moznosti[i]=[moznosti[i],hodnoty[i]]
    moznosti.sort(key=lambda x: x[1])
    if self.sign==1:
      moznosti=list(reversed(moznosti))
    for i in range(len(moznosti)): 
      moznosti[i]=moznosti[i][0]  #moznosti serazene podle hodnoty od nejmensi
    delka=int(len(moznosti)/2)
    moznosti=moznosti[0:delka+1]  #vyber pouze lepsich moznosti
    novemoznosti=[]
    for moznost in moznosti:
      for dalsimoznost in self.najdi_tahy([moznost]):
         novemoznosti.append([moznost,dalsimoznost])  #mozny tah algoritmu a dalsi tah protivnika
    
    hodnoty=[]
    for moznost in range(len(novemoznosti)): #1 tah dopredu
      indexy=novemoznosti[moznost]
      hodnota_ted=sum(self.seznam_hodnot)
      hodnota_potom=sum(self.prepocti(indexy,self.sign))
      hodnota_tahu=hodnota_potom-hodnota_ted
      hodnoty.append(hodnota_tahu)
    #ted odstranit pro kazdy tah algoritmu vsechny spatne tahy protivnika
    seznam_nejlepsich=[] #seznam nejlepsiho tahu protivnika s hodnotou pro kazdy tah algoritmu
    for prvnitah in moznosti:
      kandidati=[] #seznam pozic kombinaci tahu se stejnym prvnim tahem
      for indexkandidat in range(len(novemoznosti)):
        if novemoznosti[indexkandidat][0]==prvnitah:
          kandidati.append(indexkandidat)
      nejlepsi=kandidati[0]
      for kandidat in kandidati:
        tatohodnota=hodnoty[kandidat]
        if tatohodnota>hodnoty[nejlepsi]:
          nejlepsi=kandidat
      seznam_nejlepsich.append([novemoznosti[nejlepsi],hodnoty[nejlepsi]]) 
    
    seznam_nejlepsich.sort(key=lambda x: x[1]) 
    tah=seznam_nejlepsich[0][0][0]
    return (tah)
  
  def najdi_tahy(self,indexy): #dostane navic zaplnene indexy, vrati seznam mist sousedicich se hrou
    pole=self.pole.copy()
    for index in indexy:
      pole[index]=1
    seznam=[]
    for index in range(len(pole)):
      if pole[index]==0:
        y=int(index/15)
        x=index%15
        for i in [[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]:
          if i[0]>=0 and i[0]<=14 and i[1]>=0 and i[1]<=14:
            misto=15*i[1]+i[0]
            if pole[misto]!=0:
              seznam.append(index)
              break
    return seznam
        
  def prepocti(self, indexy, sign): #dostane indexy tahu po sobe a kdo zacina, a vrati novy seznam hodnot
    novepole=self.pole.copy()
    novyseznamhodnot=self.seznam_hodnot.copy()
    kdo=sign
    for index in indexy:
        novepole[index]=kdo
        kdo=-kdo
    hodnocene_skupiny=[] #ve kterych skupinach je index
    for index in indexy:
      for i in range(len(self.seznam_skupin)):
        if index in self.seznam_skupin[i]:
          hodnocene_skupiny.append(i)
    for i in hodnocene_skupiny:
      skupina=self.seznam_skupin[i]
      novaskupina=[]
      for index in skupina:
        novaskupina.append(novepole[index])
      novyseznamhodnot[i]=self.hodnota(novaskupina)
    return(novyseznamhodnot)

  def hodnota(self, skupina):  
    hodnota=0
    for i in range(len(skupina)-4):
        skupinka=skupina[i:i+5]
        if (-1 in skupinka)!=(1 in skupinka):
           soucet=sum(skupinka)
           pocet=abs(soucet)
           ktery=soucet/pocet
           hodnota=hodnota+(ktery*(10**pocet))
           if pocet>=5:
              if ktery!=self.sign:
                  hodnota=-self.sign*99999999999999 #prohra
              else:
                  hodnota=self.sign*99999999999 #vyhra
    return hodnota 


