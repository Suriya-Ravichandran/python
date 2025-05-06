class Parent():

    def house(self):
        print("Access our house")

    def money(self):
        print("Take money")

class child(Parent):
    pass

ch1=child()

ch1.house()
ch1.money()