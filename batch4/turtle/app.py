import turtle

window=turtle.Screen()

window.title("first turtle")

pen=turtle.Turtle()
for i in range(100): 
    pen.circle(5*i) 
    pen.circle(-5*i) 
    pen.left(i)
turtle.done()