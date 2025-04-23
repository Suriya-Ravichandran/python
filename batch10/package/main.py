from apps import evenodd
from apps import voteragedect
print("Press 1 To Odd or Even App, Press 2 to Voter Age Dectector App")
choice=int(input("Choose your App: "))

if(choice==1):
    print("1 to Even ,2 to Odd")
    choice2=int(input("Enter your choice: "))
    if(choice2==1):
        val=int(input("Enter Your Range Number: "))
        evenodd.even(val)
    