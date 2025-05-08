box=[]

for x in range(3):
    box.append(f"Book {x+1}")

print(box)

for x in range(len(box)):
    box.pop()
    print(box)
