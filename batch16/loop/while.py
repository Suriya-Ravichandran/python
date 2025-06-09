# data=["Hello","World","foo"]


# i=0
# while True:
#     print(data[i])
#     if i==len(data)-1:
#         break
#     i+=1
 

while True:

    print("Press 1 to Red,press 2 yellow,press 3 to Green")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Red")
    elif choice==2:
        print("Yellow")
    elif choice==3:
        print("Green")
    elif choice==4:
        print("Exit")
        break
    else:
        print("Invaild choice")
