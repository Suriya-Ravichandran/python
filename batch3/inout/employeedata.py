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
print("---------- Salary Overview --------------------")
print("|\tEQSAL   |\tEHSAL   |\tEASAL    |")
print("-----------------------------------------------")
print(f"|\t{EQSAL}|\t{EHSAL}|\t{EASAL}|")
print("-----------------------------------------------")



