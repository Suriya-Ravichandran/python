import random

hos=[]

for x in range(5):
    hos.append(f"Person {x+1}")

print(hos)
attack=random.randint(0,len(hos)-1)

find=hos.pop(attack)
print(find)
