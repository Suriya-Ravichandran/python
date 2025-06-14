class Parent:
    def money(self):
        print("Take Money")

class Child1(Parent):
    def dress(self):
        print("New Dress")

class Child2(Child1,Parent):
    def toy(self):
        print("play with toy")

class Child3(Child2,Child1,Parent):
    pass