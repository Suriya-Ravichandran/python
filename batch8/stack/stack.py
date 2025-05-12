box=[]

for x in range(1,4):
    box.append(f"Book {x}")
    print(box)


for x in box:
    box.pop()
    print(box)
