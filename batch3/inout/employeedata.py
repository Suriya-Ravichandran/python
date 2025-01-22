from tabulate import tabulate

print("press to 1 Resgister\npress to 2 exit")
choice=int(input("Enter your choice"))

if choice==1:
    print("----------Employee Registration App------------")
    Ename=str(input("Enter Ename: "))
    EID=int(input("Enter EID: "))
    Eage=int(input("Enter Eage: "))
    EDOB=str(input("Enter EDOB: "))
    Esalary=float(input("Enter Esalary: "))
    EQSAL=Esalary*3
    EHSAL=Esalary*6
    EASAL=Esalary*12
    print("---------Employee Details----------")
    print(f"Ename:{Ename}")
    print(f"Eid:{EID}")
    print(f"Eage:{Eage}")
    print(f"EDOB:{EDOB}")
    print(f"Esalary:{Esalary}")

    data = [
        [EQSAL, EHSAL, EASAL],
    ]

    # Column headers
    headers = ["Qsalary", "Hsalary", "Asalary"]

    # Generate table with tabulate
    table = tabulate(data, headers, tablefmt="grid")

    print(table)
elif choice==2:
    print("Exiting....")
else:
    print("invaild choice")


