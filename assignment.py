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
    print(self.win, self.loss, self.tie, self.gameN)    
    #return self.win, self.loss, self.tie, self.gameN


  def resetS(self):
    print(f"You played {self.gameN} games")
    k=str(input("Are you sure resetting the game? (yes or no)"))
    if k=="yes":
      self.win=0
      self.loss=0
      self.tie=0
      self.gameN=0
    print("game reseted")

  def finish(self):
    print(f"win:{self.win}\n loss:{self.loss}\n tie:{self.tie}\n #ofGame:{self.gameN}")
    

  def __init__(self):
    pass


# This is the only command allowed that is not in the class template. All code must be done there.
g = game()
g.gameSauto(10)

"""g.gameN1("rock")
g.gameN1("Scissors")
g.gameN1("Scissors")
g.resetS()
g.gameN1("rock")
g.gameN1("Scissors")
g.gameN1("Scissors")
g.gameN1("Scissors")"""


