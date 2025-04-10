from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("New Window")
window.geometry("400x400")

def printtext():
    message=messagebox.showerror("message","Hello World")


btn=Button(window,text="Click Me",fg="white",background="red",command=printtext)
btn.place(x=30,y=50)

window.mainloop()