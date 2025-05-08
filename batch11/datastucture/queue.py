shop=[]

for x in range(5):
    shop.append(f"Person {x+1}")

print(shop)

for x in range(len(shop)):
    del shop[0]
    print(shop)

