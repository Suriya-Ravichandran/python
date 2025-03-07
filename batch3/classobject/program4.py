class Student:
    # def setdata(self,name,age):
    #     self.sname=name
    #     self.sage=age
    
    def printdata(self):
        print("hello")


    def __init__(self,name,age):
        self.sname=name
        self.sage=age
        self.printdata()


s1=Student("foo",18)

# s1.setdata()

s1.printdata()
print(s1.sname)
print(s1.sage)
