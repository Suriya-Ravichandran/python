def poweron():
    print("Ac is on")

def poweroff():
    print("Ac is off")


print("Press 1 to ON\nPress 2 to OFF")
while True:
    choice=int(input("Enter the choice: "))
    if choice==1:
        poweron()
    elif choice==2:
        poweroff()
    else:
        print("Invaild Choice !!!")
        break