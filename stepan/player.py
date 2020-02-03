import time
class Player:
  def __init__(self, player_sign):
    self.sign = player_sign
    self.name = 'stepan'
    self.pole=[] #seznam: 225 cisel, prazdne 0, algoritmus=1, nepritel=-1
    self.cas=300
    self.budoucnost=4
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
    self.stav=0
    #seznam skupin je spravne

  def play(self, opponent_move):
    zacatek=time.time()
    if self.cas<20:
      self.budoucnost=0
    if opponent_move!=None:
      y, x = opponent_move
      index=15*y+x
      self.pole[index]=-1
      self.seznam_hodnot=self.prepocti([index],-1)
    self.stav=sum(self.seznam_hodnot)
    tah=self.vyber_tah()
    if tah==None:
      return None
    self.pole[tah]=1
    self.seznam_hodnot=self.prepocti([tah],1)
    if "prohra" not in self.seznam_hodnot and "vyhra" not in self.seznam_hodnot:
      self.stav=sum(self.seznam_hodnot)
    konec=time.time()
    cas=konec-zacatek
    if cas>15 and self.budoucnost>0:
      self.budoucnost=self.budoucnost-1
    self.cas=self.cas-cas
    return (int(tah/15), tah%15)
  
  def vyber_tah(self):
    moznosti=self.najdi_tahy([])
    if len(moznosti)==0:
      if 0 in self.pole:
        return (112)
      else:
        return None
    podrobne_moznosti=moznosti.copy()
    hodnoty=[]
    for i in moznosti:
      hodnoty.append(self.hodnota_tahu([i]))
    novehodnoty=hodnoty.copy()
    budoucnost=self.budoucnost
    while len(moznosti)>1:
      print("spoustim "+str(moznosti))
      seznam=(self.pridej_moznosti([],podrobne_moznosti,hodnoty).copy())
      podrobne_moznosti=seznam[0]
      hodnoty=seznam[1]
      novehodnoty=hodnoty.copy()
      while len(novehodnoty)==len(podrobne_moznosti):
        novehodnoty=(self.zkrouhni(novehodnoty,1)).copy()
      indexy=list(reversed(self.serad(novehodnoty))).copy()
      if "vyhra" in novehodnoty:
        moznosti=[moznosti[indexy[0]]]
      else:
        novemoznosti=[]
        novepodrobne_moznosti=[]
        novehodnoty=[]
        konec=budoucnost
        if konec<1:
          konec=1
        for index in indexy[0:konec]:
          novemoznosti.append(moznosti[index])
          novepodrobne_moznosti.append(podrobne_moznosti[index*2])
          novepodrobne_moznosti.append(podrobne_moznosti[index*2+1])
          novehodnoty.append(hodnoty[index*2])
          novehodnoty.append(hodnoty[index*2+1])
        moznosti=novemoznosti.copy()
        podrobne_moznosti=novepodrobne_moznosti.copy()
        hodnoty=novehodnoty.copy()    
        budoucnost=budoucnost-1
    tah=moznosti[0]
    print("tah: "+str(tah))
    return (tah)
  
  def serad(self, seznam): #vrati seznam indexu, kde seznam[index] jde vzestupne
    prohry=[]
    mezi=[]
    vyhry=[]
    for index in range(len(seznam)):
      if seznam[index]=="prohra":
        prohry.append(index)
      elif seznam[index]=="vyhra":
        vyhry.append(index)
      else:
        mezi.append([index,seznam[index]])
    mezi.sort(key=lambda x: x[1])
    for i in range(len(mezi)):
      mezi[i]=mezi[i][0]
    return(prohry+mezi+vyhry)
    
  def pridej_moznosti(self,plne,moznosti,hodnoty):
    novemoznosti=[]
    novehodnoty=[]
    if type(moznosti[-1])!=list:
      for i in range(len(moznosti)):
        novemoznosti.append(moznosti[i])
        novehodnoty.append(hodnoty[i])
        noveplne=plne.copy()
        noveplne.append(moznosti[i])
        novyseznam=(self.najdi_tahy(noveplne))
        novyseznamhodnot=[]
        for i in range(len(novyseznam)):
          novyseznamhodnot.append(self.hodnota_tahu(noveplne+[novyseznam[i]]))
        indexy=self.serad(novyseznamhodnot).copy()  #indexy od prohry k vyhre
        kdo=-1
        if len(noveplne)%2==0:
          kdo=-kdo
        if "prohra" in novyseznamhodnot and kdo==-1:
          novyseznam=[novyseznam[indexy[0]]]
          novyseznamhodnot=[novyseznamhodnot[indexy[0]]]
        elif "vyhra" in novyseznamhodnot and kdo==1:
          novyseznam=[novyseznam[indexy[-1]]]
          novyseznamhodnot=[novyseznamhodnot[indexy[-1]]]
        else:
          if kdo==1:
            indexy=(list(reversed(indexy))).copy() #indexy od vyhry k prohre
          konec=int(len(indexy)/2)
          if konec<1:
            konec=1
          staryseznam=novyseznam.copy()
          staryseznamhodnot=novyseznamhodnot.copy()
          novyseznam=[]
          novyseznamhodnot=[]
          for index in indexy[0:konec]:
            novyseznam.append(staryseznam[index])
            novyseznamhodnot.append(staryseznamhodnot[index])
        novemoznosti.append(novyseznam.copy()) #oriznuto podle hodnot-vyhazena horsi polovina
        novehodnoty.append(novyseznamhodnot.copy()) #oriznuto podle hodnot-vyhazena horsi polovina
    else:
      for i in range(len(moznosti)):
        if type(moznosti[i])==list:
          novemoznosti.append(moznosti[i-1])
          novehodnoty.append(hodnoty[i-1])
          noveplne=plne.copy()
          noveplne.append(moznosti[i-1])
          novyvysledek=self.pridej_moznosti(noveplne,moznosti[i],hodnoty[i])
          novemoznosti.append(novyvysledek[0])
          novehodnoty.append(novyvysledek[1])
    return ([novemoznosti,novehodnoty])
  
  def zkrouhni(self,hodnoty,kdo): 
    novehodnoty=[] 
    if type(hodnoty[-1][-1])!=list:
      for i in range(0,len(hodnoty),2):
        if hodnoty[i]=="prohra" or hodnoty[i]=="vyhra": 
          novahodnota=hodnoty[i]
        else:
          indexy=self.serad(hodnoty[i+1]).copy()
          if kdo==1:
            novahodnota=hodnoty[i+1][indexy[0]]
          else:
            novahodnota=hodnoty[i+1][indexy[-1]]
        novehodnoty.append(novahodnota)
    else: #rekurze
      for i in range(len(hodnoty)):
        if type(hodnoty[i])!=list:
          novehodnoty.append(hodnoty[i])
        else:
          novehodnoty.append(self.zkrouhni(hodnoty[i],-kdo))
    return(novehodnoty)
            
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
      
  def hodnota_tahu(self,indexy):    #dostane indexy tahu po sobe, vrati soucet nebo prohra/vyhra
    seznam_hodnot=self.prepocti(indexy,1)
    if "prohra" in seznam_hodnot:
      return "prohra"
    if "vyhra" in seznam_hodnot:
      return "vyhra"
    else:
      return (sum(seznam_hodnot)-self.stav)
    
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
      skupina=self.seznam_skupin[i].copy()
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
              if ktery==-1:
                return "prohra" 
              else:
                return "vyhra" 
    return hodnota 


