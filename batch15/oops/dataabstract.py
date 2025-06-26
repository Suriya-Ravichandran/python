class sony():

    def voice(self):
        print("Voice is  working")

    def mouse(self):
        pass

class sonypro(sony):
    def mouse(self):
        print("working")


tv1=sony()

tv1.voice()
tv1.mouse()

tv2=sonypro()

tv2.mouse()
tv2.voice()