from tkinter import *

window=Tk()

window.title("Hello world")
window.geometry("400x400")

label=Label(window,text="Hello world",font=("bold",25),fg="red",bg="yellow")


label.place(x=100,y=200)
window.mainloop()