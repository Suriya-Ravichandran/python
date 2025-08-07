import turtle
import colorsys

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest
pen.width(2)

# Colors using HSV
hue = 0
n = 36  # Number of petals

for i in range(360):
    col = colorsys.hsv_to_rgb(hue, 1, 1)
    pen.color(col)
    pen.circle(100)
    pen.left(10)
    hue += 1/n

pen.hideturtle()
turtle.done()
