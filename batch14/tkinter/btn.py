from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("600x600")

def clickme():
    def printhello():
        return "Hello world"
    messagebox.showinfo("Infromation",printhello())
   

btn=Button(window,text="click me",height=2,width=14,bg="blue",fg="white",command=clickme).place(x=225,y=50)

window.mainloop()