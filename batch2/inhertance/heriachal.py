class father:
    def takebike(self):
        print("Ride safely")

class mother():
    def takemoney(self):
        print("take money")

class child(father,mother):
    pass

ch1=child()

ch1.takebike()
ch1.takemoney()