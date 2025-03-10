class AI:  #AI class creatation

    def VoiceAssistance(self):
        # print("Voice Assistance is Inactive")
        pass

class Tv(AI): #Tv class Creatation

    def VoiceAssistance(self): # override a AI class function  Voice Assistance in Tv class 
        print("Voice Assistance is Active ")


sonypro=Tv() #create a object of Tv class 
sonyproMax=Tv() 

sonypro.VoiceAssistance() #call a Voice Assistance Function 
sonyproMax.VoiceAssistance()

print(id(sonypro))
print(id(sonyproMax))
