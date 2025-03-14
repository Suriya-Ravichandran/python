class abstractclass:
    def hello(self):
        pass

class overrridingclass(abstractclass):
    def hello(self): #override a hello function
        print("Hello World")


poly=overrridingclass()
poly.hello()