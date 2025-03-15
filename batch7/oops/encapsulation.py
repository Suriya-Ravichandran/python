class user:

    def __init__(self,name,email):
        self.name=name
        self.email=email

    def setname(self,name):
        self.name=name

    def getname(self):
        return self.name
    
    def setemail(self,email):
        self.email=email

    def getemail(self):
        return self.email
    

u1=user("foo","foo@email")

print(u1.getname())

u1.setname("boo")

print(u1.getname())