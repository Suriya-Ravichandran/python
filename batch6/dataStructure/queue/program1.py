shop=[]

print("Queue creating")
for x in range(1,6):
    shop.append(f"person{x}")
    print(shop)

print("Queue Removing")

for x in range(len(shop)):
    del shop[0]
    print(shop)