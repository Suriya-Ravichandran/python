import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Rocket Launch")

# Rocket turtle
rocket = turtle.Turtle()
rocket.speed(0)
rocket.penup()
rocket.goto(0, -200)
rocket.pendown()

# Function to draw the rocket
def draw_rocket():
    # Body
    rocket.color("gray")
    rocket.begin_fill()
    rocket.forward(20)
    rocket.left(90)
    rocket.forward(100)
    rocket.left(90)
    rocket.forward(40)
    rocket.left(90)
    rocket.forward(100)
    rocket.left(90)
    rocket.forward(20)
    rocket.end_fill()

    # Nose cone
    rocket.color("red")
    rocket.begin_fill()
    rocket.left(90)
    rocket.forward(100)
    rocket.right(135)
    rocket.forward(28)
    rocket.right(90)
    rocket.forward(28)
    rocket.right(135)
    rocket.end_fill()

    # Side fins
    rocket.color("blue")
    rocket.penup()
    rocket.goto(-20, -100)
    rocket.setheading(0)
    rocket.pendown()
    rocket.begin_fill()
    rocket.goto(-40, -120)
    rocket.goto(-20, -120)
    rocket.goto(-20, -100)
    rocket.end_fill()

    rocket.penup()
    rocket.goto(20, -100)
    rocket.setheading(0)
    rocket.pendown()
    rocket.begin_fill()
    rocket.goto(40, -120)
    rocket.goto(20, -120)
    rocket.goto(20, -100)
    rocket.end_fill()

# Fire turtle
fire = turtle.Turtle()
fire.hideturtle()
fire.speed(0)

# Function to draw fire
def draw_fire(x, y):
    fire.clear()
    fire.penup()
    fire.goto(x, y)
    fire.pendown()
    fire.color("orange")
    fire.begin_fill()
    fire.circle(10)
    fire.end_fill()

    fire.penup()
    fire.goto(x, y - 10)
    fire.pendown()
    fire.color("red")
    fire.begin_fill()
    fire.circle(5)
    fire.end_fill()

# Draw the rocket initially
draw_rocket()

# Launch animation
for i in range(100):
    rocket.clear()
    rocket.penup()
    rocket.goto(0, -200 + i * 5)
    rocket.setheading(0)
    rocket.pendown()
    draw_rocket()
    draw_fire(0, -100 + i * 5)
    time.sleep(0.05)

fire.clear()
rocket.hideturtle()
turtle.done()
