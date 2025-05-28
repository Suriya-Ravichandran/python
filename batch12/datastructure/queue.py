ration=[]

for x in range(4):
    ration.append(f"{x+1} Person")

print("-------Queue formed----------")
print(ration)

print("-------Queue cleared----------")
for x in range(len(ration)):
    del ration[0]
    print(ration)
