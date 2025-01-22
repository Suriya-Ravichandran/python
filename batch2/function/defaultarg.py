def gender(types="none"):
    data=types
    print(data)

print("Skip gender press 0\nSet gender press 1")
choice=int(input("Enter your choice"))

if(choice==1):
    setgender=str(input("Enter gender: "))
    gender(setgender)
else:
    gender()
