num1=[]
num2=[]
result=[]

value=int(input("How many value to add a list: "))

for x in range(value):
    data=int(input("Enter a value of 1st list: "))
    num1.append(data)

for y in range(value):
    data=int(input("Enter a value of 2st list: "))
    num2.append(data)


for z in range(value):
   result.append(num1[z]+num2[z])

print(num1)
print(num2)
print(result)
