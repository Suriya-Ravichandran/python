import random
while True:
    print("Choices: stone,paper,scissor,exit")
    user_choice=str(input("Enter your Choice: "))
    if user_choice=="stone" or user_choice=="paper" or user_choice=="scissor":
        computer=["stone","paper","scissor"]
        rand_index=random.randint(0,2)
        computer_choice=computer[rand_index]
        print("Computer choice:",computer_choice) 
        if computer_choice=="stone" and user_choice=="paper":
            print("You win")
        elif computer_choice=="paper" and user_choice=="stone":
            print("Computer win")
        elif computer_choice=="scissor" and user_choice=="stone":
            print("You win")
        elif computer_choice=="stone" and user_choice=="scissor":
            print("Computer win")
        elif computer_choice=="paper" and user_choice=="scissor":
            print("You win")
        elif computer_choice=="scissor" and user_choice=="paper":
            print("Computer win")
        elif computer_choice=="stone" and user_choice=="stone":
            print("both are tie")
        elif computer_choice=="paper" and user_choice=="paper":
            print("both are tie")
        elif computer_choice=="scissor" and user_choice=="scissor":
            print("both or tie")
        else:
            print("App error !! please try again later")

    elif user_choice=="exit":
        print("Exiting....")
        break
    else:
        print("invaild choice !!")



