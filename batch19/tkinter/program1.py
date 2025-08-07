from tkinter import *

window=Tk()
window.geometry("600x600")
window.title("Text show")

text=Label(window,text="Hello world",font=("Arial",18),fg="red").place(x=50,y=50)


window.mainloop()