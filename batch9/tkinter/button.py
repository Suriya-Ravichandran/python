from tkinter import *
from tkinter.messagebox import *
window=Tk()
window.title("BUTTON WINDOW")
window.geometry("600x600")

# event

def clicked():
    showinfo("Information","Button clicked")

btn=Button(window,text="click me",bg="black",fg="white",height=2,width=10,command=clicked).place(x=250,y=50)


window.mainloop()