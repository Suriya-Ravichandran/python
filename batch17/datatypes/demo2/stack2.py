hwb=int(input("Enter How many book to add: "))
box=[" "]*hwb

for x in range(hwb):
    box[x]=f"book {x+1}"

print(box)

flag=0
for x in range(hwb):
    flag+=1

for x in range(flag):
    del box[-1]
    print(box)
