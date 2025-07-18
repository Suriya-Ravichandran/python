class grantParent:
    def money(self):
        print("Take money")

class parent(grantParent):
    def house(self):
        print("Enjoy in house")

class child(parent):
    pass

ch1=child()

ch1.money()
ch1.house()
p1=parent()
p1.money()
p1.house()