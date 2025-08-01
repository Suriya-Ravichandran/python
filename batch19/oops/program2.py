class BE: #create a class
    def student1(self):
        print(self)
        print("foo")

    def student2(self):
        print(self)
        print("boo")

t1=BE() # object creations
t2=BE()

t1.student1() # access the instances
t2.student1()