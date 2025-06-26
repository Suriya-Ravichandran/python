class User:

    def __init__(self,name,email,password,age):
        self.name=name
        self.email=email
        self.password=password
        self.age=age
    
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


    def setage(self,age):
        self.age=age
    
    def getage(self):
        return self.age
        