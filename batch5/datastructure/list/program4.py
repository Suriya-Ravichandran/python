userdata=[]
squarenum=[]


size=int(input("How many Number to Add a list:"))

for x in range(size):
    data=int(input(f"Enter the {x+1} num:"))
    userdata.append(data)

for x in userdata:
    data=x*x
    squarenum.append(data)

print("Given Number:",userdata)
print("Square Number:",squarenum)