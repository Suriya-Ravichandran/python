books=int(input("How many books you want to add: "))
box=[" "]*books

for x in range(books):
    box[x]=f"book {x+1}"

print(box)

count=0
for x in box:
    count+=1


for x in range(count):
    del box[-1]
    print(box)