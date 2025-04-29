class User:

    def __init__(self,name,age,dob):
        self.name=name
        self.age=age
        self.dob=dob
        print(self)

    def getname(self):
        return self.name
    
    def getage(self):
        return self.age
    
    def getdob(self):
        return self.dob
    
    def setname(self,name):
        self.name=name

    def setage(self,age):
        self.name=age

    def setdob(self,dob):
        self.dob=dob
        
    def __end__():
        pass


u1=User("foo",29,"12-02-1970")
u2=User("boo",29,"20-02-1990")

print("User 1 Name:",u1.getname())
print("User 2 Name:",u2.getname())


print("User 1 Name:",u1.getname())

u2.setname("koo")

print("User 2 Name:",u2.getname())



