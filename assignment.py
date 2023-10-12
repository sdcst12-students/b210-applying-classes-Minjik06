#! python3
import random
class game:
  win=0
  loss=0
  tie=0
  gameN=0


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
    self.finish()

  def gameN1(self,rps):
    self.gameN+=1
    rps1=[1,2,3]
    a=random.choice(rps1)
    if rps=="rock":
      if a==1:
        self.tie+=1
      elif a==2:
        self.loss+=1
      else:
        self.win+=1
    elif rps=="paper":
      if a==1:
        self.win+=1
      elif a==2:
        self.tie+=1
      else:
        self.loss+=1
    else:
      if a==3:
        self.tie+=1
      elif a==1:
        self.loss+=1
      else:
        self.win+=1
    print(f"win : {self.win} loss : {self.loss} tie : {self.tie}, # of Game : {self.gameN}")    
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
      l=str(input("Playing game again? yes or no: "))
      if l=="yes":
        b=int(input("How many times do you want to play the game?: "))
        c=str(input("Do you want to play game with auto? yes or no: "))
        if c=="yes":
          self.gameSauto(b)
        elif c=="no":
          self.gameNauto(b)
      else:
        exit()
    else:
      a=str(input("continue game yes or no: "))
      if a=="yes":
        b=int(input("How many times do you want to play the game?: "))
        c=str(input("Do you want to play game with auto? yes or no: "))
        if c=="yes":
          self.gameSauto(b)
        elif c=="no":
          self.gameNauto(b)
      else:
        exit()
      

  def finish(self):
    print()
    print(f"win:{self.win}\nloss:{self.loss}\ntie:{self.tie}\n#ofGame:{self.gameN}")
    print()
    self.resetS()

  def __init__(self):
    pass


# This is the only command allowed that is not in the class template. All code must be done there.
g = game()
g.gameSauto(15)

"""g.gameN1("rock")
g.gameN1("Scissors")
g.gameN1("Scissors")
g.resetS()
g.gameN1("rock")
g.gameN1("Scissors")
g.gameN1("Scissors")
g.gameN1("Scissors")"""


