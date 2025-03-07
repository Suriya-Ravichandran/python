class user:

    # def __init__(self,name,email,phone,password):
    #     self.uname=name
    #     self.uemail=email
    #     self.uphone=phone
    #     self.upassword=password
   
    

    def setname(self,name):
        self.uname=name

    def getname(self):
        return self.uname
    
    def setemail(self,email):
        self.uemail=email

    def getemail(self):
        return self.uemail
    
    def setphone(self,phone):
        self.uphone=phone

    def getphone(self):
        return self.uphone
    
    def setpassword(self,password):
        self.upassword=password
    
    def getpassword(self):
        return self.upassword
    

    def __init__(self,name,email,phone,password):
        self.uname=name
        self.uemail=email
        self.uphone=phone
        self.upassword=password
        print("UserName:",self.getname())
        print("UserEmail:",self.getemail())
        print("UserPhone:",self.getphone())
        print("UserPassword:",self.getpassword())

    def __end__(self):
        pass