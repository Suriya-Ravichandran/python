#  single inhertance

class parent:
    def money(self):
        print("Take a money")

class child(parent):
    pass

ch=child()


ch.money()



# # multiple inhertance

class parent:
    def money(self):
        print("take money")

class child1(parent):
    def dress(self):
        print("Yamini dress")

class child2(parent):
    def makeupset(self):
        print("makeupset")


ch1=child1()

ch1.money()
ch1.dress()

ch2=child2()
ch2.makeupset()
ch2.money()


class parent:
    def money(self):
        print("take money")

class child1(parent):
    def dress(self):
        print("Yamini dress")

class child2(child1):
    def makeupset(self):
        print("makeupset")


ch1=child1()

ch1.money()
ch1.dress()

ch2=child2()
ch2.makeupset()
ch2.money()
ch2.dress()