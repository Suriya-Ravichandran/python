class grandparentfather:
    def fathersideland(self):
        print("Take my land")
class grandparentmother:
    def mothersideland(self):
        print("Take my land")

class father(grandparentfather):
    pass

class mother(grandparentfather,grandparentmother):
    pass

class child1(father,mother):
    pass
