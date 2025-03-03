data=()
listdata=[]
size=int(input("Enter how Many Data to add tuple:"))
for x in range(size):
    values=int(input(f"Enter value {x+1}: "))
    listdata.append(values)
    data=tuple(listdata)
print(data)