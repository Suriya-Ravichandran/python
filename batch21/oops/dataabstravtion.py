from abc import ABC,abstractmethod

class Sony(ABC):

    @abstractmethod
    def voice(self):
        pass

class Sonypro(Sony):

    def voice(self):
        print("Voice is working")


s1=Sony()
print("-------------")
s2=Sonypro()
s2.voice()