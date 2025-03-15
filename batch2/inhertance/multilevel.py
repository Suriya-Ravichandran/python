class grandparent:
    def land(self):
        print("take land")

class parent(grandparent):
    def takemoney(self):
        print("take money")

class child(parent):
    pass

ch1=child()

ch1.land()
ch1.takemoney()
