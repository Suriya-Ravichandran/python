class User:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password

    def setName(self,name):
        self.name=name
    
    def setEmail(self,email):
        self.email=email

    def setPassword(self,password):
        self.password=password

    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password
    

# tesing 

# user1=User("Foo","foo@gmail.com","foo@123")
# user2=User("Boo","boo@gmail.com","boo@123")

# print(user1.getName())
# print(user2.getName())
# print(user1.getName())
