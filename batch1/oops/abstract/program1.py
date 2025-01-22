class features:
    #abstractmethod
    def voice():
        pass
    #abstractmethod
    def image():
        pass
class mobile(features):
    def voice():
        print("Voice is activated")
    
    def image():
        print("image is activated")
class vivo(mobile):
    def model():
        print("Model is vivo")


v1=vivo

v1.model()
v1.voice()
v1.image()


