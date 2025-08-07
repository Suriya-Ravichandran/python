import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
panda = turtle.Turtle()
panda.pensize(3)
panda.speed(5)

def draw_circle(color, x, y, radius):
    panda.penup()
    panda.goto(x, y)
    panda.pendown()
    panda.fillcolor(color)
    panda.begin_fill()
    panda.circle(radius)
    panda.end_fill()

def draw_oval(color, x, y, width, height):
    panda.penup()
    panda.goto(x, y)
    panda.setheading(0)
    panda.pendown()
    panda.fillcolor(color)
    panda.begin_fill()
    for _ in range(2):
        panda.circle(width, 90)
        panda.circle(height, 90)
    panda.end_fill()

# Draw ears
draw_circle("black", -70, 100, 30)
draw_circle("black", 70, 100, 30)

# Draw face
draw_circle("white", 0, 0, 80)

# Draw eyes
draw_oval("black", -35, 20, 20, 40)
draw_oval("black", 35, 20, 20, 40)

# Draw eyeballs
draw_circle("white", -35, 40, 10)
draw_circle("white", 35, 40, 10)

# Draw nose
draw_circle("black", 0, 10, 8)

# Draw mouth
panda.penup()
panda.goto(-10, -10)
panda.setheading(-60)
panda.pendown()
panda.circle(10, 120)

# Draw body
draw_circle("black", 0, -130, 100)

# Draw arms
draw_oval("black", -110, -70, 20, 50)
draw_oval("black", 110, -70, 20, 50)

# Draw legs
draw_oval("black", -50, -220, 20, 40)
draw_oval("black", 50, -220, 20, 40)

panda.hideturtle()
turtle.done()
