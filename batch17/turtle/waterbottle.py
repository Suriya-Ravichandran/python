import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle
pen = turtle.Turtle()
pen.speed(2)
pen.pensize(3)

def draw_rectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_oval(t, radius, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.circle(radius,90)
        t.circle(radius//2,90)
    t.end_fill()

# Move to starting position
pen.penup()
pen.goto(-25, -150)
pen.pendown()

# Draw bottle body
draw_rectangle(pen, 50, 200, "skyblue")

# Draw bottle neck
pen.penup()
pen.goto(-15, 50)
pen.pendown()
draw_rectangle(pen, 30, 30, "skyblue")

# Draw bottle cap
pen.penup()
pen.goto(-20, 80)
pen.pendown()
draw_rectangle(pen, 40, 10, "blue")

# Draw water inside (overlay)
pen.penup()
pen.goto(-20, -140)
pen.pendown()
pen.pensize(1)
draw_rectangle(pen, 40, 180, "blue")

# Draw bottle bottom oval
pen.penup()
pen.goto(-25, -150)
pen.setheading(0)
pen.pendown()
draw_oval(pen, 25, "skyblue")

pen.hideturtle()
turtle.done()
