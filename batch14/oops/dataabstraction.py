class sonypro():
    def voice(self):
        pass
    def mouse(self):
        print("mouse is working")

class sonypromax(sonypro):
    def voice(self):
        print("voice is working")

promax=sonypromax()
promax.mouse()
promax.voice()

pro=sonypro()

pro.voice()
pro.mouse()