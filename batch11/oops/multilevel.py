class Parent():
    def money(self):
        print("Take money !!")


class child(Parent):
    pass

class child2(child):
    pass

ch2=child2()

ch2.money()