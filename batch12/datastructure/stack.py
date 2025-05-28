box=[]

for x in range(4):
    box.append(f"{x+1} Book")
print("________Add books in a box_______")
print(box)
print("____________________________________")

print("________Remove books in a box_______")
for x in range(len(box)):
    box.pop()
    print(box)

