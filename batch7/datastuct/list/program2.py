data=[]

size=int(input("How many data you want to add a list: "))

for x in range(size):
    values=str(input("Enter your List Values"))
    data.append(values) #add element in the last of list

print(data)