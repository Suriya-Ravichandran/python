import turtle

window=turtle.Screen()

window.title("first turtle")

pen=turtle.Turtle()
pen.fillcolor("red") 
pen.begin_fill() 
for x in range(4):
    pen.forward(100)
    pen.right(90)

# End the fill and stop drawing 
pen.end_fill() 
pen.hideturtle() 
pen.write("Happy New Year!", align="center", font=("Courier", 36, "bold"))
turtle.done()