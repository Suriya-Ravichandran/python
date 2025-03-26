class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getname(self):
        return self.name
    def getage(self):
        return self.age
    
    def __exit__(self):
        pass
    
s1=Student("foo","20")
print(s1.getname()) 
print(s1.getage())
