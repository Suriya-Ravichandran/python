
# def data(value="hello"):
#     print(value)



# data("suriya")


def bank(name,accountno,balance="null"):
    print(name)
    print(accountno)
    print(balance)

print("----Welcome to SBI-----")
name=str(input("Enter Your Name: "))
accountno=int(input("Enter your Accouct no: "))
balance=float(input("Enter intial Balance"))

bank(name,accountno,balance)