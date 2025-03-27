class parent:
    def money(self):
        print("Take Money")

class child1(parent):
    def toy(self):
        print("play with toy")

class child2(parent):
   def toy1(self):
        print("play with toy1")


ch2=child2()
ch2.money()
ch2.toy1()