class parent:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        
    def printname(self):
        print(self.firstname,self.lastname)

class child(parent):
    pass

x=child("foo","boo")

x.printname()