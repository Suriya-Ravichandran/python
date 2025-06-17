from tkinter import *
from tkinter import messagebox
Window=Tk()
Window.geometry("600x600")

def clickme():
    msg=messagebox.showwarning("message","Hello world")


btn=Button(Window,text="click me",height=1,width=18,bg="blue",fg="white",command=clickme).place(x=50,y=50)

Window.mainloop()