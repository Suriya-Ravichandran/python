import random

hos=[]
for x in range(5):
    hos.append(f"Person {x+1}")

print(hos)
hattack=random.randint(0,len(hos)-1)
out=hos.pop(hattack)

print(out)