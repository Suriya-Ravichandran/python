import random
hospital=[]

for x in range(3):
    hospital.append(f"Person {x+1}")

print(hospital)

heartattack=random.randint(0,len(hospital)-1)
print(hospital.pop(heartattack))