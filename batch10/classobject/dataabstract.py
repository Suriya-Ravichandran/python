class sony():

    def voice():
        pass

class sonypro(sony):
    #override
    def voice():
        print(" Voice is actived")

sp1=sonypro()

sp1.voice()