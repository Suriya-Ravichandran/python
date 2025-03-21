box=[]

print("-----Adding Stack Values------")
for x in range(1,6):
    box.append(F"BOOK {x}")
    print(box)

print("----------Removing Stack Values-------")
for x in range(len(box)):
    box.pop()
    print(box)
