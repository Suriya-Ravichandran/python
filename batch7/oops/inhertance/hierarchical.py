class mother():
    def shegivemoney(self):
        print("take money from mother")
    
class father():
    def hegivemoney(self):
       print("take money from father")

class child(mother,father):
    pass

ch=child()
ch.shegivemoney()
ch.hegivemoney()