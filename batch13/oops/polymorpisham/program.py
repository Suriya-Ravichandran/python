class Calculation():
    def square(self,*num):
        for x in num:
            print(x*x)

p1=Calculation()
print("------------")
p1.square(10)
print("------------")
p1.square(10,20)
print("------------")
p1.square(10,30,40)