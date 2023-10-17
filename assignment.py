#! python3
import random
import math
class game:
  win=0
  loss=0
  tie=0
  gameN=0

  winblack=0
  lossblack=0
  tieblack=0

  def gameSauto(self, numberOfGame):
    rockps=["rock","paper","scissors"]
    for i in range(numberOfGame):
      p=random.choice(rockps)
      self.gameN1(p)
    self.finish()

  def gameNauto(self, nOg):
    for i in range(nOg):
      a=str(input("rock or paper or scissors? : "))
      self.gameN1(a)
      print()
    self.finish()

  def gameN1(self,rps):
    self.gameN+=1
    rps1=[1,2,3]
    a=random.choice(rps1)
    if rps=="rock":
      if a==1:
        self.tie+=1
        print("\ntie")
      elif a==2:
        self.loss+=1
        print("\nloss")
      else:
        self.win+=1
        print("\nwin")
    elif rps=="paper":
      if a==1:
        self.win+=1
        print("\nwin")
      elif a==2:
        self.tie+=1
        print("\ntie")
      else:
        self.loss+=1
        print("\nloss")
    else:
      if a==3:
        self.tie+=1
        print("\ntie")
      elif a==1:
        self.loss+=1
        print("\nloss")
      else:
        self.win+=1
        print("\nwin")
    print(f"#{self.gameN} - win : {self.win} | loss : {self.loss} | tie : {self.tie}\n")    
    #return self.win, self.loss, self.tie, self.gameN

  def resetS(self):
    k=str(input("Do you want to reset the game? (yes or no): "))
    if k=="yes":
      self.win=0
      self.loss=0
      self.tie=0
      self.gameN=0
      print("game reseted")
      print()
      l=str(input("Playing game again? yes or no or change: "))
      print()
      if l=="yes":
        c=str(input("Do you want to play game with auto? yes or no: "))
        b=int(input("How many times do you want to play the game?: "))
        print()
        if c=="yes":
          self.gameSauto(b)
        elif c=="no":
          self.gameNauto(b)
      elif l=="change":
        self.blackj()
      else:
        exit()
    else:
      a=str(input("continue game yes or no or change: "))
      print()
      if a=="yes":
        c=str(input("Do you want to play game with auto? yes or no: "))
        b=int(input("How many times do you want to play the game?: "))
        print()
        if c=="yes":
          self.gameSauto(b)
        elif c=="no":
          self.gameNauto(b)

      elif a=="change":
        self.blackj()
      else:
        exit()
      
  def finish(self):
    print(f"win:{self.win}\nloss:{self.loss}\ntie:{self.tie}\n#ofGame:{self.gameN}")
    print()
    self.resetS()

  def pickC(self):
    card=[1,2,3,4,5,6,7,8,9,10,10,10,11]
    a=random.choice(card)
    return a

  def blackjA(self):
    card=[1,2,3,4,5,6,7,8,9,10,10,10,11]
    a=random.choice(card)
    b=random.choice(card)
    total=a+b
    cardk=[]
    cardk.append(a)
    cardk.append(b)

    if 18<total<25:  #19 20 21 22 23 24
      return total
    else:  # 18 17 16.... 25 26 27 28....
      if total<19:  #18 17 16.....
        while 19>total:
          o=self.pickC()
          cardk.append(o)
          total=total+o
          if total==21:
            return 21
          elif 18<total<25:
            return total
          elif total>24: # 25 26 27...
            if 11 in cardk: #cardk.contains(11):
              total=total-10
              c=self.pickC()
              cardk.append(c)
            else:
              return total
      else:
        while total>24:
          if 11 in cardk:
              total=total-10
              c=self.pickC()
              cardk.append(c)
          else:
            return total
        return total



    
  def blackj(self):
    card=["A",2,3,4,5,6,7,8,9,"J","Q","K"]
    str(input("Enter 'pick' to chose the card: "))
    
    for i in range(2):
      card1=random.choice(card)
      card2=random.choice(card)
    
    print(f"your cards: {card1},{card2}")
  
    cardp=[]
    cardp.append(card1)
    cardp.append(card2)

    print()
    
    a=str(input("Do you want to pick more card? yes or no: "))

    while a=="yes":
      card3=random.choice(card)
      cardp.append(card3)
      print(f"your cards: {cardp}")
      a=str(input("Do you want to pick more card? yes or no: "))

    total=0
  
    for i in range(len(cardp)):
      if cardp[i]=="A":
        k=int(input("A= 1? or 11? :" ))
        total+=k
      elif cardp[i]=="J" or cardp[i]=="Q" or cardp[i]=="K":
        total+=10
      elif cardp[i]!="A" and cardp[i]!="J" and cardp[i]!="Q" and cardp[i]!="K":
        total=cardp[i]+total

    p=self.blackjA()
    if abs(21-p) < abs(21-total):
      print(f"\nyour card total : {total}, other player card total : {p}")
      print("\nYou loss")
      self.lossblack+=1
    elif abs(21-p) > abs(21-total):
      print(f"\nyour card total : {total}, other player card total : {p}")
      print("\nYou win")
      self.winblack+=1
    else:
      print(f"\nyour card total : {total}, other player card total : {p}")
      print("\ntie")
      self.tieblack+=1
    print("\nblack jack game - your score is not resetted until you exit the game! \n")
    print(f"win:{self.winblack}\nloss:{self.lossblack}\ntie:{self.tieblack}\n")
    l=str(input("Do you want to play game again? yes or no or change game: "))
    print()
    if l=="yes":
      self.blackj()
    elif l=="no":
      exit()
    else:
      o=str(input("playing rock paper scissors with auto? yes or no?: "))
      if o=="yes":
        u=int(input("How many times do you want to play rock paper scissors game?: "))
        self.gameSauto(u)
      elif o=="no":
        u=int(input("How many times do you want to play rock paper scissors game?: "))
        self.gameNauto(u)







    """cardOp=[]
    cardOp.append(cardO1)
    cardOp.append(cardO2)
    cardOt=0
    numberOfA=0

    
        
    while True:
      for i in cardOp:
        if cardOp[i]!="A" or cardOp[i]!="J" or cardOp[i]!="Q" or cardOp[i]!="K":
          cardOt+=cardOp[i]
        if cardOp[i]=="A":"""
      

  def __init__(self):
    k=int(input("Game Options\n1.rock paper scissors\n2.blackjack\n: "))
    if k==1:
      print("\n-------------------")
      print("ROCK PAPER SCISSORS")
      print("-------------------\n")
      a=str(input("Do you want to start the game with auto? yes or no: "))
      b=int(input("How many times do you want to play rock paper scissors game?: "))
      print()
      if a=="yes":
        self.gameSauto(b)
      else:
        self.gameNauto(b)
    else:
      print("\n----------")
      print("BLACK JACK")
      print("----------\n")
      self.blackj()


# This is the only command allowed that is not in the class template. All code must be done there.
g = game()




