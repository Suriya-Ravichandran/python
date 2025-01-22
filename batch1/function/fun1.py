

def average(value):
    result=sum(value)/len(value)
    print(result)

number=int(input("How many to Add a list: "))
list1=[]

for x in range(number):
    value=int(input(f"Enter the value {x+1} : "))
    list1.append(value)
    print(list1)
average(list1)