class parent:
    def money(self):
        print("Take money get lost")

class child(parent):
    def makeupset(self):
        print("I BUY A NEW MAKEUPSET")

class child2(child):
    pass



dhanapriya=child2()

dhanapriya.money()
dhanapriya.makeupset()