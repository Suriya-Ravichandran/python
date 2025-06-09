import random
shop=[]

for x in range(5):
    shop.append(f"Person {x+1}")
print(shop)

high=random.randint(0,len(shop)-1)
hattack=shop.pop(high)
print(hattack)
