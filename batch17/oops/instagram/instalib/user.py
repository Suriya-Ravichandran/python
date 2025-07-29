class User:

    def __init__(self, name, email, password, bio, age):
        self.name = name
        self.email = email
        self.password = password
        self.bio = bio
        self.age = age


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
    
    def setbio(self,bio):
        self.bio=bio
    
    def getbio(self):
        return self.bio
    
    def setage(self,age):
        self.age=age
    
    def getage(self):
        return self.age
    

# test

# u1=User("foo","foo@gmail.com","foo@123","I am foo boy developer",35)

# print(u1.getname())


        