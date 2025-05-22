

def AcOn():
    print("Ac is On")
def AcOff():
    print("Ac is On")
def temp_increase():
    print(f"Tempture increase")
def temp_decrease():
    print(f"Tempture decrease")

while True:
    print("Press 1 to AC On,Press 2 to AC Off,Press 3 to Temp increase,Press 4 to Temp Decrease")
    choice=int(input("Enter your choice: "))
    if choice==1:
        AcOn()
    elif choice==2:
        AcOff()
    elif choice==3:
        temp_increase()
    elif choice==4:
        temp_decrease()
    else:
        print("Invaild choice")