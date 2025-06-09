box=[]
HMB=int(input("Enter How many books to store a box: "))
for x in range(HMB):
    box.append(f"Book {x+1}")

print("-----------Books in box----------")
print(box)

print("-----------Book Remove in the box-------------")
for x in range(len(box)):
    box.pop()
    print(box)


