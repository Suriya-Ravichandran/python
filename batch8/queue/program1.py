shop=[]

for x in range(1,4):
    shop.append(f"Person {x}")
    print(shop)


for x in shop:
    del shop[0]
    print(shop)
    
