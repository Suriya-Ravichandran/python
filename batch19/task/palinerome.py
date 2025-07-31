data=[]
hwd=int(input("How many string to add: "))

for x in range(hwd):
    d1=str(input(f"Enter your string {x+1}: "))
    data.append(d1)
    
print(data)

for x in data:
    rev=x[::-1]
    if x==rev:
        print(f"Palinerome: {x}")
    else:
        print(f"Non Palinerome: {x}")