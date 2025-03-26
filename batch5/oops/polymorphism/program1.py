class sony:
    def videorecorder(self):
        print("Recoder is Inactive")

class sonypro(sony):
    def videorecorder(self):
        print("Recoder is Active")


s=sony()
sp=sonypro()
s.videorecorder()
sp.videorecorder()
