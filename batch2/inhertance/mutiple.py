class parent:
    def takemoney(self):
        print("take money")

class child1(parent):
    pass

class child2(parent):
    pass

ch1=child1()
ch1.takemoney()
ch2=child2()
ch2.takemoney()