class User():

    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password

    def setname(self,name):
        self.name=name
    
    def getname(self):
        return self.name
    
    def setemail(self,email):
        self.email=email
    
    def getemail(self):
        return self.email
    
    def setpassword(self,password):
        self.password=password
    
    def getpassword(self):
        return self.password
    


# u1=User(name="foo",email="foo@gmail.com",password="foo@123")

# print(u1.getname())
# u1.setname("Boo")

# print(u1.getname())


