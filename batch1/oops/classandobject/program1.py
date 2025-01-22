
class hello:
    def __init__(self,name,age,phone,address):
       self.name=name
       self.age=age
       self.phone=phone
       self.Address=address

    def getdata(self):
        print("--------Detials--------")
        print(f"Name:{self.name}")
        print(self.age)
        print(self.phone)
        print(self.Address)


       

  
print("--------Student bio-------")
Name=str(input("Enter your name: "))
age=int(input("Enter Your age: "))
Phone = int(input("Enter phone number: "))
Address=str(input("Enter your Address: "))
h1=hello(Name,age,Phone,Address)
h1.getdata()  
