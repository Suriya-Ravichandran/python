import turtle
import random
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fireworks with Turtle")

# Create turtle
firework = turtle.Turtle()
firework.hideturtle()
firework.speed(0)
firework.width(2)

colors = ["red", "yellow", "blue", "green", "purple", "orange", "white", "cyan", "magenta"]

def draw_firework(x, y, color):
    firework.penup()
    firework.goto(x, y)
    firework.pendown()
    firework.color(color)
    
    for _ in range(36):
        firework.forward(100)
        firework.backward(100)
        firework.left(10)

def clear_firework():
    firework.clear()

# Show multiple fireworks
for _ in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    color = random.choice(colors)
    draw_firework(x, y, color)
    time.sleep(0.5)
    clear_firework()

# Leave the last firework on screen
x = random.randint(-300, 300)
y = random.randint(-200, 200)
color = random.choice(colors)
draw_firework(x, y, color)

turtle.done()
