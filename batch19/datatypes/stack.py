hmb=int(input("Enter How many book to store in a box: "))
box=[]

for x in range(hmb):
    box.append(f"Book {x+1}")

print("---------book List----------")
print(box)
print("----------Removing books-------")
for x in range(len(box)):
    box.pop()
    print(box)


