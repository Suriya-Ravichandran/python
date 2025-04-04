class studentBio:
    # def printhello(self):
    #     print("hello")
    def __init__(self,name,dept,age):
        self.name=name
        self.dept=dept
        self.age=age

    def setname(self,name):
        self.name=name
    
    def setdept(self,dept):
        self.dept=dept

    def setage(self,age):
        self.age=age
    
    def getname(self):
        return self.name
    
    def getdept(self):
        return self.dept
    def getage(self):
        return self.age
    # def __exit__(self):
    #     self.name=""
    #     self.age=""
    #     self.dept=""
    
    

s1=studentBio("Foo","BCA","34")
print("-----Get all data-----")
print("Name:",s1.getname())
print("Dept: ",s1.getdept())
print("Age: ",s1.getage())

s1.setname("Boo")

print("-----Get all data-----")
print("Name:",s1.getname())
print("Dept: ",s1.getdept())
print("Age: ",s1.getage())

