from tkinter import *

window=Tk()
window.geometry("600x600")
window.config(bg="#27F568")

text=Label(window,text="Hello world",font=("bold",18),fg="red",bg="yellow").place(x=50,y=50)

window.mainloop()