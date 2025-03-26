class parent:
    def money(self):
        print("Take money get lost")

class child(parent):
    def dress(self):
        print("I buy new dress")

class child2(parent):
    def makeupset(self):
        print("I BUY A NEW MAKEUPSET")


ch1=child()
ch2=child2()

ch1.money()
ch1.dress()

ch2.money()
ch2.makeupset()