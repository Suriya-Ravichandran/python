from tkinter import *

from tkinter import messagebox
window=Tk()

window.title("Button Example")
window.geometry("400x400")


# btn actions
def showmessage():
    msg=messagebox.showinfo("Geeting","Hello Deepak")


btn1=Button(window,text="Click me !",command=showmessage)

btn1.place(x=50,y=50)

window.mainloop()