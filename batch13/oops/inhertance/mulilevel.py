class Parent:
    def money(self):
        print("Take Money")

class Child(Parent):
    def dress(self):
        print("New Dress")

class Child2(Child):
    def toy(self):
        print("play with toy")

ch1=Child()
ch2=Child2()

ch2.dress()
ch2.money()
ch2.toy()

ch1.dress()
ch1.money()




