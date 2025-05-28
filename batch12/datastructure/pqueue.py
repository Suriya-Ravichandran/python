hospital=[]

for x in range(4):
    hospital.append(f"{x+1} Patient")
print("--------treatment--------")
print(hospital)

doctor=set(hospital)
heartattack=list(doctor)
print(heartattack[0])