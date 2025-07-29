from abc import ABC,abstractmethod

class sony(ABC):
    @abstractmethod
    def voice(self):
        pass

class sonypro(sony):

    def voice(self):
        print("voice is working")
    

c1=sonypro()

c1.voice()