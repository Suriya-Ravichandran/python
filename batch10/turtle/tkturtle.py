import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas
import math

def draw_flower(turtle, petals=6, radius=100):
    turtle.speed(0)
    turtle.color("magenta")
    for _ in range(petals):
        draw_petal(turtle, radius)
        turtle.left(360 / petals)

def draw_petal(turtle, radius):
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.left(120)

# Setup Tkinter window
root = tk.Tk()
root.title("Turtle Flower Diagram")

# Create a canvas for Turtle to draw on
canvas = ScrolledCanvas(root)
canvas.pack(fill=tk.BOTH, expand=tk.YES)

# Create a Turtle object linked to this canvas
t = RawTurtle(canvas)
t.pensize(2)
t.pencolor("purple")
t.fillcolor("violet")
t.begin_fill()

# Draw the flower
draw_flower(t, petals=8, radius=100)

t.end_fill()

# Run the Tkinter main loop
root.mainloop()
