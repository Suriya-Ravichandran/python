class Grandparent():
    def house(self):
        print("Access our house")
class Parent(Grandparent):
    def money(self):
        print("Take money")

    def bike(self):
        print("Theft the bike")

class child(Parent):
    def collage(self):
        print("I am going collage")


