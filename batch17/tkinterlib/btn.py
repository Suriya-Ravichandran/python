from tkinter import *
from tkinter import messagebox


window=Tk()
window.geometry("600x600")

def clickme():
    print("btn clicked")
    msg=messagebox.showerror("information","Hello world")


btn=Button(window,text="click me",height=2,width=18,bg="blue",fg="white",command=clickme).place(x=50,y=50)

window.mainloop()