class Parent():
    def money(self):
        print("Take money")
    def house(self):
        print("Take my house")

class Child(Parent):
    def collage(self):
        print("I am going collage")

class Child2(Parent):
     def school(self):
        print("I am going school")


ch1=Child()
ch1.collage()
ch1.house()
ch1.money()

ch2=Child2()
ch2.school()
ch2.house()
ch2.school()