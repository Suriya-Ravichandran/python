class sony():

    def voice(self):
        pass
class sonypro(sony):
    #override
    def voice(self):
        print("Voice is activated")


sp1=sonypro()

sp1.voice()

