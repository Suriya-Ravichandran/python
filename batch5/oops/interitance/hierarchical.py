class parent:
    def money(self):
        print("Take money get lost")

class child(parent):
    def makeupset(self):
        print("I BUY A NEW MAKEUPSET")

class child2(child,parent):
    pass

ch1=child()
ch2=child2()
ch1.makeupset()
ch1.money()
ch2.money()
ch2.makeupset()