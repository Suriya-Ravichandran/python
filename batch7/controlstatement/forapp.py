
size=int(input("Enter how many employee to add: "))

for i in range(size):
    print("---------------------------")
    name=str(input("Enter Ename: "))
    salary=str(input("Enter ESal: "))
    print(f"Ename: {name}")
    print(f"ESal: {salary}")
    print("---------------------------")
    print(f"{i+1} Employee Register")
