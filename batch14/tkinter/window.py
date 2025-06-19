from tkinter import *

window=Tk()
window.geometry("600x600")
window.config(bg="black")

label=Label(window,text="Hello world",font=("Arial",18),fg="red",bg="yellow").place(x=225,y=50)

window.mainloop()