class Player:
  def __init__(self, player_sign):
    self.name="stepanMK1"
    self.sign = player_sign
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
      
    self.celkovy_stav=0

  def play(self, opponent_move):
    tah=112
    if opponent_move!=None:
      y, x = opponent_move
      index=15*y+x
      self.pole[index]=-(self.sign)
      self.prepocti(index)
      tah=self.vyber_tah(self.sign)
      self.pole[tah]=self.sign
      self.prepocti(tah)
    return (int(tah/15), tah%15)
  
  def vyber_tah(self, hrac):
    stare_pole=self.pole.copy()
    stary_seznam_hodnot=self.seznam_hodnot.copy()
    stary_celkovy_stav=self.celkovy_stav
    moznosti=self.najdi_tahy()
    hodnoty=[]
    for moznost in range(len(moznosti)):
      index=moznosti[moznost]
      self.pole[index]=hrac
      self.prepocti(index)
      hodnoty.append(self.celkovy_stav)
      self.pole=stare_pole.copy()
      self.seznam_hodnot=stary_seznam_hodnot.copy()
      self.celkovy_stav=stary_celkovy_stav
    nejlepsi=0
    for i in range(len(hodnoty)):
      if hrac<0:
        if hodnoty[i]<hodnoty[nejlepsi]:
            nejlepsi=i
      elif hodnoty[i]>hodnoty[nejlepsi]:
        nejlepsi=i 
    return (moznosti[nejlepsi])
  
  def najdi_tahy(self): #vrati seznam mist sousedicich se hrou
    seznam=[]
    for index in range(len(self.pole)):
      if self.pole[index]==0:
        for i in [index-16,index-15,index-14,index-1,index+1,index+14,index+15,index+16]:
          if i>=0 and i<=224:
            if self.pole[i]!=0:
              seznam.append(index)
              break
    return seznam
        
  
  def prepocti(self,index): #prepocte celkovy stav kdyz se zmeni cislo pod indexem
    seznam=[]
    for i in range(len(self.seznam_skupin)):
      if index in self.seznam_skupin[i]:
        seznam.append(i)
    #seznam indexu skupin je spravne
    for i in seznam:
        self.celkovy_stav=self.celkovy_stav-self.seznam_hodnot[i]
        skupina=self.seznam_skupin[i]
        novaskupina=[]
        for index in skupina:
            novaskupina.append(self.pole[index])
        self.seznam_hodnot[i]=self.hodnota(novaskupina)
        self.celkovy_stav=self.celkovy_stav+self.seznam_hodnot[i]

  def hodnota(self, skupina):
    hodnota=0
    for i in range(len(skupina)-4):
        skupinka=skupina[i:i+5]
        if (-1 in skupinka)!=(1 in skupinka):
           soucet=sum(skupinka)
           pocet=abs(soucet)
           ktery=soucet/pocet
           if self.sign!=ktery:
              pocet=pocet+0.5
           hodnota=hodnota+(ktery*(10**pocet))
           if pocet>=5:
              if ktery!=self.sign:
                  hodnota=-self.sign*9999999999999 #prohra
              else:
                  hodnota=self.sign*999999999 #vyhra
    return hodnota 

