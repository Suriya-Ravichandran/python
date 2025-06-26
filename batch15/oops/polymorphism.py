class cal:

    def square(self,*num):
        for x in num:
            print(x*x)

p1=cal()

p1.square(100)
p1.square(100,200)
p1.square(100,200,300,400)