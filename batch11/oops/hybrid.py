class Parent():
    def money(self):
        print("Take money !!")


class child(Parent):
    def dress(self):
        print("Dont ware my dress !!")

class child2(child,Parent):
    pass

ch2=child2()

ch2.money()
ch2.dress()