class parent:
    
    def givingmoney(self): # function inside a class can't be empty
        print("Take Money !!")

class child(parent):
    pass

ch=child()

ch.givingmoney()