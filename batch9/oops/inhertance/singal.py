class Parent():
    def money(self):
        print("Take money")
    def house(self):
        print("Take my house")

class Child(Parent):
    def school(self):
        print("I am going school")


ch1 = Child()

ch1.money()
ch1.house()
ch1.school()

