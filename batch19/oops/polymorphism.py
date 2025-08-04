class Calcu:
    def square(self,*num):
        for x in num:
            print(x*x)


c1=Calcu()
c2=Calcu()

c1.square(10,30)
c2.square(10,40,50,60)