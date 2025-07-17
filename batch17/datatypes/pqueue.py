import random

hospital=[]

for x in range(5):
    hospital.append(f"{x+1} Person")
print("------Queue-------")
print(hospital)

hattack=random.randint(0,len(hospital)-1)
outperson=hospital.pop(hattack)
print(f"Heart attack person is: {outperson}")