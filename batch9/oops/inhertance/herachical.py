class grandparent():
    def house(self):
        print("Take my house")

    def land(self):
        print("Take my land")
    
class parent1(grandparent):
    def bike(self):
        print("Ready to ride")

class parent2(grandparent):
    def car(self):
        print("Ready to car ride")

class child1(parent1):
    def collage(self):
        print("I am going collage")

class child2(parent2):
    def beautyparall(self):
        print("Makeup overload")
    
