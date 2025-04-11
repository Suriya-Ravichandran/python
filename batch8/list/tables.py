tables=[]
mulby=int(input("Which table you want to print: "))
times=int(input("Enter How many times you want to print: "))

for x in range(1,times+1):
    data=x*mulby
    tables.append(data)

print(tables)