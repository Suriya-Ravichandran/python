class User:

    def __init__(self,name,age,email,password):
        self.name=name
        self.email=email
        self.age=age
        self.password=password

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name
    
    def setAge(self,age):
        self.age=age

    def getAge(self):
        return self.age
    
    def setEmail(self,email):
        self.email=email

    def getEmail(self):
        return self.email
    
    def setPassword(self,Password):
        self.password=Password

    def getPassword(self):
        return self.password
    

# Testing

# u1=User("foo",28,"foo@gmail.com","foo@123")

# print(u1.getName())
