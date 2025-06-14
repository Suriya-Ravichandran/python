class sonypro:

    def mouse(self):
        print("Mouse is working")
    
    def voice(self):
        pass

class sonypromax(sonypro):
    def voice(self):
        print("Voice is working")

pro=sonypro()

pro.mouse()
pro.voice()

promax=sonypromax()

promax.mouse()
promax.voice()