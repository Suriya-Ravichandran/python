# for x in range(10):
#     print(x)


print("----------Welcome to Employee Add App------------")
times=int(input("Enter how many Employee to add: "))

for x in range(times):
    name=str(input("Enter EMP Name: "))
    salary=float(input("Enter EMP salary: "))
    print("----------Employee Data-------")
    print("EName:",name)
    print("EName:",salary)
    print(f"{x+1}Employee Register !!")

