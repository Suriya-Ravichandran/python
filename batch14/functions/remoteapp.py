def on():
    print("AC is on")
def off():
    print("AC is off")
def tempinc():
    print("Ac temp is increase")
def tempdec():
    print("Ac temp is decrease")

while True:
    choice=int(input("Enter your choice: "))
    if choice==1:
        on()
    elif choice==2:
        off()
    elif choice==3:
        tempinc()
    elif choice ==4:
        tempdec()
    elif choice==5:
        print("Exit")
        break
    else:
        print("Invaild choice")