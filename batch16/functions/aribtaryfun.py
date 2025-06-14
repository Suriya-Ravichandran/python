def square(*x):
    for i in range(len(x)):
        print(x[i]*x[i])

square(10,20)
square(30,40,50,60,70)