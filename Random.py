import random
cards =['A','K','Q','J','2','3','4','5','6','7','8','9','10']
signs =['Heart','CLUB','DIAMOND','SPADE']
random_number = random.choice(cards)
random_sign = random.choice(signs)
random_card = random_number,random_sign
print(random_card)