import random

hostpital=[]

for x in range(1,4):
    hostpital.append(f"paitent {x}")
    print(hostpital)

rp=random.randint(0,2)
print(hostpital[rp])
del hostpital[rp]
print(hostpital)