class auth:

    def __init__(self,name,password):
        self.username=name
        self.password=password
        print("Signin success")

    def getusername(self):
        return self.username
    
    def getpassword(self):
        return self.password
    
    def login(self,verifypassword,password):
        if(verifypassword==password):
            print("login success")
        else:
            print("login failed")
