box=[]
index=[]
for x in range(5):
    box.append(f"book {x+1}")

print(box)

for x in range(len(box)):
    index.append(x)

index.reverse()
for x in index:
    del box[x]
    print(box)



