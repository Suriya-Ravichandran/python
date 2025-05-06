class Grandparent:
    def house(self):
        print("Take my house")

class Parent(Grandparent):
    def money(self):
        print("Take money")
    

class Child(Parent):
    def school(self):
        print("I am going school")


p1=Parent()

p1.house()
p1.money()


ch1=Child()

ch1.house()
ch1.money()
ch1.school()