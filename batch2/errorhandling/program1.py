#try except else 


def div(num1,num2):
    try:
       Result=num1/num2
       print("Result:",Result)
    except:
        print("You Divide by Zero Please Try different num")
    else:
        print("No Error founed")
    finally:
        print("try and expect is runed success")
    


while(True):
    num1=int(input("Enter Num1: "))
    num2=int(input("Enter Num2: "))
    div(num1,num2)


