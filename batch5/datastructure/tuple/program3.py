data=(1,2,3,4,5)

data2=[]
size=int(input("Enter the extra value size: "))
for x in range(size):
     values=int(input(f"Enter value {x+1}: "))
     data2.append(values)

data3=list(data)
data=tuple(data3+data2)
print(data)    