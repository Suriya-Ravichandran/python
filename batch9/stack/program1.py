box=[]

for x in range(3):
    box.append(f"book {x+1}")
print("------------Adding element---------")
print(box)
print("\n")


print("---------removing elements-----------")
for x in range(len(box)):
    box.pop()
    print(box)

