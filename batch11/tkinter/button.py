from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("New window")
window.geometry("600x600")


def clickme():
    msg=messagebox.showwarning("information","Hello world")

btn=Button(window,text="click me",height=1,width=20,fg="red",bg="blue",command=clickme).place(x=50,y=50)

window.mainloop()