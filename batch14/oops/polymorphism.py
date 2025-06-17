class calculation():

    def square(self,*num):
        for x in num:
            print(x*x)


cal=calculation()

cal.square(10)
cal.square(10,20)
cal.square(10,20,30)