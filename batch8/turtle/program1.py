import turtle

window=turtle.Screen()
window.title("New turtle")

pen=turtle.Turtle()

# for x in range(20):
#     pen.forward(100)
#     pen.right(60)
#     pen.right(90)
# for x in range(20):
#     pen.circle(100)
#     pen.forward(10)
#     pen.left(30)

for x in range(20):
    pen.forward(40)
    pen.right(90)
    pen.backward(50)
    pen.left(60)




turtle.done()