import random

hosiptal=[]

for x in range(5):
    hosiptal.append(f"Person {x+1}")

print(hosiptal)
# attack=set(hosiptal)
# hosiptal=list(attack)
# out=hosiptal.pop(0)
# print(out)

randomperson=random.randint(0,len(hosiptal)-1)
print(hosiptal.pop(randomperson))
