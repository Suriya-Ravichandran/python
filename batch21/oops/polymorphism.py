class Calcu():

    def square(self,*num):
        for x in num:
            print(x*x)


c1=Calcu()
c2=Calcu()
print("-------------------")
c1.square(30,60,70)
print("-----------------------")
c1.square(10,50,70,90,100,500,400,200)

