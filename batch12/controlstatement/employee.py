
times=int(input("Enter how many Employee to REG: "))
for x in range(times):
    name=str(input("Enter Employee Name: "))
    salaree=float(input("Enter Employee salaree: "))
    dept=str(input("Enter Employee Dept: "))

    print("---------------------------------")
    print("Name:",name)
    print("Salaree:",salaree)
    print("Department:",dept)
    print(f"{x+1} Employee Registered")
