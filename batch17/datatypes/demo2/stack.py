box=[]

hwb=int(input("How many book you want to add: "))

for x in range(hwb):
    box.append(f"{x+1} Book")

print("----Books added----")
print(box)

print("-----Removing Books------")
for x in range(len(box)):
    box.pop()
    print(box)


