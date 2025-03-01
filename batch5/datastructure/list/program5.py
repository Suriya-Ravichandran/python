mul=[1,2,3,4,5,6,7,8,9,10]

table=[]

userdata=int(input("Which Tables You Want: "))
for x in mul:
    data=userdata*x
    table.append(data)

print("Table:",table)