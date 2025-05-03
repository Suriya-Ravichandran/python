from tkinter import *

from tkinter import messagebox

window=Tk()

window.title("Hello world")
window.geometry("400x400")

def event():
    msg=messagebox.showinfo("Button clicked","Hello world")
    
btn=Button(window,text="click me",fg="white",bg="blue",height=3,width=25,command=event)

btn.place(x=100,y=100)
window.mainloop()