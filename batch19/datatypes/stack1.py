hmb=int(input("Enter How many book to store in a box: "))
box=[""]*hmb

for x in range(hmb):
    box[x]=f"Book {x+1}"

print(box)

count=0
for x in box:
    count+=1

for x in range(count):
    del box[-1]
    print(box)

    