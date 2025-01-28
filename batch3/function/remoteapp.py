def poweron():
    print("Tv is On")

def poweroff():
    print("Tv is Off")

def channelforword():
    print("channel change forword")

def channelbackword():
    print("channel change Backword")

def volmueincrease():
    print("increase Volume")

def volmuedecrease():
    print("decrease Volume")


while True:
    print("Press 1 to Tv ON\nPress 2 to ChangechannelFor\nPress 3 to Changechannelback\nPress 4 to Volume Increase\nPress 5 to volume Decrease\nPress 0 to Tv off")
    action=int(input("Enter your Choice"))
    if(action==1):
        poweron()
    elif(action==2):
        channelforword()
    elif(action==3):
        channelbackword()
    elif(action==4):
        volmueincrease()
    elif(action==5):
        volmuedecrease()
    elif(action==0):
        poweroff()
        break
    else:
        print("invaild button")
