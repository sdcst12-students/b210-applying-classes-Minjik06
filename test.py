import random

card=["A",2,3,4,5,6,7,8,9,"J","Q","K"]
    
for i in range(2):
    card1=random.choice(card)
    card2=random.choice(card)
    
print(f"your cards: {card1},{card2}")
  
cardp=[]
cardp.append(card1)
cardp.append(card2)

for j in range(len(cardp)):
    print(j)
    print(cardp[j])

for j in cardp:
    print(j)
    print(cardp[j])