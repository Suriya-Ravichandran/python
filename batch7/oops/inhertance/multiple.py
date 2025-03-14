class parent():
    def givingmoney(self): # function inside a class can't be empty
        print("Take Money !!")

class child1(parent):
    pass

class child2(parent):
    pass


ch1=child1()
ch1.givingmoney()

ch2=child2()
ch2.givingmoney()