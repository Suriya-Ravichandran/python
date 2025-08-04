from abc import ABC ,abstractmethod

class sony(ABC):
    @abstractmethod
    def voice(self):
        pass

class sonypro(sony):
    def voice(self):
        print("voice is working !!")


s2=sonypro()
s2.voice()